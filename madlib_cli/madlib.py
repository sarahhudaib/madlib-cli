from textwrap import dedent 
import re  # for regex 

"""
Mad Libs
The user is prompted to input random words which
will be used to form a story with a default text file
"""

def greet_user():
    """
    This greets the user when they first start
    No input/output
    """

    ln_1 = 'Welcome to Madlibs Game!!'
    ln_2 = 'You will be asked to input some words to play the game !!!'
    ln_3 = 'When done, you\'ll receive a funny story!!!'
    ln_4 = 'your completed madlibs will be saved in a filled_template.txt file.'
    ln_5 = 'To exit at any time, don\'t type "quit" you can easily press the x button on your window :)'

    print(dedent(f'''
    {'*' * 100}
    {'{:^100}'.format(ln_1)}
    {'{:^100}'.format(ln_2)}
    {'{:^100}'.format(ln_3)}
    {'{:^100}'.format(ln_4)}
    {'{:^100}'.format(ln_5)}
    {'*' * 100}
    '''))
    
    
def read_template():
    """
    Returns the template.txt file 
    """
    try:
        file = open("madlib_cli/assets/template.txt",'r')
        content = file.read()
        return content   
    except FileNotFoundError:
        raise FileNotFoundError('Your file was not found')
    except IOError:
        raise IOError('There was an error reading your file')
    


def parse(constant): # constant refers to the text
    """
    Returns a list of words inside {} in a given text
    Arguments:
        constant {string} -- text contains words inside {}
    Output:
        lst {list of string} -- the words inside {} 
    """
    print("Please provide the following words: ")
    lst=[]
    res = re.findall(r'\{.*?\}', constant) 
# to find all the curly braces which have value inside it too 
# then put all of them and their values inside res
    for i in res:
        lst.append(i.strip("{ }")) 
      
        
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
        
# to remove every value in curly braces ,and get empty curly braces 
    return lst

def merge(constant , words):  

    """
    Returns a string with user input strings
    Arguments:
        constant {string} -- text contains empty {}
    Output:
         {string} -- replacing {} to words from the user 
    """
    lst = parse(constant)  
# constant is the parsed text which has text and empty{} 
# to put things inside curly braces in the step below
    
    return (re.sub(r' {[^}]*}',' {}',constant)).format(*words) 
# sub() function is used to replace occurrences of a particular sub-string with another sub-string. 
# we use string.format() to give the string text which have text and 
# empty curly braces values one by one from the values in format 

""" we put * before the name of array so it will take elements one 
    by one in the array which is (words), then put each value into 
    empty braces """

def copyFile(text):
    print(text)
    file = open('madlib_cli/assets/filled_template.txt','w')
    file.write(text)

def run():
    """
    this is the brains of the operation
    This runs the whole madlibs program.
    """
    greet_user()
    
    content = read_template()
    lst = parse(content)
    words=[]
    for i in range(len(lst)):
        words.append(input("enter a {} ".format(lst[i])))
 
 
    copyFile(merge(content, words))


if __name__ == "__main__":
    run()
    