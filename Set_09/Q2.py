import heapq
G={"S":[("A",1),("B",5)],"A":[("C",2),("D",4)],"B":[("D",1)],"C":[("G",5)],"D":[("G",2)],"G":[]}
# True cheapest remaining costs: h(S)=5, h(A)=4, h(B)=3, h(C)=5, h(D)=2, h(G)=0.
H={"S":5,"A":4,"B":3,"C":5,"D":2,"G":0}
def astar(h):
    q=[(h["S"],0,"S")];best={"S":0};parent={"S":None};trace=[];details=[]
    while q:
        f,g,u=heapq.heappop(q)
        if g!=best.get(u):continue
        trace.append(u);details.append((u,g,h[u],f))
        if u=="G":
            p=[];n=u
            while n is not None:p.append(n);n=parent[n]
            return p[::-1],g,trace,details
        for v,c in G[u]:
            ng=g+c
            if ng<best.get(v,float("inf")):
                best[v]=ng;parent[v]=u;heapq.heappush(q,(ng+h[v],ng,v))
    return None,float("inf"),trace,details
for label,h in [("Admissible heuristic",H),("Overestimate h(A)=20",{**H,"A":20})]:
    p,c,t,d=astar(h);print(f"\\n{label}: {h}");print("Expansion=",t);print("(node,g,h,f)=",d);print("Path=",p,"cost=",c)
print("An admissible heuristic never exceeds the true least remaining cost. Overestimation can misorder nodes and remove A*'s general optimality guarantee.")
