glossary = { 
    # VIM Normal Mode Keys
    '<h|j|k|l>':           'Motion commands: h - left, j - down, k - up, l - right.',

    'alt + <motion cmd>':  'Exit insert mode, enter normal mode, and move in the desired direction.',

    'w':                   'Move to the beginning of the next word.',

    'e':                   'Move to the end of current or next word if already at the end.',

    'b':                   'Move to the beginning of the previous word.',

    ':<*>':                'Indicates to vim that you are creating a command. \n\t\t'
                            'Coloned entries can be stacked into a single command.',

    'i':                   'Switch to insert mode.',

    'a':                   'Switch to insert mode *after* the cursor.',

    'shift-r':             'Switch to replace mode.',

    'esc/ctrl-c':          'Switch to normal mode.',

    ':q':                  'Quit the editor.',

    ':*a':                 'Perform on all open files.',

    ':*!':                 'Force the operation.',

    ':w':                  'Write to buffer.',

    ':e <path/to/file>':   'Edit a different file from the current one.',

    'ctrl-g':              'Check the file you are currently working on.',

    '/':                   'Forward search using regex. Can be appended to other commands.',

    '?':                   'Backward search using regex. Can be appended to other commands.',

    '(':                   'Move backwards to the beginning of the next sentence.',

    ')':                   'Move forwards to the beginning of the previous sentence.',

    '{':                   'Move down to the beginning of the next paragraph.',

    '}':                   'Move up to the beginning of the previous paragraph.',

    'gg':                  'Move to beginning of text/file.',

    'G (shift-g)':         'Move to end of text/file.',

    '<#><cmd>':            'Repeats <cmd>, <#> times.',

    'ctrl-f':              'Move down one page.',

    'ctrl-b':              'Move up one page.',

    ':<#>':                'Brings you to the specified line number "#". \n\t\t'
                            'Can also be used for read operations.',

    '<#> shift g':         'Another way to go to a specific line.',

    '$':                   'Move to end of line.',

    '0':                   'Move to beginning of line.',

    'B (shift-b)':         'Move to the beginning of the first word of a line.',

    '$ vim <path/to/file> +<#>': 'Open file at a specific line. "+" will execute any vim command as the file opens.',

    '*':                   'Move forward to the next occurrence of the word the cursor is on.',

    '#':                   'Move backward to the previous occurrence of the word the cursor is on.',

    'd<motion cmd>':       'Delete the specified thing. \n\t\t'
                            '-- dw deletes the word the cursor is on. \n\t\t'
                            '-- d) deletes the whole sentence starting from the cursor. \n\t\t'
                            '-- dd deletes the whole line. \n\t\t'
                            '-- d/<regex> deletes up to the found regex.',

    'u':                   'Undo the last action.',

    'ctrl-r':              'Redo the last undone action.',

    'y':                   'Yank (copy) the specified text. \n\t\t'
                            '-- yy copies the whole line. "p" will paste it on the current line. \n\t\t'
                            '-- y<motion> copies the text specified by the motion.',

    'p':                   'Paste the yanked text after the cursor.',

    'P':                   'Paste the yanked text before the cursor.',

    'x':                   'Deletes the character under the cursor and places it in the register.',

    'o':                   'Create a new line below the current line and move to insert mode.',

    'shift-o':             'Create a new line above the current line and move to insert mode.',

    'c':                   'Change text: deletes the specified portion and enters insert mode.',

    'V':                   'Enter visual mode and select the line.',

    'gf':                  'Go to file. Open the file under the cursor if it references another file.',

    'gF (g+shift-f)':      'Go to line in a file, useful for error code line numbers.',

    'ctrl-v':              'Visual block mode. Extend selection as desired. \n\t\t'
                            'You can modify selected lines using "c" and apply the change to all selected lines.',

    'ctrl-g':              'Prints the current file name in the window.',

    '1 ctrl-g':            'Prints the full path of the current file.',

    '$ vim <path/to/file> +<#>': 'Open the file and start at line <#> upon opening.',

    '$ vim <path/to/file> /<regex>': 'Opens the file and searches for the specified regex, placing the cursor on the first match.',

    '$ vim +1,2d +wq <path/to/file>': 'Delete lines 1 through 2 and save the file with wq.',

    # Registers
    ':"<a-z,A-Z>':         'Use "double quote" followed by an alphabet char to store data in one of the 52 registers.',

    ':com! <cmdName> ! <ext cmd> %': 'Defines a vim command that runs an external command using the current file.',

    # Search and Replace
    ':s/<regex>/<replacement>/<flags>': 'Replace the first instance of <regex> with <replacement>. \n\t\t'
                                        '-- %s/... replaces across the whole file. \n\t\t'
                                        'Flags: \n\t\t'
                                        '- g: global replacement. \n\t\t'
                                        '- c: confirm before replacing. \n\t\t'
                                        '- i: case insensitive replacement.',

    # Marks
    ':m{<a-z>,<A-Z>}':     'Create a mark. Lowercase marks are local to the current buffer, while uppercase marks are across files.',

    ":'<markName>":        'Jump to the specified mark in the current file.',

    # Jump List
    'ctrl-o':              'Move forward through the jump list one step at a time.',

    'ctrl-i':              'Move backward through the jump list one step at a time.',

    ':jumps':              'Shows the jump list.',

    # Buffers
    ':split':              'Opens a new window below the current buffer.',

    ':vert <split/new/diff>': 'Opens a new vertical window.',

    'ctrl-w<motion>':      'Move between windows using motion key options.',

    'ctrl-w w':            'Cycle through the open windows.',

    'ctrl-w c':            'Close the current window.',

    ':split<path/to/file>': 'Split the current window and open <path/to/file> in the new window.',

    ':new<path/to/file>':   'Split the current window and open <path/to/file> in a new window below.',

    ':e':                  'Open another file to edit, changing the buffer to a new file.',

    ':e tab':              'List files in the current directory (pwd).',

    ':e <path/to/file>':   'Open a specific file and browse directories with search and tab completion.',

    ':e!':                 'Force re-load the current file, removing unsaved changes.',

    ':bd':                 'Delete the current buffer and return to the previous one.',

    ':bn':                 'Move to the next buffer.',

    ':bp':                 'Move to the previous buffer.',

    ':b <path/to/file>':   'Move to a specific file in the buffer list.',

    ':b tab':              'Cycle through open buffers using tab completion.',

    ':b <#>':              'Move to a specific buffer number.',

    ':ls or :buffers':     'Print a list of currently open buffers.',

    ':r <path/to/file>':   'Read a file into the current buffer.',

    ':%! jq .':            'Format JSON data with jq.',

    # Configuration
    ':set':                'Show current options set.',

    ':set ic':             'Set search to be case-insensitive.',

    ':set noic':           'Disable case insensitivity.',

    ':set hls':            'Highlight search results.',

    ':set noh':            'Disable search highlighting.',

    ':set incsearch':      'Enable incremental search.',

    ':set noincsearch':    'Disable incremental search.',

    ':set clipboard=unnamedplus': 'Integrate vim clipboard with system clipboard.',

    ':syntax <on/off>':    'Toggle language syntax recognition.',

    ':colorscheme <scheme>': 'Set a specific color scheme for syntax highlighting.',

    ':set number':         'Enable line numbers.',

    ':set nonumber':       'Disable line numbers.',

    ':set diffopt' or ':dip': 'Show current diff options.',

    ':set diffopt+=<option>': 'Add an option to the diff settings. \n\t\t'
                               '-- vertical sets the default as vertical when opening diff.',

    # Abbreviations
    ':abb <abbreviation> <abb expansion>': 'Maps an abbreviation to an expansion. \n\t\t'
                                            'Example: :abb _ys Youngstar will replace _ys with Youngstar.',

    # Adding Commands
    ':! <cmd>':               'Run an external command <cmd> from within Vim.',

    ':com! <cmdName> ! <ext cmd> %': 'Defines a vim command that runs an external command. \n\t\t'
                                      'The % indicates the current file will be passed to the external command.',

    # Diff Mode
    '-d switch':              'Opens files in diff mode. Highlights differing lines between two files. \n\t\t'
                              'Example: vim -d <file1> <file2>.',

    'Switching windows':      'As described in Buffers, move between windows in diff mode.',

    'Closing windows':        'As described in Buffers, close windows in diff mode.',

    ':do':                    'Diff obtain: Replace the line in the current file with the line from the second file. \n\t\t'
                              'Example: :do will replace the current line with line 1 from file2.',

    ':dp':                    'Diff obtain in the opposite direction. Replace the line in the second file with the line from the current file.',

    ':diffsplit <path/to/file2>': 'If the files aren’t opened with -d switch, use this to open a diff between two files.',

    ':vert diffsplit <file>': 'Open the second file in a vertical window for a side-by-side diff.',

    # Zip Files
    'Compressed files in Vim': 'Manipulate zipped files directly in Vim: open, modify, and save. \n\t\t'
                                'Example: Open a .zip file to view its contents; modify and save files from within Vim.',

    'Moving the cursor':     'Use j & k to move through the list of compressed files. \n\t\t'
                              'Search through the list like regular files.',

    'Opening a file in zip': 'Place the cursor on a file name inside the zip and press enter to open it.',

    'Saving changes':        'If a file is modified, save changes within Vim and return to the zip list. \n\t\t'
                              'Changes will persist when you reopen the zip file.',

    # Configuration
    ':set ic':                'Enable case-insensitive search.',

    ':set noic':              'Disable case-insensitive search.',

    ':set hls':               'Enable highlighting of search results.',

    ':set noh':               'Disable search highlighting.',

    ':set incsearch':         'Enable incremental search, where the search results update as you type.',

    ':set noincsearch':       'Disable incremental search.',

    ':set clipboard=unnamedplus': 'Integrate Vim’s clipboard with the system clipboard, allowing for easier copy-pasting.',

    ':syntax <on/off>':       'Toggle syntax highlighting on and off.',

    ':colorscheme <scheme>':  'Set a specific color scheme for syntax highlighting in Vim.',

    ':set number':            'Show line numbers on the left side of the window.',

    ':set nonumber':          'Hide line numbers on the left side of the window.',

    ':se nu':                 'Short version of :set number to show line numbers.',

    ':se nonu':               'Short version of :set nonumber to hide line numbers.',

    ':set diffopt':           'Show current diff options settings.',

    ':set diffopt+=<option>': 'Add a new option to the diff settings, such as the vertical option.',

    # Abbreviations
    ':abb <abbreviation> <expansion>': 'Define an abbreviation to automatically expand to the full phrase. \n\t\t'
                                       'Example: :abb _ys Youngstar replaces _ys with Youngstar after typing a space.',

    # Commands and Keybindings
    ':! <command>':           'Run an external shell command directly from within Vim.',

    ':com! <cmdName> ! <ext cmd> %': 'Create a custom command in Vim that runs an external shell command using the current file.',

    ':e <file>':              'Open a different file for editing. You can specify a full or relative path.',

    # Vimscript
    '"':                     'Creates a comment in Vimscript. The comment must be followed by a space.',

    'example line in .vimrc': 'Sets options and configurations within the .vimrc file. \n\t\t'
                               'Example: set number will show line numbers by default.',

    # Key Mapping
    ':noremap <keyToMap> <actionToMap>': 'Remap an action to a new key. \n\t\t'
                                          'Example: remapping ctrl-f (C-F) for page down to space bar: \n\t\t'
                                          ':noremap <SPACE> <C-F>.',

    # Key Mapping Notation
    '<Nul>':                  'Represents the zero value, or CTRL-@ (decimal value 0).',

    '<BS>':                   'Represents backspace, or CTRL-H (decimal value 8).',

    '<Tab>':                  'Represents the tab key, or CTRL-I (decimal value 9).',

    '<NL>':                   'Represents the linefeed, or CTRL-J (decimal value 10).',

    '<FF>':                   'Represents formfeed, or CTRL-L (decimal value 12).',

    '<CR>':                   'Represents carriage return, or CTRL-M (decimal value 13).',

    '<Return>':               'Same as <CR> (carriage return).',

    '<Enter>':                'Same as <CR> (carriage return).',

    '<Esc>':                  'Escape key, or CTRL-[ (decimal value 27).',

    '<Space>':                'Space key (decimal value 32).',

    '<lt>':                   'Represents less-than symbol (<) (decimal value 60).',

    '<Bslash>':               'Represents backslash (\) (decimal value 92).',

    '<Bar>':                  'Represents vertical bar (|) (decimal value 124).',

    '<Del>':                  'Delete key (decimal value 127).',

    '<CSI>':                  'Command Sequence Intro, or ALT-Esc (decimal value 155).',

    '<xCSI>':                 'Special CSI sequence typed in the GUI.',

    '<EOL>':                  'End-of-line, which can be <CR>, <LF>, or <CR><LF>, depending on the system.',

    # Cursor Movement Keys
    '<Up>':                   'Up arrow key: moves the cursor up.',
    '<Down>':                 'Down arrow key: moves the cursor down.',
    '<Left>':                 'Left arrow key: moves the cursor left.',
    '<Right>':                'Right arrow key: moves the cursor right.',
    
    '<S-Up>':                 'Shift + Up arrow key.',
    '<S-Down>':               'Shift + Down arrow key.',
    '<S-Left>':               'Shift + Left arrow key.',
    '<S-Right>':              'Shift + Right arrow key.',
    
    '<C-Left>':               'Ctrl + Left arrow key.',
    '<C-Right>':              'Ctrl + Right arrow key.',
    
    '<F1> - <F12>':           'Function keys from F1 to F12.',
    '<S-F1> - <S-F12>':       'Shift + Function keys from F1 to F12.',
    
    '<Help>':                 'Help key.',
    '<Undo>':                 'Undo key.',
    '<Insert>':               'Insert key.',
    '<Home>':                 'Home key.',
    '<End>':                  'End key.',
    
    '<PageUp>':               'Page Up key.',
    '<PageDown>':             'Page Down key.',
    
    '<kHome>':                'Keypad home key.',
    '<kEnd>':                 'Keypad end key.',
    '<kPageUp>':              'Keypad page up.',
    '<kPageDown>':            'Keypad page down.',
    
    '<kPlus>':                'Keypad + key.',
    '<kMinus>':               'Keypad - key.',
    '<kMultiply>':            'Keypad * key.',
    '<kDivide>':              'Keypad / key.',
    '<kEnter>':               'Keypad Enter key.',
    '<kPoint>':               'Keypad decimal point.',
    
    '<k0> - <k9>':            'Keypad numbers 0 to 9.',
    
    '<S-...>':                'Shift key.',
    '<C-...>':                'Control key.',
    '<M-...>':                'Alt key or Meta key.',
    '<A-...>':                'Same as <M-...> (Alt or Meta key).',
    '<D-...>':                'Command key (Macintosh only).',
    
    '<t_xx>':                 'Key with a specific entry in termcap.',

    # Full Documentation
    'vimdoc':                'The full documentation for Vim can be found at: \n\t\t'
                             'https://vimdoc.sourceforge.net/htmldoc/intro.html#key-notation.',

    # Useful Vim Options
    ':set':                  'Shows the current settings in Vim.',

    ':set ic':               'Sets search to be case-insensitive (ignore case).',

    ':set noic':             'Disables case insensitivity in searches.',

    ':set hls':              'Highlights search results by enabling highlight search.',

    ':set noh':              'Disables highlighting of search results.',

    ':set incsearch':        'Turns on incremental search to search while typing the query.',

    ':set noincsearch':      'Disables incremental search.',

    ':set clipboard=unnamedplus': 'Integrates Vim’s internal clipboard with the system clipboard.',

    ':syntax <on/off>':      'Toggles language syntax highlighting on or off.',

    ':colorscheme <scheme>': 'Sets the color scheme for syntax highlighting.',

    ':set number':           'Enables line numbers to be visible on the left side of the window.',

    ':set nonumber':         'Disables line numbers on the left side of the window.',

    ':se nu':                'Short version of :set number to show line numbers.',

    ':se nonu':              'Short version of :set nonumber to hide line numbers.',

    ':set diffopt':          'Shows the current diff options.',

    ':set diffopt+=<option>': 'Adds a new option to the diff options. \n\t\t'
                              '-- vertical makes the diff view vertical by default.',
}

