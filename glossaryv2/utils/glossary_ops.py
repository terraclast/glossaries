
def view_all_terms(glossary):
    """
    Displays all terms (glossary keys) in the specified glossary.
    """

    if not glossary:
        print("The requested glossary is empty.")
        return

    terms = sorted(glossary.keys()) # Sort alphabetically
    print('Terms in this glossary: ')
    for term in terms:
        print(f" - {term}")

def view_all_entries(glossary):
    """
    Display all entries in a specified glossary (term/key, definition/value).
    """
    if not glossary:
        print("The requested glossary is empty.")
        return

    print("Glossary Entries (sorted alphabetically): ")
    for term in sorted(glossary.keys()):
        for term, data in glossary.items():
            print(f"\n{term}:")
            if isinstance(data, dict):
                # handle nested data
                for key, definition in data.items():
                    print(f"    {key}: {definition}")
            else:
                # handle flat data
                print(f"    {data}")

def view_entry(glossary, term):
    """
    Display the requested term and its associated deffinition.
    """
    if not glossary:
        print("The requested glossary is empty.")
        return

    data = glossary.get(term)
    if data:
        print(f"{term}")
        if isinstance(data, dict):
            #   handle nested data
            for key, value in data.items():
                print(f"    {key}: {value}")
        else:
            # Handle flat data
            print(f":    {data}")

    else:
        print(f"The requested term, {term}, does not currently exist in the glossary.")

def search_keyword(glossaries, keyword, scope="all", single_gloss_name=None):
    """
    Search one or all glossaries for either a term or a keyword in a definition.
    """
    if not glossaries:
        print("No glossaries available.")
        return

    keyword = keyword.lower()
    found = False
    results = []

    for gloss_name, glossary in glossaries.items():
        # Limit to the specified glossary if the scope is "single"
        if scope == "single" and gloss_name != single_gloss_name:
            continue

        for term, definition in glossary.items():
            # Ensure that both term and definition are strings
            term_lower = term.lower() if isinstance(term, str) else ""
            # Check for nested data structure
            if isinstance(definition, dict):
                for key, value in definition.items():
                    if keyword in term_lower or (isinstance(value, str) and keyword in value.lower()):
                        results.append(f"[{gloss_name}] {term} ({key}): {value}")

            elif isinstance(definition, str): 
                # Check if data is flat
                definition_lower = definition.lower() 
                if keyword in term_lower or keyword in definition_lower:
                    results.append(f"[{gloss_name}] {term}: {definition}")
    if results:
        for result in results:
            print(result)
    else:
        print(f"No results were found for keyword '{keyword}'.")
