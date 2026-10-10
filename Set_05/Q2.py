import heapq
GRAPH={"A":[("B",2),("C",3)],"B":[("D",4),("E",2)],"C":[("E",2)],"D":[("G",3)],"E":[("G",4)],"G":[]}
H={"A":6,"B":5,"C":4,"D":2,"E":3,"G":0}
def search(mode):
    pq=[(H["A"] if mode=="greedy" else H["A"],0,"A")]; gbest={"A":0}; parent={"A":None}; expanded=[]; tie=0
    while pq:
        pri,g,u=heapq.heappop(pq)
        if mode=="astar" and g!=gbest.get(u): continue
        expanded.append(u)
        if u=="G":
            path=[]; n=u
            while n is not None: path.append(n); n=parent[n]
            return path[::-1],g,expanded
        for v,c in GRAPH[u]:
            ng=g+c
            if mode=="greedy":
                if v not in parent: parent[v]=u; gbest[v]=ng; tie+=1; heapq.heappush(pq,(H[v],tie,v))
            elif ng<gbest.get(v,float("inf")):
                gbest[v]=ng; parent[v]=u; tie+=1; heapq.heappush(pq,(ng+H[v],ng,v))
    return None,float("inf"),expanded
for m in ["greedy","astar"]:
    p,c,e=search(m); print(m.upper(), "expanded=",e,"path=",p,"path cost=",c)
print("Greedy ranks only h(n), while A* ranks g(n)+h(n); a locally attractive heuristic node can lead to a more expensive route.")
