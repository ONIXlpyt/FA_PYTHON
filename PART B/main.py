import library_module

books = {
    "Python 101": "Philip Robbins",
    "Data science": "Jannah Mohd"
}

#add new book from user input
title = input("Enter book title:")
author = input("Enter book author:")
books[title] = title
books[author]= author

#save to file
with open("book.txt", "w") as f:
    for t, a in books.items():
        f.write(f"{t}:{a}\n")

#read File
with open("book.txt", "r") as file:
    lines = file.readline()


print("\nBook list from file:")
for line in lines:
    t, a = line.strip().split(":")
    b = books(t, a)
    b.Display_info()
