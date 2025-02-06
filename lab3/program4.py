file=open("/Users/sajanshrestha/Desktop/Web Programming/lab3/p3.txt","r")
file2=open("/Users/sajanshrestha/Desktop/Web Programming/lab3/p4.txt","w")
content=file.readlines()
sorted_content=sorted(content)
for e in sorted_content:
    file2.write(e)