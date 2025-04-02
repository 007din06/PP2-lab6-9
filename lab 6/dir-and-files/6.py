for i in range(0, 26):
    file = f"{chr(ord('a')+i)}.txt"
    with open(file, 'w') as file:
        file.write("Youknowwho\n")
print("text files are created")