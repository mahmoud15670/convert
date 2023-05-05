from re import search

doc=[]
tags={
   'تعريف الملف':"!DOCTYPE html",
   'البداية':"html",
   'الراس':"head",
   'الجسم':"body",
   'فقرة':"p"
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
         elif catches.group() in tags and catches.group(3) in attr:
            file write('<' + tags[catches.group(1)] + ' ' + attr[catches.group(3)] + catches.group(2).replace(catches.group(3)) + '>\n')
         else:
           file.write('</' + tags[catches.group(1)[1:]] + '>/n')
        else:
          file.write(row)
