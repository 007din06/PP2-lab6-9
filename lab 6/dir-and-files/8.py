import os

def delete(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File has been deleted.")
        else:
            print("Permission denied.")
    else:
        print("File does not exist.")

path = "test doc3.txt"
delete(path)