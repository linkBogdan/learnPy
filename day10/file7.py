# This project is meant to help with my scheduling issues. I often miss getting any work done and whenever I get back to this I have to count
# So this program will give me what file I'm on and what day.
import os
    
# Function that lists every directory that starts with 'day'.
def list_dir():
    
    with os.scandir(path=get_path()) as it:
        for entry in it:
            if entry.name.startswith('day') and entry.is_dir():
                print(entry.name)


# This will print the path to the root    
def get_path():    
    root_path = os.getcwd()
    return root_path

list_dir()