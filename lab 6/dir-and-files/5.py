def write(path, data):
    with open(path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

lst = ["You", "Know", "Who"]
path = "test doc2.txt"
write(path, lst)