import os

def check_path_access(path):
    print("Checking access for: ", path)
    print("Exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = "test doc.txt"
check_path_access(path)