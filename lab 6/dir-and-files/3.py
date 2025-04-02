import os
def check(path):
    if os.path.exists(path):
        print("The path ", path, "exists")
        print("Dir: ", os.path.dirname(path))
        print("File: ", os.path.basename(path))
    else:
        print("The path ", path, "doesn't exist")

path = "test doc.txt"
check(path)