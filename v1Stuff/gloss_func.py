'''
The glossary function that calls a specific glossary into the main glossary program in 
glossary.py
'''


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

    return glossaries.get(gloss_name.lower(), None)

