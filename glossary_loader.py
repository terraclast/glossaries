import os
import importlib

def file_reader(directory="./glossaries"):
    '''
    Read the existant glossaries in the designated glossary directory.
    Return a list of Python files.
    '''
    python_files = [
        f for f in os.listdir(directory) 
        if f.endswith("py") and os.path.isfile(os.path.join(directory, f))
    ]    

    # print("Python files found: ", python_files) # Debugging print
    return python_files


def glossary_importer(): 
    '''
    Import a glossary. 
    '''
    glossaries = {}
    python_files = file_reader("./glossaries")
    # Check if there are glossary files in the glossaries dir.
    if not python_files:
        print("No Python files found in the directory.")
        return {}
#    else:
#        print("Files to print: ", python_files)

    for raw_file_name in python_files:

        try: 
#           Remove the .py extension
            processed_file_name = raw_file_name.replace('.py', '')

#           Create the module name dynamically
            module_name = f"glossaries.{processed_file_name}"
            
#           Import the module dynamically
            module = importlib.import_module(module_name)
            glossary = getattr(module, "glossary", None)
            if glossary is None:
                print(f"The module, {module_name}, does not contain a 'glossary'.")
            else:
                glossaries[processed_file_name] = glossary
        except Exception as e:
            # Handle any errors during import
            print(f"Failed to import module, '{module_name}': {e}")
    
    return glossaries

# Load glossaries
loaded_glossaries = glossary_importer()

# Display loaded glossaries
print("Loaded Glossaries: ")
for name in loaded_glossaries.keys():
    print(f" - {name}")
