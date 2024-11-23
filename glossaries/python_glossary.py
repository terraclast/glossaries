
glossary = {

        'print(*)':             'Outputs what is in the parenthesis. Strings can be \n\t\tprinted using quotes.',

        'variable':             'Holds a value that can be called later in the program.',

        'string':               'Plain text that contains one or more characters.',

        'concatenation':        'Sticking one object on to the end of another. + is \n\t\tused for this.',

        '\\n':                  'The newline character creates a new line in a string. \n\t\t.',

        '\\t':                  'The tab character creates a tabbed indentation in a string.', 

	'\\r':			'The return carriage character returns the cursor to the beginning of \n\t\tthe current line.',

        '*.rstrip() method':    'Removes whitespace on the right of a string. This includes \n\t\tblank strings at the end of a printed file.',

        '*.lstrip() method':    'Removes whitespace on the left of a string.',

        '*.strip() method':     'Removes whitespace from both right and left sides of a \n\t\tstring.',

        '*.title() method':     'Capitalizes the first letter of a string value.',

        '*.upper() method':     'Makes all letter chars in a string value uppercase.',

        '*.lower() method':     'Makes all letter chars in a string value lower case.',

        'remove(*)':            'Remove a specific value from a list. \n\t\tEx:\n\t\t<var>.remove(<value>)',

        'integers':             'Whole numbers, like 1, 2, 42, 23459, that make up an \n\t\tobject type. Ints are truncated.',

        'floats':               'Decimal numbers, like 1.0, 3.141592, etc, that make up \n\t\tan object type. At least one is needed to avoid truncation: \n\t\t3.0/2 = 1.5',

        'str()':                'A function that makes a non-string object a string.',

        'list':                 "A type of array or vector for python; a variable with multiple \n\t\tvalues. These values can be many other object types: integers, \n\t\tfloats, another list, dictionaries, etc.\n\t\tThe values are placed in brackets [], each value is \n\t\tseparated by a comma, and can be manipulated. \n\t\tLists can be passed to functions as a function's parameter and the \n\t\tvalues will be input in the order they are listed.\n\n\t\tEx: \n\t\t\tdef greet_users(names): \n\t\t\t\t<function block with a for or while loop to process the input>\n\t\t\tusernames = ['hannah', 'ty', 'margot']\n\t\t\tgreet_users(usernames) \n\n\t\tThe above example takes a single input at a time and the \n\t\tfor/while loop goes through each list value in turn.",

        'value':                'The data contained in a variable. Can be a string, integer, \n\t\tfloat, or boolean. With regards to dictionaries, it is the \n\t\tvalue related to a specific key. They can be called either \n\t\twith <dict>[<key>], or with <dict>.values().',

        'index':                'Enables one to call a specific value by its place in a \n\t\tlist or dictionary. Numbering starts with zero (0), such that \n\t\t0, 1, 2, 3, etc. Using negative idex numbers starts you at the \n\t\tend of the list: -1 is the last, -2 is second to last, etc.',

        'slice':                'A section of a list or dictionary. Can be called using \n\t\t<list>[x:y]. If one of the two are missing, it means start from \n\t\tthe beginning if the first is missing and go to the end if the \n\t\tsecond is missing.',

        'hash comment':         'The hash symbol is used to create a comment, like in C++',

        'changing elements in a list':  'Change an element in a list by using \n\t\t<list>[x] = value. This changes the specific index value.',

        '*.append(*) method':   'Adds a value to the end of a list: <list>.append(*). \n\t\tThe "*" in the .append() argument is the object you want to \n\t\tappend to the list. You can pass strings, ints, floats, and any \n\t\tother object a list can store.',

        '*.insert(*) method':   'Inserts a value into a specified index in a list: \n\t\t<list>.insert(x, value).',

        'del <list>[<#>]':      'Removes the value at the index in both lists and \n\t\tdictionaries.',

        '*.pop(<#>) method':    'Removes a value from a list in a way that allows you to \n\t\tplace the value in another variable/object. If no index is \n\t\tspecified, <#>, it is taken from the end.',

        '*.remove(val) method': 'Removes a specified value from a list. This value \n\t\tcan also be placed in another object or removed by calling \n\t\ta var.',

        '*.sort() method' :     'Permenently puts all string values in a list into \n\t\talphabetical order.',

	'*.sorted(*) method':   "Non-permenently sorts a list's or dictionary's values \n\t\tin to alphabetical order. The argument is the name of the list or \n\t\tdictionary you want to sort. \n\n\t\tYou can sort the list or dict in \n\t\treverse alphabetical order by using sorted(<list>, \n\t\treverse=True). \n\n\t\t Often used with a for loop to print keys in alphabetical order.\n\n\t\tEx.\n\t\t\tfor k in sorted(<dict_name>.keys()):\n\t\t\t\tprint(f\"{key.rjust(15)})",

        '*.reverse() method':   'Permenently reverses the order of a list as it was \n\t\tinputted. It can be reversed by calling it again.',

        'for loop':             'Requires creating a var whose value is specified values of a \n\t\tlist or dictionary. \n\t\tEx: for <var> in <list>: \n\t\tIt then runs the code nested in the loop for each of the var \n\t\tvalues. Loop declaration must be followed by a colon (:).',

        'range(x,y)':           'Generates a series of numbers within the specified range. \n\t\tTo create a list of these values use the followiing example: \n\t\t"<list> = list(range(x,y))"',

        'min(*)':               'Find the minimum numeric value: min(<list>).',

        'max(*)':               'Find the maximum numeric value: max(<list>).',

        'sum(*)':               'Find the sum of a list of numbers.',

        'list comprehension':   'Combines a for loop with a math expression to \n\t\tcreate new values. \n\t\tEx: squares = [value**2 for value in range(1,11)]',

        'copying a list':       'Create a manipulatable copy of a list by using \n\t\t<list2> = <list1>[:]. \n\t\tIn other words, create a new list using a \n\t\tslice. Not using a slice creates one variable with two \n\t\tnames, so to speak. \n\t\tJust using the slice notation when passing a list to a function will pass the function a copy of the list, not the original. \n\n\t\t\tEx: \n\t\t\t<function_name>(<list_name>[:]) \n\n\t\tThis will pass the list to the function, but the list will be a copy, not the original.',

        'tuple':                'Same as a list only the values can only be changed via \n\t\treassignment: \n\n\t\t<tuple> = (a, b, c, etc)',

        'if-elif-else statement':       'Creates branching within a program using \n\t\tboolean testing. if this, then that. elif (else if) this, then \n\t\tthat.  else, this other thing. The final else is not required \n\t\tif all possible conditions are defined in if-elif statements.',

        'boolean':              'A conditional test that results in either true or false. \n\t\tExpressions include: >, <, ==, !=, >=, <=. Vars can be set \n\t\tas true or false and be used as tests.',

        'and':                  'Logic that states all expressions must be true to be called true.',

        'or':                   'Logic that states at least one expression must be true to be called \n\t\ttrue.',

        'checking for existance of value':      'if <value> in <list>: \n\t\t>> true or false.',

        'checking for non-existance of value':  'if <value> not in <list>: \n\t\t>> true or false.',

        'dictionary':   'An array consisting of key-value pairs. Use curly brackets \n\t\tand colons to separate its keys from their values in its \n\t\tdefinition: dict = {a: b, c: d, e: f}. a, c, and e are keys. \n\t\tb, d, and f are the keys values. Call the value by using its \n\t\tkey.  New key-value pairs are added by <dict>[newkey] = val. \n\t\tKeys are modified by reassignment: <dict>[key] = new_val.',

        'key':                  'The name of an object in a dictionary. They can be called \n\t\tusing <dict>.keys().',

        '*.get() method':       "The .get() method is how you pull values from a \n\t\tdictionary. You have to specify the key you want the value for \n\t\tin the parenthesis.\n\t\tEx: \n\t\t\tdict = {'key1': 'value1', 'key2': 'value2'} \n\t\t\tdict.get('key1') \n\t\t\t>>> value1 \n\t\tThe key must have single quotes to indicate the key is a string.",

        '*.items() method':     'This method returns a list of key-value pairs which \n\t\tcan each be stored in their own list: \n\n\t\t\tfor key, val in <dict>.items():\n\t\t\t\t<block of code>',

        '*.keys() method':      'This method returns a list of keys in a dictionary: \n\t\tfor key in <dict>.keys():.',

        '*.values() method':    'This method returns a list of values in a dictionary: \n\t\tfor val in <dict>.values():.',

        'set(*) method':        'Returns only unique values in an object. ',

        'input() method':       'Pauses a program to allow for a user to enter input \n\t\tinto said program. \n\t\tEx: message = input("Tell me something and Ill repeat it:")',

        '+=':                   'Addition assignment or iteration command: \n\t\tnice = "surely" \n\t\tnice += ", it is!" \n\t\tnice = "surely, it is!" \n\t\tAlso, for math ops: \n\t\tA = 5 \n\t\tA += 10 \n\t\tA = 5 + 10',

        'int()':                'Non-permentently changes a numerical whole number input \n\t\tfrom its natural string state to an int. It can not be used in \n\t\tthe initialization of an input variable. You need to resign \n\t\t the var as an int to make it permentent: \n\t\t<var> = "36" \n\t\t<var> = int(<var>)',

        '%':                    'The Modulo Operator- it divides the numbers on either \n\t\tside of it and returns the remainder of the division. \n\t\tEx: 4 % 3 > 1, 11 % 5 > 1.',

        'while loop':           'A loop that runs as long as a condition is true. \n\t\tEx:\n\t\t<initial var> = "" \n\t\twhile <condition w/ <initial var> is true>: \n\t\tDo something. \n\t\tWhile loops are better for manipulating and changing vals in \n\t\tlists and dictionaries. \n\n\t\tEx2:\n\t\t<initial_var> = "some stuff"\n\t\twhile <initial_var>:\n\t\t\t<block of code that does stuff>',

        'flag':                 'A var that can be used to check several conditions to \n\t\tdetermine whether the entire program is active. \n\t\tThe var must be set to either True or False.',

        'continue':             'Return to the beginning of a loop based on the result of a \n\t\tconditional test.',

        'ctrl-c':               'Stops any currently running process in a terminal window. \n\t\tParticularly helpful if you are in an infinite loop.',

        'function':             'A function is a modular block of code that receives \n\t\tinput alled arguments into variables called parameters \n\t\tand performs work in the form of computing values \n\t\tand returning processed data back to what called it. \n\t\tFunctions can take, as arguments, individually specified \n\t\tvalues and lists.  The function can also modify lists. \n\t\tEach function should have a single, specific job.',

        'positional arguments': 'A set of arguments that are dependent on the order in \n\t\twhich they are inputted.\n\t\tEx:  A function called gimmeRope(length,diameter) must \n\t\thave the arguments listed in the order <length> then <diameter>.',

        'keyword arguments':    'Each argument consists of a variable name and value.\n\t\tEx:  A function defined as gimmeRope(length,diameter) can have its \n\t\targuments given in any order as long as you list the parameter \n\t\t(variable) with the arugment: \n\n\t\t\tgimmeRope(diameter=12,length=34) \n\n\t\tYou must be careful that you use the exact name and \n\t\tspelling for each variable.',

        'default parameter value':      'Values set for one or more parameter in a \n\t\tfunction definition. If no argument is given for a parameter, \n\t\tthe default is used. However, the function will use the \n\t\targument it is given if it is given one. Default parameters \n\t\tmust be after any and all parameters without a default value. \n\n\t\t\tEx:  gimmeRope(length,diameter=1.5)\n\n\t\tIn the above, diameter is given a default value of 1.5.',

        'return value':         'Data outputted by a function after the function processes \n\t\tits input parameters. It takes data from inside the function and \n\t\tsends it back to the line that called the function.',

        'optional argument':    "An empty argument that returns a boolean false. This can be \n\t\tused to create if/else statements that enable you to widen your \n\t\tinput range, relatively simply. It is made empty by using two single quotes, '', as a parameter's default value.",

        'array':                'Lists basically function as arrays in python.  If you want to \n\t\tuse actual arrays, you will need to import a library that supports \n\t\tthem, like NumPy. That being said, like lists, they are variables \n\t\tthat contain multiple values separated by commas and captured \n\t\tby brackets: []. The values are referend via their index numbers.',

        'break statement':      'A way for a user to exit a loop at a prompt or for a \n\t\tloop to end. The break happens in a loop and the break exits \n\t\tthe loop moving on to the next line of code. \n\t\t\tEx: \n\t\t\twhile True: \n\t\t\t\tif <var> == "q": \n\t\t\t\t\tbreak\n\t\tThis will escape the loop and move to the next block of code.',

        '*<parameter>':         "Asteric [SHIFT - 8] before a parameter name in a function's \n\t\tdefinition creates a tuple with the given name.\n\t\tEx.\n\n\t\t\tdef function(*input):\n\t\t\t\t<block of code>\n\n\t\tThe parameter, input, is created as a tuple. \n\t\tIf you are mixing positional and arbitrary arguments, \n\t\tthe arbitrary argument must go last.\n\t\tEx.\n\n\t\t\tdef function(positional, *arbitrary):\n\t\t\t\t<block of code>",

        '**<parameter>':        "Asteric Astric [SHIFT 8] 2x before a parameter name in a \n\t\tfunction's definition creates a dictionary with the given name.\n\t\tEx.\n\n\t\t\tdef function(**input)\n\t\t\t\t<block of code>\n\n\t\tThe argument, input, is a dictionary that can take as many \n\t\tkey/value pairs as it is fed in it's call statement. \n\t\tThe downside is each argument must be keyworded. \n\n\t\tEx.\n\t\t\tfunction(key1 = value1, key2 = value2, key3 = value3)\n\n\t\tThe above function creates the dictionary, index, with the \n\t\tkey/value pairs: \n\n\t\tkey1: value1, key2: value2, key3: value3\n\n\t\twhich can be manipulated just as any dictionary.",

	'module':               'A file ending with ".py" that you want to import into \n\t\tyour program. This allows you to access any functions in the file \n\t\tyou imported. The way you call one of the imported functions \n\t\tis by invoking:\n\n\t\t\timport </path/to/module>.py\n\n\t\t\t</path/to/module>.<function_name>(<arguments>)\n\n\t\t***Importing a Specific Funtion***\n\n\t\tYou can avoid using the dot notation by importing a specific function \n\t\twith the following import call:\n\n\t\t\tfrom </path/to/module> import <name_of_function>\n\n\t\tUsing an astrics for the import argument will import all functions \n\t\tfrom the module.\n\n\t\t\tfrom </path/to/module> import * \n\n\t\t***Giving the Imported Function an Alias***\n\n\t\tWhen importing a function from a module, you can \n\t\tappend "as <alias>" to the end, where <alias> is the shorter, unique \n\t\tnickname within the program doing the import.\n\n\t\tfrom </path/to/module> import <function> as <alias>\n\n\t\t*** Giving the Imported Module an Alias ***\n\n\t\tAppending "as <alias>" to the module import statement will give \n\t\tthat module an alias, same as function alias assignments.\n\n\t\t\timport <module> as <alias>',

	'class': 		'A class represents real-world things and situations.  \n\t\tClasses have defined general behavior and can have an entire category \n\t\tof objects. The creation of an object is called instantiation and \n\t\twork is done on an instance of a class. \n\t\t-- Value kind and possible actions must be defined. \n\t\t-- New classes can over-lap or expand the abilities of existing classes. \n\t\t-- Classes are stored in modules and can be imported like functions. \n\n\t\tClasses have two aspects: attributes and methods. These will \n\t\thave their own glossary entries.\n\t\tConvention states that class names are capitalized while other \n\t\tvar-type names are all lowercase. \n\n\t\tEx.\n\t\t\tDog()  <-- an object class.\n\t\t\tdog()  <-- a variable with some other kind.\n\n\t\tYou can create one or more instance of the defined class\n\t\tby creating a name for the instance and passing it, at minumum \n\t\tthe arguments it requires.\n\n\t\tEx.\n\t\t\tclass <Class>():\n\n\t\t\t\tdef __init__(self, <arg1>, <arg2>):\n\t\t\t\t\tself.<arg1> = <arg1>\n\t\t\t\t\tself.<arg2> = <arg2>\n\n\t\t\t\tdef <meth1>(self):\n\t\t\t\t\t<block of code>\n\n\t\t\t\tdef <meth2>(self):\n\t\t\t\t\t<block of code> ',

	'__init__() method':	"The __init__() method automatically runs each time an \n\t\tinstance in a class is created. This helps prevent Python's default \n\t\tmethod names from conflicting with the class' method names.",

	'class attribute':	'Attributes are defined but inherrent properties of the \n\t\tclass. For example, if we have a class called Dog(), It can have \n\t\tattributes like name, age, breed, etc. \n\t\tAttributes are called using dot notation and the attribute does \n\t\tnot get parenthasis:\n\n\t\tEx.\n\t\t\tmy_dog.name\n\n\t\tAll attributes must be initialized with a value. This takes place \n\t\tin the __init__ definition. If you have a variable attribute, it must \n\t\tstart with a value like 0 or an empty string.',

	'class method': 	'Methods are defined actions or behaviors an instance \n\t\tof your class can take or have. \n\n\t\tEx.\n\t\t\tDog()  <-- a class\n\t\t\t<block of code with class deffinition>\n\t\t\tmy_dog = Dog("Beau", 6)  <-- creating an instance of the Dog() class\n\t\t\tmy_dog.sit()\n\n\t\tThe sit method is called and the block of code associated with that method\n\t\tis run. \n\t\t*** methods must have parenthasis included that *could* have arguments passes.',

	'incrementation':	'Incrementation means to increase a variable by a number, usually one.\n\n\t\tOne way to accomplish iteration is:\n\n\t\t\tEx.\n\n\t\t\t\tx = x + <#>\n\t\t\t\tx += <#>\n\n\t\tThe two statements above are equivalent and increase the \n\t\tvalue of x by <#>. If you use "+=" and you use the var, you will increase \n\t\tthe var by both the current value of the var and the \n\t\tnumerical interator.', 

	'inheritance':		'With regard to classes, this is the property of a child class \n\t\tstarting with the properties of its parent class. This is the concept \n\t\tfor when you are creating new classes based off of already existing \n\t\tclasses. The child class inherits the attributes and methods of the \n\t\tparent and those can be modified or added to as needed.\n\n\t\tIf you just want the child class to be a copy of the parent class \n\t\tonly have the word "pass" in the definition.This will cause the \n\t\tchild to use the parent\'s __init__() method.\n\n\t\tAdding the __init__() method to the child will overide the parent\'s \n\t\t__init__() method.\n\n\t\tThere are four options for the child __init__() method:\n\n\t\t- You can "pass" the parent\'s __init__ method to the child.\n\t\t\tclass <Child>(<Parent>):\n\t\t\t\tpass\n\t\t- You can define the child\'s __init__() method.\n\t\t- Import the parent\'s method with:\n\t\t\tclass <Child>(<Parent>):\n\t\t\t\tdef __init__(self,<attrib1>, <attrib2>, etc):\n\t\t\t\t\t<Parent>.__init__(self, <attrib1>, <attrib2>, etc)\n\t\t- Import the parent\'s __init__ and methods using:\n\t\t\tclass <Child>(<Parent>):\n\t\t\t\tdef __init__(self, <attrib1>, <attrib2>, etc):\n\t\t\t\t\tsuper.__init__(<attrib1>, <attrib2>, etc)\n\n\t\tFor the method using "super.__init__()" there is no need to invoke \n\t\tthe parent\'s name, or the self argument. The super method will also import \n\t\tall of the parent\'s methods.\n\n\t\tCreating a method or attribute in the child with the same name as a method \n\t\tor attribute as the parent, the child\'s definition will overide the parent\'s.',

	'child/parent classes':	'The child class is a class definition that is based off of an \n\t\talready existing class. The already existing class is called a parent class.\n\t\tThe parent class must be included in the file the child class will exist in.\n\t\tAttributes from the parent class are initialized in the child class as follows:\n\n\t\t\tclass <ParentClass>(self):\n\t\t\t\t<block of attribute and method definitions>\n\n\t\t\tclass <ChildClass>(<ParentClass>):\n\t\t\t\tdef __init__(self, <attrib1>, <attrib2>, etc):\n\t\t\t\t\tsuper().__init__(<attrib1>, <attrib2>, <attrib3>)\n\n\t\tThe super()._init__ method',

	'docstring':		'A string that beging with "\'\'\'" and ends with \n\t\tthe same.  This is a multi-line comment that should be placed at the beginning of\n\t\tfunctions, method definitions, and class modules. They look like one of \n\t\tthese two options:\n\n\t\t\t\'\'\'<text describing the code block that follows>\'\'\'\n\n\t\t\t\'\'\'\n\t\t\t<text describing the code block that follows>\'\'\'',  
	'importing classes':	'You can import classes into other programs.  The import rules basically \n\t\tstay the same.  The main difference is that you must use: \n\n\t\t\tfrom <file in same directory as the current file> import <Class>\n\n\t\tIf you want to import multiple classes from the same module, you must import each class \n\t\tseparately and the classes must be separated by a comma:\n\n\t\t\tfrom <file in same directory as the current file> import <Class1>, <Class2>, etc\n\n\t\tAnother way to import classes is to import the entire module and then use \n\t\tdot notation to call the classes from the module:\n\n\t\t\timport <module>\n\n\t\t\t<instance_name> = <module>.<ClassName>(<arguments>)',
	'module':		'A program that can be a function or a class or an entire other program.',
	'standard library':	'A module created by other programers that are automatically \n\t\tdownloaded with the installation of python. These are called in the \n\t\tsame way that any module is imported.',
	'external library': 	'A module created by other programers that you must download\n\t\tbefore you are able to import it.',
	'open()':		'A function that opens a file to use within a program.\n\t\tIt only needs one argument which is the \n\t\tname of the file, if its in the same directory as the current program,\n\t\tor the path to the file.\n\n\t\t\twith open(\'<file_name>\') as <local_name_for_file>\n\n\t\tThere are several modes you can open the file with:\n\n\t\t\t* r -- read only\n\t\t\t* r+ -- both read a write\n\t\t\t* w -- write to the file. This will create the file if it doesn\'t already \n\t\t\t\texist and will overwrite the data in the file if the file does exist.\n\t\t\t\tThis function has the method *.write() that will write to the the specified \n\t\t\t\tfile. The argument must be the data you want to write to the file.\n\t\t\t\tPython can only write strings to files. If you want to write other data\n\t\t\t\tyou must convert it to a string first using str(). If you must add a \n\t\t\t\tnewline char to the string anytime you need a newline.\n\t\t\t* a -- append to a file. Unlike \'w\' mode, this will not overwrite the file.\n\n\t\tThe full syntax for open() is:\n\n\t\t\topen(\'<path/to/file>\', mode=’r’, buffering=-1, \n\t\t\t\tencoding=None, errors=None, newline=None, closefd=True, opener=None)\n\n\t\tIf you have special chars use \'r\' before the file string to read the whole path as a string:\n\n\t\t\topen(r\'<path/to/file>\')\n\n\t\tUsing relative paths are generally shorter than absolute paths.  When using \n\t\tabsolute paths, its a good idea to store the paht in a var \n\t\tbefore passing it to open().\n\n\t\t\tfile_name = <full/path/to/file>\n\t\t\topen(file_name)', 
	'with statement':	'Used in exception handling. When used before open(), with \n\t\twill close the file when it is no longer needed.',
	'as keyword':		'The as keyword creates an alias for an object.\n\n\t\t\timport <path/to/file> as <alias>\n\n\t\tThis imports a module and is callable via its alias name.',   
	'*.read() method':	'The *.read() method reads the entire contents of the file it appends\n\t\tand stores it as a single long \n\t\tstring into the desired var name.',
	'*.readlines() method':	'The *.readlines() method reads each line of a file into \n\t\ta specified var as a list. This can be used to work with data in a file \n\t\toutside of the with statement.',
	'in statement': 	'The in statement checks for membership. For example, if a specified\n\t\tstring exists in a larger string. Can be used in an if statement and if \n\t\tTrue it runs the code block under if, if False, it runs the else block \n\t\tor moved to the next block.',
	'*.replace() method':	'The replace method can read from a string and replace the first\n\t\targument with the second argument:\n\n\t\t\tmessage = "I really like dogs!"\n\t\t\tmessage.replace(\'dog\', \'cat\')\n\n\t\tThe above will change all instances in message from \'dog\' to \'cat\'.',
	'try-except-else statement':	'A try-except-except statement handles exceptions in a way that is more \n\t\tfriendly for the user:\n\n\t\t\ttry:\n\t\t\t\t<code block>\n\t\t\texcept <expected error type>:\n\t\t\t\t<user friendly message or code block>\n\t\t\telse:\n\t\t\t\t<block that requires the try to be successful>\n\n\t\tPython with try the code block after the try statement. If it successfully \n\t\truns, it ignores the except block. If the try statement fails, Python \n\t\twill look for an except block that has a matching error type and run that \n\t\tblock. After the the try-except block runs, regardless of the outcome, the \n\t\tprogram will continue running.The else block will run if the try \n\t\tblock is successful. If the except block is invoked, Python will ignore the\n\t\telse block and continue running the rest of the code.\n\n\t\tIf you want an error to pass silently, use the keyword "pass" as the except block.\n\n\t\t\ttry:\n\t\t\t\t<code block>\n\t\t\texcept <expected error type>:\n\t\t\t\tpass\n\t\t\telse:\n\t\t\t\t<block that requires the try to be successful>', 
	'*.split() method':	'The split() method will split all the words in a string and place\n\t\tthem in a list.\n\n\t\t\ttext = <object>.split()\n\t\t\tprint(text)\n\t\t\t[<the contents of the list>]',
	'*.read() method':	'The read() method will read a quantity of data from an already \n\t\textant file. The argument is the number of characters you want to read.\n\t\tIf the arugment is empty it will read and return the entire \n\t\tcontents of the file.\n\n\t\t\t<filename>.read(<#>)',
	'*.readline() method':	'The readline() method reads a single line from an extant file. A newline (\\n) \n\t\tcharacter is left at the end of the string. Use rstrip() \n\t\tor strip() methods to remove the newline character. If the string\n\t\tis empty, only the newline character will be returned.\n\n\t\t\t<filename>.readline()',
	'*.readlines() method':	'The readlines() method returns a list containing each line in a file.',
	'json':			'JSON stands for JavaScript Object Notation. It can be used with\n\t\tmany programming languages, including Python.\n\n\t\tIt is imported into the current file with:\n\n\t\t\timport json',
	'json.load()':		'The load() method loads json data from an outside file using the \n\t\tfollowing syntax:\n\n\t\t\timport json\n\n\t\t\twith open(<filename>) as <alias>:\n\t\t\t\t<variable> = json.load(<alias>)\n\n\t\tThe above loads json data in from the file, <filename>, \n\t\topened as <alias>, and loads it into the variable, <variable>.', 
	'json.dump()':		'The dump() method exports data into a json file. If the file does not \n\t\texist, it will be created and the file must be opened or created in \n\t\twrite mode.\n\n\t\t\timport json\n\n\t\t\twith open(<filename>, \'w\') as <alias>:\n\t\t\t\tjson.dump(<object_with_data>, <filename|alias>)\n\n\t\tThe above loads the json module, opens/creates the json file in write \n\t\tmode, and loads in the data from another object', 
	'refactoring':		'The process of breaking up code into a series of functions with specific jobs.',
	'none':			'None is a keyword that should be used when you do not wish a function to \n\t\treturn anything:\n\n\t\t\tdef <func_name>():\n\t\t\t\t<block of code>\n\t\t\t\treturn None\n\n\t\tRemember that the keyword "None" must be capitalized to be a keyword.',
        }

