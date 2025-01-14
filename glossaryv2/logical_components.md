# Logical Components for the Glossary Rolodex

1. [X] Glossary Loader `glossary_loader.py`


2. [ ] Menues
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
3. [ ] Input validation
    b.  Input validation
4. [ ] Error handling 


5. [X] Glossary Operations `glossary_ops.py`
    a. Search terms across glossaries:  `search_keyword(glossaries, keyword)` -- Search for a term or keyword either in the current glossary or across all glossaries (if on the main menu)
    b. Display entry:                   `view_entry(glossary, term)` -- View a specific term/definition pair.
    c. List terms:                      `view_all_terms(glossary)` -- View all terms contained in the specified glossary.
    d. List all entries:                `view_all_entries(glossary)` -- View all term/definition pairs contained in a glossary.
    
6. Main Program `main.py`
    a. Coordinates interactions between modules and maintains the program flow.
    b. Calls ui functions for user input and glossary_ops for operations. 


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

## Component Logic

### glossary_loader

    1. Identify all glossary files in the designated directory
    2. Load their content into a usable format
    3. Return all glossaries as structured data for the rest of the program to use. 


## Future add ons

- keyword search in both the main menu and the glossary menus.
- When loading the full glossaries dir, have the dictionaries append to each other, mixing terms, but try to have the terms identified with their glossary. 
- The ability to dynamically add term/def pairs to a glossary. 
