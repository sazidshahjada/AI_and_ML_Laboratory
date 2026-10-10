from collections import deque
def search(graph,start,goal,mode):
    trace=[];parent={start:None}
    if mode=="BFS":
        q=deque([start]);seen={start}
        while q:
            u=q.popleft();trace.append(u)
            if u==goal:break
            for v in graph[u]:
                if v not in seen:seen.add(v);parent[v]=u;q.append(v)
    else:
        st=[start];seen=set()
        while st:
            u=st.pop()
            if u in seen:continue
            seen.add(u);trace.append(u)
            if u==goal:break
            for v in reversed(graph[u]):
                if v not in seen and v not in parent:parent[v]=u;st.append(v)
    path=None
    if goal in trace:
        path=[];n=goal
        while n is not None:path.append(n);n=parent[n]
        path.reverse()
    return path,trace
G={"A":["B","C"],"B":["D","E"],"C":["F"],"D":["H"],"E":["G"],"F":["G"],"G":[],"H":["G"]}
for label,graph in [("Original",G),("Reordered",{"A":["C","B"],"B":["E","D"],"C":["F"],"D":["H"],"E":["G"],"F":["G"],"G":[],"H":["G"]})]:
    print("\\n",label)
    for mode in ["BFS","DFS"]:
        p,t=search(graph,"A","G",mode);print(mode,"path=",p,"trace=",t,"expanded=",len(t))
print("BFS returns a shallowest path in this unweighted graph. DFS is usually more visibly affected by adjacency order because its branch order changes.")
