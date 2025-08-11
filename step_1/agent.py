from google.adk.agents import Agent
from .tools.get_weather import get_weather


# Define model constant
MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"
AGENT_MODEL = MODEL_GEMINI_2_5_FLASH  # Use this for consistency

# Create the weather agent (Step 1: Your First Agent - Basic Weather Lookup)
# Note: Using 'root_agent' name as expected by ADK run command
root_agent = Agent(
    name="weather_agent_v1",
    model=AGENT_MODEL, # Can be a string for Gemini or a LiteLlm object
    description="Provides weather information for specific cities.",
    instruction="You are a helpful weather assistant. "
                "When the user asks for the weather in a specific city, "
                "use the 'get_weather' tool to find the information. "
                "If the tool returns an error, inform the user politely. "
                "If the tool is successful, present the weather report clearly.",
    tools=[get_weather], # Pass the function directly
)
