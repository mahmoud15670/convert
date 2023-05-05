from re import search

doc=[]
tags={
   'تعريف الملف':"!DOCTYPE html",
   'البداية':"html"
}
with open("input.txt") as file:
    for row in file:
        doc.append(row)

print(doc)
with open("output.html", "w") as file:
    for row in doc:
        if catches := search(r'^<(/?[ابجدهوزكلمنحطى سعفصقرشتثخذضظغية]+)>$', row):
         if catches.group(1) in tags:
           file.write('<' + tags[catches.group(1)] + '>\n')
         else:
           file.write('</' + tags[catches.group(1)[1:]] + '>/n')
        else:
          file.write(row)
