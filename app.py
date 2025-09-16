"""Main module of Clerk-AI-Chat application."""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError
from clerk_ai_chat.agent import ClerkAgent
from clerk_ai_chat.web_app import startup_web_app

def main():
    """Opening the connection with OpenAI and launching the web application."""
    load_dotenv()

    # Check if API key is loaded
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please make sure your .env file contains: OPENAI_API_KEY=your_api_key_here")
        return

    # Initialize OpenAI client with API key from environment
    OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    print("OpenAI API client initialized successfully!")
    print(f"API Key loaded: {api_key[:8]}...{api_key[-4:] if len(api_key) > 12 else '***'}")

    # Initialize AI agent and run the web app
    try:
        agent = ClerkAgent()
        print("✅ Email agent initialized")
        startup_web_app(agent)
    except (ValueError, AuthenticationError, OSError, RuntimeError) as e:
        print(f"Error initializing agent or starting web app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
