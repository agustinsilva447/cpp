class Queue2Stacks(object):
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element)
    
    def dequeue(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)
    
for i in range(2):
    print(q.dequeue())

for i in range(5):
    q.enqueue(i)
    
for i in range(6):
    print(q.dequeue())