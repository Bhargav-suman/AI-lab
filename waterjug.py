x = int(input('enter the water in jar1:'))
y = int(input('enter the water in jar2:'))
z = int(input('enter the quantity you want to measure:'))
s = [0,0]
g1 = [z,0]
g2 = [0,z]
l1=[[0,0]]
l2=[[0,0]]
c1 = 0

while(s!=g1 and s!=g2):
    if(s[0]<x and s[0]==0):
        if(s[1]==0):
            s = [x,0]
            c1+=1
            l1.append(s)
        else:
            s = [x,s[1]]
            c1+=1
            l1.append(s)
    if((s[0]+s[1])>=y and s[0]>0):
        s = [(x-(y-s[1])),y]
        c1+=1
        l1.append(s)
    if(s[1]>0 and s[1]==y):
        s = [s[0],0]
        c1+=1
        l1.append(s)
    if((s[0]+s[1])<=y and s[0]>0):
        s = [0,s[0]+s[1]]
        c1+=1
        l1.append(s)

c2=0
s=[0,0]

while(s!=g1 and s!=g2):
    if(s[1]<y and s[1]==0):
        if(s[0]==0):
            c2+=1
            s = [0,y]
            l2.append(s)
        else:
            c2+=1
            s = [s[0],y]
            l2.append(s)
    if((s[0]+s[1])<=x and s[1]>0):
        c2+=1
        s = [s[0]+s[1],0]
        l2.append(s)
    if((s[0]+s[1])>=x and s[1]>0):
        c2+=1
        s = [x,(y-(x-s[0]))]
        l2.append(s)
    if(s[0]>0 and s[0]==x):
        c2+=1
        s = [0,s[1]]
        l2.append(s)

if(c1<c2):
    print('if water is poured from large jar to small jar:')
    print(l1)
    print('nuber of steps required to reach goal state ',c1-1)
else:
    print('if water is poured from smaller jug to larger jug:')
    print(l2)
    print('nuber of steps required to reach goal state is ',c2-1)
