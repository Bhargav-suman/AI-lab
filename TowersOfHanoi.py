def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        move_disk(from_rod, to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    move_disk(from_rod, to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

def move_disk(from_rod, to_rod):
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    print_rods_state()

def print_rod_state(rod_name, disks):
    print(rod_name + ":", disks)

def print_rods_state():
    for rod_name, disks in rods.items():
        print_rod_state(rod_name, disks)
    print()

n = int(input("Enter the number of disks: "))
rods = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

print(f"Tower of Hanoi Solution for {n} disks:")
print_rods_state()

TowerOfHanoi(n, 'A', 'B', 'C')




































'''n = int(input("enter no.of disks:"))
p = 2**n-1
c=0
m=[]
e=[]
g=[]
a=[]

for i in range(n):
    e.append(i+1)

m = e[:]
m = list(e)
k=m[n-1]

if n%2==0:
    a.append(e[0])
    e.remove(e[0])
    g.append(e[0])
    e.remove(e[0])
    c+=2
else:
    g.append(e[0])
    e.remove(e[0])
    a.append(e[0])
    e.remove(e[0])
    c+=2

def comp1(y,z):
    if y>z and len(e)==0 and g[0]!=k:
        g.append(z)
        a.remove(z)
    else:
        if z%2!=0 and y%2==0:
            g.append(z)
            a.remove(z)
        else:
            e.append(z)
            a.remove(z)
    return
    
def comp2(x,z):
    if x>z and len(g)==0:
        g.append(x)
        e.remove(x)
    else:
        a.append(X)
        e.remove(x)
    return

def comp3(x,y):
    if x>y and len(a)==0:
        a.append(x)
    else:
        g.append(x)
    return

def comp4(x,y,z):
    if x>y and x>z:
        if y>z:
            if(y%2!=0 and z%2!=0):
                e.insert(e[0],y)
                a.remove(y)
            else:
                g.append(z)
                a.remove(z)
        else:
            a.append(y)
            g.remove(y)
    else:
        if y>z:
            g.append(z)
            a.remove(z)
        else:
            a.append(y)
            g.remove(y)
    return

def comp5(x,y,z):
    if y==k:
        if x<z:
            g.append(z)
            a.remove(z)
        else:
            e.append(z)
            a.remove(z)
    else:
        if x>y and x<z:
            e.insert(e[0],y)
            g.remove(y)
        elif x<y and x>z:
            g.append(x)
            e.remove(x)
    return



while c!=0:
    if len(e)==0:
        comp1(g[len(g)-1],a[len(a)-1])
        c+=1
    elif(len(g)==0):
        comp2(e[0],a[len(a)-1])
        c+=1
    elif(len(a)==0):
        comp3(e[0],g[len(g)-1])
        c+=1
    else:
        if g[0]!=k:
            comp4(e[0],g[len(g)-1],a[len(a)-1])
            c+=1
        else:
            comp5(e[0],g[len(g)-1],a[len(a)-1])
            c+=1
    if(g == m.reverse()):
        break
print(c)'''


'''# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
N = 4

# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

# Contributed By Harshit Agrawal'''

    
