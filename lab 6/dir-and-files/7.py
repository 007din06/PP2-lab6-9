def copy(fr, to):
    with open(fr, 'r') as fr, open(to, 'w') as to:
        to.write(fr.read())
A = "test doc.txt"
B = "test doc3.txt"
copy(A, B)