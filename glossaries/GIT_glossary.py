glossary = {
    # Glob Patterns
    '*':                    'Matches zero or more of any character other than "/". \n\t\t'
                            'If you are looking for directories, it will not go through them. \n\t\t'
                            'Ex: \n\t\t\twill match: lib/glob.dart \n\t\t\twill not match: '
                            'lib/src/utils.dart',

    '**':                   'Matches across directories: works like * but includes "/". \n\t\t'
                            'If at the beginning, it will not match absolute paths or paths \n\t\t'
                            'beginning with ../. \n\t\tEx: \n\t\t\twill match: lib/glob.dart, '
                            'lib/src/utils.dart, etc.',

    '?':                    'Matches a single character.',

    '[]':                   'The OR operator, will find any character within the brackets.',

    '[a-zA-Z]':             'The hyphen inside brackets indicates a range match. \n\t\t'
                            'This example matches all alphabetic characters, both lower and upper case.',

    '{..., ...}':           'Matches one of several possibilities, functioning like an OR operator, \n\t\t'
                            'but can work with individual regex patterns. \n\t\tEx: \n\t\t\tlib/{*.dart,src/*} '
                            'will match both lib/glob.dart and lib/src/data.txt.',

    '\\':                   'Escape character. To match a normally special character, preface it \n\t\t'
                            'with \\ (backslash).',

    # Git Commands
    'git --help':         'Shows the manual (man) page for Git commands.',

    'man git':            'Shows Git\'s manual (man) page.',

    'git branch':         'Shows the various branches in the repository.',

    'git show':           'Displays all the changes in the main branch.',

    'git show <branch>':  'Displays the changes in a specified branch.',

    'git clone <url_to_project> <name_of_dir_for_project>': 
                            'Downloads a full copy of all data associated with a particular project \n\t\t'
                            'repository: Every file, folder, and the entire commit history. \n\t\t'
                            'Creates a directory, initializes a .git directory, and pulls all data.',

    'git add <file | directory>': 
                            'Adds the specified file or directory to the staging area.',

    'git status':         'Prints the current status of all your files; whether they are in staging \n\t\t'
                            'or committed.',

    'git diff':           'Displays the differences between what is in the working directory and \n\t\t'
                            'what is staged. \n\t\t--staged: Shows differences between staged and committed files. \n\t\t'
                            '--cached: Prints changes staged so far.',

    'git commit <file | directory>': 
                            'Commits the specified file or directory from the staging area. \n\t\t'
                            '-m: Adds a commit message. \n\t\t-v: Adds the diff output to remind you of changes. \n\t\t'
                            '-a: Commits all tracked files without staging.\n\t\t'
                            '--amend: Amends a previous commit. If you forget something in a \n\t\t\tcommit, this enables you to reform the commit and not have a ton of\n\t\t\tcommits.',

    'git rm <file>':      'Removes the file from the system and staging area. \n\t\t'
                            '-f: Forces removal. \n\t\t--cached: Removes the file from staging without deleting it \n\t\t'
                            'from the system.',

    'git mv <file_from> <file_to>': 
                            'Moves a file from one path to another, combining git rm and git add in \n\t\t'
                            'one command.',

    'git log':            'Displays the commit log in descending chronological order. \n\t\t'
                            '-p: Shows diffs for each log entry. \n\t\t--pretty: Changes the log output format. \n\t\t'
                            '--since: Limits log output by date. \n\t\t--author: Filters commits by author.',

    'git reset HEAD':     'Removes the current staging. \n\t\t--hard: Resets the working directory and index \n\t\t'
                            'to match HEAD (dangerous).',

    'git restore <file>': 'Discards changes made to the specified file in the working directory.\n\t\t'
                            '--staged <file>: Will unstage a currently staged file or directory.\n\t\t',

    'git checkout -- <file>': 
                            'Restores working tree files to their last committed state. This can be \n\t\t'
                            'dangerous.',
# Working with Remote Repositories 
    
}

