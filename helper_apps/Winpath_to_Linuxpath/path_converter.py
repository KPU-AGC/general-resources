'''
Author : Minuka Hewapathirana
Date: 09/05/2025

WINDOWS TO LINUX PATH CONVERTER 
Function which reads a string and replaces the old character with a new character
and returns a new file. The intended use for this function is to replace all
frontslashes with backslashes in a path name. This allows easy copy paste
from the windows system to linux system.

INPUT: string content, string old_char, string new_char
PROCESS: replace old_char with new_char
OUTPUT: no output, print statement within the function  
'''
def in_console_converter(content, old_char,new_char):
        
    modified_content = content.replace('Z:\\','/mnt/Z/')

    modified_content = modified_content.replace(old_char,new_char)
        
    print("Here is your linux path:\nPlease ctrl+c and paste in linux server with cd as a prefix command: \n"+ modified_content)
    
'''Main
Error handling is implemented to ensure blank entries are not allowed. 
''' 
try:  
    user_input = input("Please provide windows path: ")
    if len(user_input)<=0:
        raise ValueError("Please provide a string to convert")
    in_console_converter(user_input,'\\','/')
except ValueError as e:
    print("Invalid input:", e)
except Exception as e:
    print("An unexpected error occured:",e)

'''
This version of the function is an early prototype which uses txt files as 
input for stress testing. 
'''
def windows_to_linux_path_converter(file_path,old_char,new_char):
    try:
        with open(file_path,'r') as file:
         content = file.read()

        modified_content = content.replace('Z:\\','/mnt/Z/')
    
        modified_content = modified_content.replace(old_char,new_char)

        with open('linux_path.txt','x') as file:
            file.write(modified_content)

    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
    except Exception as e:
        print(f"An error occured:{e}")



