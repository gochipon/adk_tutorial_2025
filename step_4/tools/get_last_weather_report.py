from google.adk.tools.tool_context import ToolContext

def get_last_weather_report(tool_context: ToolContext) -> dict:
    """Retrieves the last weather report from session state.
    
    Args:
        tool_context: Tool context for accessing session state
        
    Returns:
        dict: The last weather report or error message
    """
    print("--- Tool: get_last_weather_report called ---")
    
    # Get the last weather report from state
    last_report = tool_context.state.get("last_weather_report")
    
    if last_report:
        print(f"--- Tool: Found last weather report: {last_report} ---")
        return {
            "status": "success",
            "report": last_report,
            "message": f"Last weather report: {last_report}"
        }
    else:
        print("--- Tool: No previous weather report found ---")
        return {
            "status": "error",
            "message": "No previous weather report found. Please request weather information first."
        }