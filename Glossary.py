#!/usr/bin/env python3

# A glossary program that calls outsidepython dictionary "databases" and enables searching for 
# the key to provide the key's definition and examples. 
# 
# Current "Databases"
# GIT_glossary
# linux_network_cmds
# Ubuntu_CMDs
# vim_CMDs



from glossaries import *
import sys
from glossaries.GIT_glossary import glossary as GIT_glossary

def gloss_func(gloss_name):
    '''
    Output the glossary as the return of the function based on the argument provided
    
    Arguments:
        gloss_name (str): The name of the glossary to return
    '''
    # Dictionary that maps glossary names to actually glossary databases
    glossaries = {
        'python': python_glossary,
        'git': GIT_glossary,
        'linux_networking': linux_network_cmds,
        'ubuntu': ubuntu_cmds,
        'vim': vim_cmds
    }
    if gloss_name == "end":
        sys.exit()
    else:
        return glossaries.get(gloss_name.lower(), None)


def print_term(term, definition):
    '''
    Check for unusual terms.
    '''
    if ' ' in term:
        print(f'\n\n\t{term}: {definition}')
    elif 'ctrl-c' in term:
        print(f'\n\n\t{term.upper()}: {definition}')
    else:
        print(f'\n\n\t{term}: {definition}')

# Main loop for interacting with the glossary
active = True

# Glossary selection prompt
prompt = 'Please select a glossary from the following: \n'
prompt += 'Python\nGIT\nLinux Networking\nUbuntu\nVIM\n\n'
raw_input = input(prompt).lower()

while active:
    # Call the appropriate glossary function
    glossary = gloss_func(raw_input)
    if glossary:
        # Select the term
        prompt4term = 'Which term would you like to see?\n'
        prompt4term += 'If you want to see the entire glossary, type "all".\n'
        prompt4term += 'Type "end" to close the program or "search" to see all possible terms\n'
        
        # Place the term into a checkable var
        term = input(prompt4term)
    
        if term in glossary.keys():
            # place the glossary into a var
            definition = glossary[term]
            print_term(term, definition + '\n\n')
        
        # So the user can exit the program cleanly
        elif term == 'end':
            active = False
        
        # Prints the entire glossary
        elif term == 'all':
            for word, value in glossary.items():
                print_term(word, value)
        
        # Enables searching through the available terms
        elif term == 'search':
            for key in glossary.keys():
                print('\t' + key + '\n')
    
        # error handling for bad input
        else:
            print('The term "' + term + '" is not in this glossary, please try again.\n')

    elif glossary == "end":
        break
    
    else:
        print(f"{raw_input} is not a currently supported glossary. Please choose again.\n")
