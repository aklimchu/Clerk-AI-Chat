"""Functionality tests for AI Agent."""

import pytest
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Clerk_AI_Chat.agent import ClerkAgent

@pytest.fixture
def agent():
    """Get API key."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY not set, skipping tests")
    return ClerkAgent()

def test_basic_emails(agent):
    """Test basic emails generation."""
    summary = "Thank the client for their inquiry about our services and provide information about our pricing packages"
    result = agent.generate_email_reply(
        summary=summary,
        tone="professional"
    )
    assert result["success"], f"Basic email generation failed: {result.get('error', 'Unknown error')}"
    assert "email" in result, "Result missing email key"
    assert "subject" in result["email"], "Email missing subject"
    assert "body" in result["email"], "Email missing body"
    assert len(result["email"]["body"]) > 0, "Email body is empty"

def test_variations_emails(agent):
    """Test generation of variation emails."""
    summary = "Decline a meeting request due to scheduling conflicts and suggest alternative times"
    variations_result = agent.generate_multiple_variations(
        summary=summary,
        num_variations=2,
        tone="friendly"
    )
    assert variations_result["success"], f"Variations generation failed: {variations_result.get('error', 'Unknown error')}"
    assert "variations" in variations_result, "Result missing variations key"
    assert len(variations_result["variations"]) == 2, f"Expected 2 variations, got {len(variations_result['variations'])}"
    for variation in variations_result["variations"]:
        assert "email" in variation, f"Variation {variation.get('variation')} missing email key"
        assert "subject" in variation["email"], f"Variation {variation.get('variation')} missing subject"
        assert "body" in variation["email"], f"Variation {variation.get('variation')} missing body"
        assert len(variation["email"]["body"]) > 0, f"Variation {variation.get('variation')} has empty body"
