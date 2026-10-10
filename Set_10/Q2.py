from collections import deque
import heapq
# Explicit positive costs and reasonable heuristic values, as requested in the question.
G={"S":[("A",2),("B",5)],"A":[("C",2),("D",4)],"B":[("D",1),("E",3)],"C":[("G",4)],"D":[("G",2)],"E":[("G",2)],"G":[]}
H={"S":5,"A":4,"B":3,"C":4,"D":2,"E":2,"G":0}
def path(parent,goal):
    if goal not in parent:return None
    out=[];n=goal
    while n is not None:out.append(n);n=parent[n]
    return out[::-1]
def bfs():
    q=deque(["S"]);parent={"S":None};seen={"S"};exp=[]
    while q:
        u=q.popleft();exp.append(u)
        if u=="G":break
        for v,c in G[u]:
            if v not in seen:seen.add(v);parent[v]=u;q.append(v)
    p=path(parent,"G");cost=sum(next(c for v2,c in G[u] if v2==v) for u,v in zip(p,p[1:])) if p else None
    return p,cost,exp
def informed(mode):
    q=[(H["S"] if mode=="greedy" else H["S"],0,"S")];parent={"S":None};best={"S":0};exp=[];serial=0
    while q:
        pri,g,u=heapq.heappop(q)
        if mode=="astar" and g!=best.get(u):continue
        exp.append(u)
        if u=="G":return path(parent,"G"),g,exp
        for v,c in G[u]:
            ng=g+c
            if mode=="greedy":
                if v not in parent:parent[v]=u;best[v]=ng;serial+=1;heapq.heappush(q,(H[v],serial,v))
            elif ng<best.get(v,float("inf")):
                best[v]=ng;parent[v]=u;serial+=1;heapq.heappush(q,(ng+H[v],ng,v))
    return None,None,exp
for name,fn in [("BFS (fewest edges)",bfs),("Greedy Best-First",lambda:informed("greedy")),("A*",lambda:informed("astar"))]:
    p,c,e=fn();print(f"{name}: expansion={e}, path={p}, path_cost={c}")
print("BFS minimizes edge count in an unweighted interpretation; with unequal costs, fewest edges need not be cheapest. A* accounts for accumulated edge cost.")
