myfile = open('test.txt')

#Read method just returns the string in the text file
myfile.read()
#if you do another .read() it will return nothing because of the curser
#read method has a curser beginning at the file, so you have reset back to the beginning using seek(0)
myfile.seek(0)

#readlines returns each line in the text as its own line in a list.
myfile.readlines()

#To open a file at any location, use the full file path
#
#Best Practice, if the file is already open you need the with statement. If you use the with statement, you don't have to worry about closing the file at the end

with  open('test.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

# myfile.close() at the end

#Write to file
#Modes in open, r is read only 
# \w is write only (overwrites files or creates new)
# a is append only, r+ is reading and writing
# w+ is writing and reading (overwrites existing files or creats a new file!)

with open('test.txt',mode='r') as f:
    print(f.read())

# to append

with open('test.txt',mode='a') as f:
    f.write('\nthis is the fourth line')

with open('test.txt',mode='r') as f:
    print(f.read())

#writing, if the file doesn't exit it makes a new file

with open('newfile.txt',mode='w') as f:
    f.write('I created this file')

