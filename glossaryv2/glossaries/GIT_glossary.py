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
    'git remote':           'Checks which remote servers are currently configured. If you\n\t\tcloned a remote server, it should at least show you "origin".\n\n\t\t'
                            '-v: Prints the URLs for each shortname used to fetch and push to the remote.\n\n\t\t'
                            '--add <shortname> <url>: adds a new remote repo explicitly.',    

    'git clone':            'Creates a local copy of a GIT repo, including all files and\n\t\t'
                            'directories, full commit history, branches, and tags, and repo \n\t\t'
                            'metadata. It checks out the latest commit from the default\n\t\t'
                            'branch.The cloned repo has a link to the remote repo named \n\t\t'
                            '"origin" and is used to fetch or push changes.\n\t\t'
                            'It automatically sets up the local repo to track the remote master.\n\n\t\t'
                            'Syntax:\n\t\t\t git clone <repo_url> [</path/to/dest_folder>]\n\n\t\t'
                            '--branch <branch>: Clones the specified branch.\n\t\t'
                            '--depth <#>: Creates a shallow clone with only the specified\n\t\t\t' 
                            'number of previous commits.\n\t\t'
                            '--mirror: Creates a bare clone that mirrors the original repo; for backups',

    'git fetch':             'Pulls all data from the specified remote project that is not\n\t\t'
                            'on the local machine. If cloning a repo, it automatically \n\t\t'
                            'creates the remote repo under the name "origin". Fetched repos\n\t\t'
                            'do not merge the pulled work, that must be done manually.\n\n\t\t'
                            'Syntax:\n\t\t\tgit fetch <remote_name>',

    'git pull':             'Pulls and merges a remote branch into your current work.',

    'git config':           'Used to configure and customize GIT settings like user \n\t\t'
                            'information, editor preferences, aliases, and behavior.\n\n\t'
                            '--system: Setting will apply to all users and is usually located\n\t\t'
                            'in /etc/gitconfig\n\n\t\t'
                            '--global: Applies to the user who set it but all their repos.\n\t\t'
                            'It is located ~/.gitconfig\n\n\t\t'
                            '--local: Only affects the current repo. It is located within the\n\t\t\t'
                            '.git/config directory in the repo.\n\n\t\t'
                            'Common settings: user.name, user.email, core.editor, alias.co\n\t\t'
                            'Syntax: git config [<config_level>] <config_to_set> <setting> \n\n\t\t'
                            'Viewing configs:\n\t\t\t'
                            'git config --list: lists all configs.\n\t\t\t'
                            'git config user.name: Lists all configs for the specified user',

    'git push':             'Uploads local repository changes to a remote repository. \n\t\t'
                            'It sends committed changes from your local branch to the corresponding \n\t\t'
                            'remote branch, updating the remote repository with any new commits. \n\t\t'
                            'Common syntax: \n\t\t'
                            '   git push <remote> <branch>  \n\t\t'
                            '-- <remote>: The name of the remote repository (e.g., origin). \n\t\t'
                            '-- <branch>: The local branch you want to push to the remote. \n\t\t'
                            'Example: \n\t\t'
                            '   git push origin main  \n\t\t'
                            'This pushes the local "main" branch to the "origin" remote repository.',

}

