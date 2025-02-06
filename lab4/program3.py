class Inventory:
    def __init__(self,id,name,count,price):
        self.id=id
        self.name=name
        self.count=count
        self.price=price
    def add_item(self,count):
        self.count+=count
    def update_item(self,name):
        self.name=name
    def check_item(self):
        if(self.count==0):
            return False
        return True

dict={}
n=int(input("Enter the total number of item: "))
for i in range(n):
    obj=Inventory(i,input("Name: "),int(input("Count: ")),int(input("Price: ")))
    dict[obj.id]=obj
for id,obj in dict.items():
    print(id,obj.name)