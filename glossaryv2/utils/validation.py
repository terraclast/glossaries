def validate_menu_choice(choice, options):
    """
    Validates whether the user's input maps to an available main menu option.

    Args:
        choice (str): User's input
        options (set): Valid options for the main menu.

    Returns:
        bool: True if the choice is valid, False if not. 
    """
    
    return choice in options




