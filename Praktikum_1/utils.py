cities = ['Or', 'Ne', 'Ze', 'Ia', 'Ar', 'Si', 'Fa',
 'Va', 'Ri', 'Ti', 'Lu', 'Pi', 'Ur', 'Hi',
 'Me', 'Bu', 'Dr', 'Ef', 'Cr', 'Gi'],
[
   ('Or', 'Ze', 71), ('Or', 'Si', 151),
   ('Ne', 'Ia', 87), ('Ze', 'Ar', 75),
   ('Ia', 'Va', 92), ('Ar', 'Si', 140),
   ('Ar', 'Ti', 118), ('Si', 'Fa', 99),
   ('Si', 'Ri', 80), ('Fa', 'Bu', 211),
   ('Va', 'Ur', 142), ('Ri', 'Pi', 97),
   ('Ri', 'Cr', 146), ('Ti', 'Lu', 111),
   ('Lu', 'Me', 70), ('Me', 'Dr', 75),
   ('Dr', 'Cr', 120), ('Cr', 'Pi', 138),
   ('Pi', 'Bu', 101), ('Bu', 'Gi', 90),
   ('Bu', 'Ur', 85), ('Ur', 'Hi', 98),
   ('Hi', 'Ef', 86)
]

def getNode(name, l):
   return next(( i for i in l if i.name == name), -1)

class Queue:
    def __init__(self):
        self.fifo = []
        self.lifo = []
        self.prio = {}
    
    def fifoEnque(self,element:object) -> bool:
        self.fifo.insert(0,element)
        return True
            
    def fifoDeque(self) -> bool:
        if(len(self.fifo)>0):
            self.fifo.pop()
            return True
        return False
    
    def lifoEnque(self,element:object) -> bool:
        self.lifo.insert(0,element)
        return True
    
    def lifoDeque(self) -> bool:
        if(len(self.lifo) >0):
            self.lifo.pop(0)
            return True
        return False
    
    # def prioEnque(self,priority:int,element:object) -> bool:
    #implement when it gets clear what to do with it      
    