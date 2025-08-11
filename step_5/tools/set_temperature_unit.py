from google.adk.tools.tool_context import ToolContext

def set_temperature_unit(unit: str, tool_context: ToolContext) -> dict:
    """Sets the user's preferred temperature unit in session state.
    
    Args:
        unit: Temperature unit to set ("Celsius" or "Fahrenheit")
        tool_context: Tool context for accessing session state
        
    Returns:
        dict: Status of the operation
    """
    print(f"--- Tool: set_temperature_unit called with unit: {unit} ---")
    
    # Validate the unit
    if unit.lower() not in ["celsius", "fahrenheit"]:
        return {
            "status": "error", 
            "message": "Invalid unit. Please use 'Celsius' or 'Fahrenheit'."
        }
    
    # Normalize the unit name
    normalized_unit = unit.capitalize()
    
    # Update the state
    tool_context.state["user_preference_temperature_unit"] = normalized_unit
    print(f"--- Tool: Updated temperature unit preference to: {normalized_unit} ---")
    
    return {
        "status": "success",
        "message": f"Temperature unit preference updated to {normalized_unit}."
    }
