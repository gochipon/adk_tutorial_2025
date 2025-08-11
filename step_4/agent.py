from google.adk.agents import Agent
from google.adk.runners import Runner
from .tools.get_weather_stateful import get_weather_stateful
from .tools.get_last_weather_report import get_last_weather_report
from .tools.set_temperature_unit import set_temperature_unit
from .session import session_service_stateful, create_session_sync, APP_NAME
from .agents.greeting_agent import greeting_agent
from .agents.farewell_agent import farewell_agent

# Define model constant
MODEL_GEMINI_2_5_FLASH = "gemini-2.5-flash"
AGENT_MODEL = MODEL_GEMINI_2_5_FLASH  # Use this for consistency

# Create the weather agent (Step 1: Your First Agent - Basic Weather Lookup)
# Note: Using 'root_agent' name as expected by ADK run command
if greeting_agent and farewell_agent and 'get_weather_stateful' in globals():
    # Let's use a capable Gemini model for the root agent to handle orchestration

    root_agent= Agent(
        name="weather_agent_v4_stateful", # Give it a new version name
        model=AGENT_MODEL,
        description="Main agent: Provides weather (state-aware unit), delegates greetings/farewells, saves report to state.",
        instruction="You are the main Weather Agent. Your job is to provide weather using 'get_weather_stateful'. "
                    "The tool will format the temperature based on user preference stored in state, but you can override this by passing a 'unit' parameter if the user specifically requests Celsius or Fahrenheit. "
                    "When the user mentions a specific temperature unit (Celsius/Fahrenheit), you can either: "
                    "1. Use that unit for the current request by passing 'unit' parameter to get_weather_stateful, or "
                    "2. Update their preference permanently using 'set_temperature_unit' tool. "
                    "Delegate simple greetings to 'greeting_agent' and farewells to 'farewell_agent'. "
                    "You can also retrieve the last weather report using 'get_last_weather_report' tool when users ask for previous weather information. "
                    "The 'output_key' automatically saves your final response to 'last_weather_report' in the session state. "
                    "Handle weather requests, greetings, farewells, and last report queries.",
        tools=[get_weather_stateful, get_last_weather_report, set_temperature_unit], # Root agent tools
        # Key change: Link the sub-agents here!
        sub_agents=[greeting_agent, farewell_agent],
        output_key="last_weather_report" 
    )

    # Ensure the session exists when running as a plain Python script
    try:
        create_session_sync()
    except Exception:
        # If session already exists or cannot be created, continue
        pass

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful  # Pass the session service instance
    )
