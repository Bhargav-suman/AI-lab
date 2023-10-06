c = int(input('enter no.of cannibals:'))
m = int(input('enter no.ofmissionaries:'))
b=1
c1=0
m1=0
b1=0
l = []
s = [c,m,b]
g = [c1,m1,b1]
while(s!=g):
    if b==1:
        if (s == [c,m,b] and g == [c1,m1,b1]):
            c-=1
            m-=1
            b=0
            c1+=1
            m1+=1
            b1=1
            l.append(s)
            l.append(g)
            print(l)
            l=[]
    else:
        if (s == [c-1,m-1,0] and g == [c1+1,m1+1,1]):
            c+=1
            b=1
            c1-=1
            b1=0
            l.append(s)
            l.append(g)
            print(l)
            l=[]
            break
        
