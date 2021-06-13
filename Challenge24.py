#Some of it probably only works on windows 10
import os
import platform
import os.path
import string
import random

def open_editor():
    operating_system = platform.system()
    #Windows
    if operating_system == "Windows":
        os.system("start file.txt")
    #Mac honestly no idea whether or not this works
    elif operating_system == "Darwin":
        os.system("open " + shlex.quote("file.txt"))

def suggest_pass():
    s_pass = ""
    for i in range(8):
        char = random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        s_pass += char
    return s_pass

if __name__ == "__main__":
    if os.path.isfile("file.txt"):
        open_editor()
    else:
        n_pass = suggest_pass()
        print(n_pass)
        file = open("file.txt", "a")
        file.close()
    


