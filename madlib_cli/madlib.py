from textwrap import dedent
import re  # import using regex

"""
Mad Libs
The user is prompted to input random words which
will be used to form a story with a default text file
"""  
def greeting():
    """Greet the user and provide instructions."""
    line_one = 'Welcome to madlibs game !!!!'
    line_two = 'You will be asked to input some words to play the game !!!'
    line_three = 'To exit the game please , type "quit"'

    print(dedent(f'''
        {'*' * 60}
        {line_one}
        {line_two}
        {line_three}
        {'*' * 60}
        '''))
    
    
######################################################################### 

def read_template(path):
    """Read a file path and return its contents as a string"""
    with open(path, 'r') as f:
        return f.read()
    
    
    
#########################################################################    
def write_file(path, out):
    """Write a file back to the given path."""
    with open(path, 'w') as wf:
        return wf.write(out)
    
    
######################################################################### 
def parse_template(format_string):
    """
    The text file contains several words classes
    surrounded by curly braces. and its gonna use those curly braces to
    create keys for each of them.
    First, to find out how many keys I need to run a count
    on the input string for all the open curly braces
    Then form the keys by finding the index of
    each set of curly and slicing out substring
    of each.
    The end result should be an array of each word contained
    in two curly braces
    """
    keys = []
    end = 0

    word_count = format_string.count('{')
    for i in range(word_count):
        # +1 so we get the first char inside the curly
        start = format_string.find('{', end) + 1
        end = format_string.find('}', start)
        key = format_string[start:end]
        keys.append(key)
    print(keys)
    return keys


######################################################################### 
def merge(constant , words):
    """
    Returns a string with user input strings
    Arguments:
        constant {string} -- text contains empty {}
    Output:
         {string} -- replacing {} to words from the user 
    """
    lst = parse_template(constant)  
    return (re.sub(r' {[^}]*}',' {}',constant)).format(*words) 



######################################################################### 
def copyFile(text):
    print(text)
    file = open('./assets/template.txt','w')
    file.write(text)



######################################################################### 
if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("You will be asked to input some words to play the game !!!")
    
    content = read_template()
    
    lst = parse_template(content)
    
    words=[]
    for i in range(len(lst)):
        words.append(input("enter a {} ".format(lst[i])))
    toCopy = merge(content, words)
    copyFile(toCopy)
    
