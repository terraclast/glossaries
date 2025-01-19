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
    'git --help':           'Shows the manual (man) page for Git commands.',

    'man git':              'Shows Git\'s manual (man) page.',

    'git branch':           'Shows the various branches in the repository.\n\n\t\t'
                            '<name>: When appended to git branch, it creates a new branch but does\n\t\t'
                            'not move the HEAD to the new branch. Moving branches moves the HEAD\n\t\t'
                            'and it reverts all your files to what the specified branch points to.\n\t\t'
                            'Any changes diverge from this point on. If Git cannot move you cleanly\n\t\t'
                            'to the branch (changing files in the pwd to the last commit of the \n\t\t'
                            'branch you changed to) it won\'t allow the move.',

    'git show':             'Displays all the changes in the main branch.',

    'git show <branch>':    'Displays the changes in a specified branch.',

    'git clone <url_to_project> <name_of_dir_for_project>': 
                            'Downloads a full copy of all data associated with a particular project \n\t\t'
                            'repository: Every file, folder, and the entire commit history. \n\t\t'
                            'Creates a directory, initializes a .git directory, and pulls all data.',

    'git add <file | directory>': 
                            'Adds the specified file or directory to the staging area.',

    'git status':           'Prints the current status of all your files; whether they are in staging \n\t\t'
                            'or committed.',

    'git diff':             'Displays the differences between what is in the working directory and \n\t\t'
                            'what is staged. \n\t\t--staged: Shows differences between staged and committed files. \n\t\t'
                            '--cached: Prints changes staged so far.',

    'git commit <file | directory>': 
                            'Commits the specified file or directory from the staging area. \n\t\t'
                            '-m: Adds a commit message. \n\t\t-v: Adds the diff output to remind you of changes. \n\t\t'
                            '-a: Commits all tracked files without staging.\n\t\t'
                            '--amend: Amends a previous commit. If you forget something in a \n\t\t\tcommit, this enables you to reform the commit and not have a ton of\n\t\t\tcommits.',

    'git rm <file>':        'Removes the file from the system and staging area. \n\t\t'
                            '-f: Forces removal. \n\t\t--cached: Removes the file from staging without deleting it \n\t\t'
                            'from the system.',

    'git mv <file_from> <file_to>': 
                            'Moves a file from one path to another, combining git rm and git add in \n\t\t'
                            'one command.',

    'git log':              'Displays the commit log in descending chronological order. \n\t\t'
                            '-p: Shows diffs for each log entry. \n\t\t--pretty: Changes the log output format. \n\t\t'
                            '--since: Limits log output by date. \n\t\t--author: Filters commits by author.\n\t\t'
                            '--decorate: Shows where branch pointers are pointing.\n\t\t'
                            '--oneline: Shorthand for "--pretty=oneline --abbrev-commit" and shows\n\t\t\t'
                            'the full 40-byte hext commit object name.\n\n\t\t'
                            '--all: Displays logs for all branches.\n\t\t'
                            '--graph: Draws a graphical representation of the commit history.\n\n\t\t'
                            'git log <branch>: Git log will only show you commits for the branch you \n\t\t\t'
                            'are currently on (without using --all). If you want to see the log for\n\t\t'
                            'other branches, it must be specified.',

    'git reset HEAD':       'Removes the current staging. \n\t\t--hard: Resets the working directory and index \n\t\t'
                            'to match HEAD (dangerous).',

    'git restore <file>':   'Discards changes made to the specified file in the working directory.\n\t\t'
                            '--staged <file>: Will unstage a currently staged file or directory.\n\t\t',

    'git checkout -- <file>': 
                            'Restores working tree files to their last committed state. This can be \n\t\t'
                            'dangerous.\n\t\tOptions:\n\t\t\t'
                            '-b <branch_name> : Creates a new branch.\n\n\t\t'
                            'Use git checkout <branch> to change to the <branch> branch; moves the\n\t\t'
                            'HEAD to the branch. This will only move the head on the branch you are\n\t\t'
                            'currently in, leaving all other branches where they were.',
# Working with Remote Repositories 
    'git remote':           'Checks which remote servers are currently configured. If you\n\t\tcloned a remote server, it should at least show you "origin".\n\n\t\t'
                            '-v: Prints the URLs for each shortname used to fetch and push to the remote.\n\n\t\t'
                            '--add <shortname> <url>: adds a new remote repo explicitly.\n\n\t\t'
                            'rename <old_name> <new_name>: renames the remote\'s short name and all\n\t\t'
                            'remote tracking branches.\n\t\t\t'
                            'Example:\n\t\t\t\tgit remote rename pb paul\n\t\t\t'
                            'This changes the reference from pb/master to paul/master\n\t\t'
                            'remote remove|rm <remote>: Removes a remote with the specified name.\n\t\t'
                            'All remote-tracking branches and configs are also deleted.\n\n\t\t', 

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
                            'git config user.name: Lists all configs for the specified user\n\n\t'
                            'Creating alieses:\n\t\t'
                            'git config --[global | local] alias.<name> <whats_aliased>\n\t\t\t'
                            'Example:\n\t\t\tgit config --global alias.co checkout\n\t\t\t'
                            'Instead of writing "git checkout" you just have to write "git co"',

    'git push':             'Uploads local repository changes to a remote repository. \n\t\t'
                            'It sends committed changes from your local branch to the corresponding\n\t\t'
                            'remote branch, updating the remote repository with any new commits. \n\t\t'
                            'Syntax: \n\t\t'
                            '   git push <remote> <branch> <tag_name> \n\t\t'
                            '-- <remote>: The name of the remote repository (e.g., origin). \n\t\t'
                            '-- <branch>: The local branch you want to push to the remote. \n\t\t'
                            'Example: \n\t\t'
                            '   git push origin main  \n\t\t'
                            'This pushes the local "main" branch to the "origin" remote repository.\n\n\t\t'
                            '-- <tag_name>: Pushes the specified tag to the remote.\n\t\t'
                            'Options:\n\t\t\t'
                            '--delete <tag_name>: deletes the specified tag from the remote.',

    'git show <remote>':    'Displays information about a specified remote: diffs from the same \n\t\t'
                            'uploaded file but the diff is between the last push and the previous.',
    
    'tags':                 'Tags enable marking "special" versions of the code base. Typically\n\t\t'
                            'used to mark things like v1.0, v2.0, etc.\n\t\tWorking with tags:\n\t\t\t'
                            'List existing tags\n\t\t\tTag creation and deletion.\n\t\tTypes:\n\n\t\t\t'
                            'Tag Creation:\n\t\t\t\tlightweight -- A pointer to a specific commit. \n\t\t\t\t'
                            'annotated -- Stored as full objects in the Git database; suggested tag type:\n\t\t\t\t\t'
                            'Checksummed\n\t\t\t\t\tTagger name\n\t\t\t\t\tEmail\n\t\t\t\t\t'
                            'Date\n\t\t\t\t\tMessage\n\t\t\t\t\tGNU Privacy Guard (GPG) signage.\n\t\t\t\t'
                            '-a: indicates the annotated type.\n\t\t\t\t-m: indicates the message\n\t\t\t\t'
                            '-s: Creates a GPG signed tag.\n\n\t\t\t\t'
                            '-d: Deletes a tag specified by <tag_name>\n\t\t\t\t\tSyntax: git tag -d <tag_name>\n\t\t\t\t\t'
                            'Does not remove tags from remote servers.\n\t\t\t\t\t'
                            'Deleting from remote servers; there are two options:\n\t\t\t\t\t\t'
                            'git push <remote> :refs/tags/<tag_name> -- the null val before ":" gets pusheed \n\t\t\t\t\t\t' 
                            'to the remote server, deleting what was originally there.\n\t\t\t\t\t\t'
                            'git push origin --delete <tag_name> -- Much more intuitive.\n\t\t'
                            'Checking out tags:\n\t\t\t'
                            'git checkout <tag_name>:\n\t\t\t'
                            'Checks out the specified tag in a "detached HEAD" state. This means\n\t\t\t'
                            'You can make and commit changes but they will not be accessable\n\t\t\t'
                            'except with the exact commit hash. It is better to create a branch\n\t\t\t'
                            'work in a detached state:\n\t\t\t\tgit checkout -b <branch_name> <tag_name>',
    
    'git tag':              'Lists all currently extant tags. Listing is assumed with this cmd.\n\t\t\t'
                            '-l | --list:  Explicitly asking for a list.\n\t\t\tYou can also '
                            'search for and list specific tags or groups of tags:\n\t\t\t'
                            'Syntax:\n\t\t\tgit tag <tag_name>\n\n\t\t\t'
                            'Example:\n\t\t\t\tgit tag -l 1.85*\n\t\t\t'
                            'Lists all tags that start with "1.85", searching this way requires\n\t\t\t'
                            '-l or --list because of the wildcard char "*".\n\n\t\t'
                            'Syntax 1:\n\t\t\tgit tag -a <tag_name> -m "<msg>"\n\t\t'
                            'The above creates an annotated tag (-a) with tag name <tag_name> and\n\t\t'
                            'message (-m) <msg>. The message works just like the commit -m option.\n\t\t'
                            'Syntax 2:\n\t\t\tgit tag <tag_name>\n\t\t'
                            'Creates just the tag without any of annotated\'s metadata, i.e. a\n\t\t'
                            'lightweight tag.\n\n\t\t'
                            'Tagging later: If you\'ve moved past a particular point but must tag\n\t\t'
                            'that point:\n\n\t\t\t'
                            'Syntax:\n\t\t\t\tgit tag -a <tag_name> <1st_7_hash_digits>\n\t\t'
                            '<1st_7_hash_digits> -- The first 7 digits of the commit hash of the tag point.\n\n\t\t'
                            'Sharing tags: git push does not, by default push tags to remotes. To\n\t\t'
                            'do this, you must be explicit in the push:\n\t\t\t'
                            'Syntax:\n\t\t\t\tgit push <remote_branch> [<tag_name> | --tags]\n\t\t'
                            '--tags: Signals to push all tags, regardless of whether they are\n\t\t'
                            'lightweight or annotated.\n\t\t--follow-tags: Signals to only push annotated tags.\n\n\t\t',

    'aliases':              'Enables execution of a partially typed, but aliased cmd. Set up with "git config".',
    'branching':            'Git branching is lightweight and fast. Git stores data as snapshots.\n\t\t'
                            'There are pointers to each snapshot. Branches are the pointers to the\n\t\t'
                            'snapshots.\n\n\t\t'
                            'Creating a new branch:\n\t\t\t'
                            'Creates a new pointer to the commit you\'re currently on: where the\n\t\t\t.'
                            'HEAD is currently pointing.\n\t\t'
                            'To switch branches, use git checkout.',
    'HEAD':                 'A pointer to the local branch you are currently on.',
    'git switch':           'Replaces git checkout -b <branch> for Git versions >= 2.23.\n\t\t\t'
                            'git switch <branch>: Switches to an existing branch\n\t\t\t'
                            'git switch [-c | --create] <new_branch>: Creates and switchest to a new branch.\n\t\t\t'
                            'git switch - : Returns to the previously checked out branch.\n\n\t\t\t'
                            'Options:\n\t\t\t\t'
                            '-c | --create: Creates a branch with name <new_branch>.',
}

