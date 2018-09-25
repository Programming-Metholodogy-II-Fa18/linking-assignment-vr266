class ArbitraryArray: 
    l=[]
    count=1
    def ArbitraryArray(self):
          z=[]  
    def Insert(self,e,q):
        n=len(ArbitraryArray.l)
        if e>n:
            print("change") 
        else:
            ArbitraryArray.l +=[0]*1
            i=len(ArbitraryArray.l)
            while i>e:
                ArbitraryArray.l[i-1]=ArbitraryArray.l[i-2]
                i-=1
            ArbitraryArray.l[e]=q
            print(ArbitraryArray.l)
    def Push(self,q):
            ArbitraryArray.l += [0]*1
            
            i=len(ArbitraryArray.l)
            while i>0:
                ArbitraryArray.l[i-1]=ArbitraryArray.l[i-2]
                i-=1
            ArbitraryArray.l[0]=q
            print(ArbitraryArray.l)
            ArbitraryArray.count+=1
    def Enqueue(self,q):
        ArbitraryArray.l += [0]*1
        ArbitraryArray.l[len(ArbitraryArray.l)-1]=q
        print(ArbitraryArray.l)
    def Pop(self):
        z=[0]*(len(ArbitraryArray.l)-1)
        i=len(z)
        while i>0:
            z[i-1]=ArbitraryArray.l[i]
            i-=1  
        print(ArbitraryArray.l[0])
        print(z)
    def Dequeue(self):
        z=[0]*(len(ArbitraryArray.l)-2)
        i=0
        print(z)
        while i<len(z):
            z[i]=ArbitraryArray.l[i+1]
            i+=1  
        print(ArbitraryArray.l[len(z)+1])
        print(z)
    def Transverse(self,q)
        print(ArbitraryArray.l[q])
