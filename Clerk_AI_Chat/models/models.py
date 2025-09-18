"""
Module: abs_agent
Defines the Setup dataclass and Agent class for interacting with OpenAI models.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


# pylint: disable=too-few-public-methods
@dataclass
class Setup:
    """Configuration object for initializing an Agent.

    Attributes:
        model (str): The OpenAI model name.
        instructions (str): The system instructions for the agent.
        input (str): The input message or data.
    """

    model: str
    instructions: str
    input: str


class Agent:
    """Agent that interacts with OpenAI API using a provided Setup."""

    def __init__(self, setup: Setup):
        """
        Initialize the agent with a setup configuration.

        Args:
            setup (Setup): Configuration object containing model,
                instructions, and input.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env.")

        # create client
        self.client = OpenAI(api_key=api_key)

        # request response
        self.response = self.client.responses.create(
            model=setup.model,
            instructions=setup.instructions,
            input=setup.input,
        )

    def get_output(self) -> str:
        """Return text output from the response."""
        return self.response.output_text
