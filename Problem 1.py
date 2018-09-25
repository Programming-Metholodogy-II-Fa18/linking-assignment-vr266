class ArbitraryQueue: 
    l=[]
    count=1
    def ArbitraryQueue(self):
          z=[]  
    def Push(self,q):
            ArbitraryQueue.l += [0]*1
            
            i=len(ArbitraryQueue.l)
            while i>0:
                ArbitraryQueue.l[i-1]=ArbitraryQueue.l[i-2]
                i-=1
            ArbitraryQueue.l[0]=q
            print(ArbitraryQueue.l)
            ArbitraryQueue.count+=1
    def Enqueue(self,q):
        ArbitraryQueue.l += [0]*1
        ArbitraryQueue.l[len(ArbitraryQueue.l)-1]=q
        print(ArbitraryQueue.l)
    def Pop(self):
        z=[0]*(len(ArbitraryQueue.l)-1)
        i=len(z)
        while i>0:
            z[i-1]=ArbitraryQueue.l[i]
            i-=1  
        print(ArbitraryQueue.l[0])
        print(z)
    def Dequeue(self):
        z=[0]*(len(ArbitraryQueue.l)-2)
        i=0
        print(z)
        while i<len(z):
            z[i]=ArbitraryQueue.l[i+1]
            i+=1  
        print(ArbitraryQueue.l[len(z)+1])
        print(z)
    def Transverse(self,q)
        print(ArbitraryQueue.l[q])

