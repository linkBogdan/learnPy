# This project is meant to help with my scheduling issues. I often miss getting any work done and whenever I get back to this I have to count
# So this program will give me what file I'm on and what day.
import os
import re
    
# Function that lists every directory that starts with 'day'.
def list_dir():
    
    with os.scandir(path=get_path()) as it:
        for entry in it:
            if entry.name.startswith('day') and entry.is_dir():
                print(entry.name)


# This will print the path to the root    
def get_path():    
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return root_path

entries = list(list_dir())
for entry in entries:
    match = re.match(r"day(\d+)$", list_dir())


x = get_path()
print (x)