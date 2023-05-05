from re import search

doc=[]
tags={
   'تعريف الملف':"!DOCTYPE html",
   'البداية':"html"
}
attr={
  'تصميم':"style",
  'لينك':"herf"
}
with open("input.txt") as file:
    for row in file:
        doc.append(row)

print(doc)
with open("output.html", "w") as file:
    for row in doc:
        if catches := search(r'^<(/?[ابجدهوزكلمنحطى سعفصقرشتثخذضظغية]+)( ([ابجدهوزكلمنحطى سعفصقرشتثخذضظغي]+)=".+")?>$', row):
         if catches.group(1) in tags:
           file.write('<' + tags[catches.group(1)] + '>\n')
           print(catches.group(2))
         else:
           file.write('</' + tags[catches.group(1)[1:]] + '>/n')
        else:
          file.write(row)
