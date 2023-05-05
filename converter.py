from re import search

doc=[]
with open("input.txt") as file:
    for row in file:
        doc.append(row)

with open("output.html") as file:
    for row in doc:
        if catches := search(r'(<\?[ابجدهوزكلمنحطىسعفصقرشتثخذضظغية ]+)>', row):
            print(catches.group(1))
