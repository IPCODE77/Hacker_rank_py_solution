class train:
    def __init__(self,name,seats,cost,time):
        self.name=name
        self.seats=seats
        self.cost=cost
        self.time=time
    def bookticket(self):
        print(f'Hii {self.name} Indian Railway welcomes to you.')
        if(len(self.seats)>0):
            ticket=int(input("Enter which set you want--> "))
            length=len(self.seats)
            for i in self.seats:
                if(ticket==i):
                    print("Your seat is booked")
                    self.seats.remove(ticket)
                    length=length-1
                    break
                else:
                    print("invalid seat number") 
        else:
            print("Sorry train is full")            
                     
    def cancel(self):
        cancelticket=int(input("Enter your ticket number--> "))
        length=len(self.seats)
        self.seats.append(cancelticket)
        self.seats.sort()
        # or
        # self.seats.insert(cancelticket-1,cancelticket)
        length=length+1
    def statuc(self):
        print(f'Train name {self.name} total number of set present is {self.seats} {len(self.seats)} per seat cost is {self.cost} on time {self.time}')   

list=[1,2,3,4,5,6,7,8,9,10]
people=train('local',list,90,'1.20pm')
print(people.statuc())    
print(people.bookticket())    
print(people.statuc())    
print(people.cancel())
print(people.statuc())    


