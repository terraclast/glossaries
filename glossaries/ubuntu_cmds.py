glossary = {
    # System Information Commands
    'open terminal window hotkey': 'ctrl+alt+t \n\t\tAssumes the shell is Bash.',

    '$ ls /boot | grep vmlinuz-': 'Prints all available kernels that are available on the box.',

    '$ lsof':                'Lists open files.',

    '$ uname':               'Prints system information. \n\t\t'
                             '-a: Prints all information. \n\t\t'
                             '-s: Prints kernel info. \n\t\t'
                             '-n: Prints the network node hostname. \n\t\t'
                             '-r: Prints the kernel release. \n\t\t'
                             '-v: Prints the kernel version. \n\t\t'
                             '-m: Prints the machine hardware name. \n\t\t'
                             '-p: Prints the processor type (non-portable). \n\t\t'
                             '-i: Prints the hardware platform (non-portable). \n\t\t'
                             '-o: Prints the operating system. \n\t\t'
                             '--version: Displays version info of uname and exits.',

    '$ lscpu':               'Prints detailed CPU information.',

    '$ lshw':                'Shows detailed hardware information. Run as sudo for complete info.',

    '$ lsb_release':         'Prints distribution-specific information (LSB == Linux Standard Base). \n\t\t'
                             '-v: Shows the version of the LSB. \n\t\t'
                             '-i: Displays the distributor\'s ID. \n\t\t'
                             '-d: Displays a description of the installed distribution. \n\t\t'
                             '-r: Displays the release number of the installed distribution. \n\t\t'
                             '-c: Displays the code name of the installed distribution. \n\t\t'
                             '-a: Displays all of the above information. \n\t\t'
                             '-s: Uses a short output format. \n\t\t'
                             '-h: Shows summary of options.',

    '$ fdisk':               'Displays disk information for the local host.',

    '$ df':                  'Displays disk space usage.',

    '$ fsck':                'Checks and repairs a Linux filesystem.',

    '$ dkms':                'Dynamic Kernel Module Support. \n\t\t'
                             'Syntax: dkms <action> <options> <module/module-version> \n\t\t'
                             '<path/to/source-tree> <path/to/tarball.tar> <path/to/driver.rpm>. \n\t\t'
                             'Actions: \n\t\t'
                             '- add: Adds the module to the tree for builds and installs. \n\t\t'
                             '- remove: Removes the module from the tree. \n\t\t'
                             '- build: Builds the module for the specified kernel/arch. \n\t\t'
                             '- install: Installs a built module onto the kernel. \n\t\t'
                             '- uninstall: Uninstalls a module from the kernel/arch. \n\t\t'
                             '- status: Returns the current status of modules and kernels. \n\t\t'
                             '- autoinstall: Attempts to install the latest revision of modules.',

    # File Commands
    '$ !$':                  'Repeats the last argument or command.',

    '$ clear':               'Clears the terminal screen.',

    '$ ls':                  'Lists objects in a directory. \n\t\t'
                             '-l: Long form list. \n\t\t'
                             '*<string>*: Lists contents that contain what\'s between the \'* *\'.',

    '$ cd':                  'Changes directory (enter the directory).',

    '$ cd ..':               'Moves up to the parent directory ("back out" of the current directory).',

    '$ touch':               'Creates a new file.',

    '$ mkdir':               'Creates a new directory.',

    '$ rm':                  'Removes a file. \n\t\t'
                             '-r: Recursive removal. \n\t\t'
                             '-f: Forces removal without warnings. \n\t\t'
                             '-r -f: Removes directories and their contents, use with caution.',

    '$ rmdir':               'Removes an empty directory.',

    '$ cat':                 'Concatenates and displays the contents of a file.',

    '$ mv':                  'Moves or renames a file. \n\t\t'
                             'Syntax: $ mv [file to move] [destination]/ \n\t\t'
                             'Example: $ mv newfile Desktop/ \n\t\t'
                             'Renaming example: $ mv newfile NewFile',

    '$ cp':                  'Copies a file. \n\t\t'
                             'Syntax: $ cp [file to copy] [new file name].',

    '$ ln':                  'Creates links. \n\t\t'
                             '1. Hard linking: Duplicates the file. Changes reflect in both files. \n\t\t'
                             'Syntax: $ ln <source> <destination>. \n\t\t'
                             '2. Symbolic linking: Creates a shortcut or reference. \n\t\t'
                             'Syntax: $ ln -s <source> <destination>.',

    '$ man [command]':       'Displays the manual for a command. \n\t\t'
                             'Example: $ man ls.',

    # Application Calls
    '$ nano [file]':         'Text editor in the terminal.',

    '$ vi or vim [file]':    'More complex text editor than nano, with advanced features.',

    '$ emacs':               'A text editor currently in use.',

    '$ evince [file]':       'Opens the Document Viewer app for the specified file.',

    '$ zip':                 'Compresses a file into a .zip format. \n\t\t'
                             'Children: \n\t\t'
                             '- unzip: Extracts files from a .zip archive.',

    '$ gzip':                'Compresses a file into a .gz format. \n\t\t'
                             'Children: \n\t\t'
                             '- gzip: Creates a .gz compressed file. \n\t\t'
                             '- gunzip: Extracts a .gz file. \n\t\t'
                             '- zcat: Outputs a .gz file content.',

    '$ telnet':              'Allows remote access via Telnet. Insecure as data is sent in clear text. \n\t\t'
                             'Syntax: telnet <ip> <port>.',

    '$ ssh [user@address]':  'Secure remote access using SSH. Encrypted and authenticated. \n\t\t'
                             'Syntax: ssh <flags> <username@address>.',

    '$ john [options]':      'John the Ripper: A password cracker that checks for weak passwords.',

    '$ cron':                'Starts on system boot and automates tasks.',

    '$ crontabs':            'Method to interact with cron. \n\t\t'
                             'Requires 6 values: MIN, HOUR, DOM, MON, DOW, CMD. \n\t\t'
                             'Syntax: crontab -e.',

    # Operators/Redirectors
    '> or >>':              'Output Redirection: [program or command] > (create/overwrite \n\t\t'
                            'file) or >> (append to a file) [filename]. \n\t\t'
                            'Example: $ echo "a new world" >> helloworld \n\t\t'
                            'adds "a new world" to the end of the "helloworld" file. \n\t\t'
                            'STDIN -> 0, STDOUT -> 1, STDERR -> 2. \n\t\t'
                            'To specify output type, use the number before > or >> \n\t\t'
                            'Example: STDERR2>>.',

    '<':                    'Input Redirection. Redirects input from a file or stream.',

    '<<':                   'Here document: Embed input for stdin inside a script. \n\t\t'
                            'Example: \n\t\t'
                            'sort <<END \n\t\t'
                            'pineapple \n\t\t'
                            'banana \n\t\t'
                            'spider \n\t\t'
                            'car \n\t\t'
                            'toaster \n\t\t'
                            'END.',

    '0>, 1>, 2>':           'Redirects stdin (0), stdout (1), or stderr (2) to a file. \n\t\t'
                            'Example: <command> > stdout-here 2> stderr-here < stdin-from-here.',

    '(&> or &>>):':         'Redirects both stdout and stderr into the specified file.',

    '|':                    'Pipe character: Directs the output from one process as input \n\t\t'
                            'into another. \n\t\t'
                            'Example: <command1> | <command2>.',

    '&&':                   'Boolean "AND" symbol: Runs the next command only if the first \n\t\t'
                            'command succeeds. \n\t\t'
                            'Example: $ [file] && echo "it worked".',

    ';':                    'Executes multiple commands sequentially, regardless of success.',

    '&':                    'Runs a command in the background, allowing other commands \n\t\t'
                            'to be executed simultaneously.',

    'Arithmetic Operators': 'Used with (()) or let: \n\t\t'
                            'id++: Increment by 1. \n\t\t'
                            'id--: Decrement by 1. \n\t\t'
                            '++id: Pre-increment. \n\t\t'
                            '--id: Pre-decrement. \n\t\t'
                            '! : Not operator. \n\t\t'
                            '**: Exponentiation. \n\t\t'
                            '*: Multiplication. \n\t\t'
                            '/: Division. \n\t\t'
                            '%: Modulo (remainder). \n\t\t'
                            '+: Addition. \n\t\t'
                            '-: Subtraction. \n\t\t'
                            '<<: Left bitwise shift. \n\t\t'
                            '>>: Right bitwise shift. \n\t\t'
                            '<= >=: Comparison (less/greater or equal). \n\t\t'
                            '< >: Comparison (less/greater than). \n\t\t'
                            '== !=: Equality and non-equality. \n\t\t'
                            '&: Bitwise AND. \n\t\t'
                            '^: Bitwise XOR. \n\t\t'
                            '|: Bitwise OR. \n\t\t'
                            '&&: Logical AND. \n\t\t'
                            '||: Logical OR. \n\t\t'
                            'expr?expr:expr: Conditional operator (ternary).',

    # SysAdmin Commands
    '$ sudo':               'Superuser command: "super user do." Requires specific user \n\t\t'
                            'permissions. \n\t\t'
                            'Example: $ sudo apt-get update.',

    'su':                   'Switch user. \n\t\t'
                            'Example: $ su - [username] to switch users. \n\t\t'
                            'To switch to root: $ su -.',

    '$ apt-get update':     'Searches for updates for programs on the system.',

    '$ apt-get upgrade':    'Upgrades the software found by apt-get update.',

    '$ apt-get install':    'Installs the specified program.',

    '$ apt-get remove':     'Uninstalls the specified program.',

    '$ apt-cache search':   'Searches for programs available for installation.',

    '$ chown':              'Changes user and group ownership of a file. \n\t\t'
                            'Syntax: chown <user>:<group> <file>.',

    '$ adduser':            'Adds a new user to the system. \n\t\t'
                            'Syntax: adduser <username>.',

    '$ useradd':            'Low-level way to add a user (prefer adduser). \n\t\t'
                            'Example: useradd -m -d /home/testuser -u 1501 -g 66 -s \n\t\t'
                            '/bin/bash testuser.',

    '$ addgroup':           'Adds a new group. \n\t\t'
                            'Syntax: addgroup <groupname>.',

    '$ usermod':            'Adds a user to a group. \n\t\t'
                            'Syntax: usermod -a -G <groups> <user>.',

    '$ chmod':              'Changes file permissions. Uses octal (binary) notation: \n\t\t'
                            '7 (111) rwx \n\t\t'
                            '6 (110) rw- \n\t\t'
                            '5 (101) r-x \n\t\t'
                            'Example: $ chmod 640 [file].',

    '$ userdel':            'Deletes a user.',

    '$ hd <file>':          'Hexdump: Shows the hexadecimal content of the specified file.',

    '$ usermod':            'Modifies a user\'s account. \n\t\t'
                            '-L: Locks the user out. \n\t\t'
                            '-U: Unlocks the user.',

    '$ hd <file>':          'Hexdump: Shows the hexadecimal content of the specified file.',

    '$ cut':                'Extracts specific parts of a file. \n\t\t'
                            'Example: cut -d":" -f1 /etc/passwd.',

    '$ sort':               'Sorts the contents of a file alphabetically.',

    '$ uniq':               'Filters out repeated lines. \n\t\t'
                            'Works best when repeated lines are adjacent. \n\t\t'
                            'Example: uniq <file>.',

    '$ seq':                'Generates a sequence of numbers or letters. \n\t\t'
                            'Example: seq 1 5 outputs 1, 2, 3, 4, 5.',

    '$ wc':                 'Word count: Prints newline, word, and byte counts for each file. \n\t\t'
                            'Syntax: wc <filename>.',

    '$ echo':               'Prints a string to the terminal or file. \n\t\t'
                            'Example: $ echo "hello" > file.txt creates file.txt with "hello".',

    '$ grep':               'Search tool: Filters output based on a pattern. \n\t\t'
                            'Can search multiple files or use piping. \n\t\t'
                            'Syntax: grep <pattern> <file>.',

    '$ ps':                 'Displays a snapshot of user-created processes. \n\t\t'
                            '-ef: Shows all system processes.',

    '$ kill':               'Terminates a process using its Process ID (PID). \n\t\t'
                            'Syntax: kill <PID>.',

    '$ systemctl':          'Controls the state of systemd services. \n\t\t'
                            '-stop: Stops a unit. \n\t\t'
                            '-start: Starts a unit. \n\t\t'
                            '-restart: Restarts a unit.',

    '$ /etc/init.d/<service>': 'Stops a running service.',

    '$ service --status-all': 'Displays all running services.',

    '$ service <service> stop': 'Stops a specific service.',

    '$ chkconfig <service> off': 'Turns off a service (older systems).',

    '$ top':                'Shows processes consuming the most resources.',

    '$ initctl list':       'Lists upstart jobs and their status.',

    '$ w':                  'Shows who is logged on and what they are doing.',

    '$ whoami':             'Displays the current user.',

    '$ id':                 'Displays detailed user information, including groups.',

    '$ cat /etc/passwd':    'Lists all users on the system. \n\t\t'
                            'Includes username, UID, GID, home directory, and login shell.',

    '$ which <command>':    'Locates a command within the $PATH directories.',

    '$ find [file]':        'Finds files based on criteria. \n\t\t'
                            'Recursive search: find /. \n\t\t'
                            'Example: find <dir> -user <user>.',

    '$ whereis [file]':     'Prints the location of a file or directory.',

    '$ locate [file]':      'Finds files by name using an index (updatedb).',

    '* cut, copy, paste':   'Shortcuts: ctrl+shift+(x, c, v).',

    '* ctrl+c':             'Interrupts a running process (prints "^C").',

    '* ctrl+d':             'Ends a running process and creates a newline.',

    '* ctrl+l':             'Clears the terminal screen.',

    '$ export':             'Redefines the value of a variable. \n\t\t'
                            'Example: $ export nootnoot=1111.',

    # Variable Manipulation
    '$ $*':                 'Denotes environment variables. Changes affect system processes.',

    '$ export':             'Exports an object globally. \n\t\t'
                            '-f: Exports functions.',

    '$ typeset':            'Declares local variables. \n\t\t'
                            '-i: Declares an integer variable.',

    '$ let':                'Performs arithmetic operations. \n\t\t'
                            'Example: let x++, x=x*3.',

    '$ declare':            'Declares variables. \n\t\t'
                            '-l: Converts values to lowercase. \n\t\t'
                            '-u: Converts values to uppercase. \n\t\t'
                            '-r: Makes the variable read-only.',

    '$ read':               'Reads input into variables. \n\t\t'
                            'Example: read a b.',

    '$ exec':               'Executes a command, stopping the current shell process.',

    # Statements/Loops
    'while loop':           'Repeats while a condition is true. \n\t\t'
                            'Syntax: \n\t\t'
                            'while [condition] \n\t\t'
                            'do \n\t\t'
                            '  commands \n\t\t'
                            'done.',

    'for loop':             'Iterates over a list of values. \n\t\t'
                            'Syntax: \n\t\t'
                            'for var in list \n\t\t'
                            'do \n\t\t'
                            '  commands \n\t\t'
                            'done.',

    'case statement':       'Substitutes for if/then/elif/else statements. \n\t\t'
                            'Syntax: \n\t\t'
                            'case <value> in \n\t\t'
                            '  pattern1) commands ;; \n\t\t'
                            '  pattern2) commands ;; \n\t\t'
                            'esac.',

    'if-then-else':         'Conditional branching. \n\t\t'
                            'Syntax: \n\t\t'
                            'if [condition] \n\t\t'
                            'then \n\t\t'
                            '  commands \n\t\t'
                            'else \n\t\t'
                            '  commands \n\t\t'
                            'fi.',

    '$ test':               'Evaluates conditions. \n\t\t'
                            'Example: test -f file.',

    # Functions
    'function':             'Defines a function. \n\t\t'
                            'Syntax: function name { commands }.',

    'return':               'Exits a function without executing further commands.',

    'exit':                 'Exits the shell script. \n\t\t'
                            'Syntax: exit <value>.'
}
                             
