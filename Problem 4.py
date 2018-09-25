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
