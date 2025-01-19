import os
import importlib
import json
import py_compile
from utils.validation import validate_glossary

def is_valid_python_file(file_path):
    '''
    Check that a python dictionary is properly formed.
    '''
    try:
        py_compile.compile(file_path, doraise=True)
        return True
    except py_compile.PyCompileError:
        return False

def file_reader(directory="./glossaries", verbose = True):
    '''
    Read the existant glossaries in the designated glossary directory.
    Return a list of Python and JSON files, excluding __init__.py.
    '''
    glossary_files = [
        f for f in os.listdir(directory) 
        if f.endswith("py") or f.endswith("json") 
            and os.path.isfile(os.path.join(directory, f))
            and f != "__init__.py"  # Exclude __init__.py
    ]    

    # print("Glossary files found: ", glossary_files) # Debugging print
    return glossary_files


def glossary_importer(): 
    '''
    Import a glossary. 
    '''
    glossaries = {}
    glossary_files = file_reader("./glossaries")
    # Check if there are glossary .files in the glossaries dir.

    if not glossary_files:
        print("No glossary files found in the directory.")
        return {}

    for raw_file_name in glossary_files:
        try: 
            full_path = os.path.join("./glossaries", raw_file_name)
            # Process glossary filenames
            if raw_file_name.endswith(".py"):
                # Process python filenames
                processed_file_name = raw_file_name.replace('.py', '')
                # Create the module name dynamically
                module_name = f"glossaries.{processed_file_name}"
                
                # Import the module dynamically
                module = importlib.import_module(module_name)
                glossary = getattr(module, "glossary", None)
                if glossary is None:
                    print(f"The module, {module_name}, does not contain a 'glossary'.")
                else:
                    # Validate and process .py glossaries
                    if not is_valid_python_file(full_path):
                        print(f"ERROR: Malformed Python glossary '{raw_file_name}', skipping.")
                        continue
                    else:
                        validated_glossary = validate_glossary(processed_file_name, glossary)
                        if validated_glossary:
                            glossaries[processed_file_name] = validated_glossary

            # Validate and process .json glossaries
            elif raw_file_name.endswith(".json"):

                with open(full_path, "r", encoding="utf-8") as f:
                    glossary = json.load(f)

                validated_glossary = validate_glossary(raw_file_name, glossary)
                if validated_glossary:
                    glossaries[raw_file_name.replace('.json', '')] = validated_glossary

        except Exception as e:
            # Handle any errors during import
            if raw_file_name.endswith(".py") and raw_file_name != "__init__.py":
                print(f"ERROR: Failed to import Python glossary '{module_name}': {e}")
            elif raw_file_name.endswith(".json"):
                print(f"ERROR: Failed to process JSON glossary '{raw_file_name}': {e}")
    
    return glossaries

# Load glossaries
loaded_glossaries = glossary_importer()

