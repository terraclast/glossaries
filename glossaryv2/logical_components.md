# Logical Components for the Glossary Rolodex

1. Glossary Loader

2. User Interface
    a. Menues
    b. User input

3. Glossary Operations
    a. Search via terms
    b. Display definitions
    c. List terms

4. Error Handling
    Graceful handling of:
    a. invalid inputs
    b. missing data


## File Structure 

glossaryv2/
├── glossaries/                # Folder for glossary files
│   ├── GIT_glossary.py
│   ├── python_glossary.py
│   └── <other glossaries>.py
├── utils/
│   ├── glossary_loader.py      # Handles loading glossaries
│   ├── error_handler.py        # Handles error messages (optional)
│   └── <future utilities>.py
├── main.py                     # Main program logic
├── README.md                   # Documentation for the project
└── logical_components.md       # Detailed breakdown of logical components

## Component Logic

### glossary_loader

    1. Identify all glossary files in the designated directory
    2. Load their content into a usable format
    3. Return all glossaries as structured data for the rest of the program to use. 
