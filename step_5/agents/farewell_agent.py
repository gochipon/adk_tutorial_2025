from google.adk.agents import Agent
from ..tools.say_goodbye import say_goodbye

MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"

farewell_agent = Agent(
        model = MODEL_GEMINI_2_5_FLASH,
        name="farewell_agent",
        instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message using the 'say_goodbye' tool. Do not perform any other actions.",
        description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
        tools=[say_goodbye],
    )