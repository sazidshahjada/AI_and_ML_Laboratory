import heapq
GRAPH={"S":["A","B","C"],"A":["D"],"B":["E"],"C":["F"],"D":["G"],"E":["G"],"F":["G"],"G":[]}
def greedy(H):
    q=[(H["S"],0,"S")]; parent={"S":None}; seen=set(); trace=[]; serial=0
    while q:
        _,_,u=heapq.heappop(q)
        if u in seen:continue
        seen.add(u);trace.append(u)
        if u=="G":break
        for v in GRAPH[u]:
            if v not in parent:parent[v]=u;serial+=1;heapq.heappush(q,(H[v],serial,v))
    path=None
    if "G" in seen:
        path=[];n="G"
        while n is not None:path.append(n);n=parent[n]
        path.reverse()
    return path,trace
H1={"S":7,"A":4,"B":5,"C":3,"D":2,"E":2,"F":1,"G":0}
# Misleading variant: makes the branch through A look especially attractive
H2={"S":7,"A":0,"B":1,"C":9,"D":0,"E":8,"F":10,"G":0}
for label,h in [("Original",H1),("Misleading heuristic",H2)]:
    p,t=greedy(h);print(label,"heuristic=",h,"trace=",t,"path=",p)
print("Greedy is guided only by h(n); changing h can make it explore a less useful branch first.")
