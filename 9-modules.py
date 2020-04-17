#Modules are just .py scripts that you call in another .py script
#Packages are a collection of modules.

#to import packages, the directory needs a __init__.py file
#example:
#Parent directory 'MyMainPackage' has a file called 'some_main_script'
#from MyMainPackage import some_mainscript
#example2:
#Parent directory 'MyMainPacakge' has a subfolder 'SubPackage' has a file called 'mysubscript'
#from MyMainPackage.SubPackage import mysubscript

def myfunc ():
    print('I am in 9-modules.py')
