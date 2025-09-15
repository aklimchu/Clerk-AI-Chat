"""
Interactive test script for ClerkAgent.
Allows manual testing of email generation features.
Requires OPENAI_API_KEY in .env file.
Usage: python scripts/demo_agent.py
"""

import os
import sys
from dotenv import load_dotenv
# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Clerk_AI_Chat.agent import ClerkAgent

def email_agent_tests(agent):
    """Create sample emails."""
    # Example 1: Basic email generation
    print("\n" + "="*50)
    response = input("Would you like to perform the tests with basic emails? (y/n): ").strip().lower()
    if response in ['y', 'yes']:
        basic_emails(agent)

    # Example 2: Multiple variations
    print("\n" + "="*50)
    response = input("Would you like to perform the tests with multiple variations? (y/n): ").strip().lower()
    if response in ['y', 'yes']:
        variations_emails(agent)

    # Example 3: Interactive tests
    print("\n" + "="*50)
    response = input("Would you like to try interactive mode? (y/n): ").strip().lower()
    if response in ['y', 'yes']:
        interactive_test(agent)

def basic_emails(agent):
    """Create a basic email."""
    print("=== Example 1: Basic Email Generation ===")
    summary = "Thank the client for their inquiry about our services and provide information about our pricing packages"
    result = agent.generate_email_reply(
        summary=summary,
        tone="professional",
        recipient_context="potential client",
        sender_name="John Smith",
        sender_title="Sales Manager",
        company="Tech Solutions Inc."
    )
    if result["success"]:
        email = result["email"]
        print(f"Subject: {email['subject']}")
        print(f"\nBody:\n{email['body']}")
    else:
        print(f"Error: {result['error']}")
    print("\n" + "="*60 + "\n")

def variations_emails(agent):
    """Create emails with multiple variations."""
    print("=== Example 2: Multiple Variations ===")
    summary = "Decline a meeting request due to scheduling conflicts and suggest alternative times"

    variations_result = agent.generate_multiple_variations(
        summary=summary,
        num_variations=2,
        tone="friendly",
        recipient_context="colleague"
    )

    if variations_result["success"]:
        for variation in variations_result["variations"]:
            if "email" in variation:
                print(f"\n--- Variation {variation['variation']} ---")
                email = variation["email"]
                print(f"Subject: {email['subject']}")
                print(f"Body: {email['body']}")
            else:
                print(f"Variation {variation['variation']} failed: {variation['error']}")

def interactive_test(agent):
    """Create email based on a user input."""
    try:
        while True:
            summary = input("\n📝 Summary: ").strip()
            if summary.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break

            if not summary:
                print("Please enter a summary.")
                continue

            tone = input("🎭 Tone (professional/friendly/formal/casual) [professional]: ").strip() or "professional"
            recipient = input("👤 Recipient context (optional): ").strip() or None
            sender_name = input("✍️ Your name (optional): ").strip() or None
            sender_title = input("💼 Your title (optional): ").strip() or None
            company = input("🏢 Company (optional): ").strip() or None
            print("\n⏳ Generating email...")
            result = agent.generate_email_reply(
                summary=summary,
                tone=tone,
                recipient_context=recipient,
                sender_name=sender_name,
                sender_title=sender_title,
                company=company
            )
            if result["success"]:
                email = result["email"]
                print("\n✅ Email Generated Successfully!")
                print("=" * 50)
                print(f"Subject: {email['subject']}")
                print(f"\nBody:\n{email['body']}")
                print("=" * 50)
            else:
                print(f"❌ Error: {result['error']}")
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! (Exited with Ctrl+C)")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Perform the demo tests."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return

    try:
        agent = ClerkAgent()
        print("✅ Email agent initialized")
        email_agent_tests(agent)
    except Exception as e:
        print(f"Error initializing agent: {e}")

if __name__ == "__main__":
    main()
