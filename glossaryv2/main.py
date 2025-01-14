from utils.glossary_loader import glossary_importer 
from utils.glossary_ops import view_all_terms, view_all_entries, view_entry, search_keyword
from utils.menu import main_menu, gloss_menu

glossaries = glossary_importer()
ACTION_QUIT = "quit"
ACTION_SEARCH = "search"

print("\nLoaded Glossaries:")
for glossary_name in glossaries.keys():
    print(f" - {glossary_name}")
print("\n")


def get_cased_input(prompt):
    """
    Take in case sensitive input from users.
    """
    return input(prompt).strip()


while True:
    selected_glossary_name = main_menu(glossaries)
    
    if selected_glossary_name == ACTION_QUIT:
        print("Goodbye!")
        break
    elif selected_glossary_name == ACTION_SEARCH:
        keyword = get_cased_input("Enter a keyword to search across all glossaries: ")
        search_keyword(glossaries, keyword, scope="all")

    else:
        choice = gloss_menu(glossaries[selected_glossary_name], selected_glossary_name)
        if choice in range(1, 4):
            choice = int(choice)
        match choice:
            case 1:     # View an entry
                term = get_cased_input("Enter a term: ")
                view_entry(glossaries[selected_glossary_name], term)
            case 2:     # View all terms
                view_all_terms(glossaries[selected_glossary_name])
            case 3:     # View the entire glossary
                view_all_entries(glossaries[selected_glossary_name])
            case 4:     # Search the current glossary
                keyword = get_cased_input("Enter a keyword: ")
                search_keyword(glossaries, keyword, scope="single", single_gloss_name=selected_glossary_name)
            case "b":   
                continue    # Return to the main menu
            case "q":
                print("Goodbye!")
                break
