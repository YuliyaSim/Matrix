"""
The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column,
select only the alphanumeric characters and connect them, then he replaces every group of symbols
between two alphanumeric characters by a space.
"""

matrix =[
    ("7"," ","3"),
    ("T","s","i"),
    ("h", "%", "x"),
    ("i", " ", "#"),
    ("s", "M", " "),
    ("$", "a", " "),
    ("#", "t", "%"),
    ("i", "r", "!")
]

for column in range(3):
    for elem in matrix:
        a = elem[column]
        if a.isalnum():
            print(a)
        else:
            print(" ")



