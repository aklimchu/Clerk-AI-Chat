import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import Optional, Dict, Any
import json

# Load environment variables from .env file
load_dotenv()

class ClerkAgent:
    """
    OpenAI Agent for generating official emails based on user summaries.
    This agent can create professional, contextually appropriate emails from simple descriptions.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Email Reply Agent.
        
        Args:
            api_key: OpenAI API key. If not provided, will use OPENAI_API_KEY from environment.
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = "gpt-4-turbo"  # Using GPT-4-turbo for advanced email generation
        
    def generate_email_reply(self, 
                           summary: str, 
                           tone: str = "professional",
                           recipient_context: Optional[str] = None,
                           sender_name: Optional[str] = None,
                           sender_title: Optional[str] = None,
                           company: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate an official email based on the provided summary.
        
        Args:
            summary: Short summary describing what the email should say
            tone: Tone of the email ("professional", "friendly", "formal", "casual")
            recipient_context: Context about the recipient (e.g., "client", "colleague", "vendor")
            sender_name: Name of the sender
            sender_title: Title/position of the sender
            company: Company name
            
        Returns:
            Dictionary containing the generated email with subject, body, and metadata
        """
        
        # Build the system prompt
        system_prompt = self._build_system_prompt(tone, recipient_context, sender_name, sender_title, company)
        
        # Build the user prompt
        user_prompt = f"""Based on the following summary, create an official email:

        Summary: {summary}

        Please generate a complete email with:
        1. An appropriate subject line
        2. A professional email body that expands on the summary
        3. Proper greeting and closing
        4. Clear and detailed content that fully develops the ideas in the summary

        Make sure the email is:
        - Professional and well-structured
        - Appropriate for the specified tone: {tone}
        - Clear and actionable
        - Free of grammatical errors
        - Properly formatted for business communication
        - An original email (not a reply to something)"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            email_content = response.choices[0].message.content
            
            # Parse the response to extract subject and body
            parsed_email = self._parse_email_response(email_content)
            
            return {
                "success": True,
                "email": parsed_email,
                "metadata": {
                    "model": self.model,
                    "tone": tone,
                    "summary": summary,
                    "recipient_context": recipient_context,
                    "sender_name": sender_name,
                    "sender_title": sender_title,
                    "company": company
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "metadata": {
                    "summary": summary,
                    "tone": tone
                }
            }
    
    def _build_system_prompt(self, tone: str, recipient_context: Optional[str], 
                           sender_name: Optional[str], sender_title: Optional[str], 
                           company: Optional[str]) -> str:
        """Build the system prompt for the email generation."""
        
        prompt = """You are an expert business communication assistant specializing in writing professional emails. 
        Your task is to create original, well-structured emails based on user summaries.
        
        Guidelines for email creation:
        1. Use proper business email format with clear subject lines
        2. Include appropriate greeting and professional closing
        3. Write in clear, detailed language that expands on the summary
        4. Ensure the tone matches the specified style
        5. Make the email actionable and professional
        6. Use proper email etiquette
        7. Create an ORIGINAL email (not a reply to something)
        
        Email Structure:
        - Subject: Clear, descriptive subject line
        - Greeting: Appropriate salutation
        - Body: Well-organized paragraphs that fully develop the summary
        - Closing: Professional sign-off
        - Signature: Include sender details if provided
        
        Tone Guidelines:
        - Professional: Formal, respectful, business-appropriate
        - Friendly: Warm but still professional
        - Formal: Very formal, traditional business style
        - Casual: Relaxed but still appropriate for business
        
        IMPORTANT: Format your response EXACTLY as follows:
        SUBJECT: [subject line]
        
        [email body with proper formatting]
        
        Make sure to:
        1. Always start with "SUBJECT: " followed by the subject line
        2. Include a blank line after the subject
        3. Then provide the complete email body with proper formatting
        4. Expand the summary into a full, detailed email"""

        if recipient_context:
            prompt += f"\n\nRecipient Context: {recipient_context}"
        
        if sender_name or sender_title or company:
            prompt += "\n\nSender Information:"
            if sender_name:
                prompt += f"\n- Name: {sender_name}"
            if sender_title:
                prompt += f"\n- Title: {sender_title}"
            if company:
                prompt += f"\n- Company: {company}"
        
        return prompt
    
    def _parse_email_response(self, email_content: str) -> Dict[str, str]:
        """Parse the AI response to extract subject and body."""
        
        lines = email_content.strip().split('\n')
        subject = ""
        body_lines = []
        
        # Extract subject line - try multiple formats
        subject_found = False
        for i, line in enumerate(lines):
            line_upper = line.upper().strip()
            if line_upper.startswith('SUBJECT:'):
                subject = line.replace('SUBJECT:', '').replace('subject:', '').strip()
                subject_found = True
                # Start collecting body from next line
                body_lines = lines[i+1:]
                break
            elif line_upper.startswith('SUBJECT '):
                subject = line.replace('SUBJECT ', '').replace('subject ', '').strip()
                subject_found = True
                body_lines = lines[i+1:]
                break
        
        # If no subject found, try to extract from first line or generate one
        if not subject_found:
            # Use first line as subject if it looks like one
            if lines and len(lines[0].strip()) < 100 and not lines[0].strip().startswith('Dear'):
                subject = lines[0].strip()
                body_lines = lines[1:]
            else:
                # Generate a generic subject
                subject = "Re: Your Message"
                body_lines = lines
        
        # Clean up body
        body = '\n'.join(body_lines).strip()
        
        # If body is empty, use the full content
        if not body:
            body = email_content.strip()
        
        return {
            "subject": subject,
            "body": body,
            "full_content": email_content
        }
    
    def generate_multiple_variations(self, summary: str, num_variations: int = 3, **kwargs) -> Dict[str, Any]:
        """
        Generate multiple variations of the same email reply.
        
        Args:
            summary: Short summary of what the email should contain
            num_variations: Number of variations to generate (default: 3)
            **kwargs: Additional arguments for generate_email_reply
            
        Returns:
            Dictionary containing all variations
        """
        variations = []
        
        for i in range(num_variations):
            result = self.generate_email_reply(summary, **kwargs)
            if result["success"]:
                variations.append({
                    "variation": i + 1,
                    "email": result["email"],
                    "metadata": result["metadata"]
                })
            else:
                variations.append({
                    "variation": i + 1,
                    "error": result["error"]
                })
        
        return {
            "success": True,
            "variations": variations,
            "total_variations": num_variations
        }