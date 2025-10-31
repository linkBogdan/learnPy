# This project is meant to help with my scheduling issues. I often miss getting any work done and whenever I get back to this I have to count
# So this program will give me what file I'm on and what day.
import os
    
# This will print the path to the root    
def get_path():    
    root_path = os.getcwd()
    return root_path

x = get_path()
print(x)