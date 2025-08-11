from google.adk.agents import Agent
from .tools.get_weather import get_weather
from .agents.greeting_agent import greeting_agent
from .agents.farewell_agent import farewell_agent

# Define model constant
MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"
AGENT_MODEL = MODEL_GEMINI_2_5_FLASH  # Use this for consistency

# Create the weather agent (Step 1: Your First Agent - Basic Weather Lookup)
# Note: Using 'root_agent' name as expected by ADK run command
if greeting_agent and farewell_agent and 'get_weather' in globals():
    # Let's use a capable Gemini model for the root agent to handle orchestration

    root_agent = Agent(
        name="weather_agent_v2", # Give it a new version name
        model=AGENT_MODEL,
        description="The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
        instruction="You are the main Weather Agent coordinating a team. Your primary responsibility is to provide weather information. "
                    "Use the 'get_weather' tool ONLY for specific weather requests (e.g., 'weather in London'). "
                    "You have specialized sub-agents: "
                    "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                    "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. "
                    "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                    "If it's a weather request, handle it yourself using 'get_weather'. "
                    "For anything else, respond appropriately or state you cannot handle it.",
        tools=[get_weather], # Root agent still needs the weather tool for its core task
        # Key change: Link the sub-agents here!
        sub_agents=[greeting_agent, farewell_agent]
    )