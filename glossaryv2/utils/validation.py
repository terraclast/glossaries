def validate_menu_choice(choice, options):
    """
    Validates whether the user's input maps to an available menu option.
    Convert the choice to the appropriate data-type.
    choice (str): User's input
    options (set): Valid options for the specifed menu.

    Returns:
        bool: True if the choice is valid, False if not. 
    """
    if choice in options:
        try:
            # Convert to int if its a digit
            if choice.isdigit():
                return int(choice)
            return choice
        except ValueError:
            return None
    return None

def validate_numeric_choice(choice, min_val, max_val):
    """
    Validate if the numeric input is within the given range.

    :param choice: User input (string).
    :param min_value: Minimum valid value (int).
    :param max_value: Maximum valid value (int).
    :return: Boolean indicating validity.
    """
    try: 
        number = int(choice)
        return min_val <= number <= max_val
    except:
        return  False

def validate_term(term, glossary):
    """
    Check if a term exists in the given glossary.

    :param term: Term to validate (string).
    :param glossary: Dictionary of glossary terms.
    :return: Boolean indicating validity.
    """
    return term in glossary.keys()

def validate_keyword(keyword):
    """
    Validate the keyword for searching.
    
    :param keyword: Keyword input (string).
    :return: Boolean indicating validity.
    """
    return bool(keyword.strip())

def validate_glossary(glossary_name, glossary):
    """
    Validate the structure of a glossary (Python dict or JSON object).
    :param glossary_name: Name of the glossary (for error messages).
    :param glossary: The glossary to validate.

    :return: A validated glossary dictionary or None if invalid.
    """
    if not isinstance(glossary, dict):
        print(f"ERROR: Glossary '{glossary_name}' is not a valid file-type.")
        return None
    
    validated_glossary = {}
    for term, definition in glossary.items():
        if isinstance(term, str) and (isinstance(definition, str) or isinstance(definition, dict)):
            validated_glossary[term] = definition
        else:
            print(f"WARNING: Skipping invalid entry in '{glossary_name}': {term} -> {definition}")
    return validated_glossary



