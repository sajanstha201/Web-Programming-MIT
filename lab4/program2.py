class sumPair:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def getPairedElement(self):
        for i in range(len(self.arr)):
            for j in range(i,len(self.arr)):
                if(self.arr[i]+self.arr[j]==self.target):
                    return i,j
        return -1

arr=list(map(int,input("Enter the list element: ").split()))
target=int(input("Enter the target element"))
obj=sumPair(arr,target)
print("index: ",obj.getPairedElement())