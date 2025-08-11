from google.adk.agents import Agent
from ..tools.say_goodbye import say_goodbye

MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"

farewell_agent = Agent(
        model = MODEL_GEMINI_2_5_FLASH,
        name="farewell_agent",
        instruction="", # 自分で書いてみよう
        description="", # 自分で書いてみよう
        tools=[say_goodbye],
    )