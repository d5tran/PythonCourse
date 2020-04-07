#methods are functions built into objects

def name_function():
    '''
    DOCSTRING: Information about hte function
    Input: name
    OUtput: hello
    '''
    print ('Hello')

name_function()
#help(name_function)

#Find if dog is in a string

def dog_string(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

#Pig Latin: starts a vowel, add 'ay' to the end
#if the word does not start with a vowel, put the first letter at the end, then add 'ay'

def pig_latin(word):
    
    first_letter = word[0]

    if first_letter in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + first_letter + 'ay'

print(pig_latin('sexy'))
