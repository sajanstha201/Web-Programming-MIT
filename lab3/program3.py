file=open("/Users/sajanshrestha/Desktop/Web Programming/lab3/p3.txt","r")
content=file.read().split(' ')
dict={}
for e in content:
    if(e not in dict.keys()):
        dict[e]=1
    else:
        dict[e]=dict[e]+1
l=list(dict.items())
for i in range(len(l)):
    for j in range(i,len(l)):
        if(l[i][1]<l[j][1]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
for i in range(10 if len(l)>10 else len(l)):
    print(l[i])