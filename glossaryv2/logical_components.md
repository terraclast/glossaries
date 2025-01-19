# Logical Components for the Glossary Rolodex

1. [X] Glossary Loader `glossary_loader.py`


2. [x] Menues
    a. Main menu
        1. Display all loaded glossaries
        2. Search entire set of glossaries for the specified keyword
        3. Provide the ability to quit the program
    b. Glossary menus
        1. View terms (keys)
        2. View specified entries (key:value pair)
        3. View entire glossary (with a less-type option) (all key:value pairs)
        4. Search the specified glossary for a keyword
        5. Provide the ability to exit the glossary sub-menu
        6. Provide the ability to exit the entire program
    c. User input collection
    d. Routing user choices to appropriate functions
3. [x] Input validation
    b.  Input validation
4. [x] Error handling -- handled within the local modules. 


5. [X] Glossary Operations `glossary_ops.py`
    a. Search terms across glossaries:  `search_keyword(glossaries, keyword)` -- Search for a term or keyword either in the current glossary or across all glossaries (if on the main menu)
    b. Display entry:                   `view_entry(glossary, term)` -- View a specific term/definition pair.
    c. List terms:                      `view_all_terms(glossary)` -- View all terms contained in the specified glossary.
    d. List all entries:                `view_all_entries(glossary)` -- View all term/definition pairs contained in a glossary.
    
6. [x] Main Program `main.py` (completing as other components are completed)
    a. Coordinates interactions between modules and maintains the program flow.
    b. Calls ui functions for user input and glossary_ops for operations. 

---

## File Structure 

glossaryv2/
├── glossaries/
├── utils/
│   ├── glossary_loader.py
│   ├── glossary_ops.py
│   ├── menu.py             # Menu display and routing
│   ├── validation.py       # Input validation utilities
│   └── error_handling.py   # Optional: Error management
├── main.py
├── README.md
└── logical_components.md

---

## Component Locations

├── glossary_loader.py
│   ├── file_reader(directory="./glossaries", verbose=True)
│   │   Reads files in the specified directory, filtering for valid Python and JSON files.
│   ├── is_valid_python_file(file_path)
│   │   Checks if a Python file is properly formed.
│   ├── glossary_importer(directory="./glossaries", verbose=True)
│       Imports and validates glossaries, returning a dictionary of valid ones.

├── glossary_ops.py
│   ├── view_all_terms(glossary)
│   │   Displays all terms (keys) in a glossary, sorted alphabetically.
│   ├── view_all_entries(glossary)
│   │   Displays all entries (key-value pairs) in a glossary, handling nested data.
│   ├── view_entry(glossary, term)
│   │   Displays the requested term and its associated definition, supporting nested dictionaries.
│   ├── nest_digger(entry, indent=0)
│   │   Recursively handles nested dictionaries and prints them with appropriate indentation.
│   ├── search_keyword(glossaries, keyword, scope="all", single_gloss_name=None)
│       Searches for a keyword or term in one or all glossaries and prints matching entries.

├── menu.py
│   ├── generate_main_menu_options(glossaries)
│   │   Dynamically generates valid options for the main menu based on available glossaries.
│   ├── display_main_menu(glossaries)
│   │   Displays the main menu, showing available glossaries and static options.
│   ├── display_glossary_menu(glossary_name)
│   │   Displays the menu for a specific glossary, listing possible actions.
│   ├── get_input(prompt)
│   │   Takes user input, trims spaces, and converts it to lowercase.
│   ├── main_menu(glossaries)
│   │   Manages the main menu logic, handling user selection and routing to the appropriate functionality.
│   ├── gloss_menu(glossary, glossary_name)
│       Handles interactions within a selected glossary, routing options like viewing entries or searching.

├── validation.py
│   ├── validate_menu_choice(choice, options)
│   │   Checks if a user's input matches available menu options and converts it to the correct data type.
│   ├── validate_numeric_choice(choice, min_val, max_val)
│   │   Validates whether a numeric input falls within a specified range.
│   ├── validate_term(term, glossary)
│   │   Checks if a term exists in a given glossary.
│   ├── validate_keyword(keyword)
│   │   Validates a keyword for searching, ensuring it’s non-empty.
│   ├── validate_glossary(glossary_name, glossary)
│       Validates the structure of a glossary (Python dict or JSON object).

├── main.py
│   ├── Main Logic
│       Integrates all modules, starting with loading glossaries and routing user interactions through menus and validation.

---

### glossary_loader

    1. Identify all glossary files in the designated directory
    2. Load their content into a usable format
    3. Return all glossaries as structured data for the rest of the program to use. 

---

## Future add ons

- The ability to dynamically add term/def pairs to a glossary. 
