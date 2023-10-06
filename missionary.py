c = int(input('enter no.of cannibals:'))
m = int(input('enter no.of missionaries:'))
c1=0
m1=0
s = [c,m,1]
g = [c1,m1,0]
while(s!=[0,0,0]):
    if(s==[c,m,1] and g==[0,0,0]):
        s=[c-1,m-1,0]
        g=[c1+1,m1+1,1]
        print(s)
        print(g)
    elif(s==[c-1,m-1,0] and g==[c1+1,m1+1,1]):
        s=[c+1,m-1,1]
        g=[c1-1,m1+1,0]
        print(s)
        print(g)
        

        
        
