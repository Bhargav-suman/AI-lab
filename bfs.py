def bfs(graph, start, goal):
    queue = []
    visited = []
    queue.append(start)
    visited.append(start)
    path = ""
    found = False
    
    while queue:
        m = queue.pop(0)
        path += m + " "
        if m == goal:
            found = True
            break
        for neighbour in graph.get(m, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    if found:
        print("Goal node found")
        print("Path:", path)
    else:
        print("Goal node not found")

n = int(input("Enter no. of nodes: "))
graph = {}
print("enter parent nodes and child nodes simultaneously")
for i in range(1,n+1):
    print('node-',i,end='\t')
    key = input()
    print(end='\t')
    value = input().split()
    graph[key] = value

start = input("Enter start node: ")
goal = input("Enter goal node: ")
bfs(graph, start, goal)
