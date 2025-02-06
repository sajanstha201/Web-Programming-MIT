class subset:
    def __init__(self,arr):
        self.arr=arr
    def subset(self,level,selected):
        if(level==len(self.arr)):
            print([self.arr[i] for i in range(len(selected)) if selected[i]])
            return
        selected[level]=0
        self.subset(level+1,selected)
        selected[level]=1
        self.subset(level+1,selected)
        return
        
    def getsubsets(self):
        selected=list([0 for i in range(len(self.arr))])
        self.subset(0,selected)
input_list=list(map(int,input("Enter the list element: ").split(' ')))
s=subset(input_list)
s.getsubsets()