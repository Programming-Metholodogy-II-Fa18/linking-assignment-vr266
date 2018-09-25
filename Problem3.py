
class integ:
    def InsertionSort(l):
        for i in range(1,len(l)):
            val = l[i]
            target = i
            while target>0 and l[target-1]>val:
            l[target]=l[target-1]
            target = target-1
         l[target]=val
    def Push(q,l):
        l+=[0]*1
        n=len(l)
        i=n
        while i>0:
            l[i-1]=l[i-2]
            i-=1
        l[0]=q
        print(l)
    def Pop(l):
        w=len(l)-1
        z=list(range(w))
        print(z)
        i=0
    while i<len(l)-1:
        z[i]=l[i+1]
        i+=1
    print(z)
    print(l[0])
    def PastPeek(l):
        print(l[len(l)-1])
