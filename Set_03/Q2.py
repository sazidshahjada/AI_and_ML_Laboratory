import heapq
GRAPH={"S":[("A",2),("B",4)],"A":[("C",2),("D",5)],"B":[("D",1)],"C":[("G",5)],"D":[("G",3)],"G":[]}
H={"S":6,"A":5,"B":4,"C":4,"D":2,"G":0}
def astar(h):
    pq=[(h["S"],0,"S")]; best={"S":0}; parent={"S":None}; expanded=[]; details=[]
    while pq:
        f,g,u=heapq.heappop(pq)
        if g!=best.get(u): continue
        expanded.append(u); details.append((u,g,h[u],g+h[u]))
        if u=="G":
            path=[]; v="G"
            while v is not None: path.append(v); v=parent[v]
            return path[::-1],g,expanded,details
        for v,c in GRAPH[u]:
            ng=g+c
            if ng<best.get(v,float("inf")):
                best[v]=ng; parent[v]=u; heapq.heappush(pq,(ng+h[v],ng,v))
    return None,float("inf"),expanded,details
for label,h in [("Given heuristic",H),("Zero heuristic (Uniform-Cost Search)",{n:0 for n in H})]:
    path,cost,expanded,details=astar(h)
    print(f"\\n{label}:")
    print("Expansion sequence:",expanded)
    print("Popped node (node,g,h,f):",details)
    print("Optimal path:",path,"total cost:",cost)
print("Note: the supplied heuristic is not guaranteed admissible/consistent; the zero heuristic reduces A* to uniform-cost search.")
