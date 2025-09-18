"""Revisor agent wiring: builds Setup and runs Agent with configured instructions."""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from models.models import Agent, Setup
# from Clerk_AI_Chat.models.models import Agent, Setup
from models.models import Agent, Setup



# globals
MAX_RESPONSE_LEN = 5

# setup
MODEL = "gpt-4.1-nano"
INSTRUCTIONS = (
    f"You are a mathematician. "
    f"You receive a number that represents the length of an email response. "
    f"If the received number is greater than {MAX_RESPONSE_LEN}, "
    f"create a message following the structure below:\n\n"
    f"- Description of the issue\n"
    f"- The actual number received\n"
    f"- The allowed maximum number ({MAX_RESPONSE_LEN})"
)

RESPONSE = "Hello world"  # test 11


def setup_agent(agent_model, agent_instructions, received_input: str) -> Setup:
    """
    Create a Setup object for initializing an Agent.

    Args:
        agent_model (str): The name of the model to use.
        agent_instructions (str): Instructions for the agent to follow.
        received_input (str): The input string provided to the agent.

    Returns:
        Setup: A configuration object containing model, instructions, and input.
    """
    return Setup(agent_model, agent_instructions, received_input)


def get_response_len(resp: str) -> str:
    """
    Calculate the length of a given response string.

    Args:
        resp (str): The response text.

    Returns:
        str: The length of the response as a string.
    """
    return str(len(resp))

# input = get_response_len(RESPONSE)

setup = setup_agent(MODEL, INSTRUCTIONS, get_response_len(RESPONSE))

# init revisor agent
revisor = Agent(setup)
print(revisor.get_output())
