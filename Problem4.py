def ProblemFourA(m):
    p=list(m)
    q=list(m)
    x=len(p)-1
    i=0
    while i<len(p):
        p[i]=q[x-i]
        i+=1
    s=''.join(p)
    print(s)

    
    
    
    
    
    
    
    def InsertionSort(l):
   for i in range(1,len(l)):
     val = l[i]
     target = i
     while target>0 and l[target-1]>val:
            l[target]=l[target-1]
            target = target-1
     l[target]=val
l = [54,26,93,17,77,31,44,55,20]
InsertionSort(l)

def Problem4C(q):
    I=9**q
    J=15**q
    K=7**q
    l=[I,J,K]
    i=0
    z=[0]*len(l)
    while i<3:
        z[i]=l[i]
        i+=1
    InsertionSort(z)
    print(z[0])
