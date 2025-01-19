# Glossary Application

## Overview

This Glossary Application is a modular tool designed to load, display, and search glossaries in both Python and JSON formats. It handles flat and nested data structures, making it versatile for a wide range of glossary styles, including technical dictionaries with hierarchical entries.

---

## Features

- **Dynamic Glossary Loading**: Supports both Python and JSON glossaries.
- **Hierarchical Display**: Handles nested data structures using a recursive approach.
- **Search Functionality**: Allows users to search keywords across all glossaries or within a specific glossary.
- **Interactive Menus**: Provides a main menu and glossary-specific menus for smooth navigation.
- **Validation and Error Handling**: Ensures robust processing of user input and glossary files.
- **Customizable Modules**: Modular design for extensibility and maintainability.

---

## File Structure

```plaintext
glossaryv2/
├── glossaries/                # Folder for glossary files
├── utils/
│   ├── glossary_loader.py     # Handles loading and validation of glossaries
│   ├── glossary_ops.py        # Core glossary operations (viewing, searching)
│   ├── menu.py                # Menu display and routing
│   ├── validation.py          # Input validation utilities
│   └── error_handling.py      # (Optional) Error management
├── main.py                    # Entry point for the application
├── README.md                  # Documentation for the project
└── logical_components.md      # Logical map of all project functions
```

## Usage

### **Prerequisites**
- Python 3.7 or later
- Compatible glossaries in Python or JSON format.

### **Running the Application**
1.  Place your glossaries in the glossaries/ directory.
2.  Run the application:

> python3 main.py

3.  Follow the on-screen menu to navigate glossaries and perform operations.

## Glossary Features

- View Entry: Displays a specific term and its definition.
- View All Terms: Lists all terms in a glossary.
- View Entire Glossary: Displays all terms and definitions in a glossary.
- Search Keyword: Searches for a keyword in one or all glossaries.

## Contribution

Contributions are more than welcome! If you want to add new features, just make sure your code is modular and follows the existing style. Please submit a pull request with clear documentation.

## License

This project is licensed under the MIT License.
