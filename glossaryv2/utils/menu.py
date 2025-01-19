from .glossary_loader import glossary_importer
from .glossary_ops import search_keyword, view_all_entries, view_entry, view_all_terms
from .validation import validate_menu_choice
import importlib
import json

glossaries = glossary_importer()


options = {
    "main":  set(),  # Dynamic options generated at runtime
    "gloss":  {"1", "2", "3", "4", "b", "q"}
}

def generate_main_menu_options(glossaries):
    """
    Generate dynamic main menu options based on available glossaries.
    :param glossaries: Dictionary of glossaries
    :return: Set of valid main menu options.
    """
    glossary_options = set(map(str, range(1, len(glossaries) + 1)))
    static_options = {"s", "q"}
    return glossary_options | static_options

def display_main_menu(glossaries):
    """
    Print the main menu with dynamically numbered glossaries
    """
    print("Glossaries and options: ")
    for i, gloss_name in enumerate(glossaries.keys(), start=1):
        print(f"{i}.) {gloss_name}")
    print("s.) Search for a keyword or term across all glossaries.")
    print("q.) Quit the program.")

def display_glossary_menu(glossary_name):
    """
    Print the glossary-specific menu.
    """
    print(f"\nGlossary: [{glossary_name}]")
    print("Glossary Options: \n\t1.) View Entry\n\t2.) View All Terms\n\t3.) View Entire Glossary\n\t4.) Keyword Search\n\tb.) Back to Main Menu\n\tq.) Quit Program")

def get_input(prompt): 
    return input(prompt).strip().lower()

def main_menu(glossaries):
    """
    Lists all currently available glossaries and provides options to: 
        a. Display a numbered dynamic list of available glossaries
        b. Select a glossary
        b. Search all glossaries for a keyword, potentially displaying multiple entries
        c. Quit the program
    """

    options["main"] = generate_main_menu_options(glossaries) # Update dynamic options

    while True:
        # Generate and display the menu. 
        display_main_menu(glossaries)
        # Take user input
        choice = get_input("Please select a glossary number, 's' to search and 'q' to quit: ")
        
        # Validate the choice against current options and either return choice 
        # or have the user try again.
        if validate_menu_choice(choice, options["main"]):
            if choice == "s":
                return "search" # Signal to return search
            elif choice == "q":
                return "quit"   # Signal to quite the program
            else:
                # Map the numeric choice to a glossary name
                glossary_index = int(choice) -1
                return list(glossaries.keys())[glossary_index]
        else: 
           print(f"'{choice}' is not a valid choice, please try again.\n")
        




def gloss_menu(glossary, glossary_name):
    """
    Presents options to move through the selected glossary:
        1. View an entry
        2. View all terms
        3. View the entire glossary
        4. Search the glossary for a keyword
        b. Exit the glossary menu to the main menu
        q. Exit the program
    """
    while True:
        display_glossary_menu(glossary_name)
        choice = get_input("Please make a choice from the above options.")
        if validate_menu_choice(choice, options["gloss"]):
            return choice
        else:
            print(f"'{choice}' is not a valid choice, please try again.")
                
            
        

