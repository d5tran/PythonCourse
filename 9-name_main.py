#Sometimes when you are importing from a module, you would like to know whether a module function is being used as an import
#or if you are using the original .py file off that module

#Have two files: one.py, two.py

#python has no "main" function
#python has a built in variable called __main__ , this variable gets assigned a string depending on how you run the script

#if you run a script directly, python automatically assigns __name__ = "__main__"

#if __name__ == "__main__"
#   myfunc()
#   myfunc2()