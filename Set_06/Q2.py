from collections import deque
GRAPH={"S":["A","B"],"A":["C","D"],"B":["E","F"],"C":["G"],"D":["H"],"E":["I"],"F":["J"],"G":[],"H":[],"I":[],"J":[]}
def bfs(s,g):
    q=deque([s]); parent={s:None}; trace=[]
    while q:
        u=q.popleft(); trace.append(u)
        if u==g: break
        for v in GRAPH[u]:
            if v not in parent: parent[v]=u; q.append(v)
    return path(parent,g),trace
def dfs(s,g):
    st=[s]; parent={s:None}; seen=set(); trace=[]
    while st:
        u=st.pop()
        if u in seen: continue
        seen.add(u); trace.append(u)
        if u==g: break
        for v in reversed(GRAPH[u]):
            if v not in seen and v not in parent: parent[v]=u; st.append(v)
    return path(parent,g) if g in trace else None,trace
def path(parent,g):
    if g not in parent:return None
    out=[]; n=g
    while n is not None:out.append(n);n=parent[n]
    return out[::-1]
def dls(s,g,limit):
    trace=[]; parent={s:None}; found=None
    def rec(u,d):
        nonlocal found
        trace.append(u)
        if u==g: found=path(parent,g); return True
        if d==limit:return False
        for v in GRAPH[u]:
            parent[v]=u
            if rec(v,d+1):return True
            parent.pop(v,None)
        return False
    rec(s,0);return found,trace
if __name__=="__main__":
    for name,fn in [("BFS",bfs),("DFS",dfs)]:
        p,t=fn("S","G");print(name,"path=",p,"expanded=",t)
    for lim in range(5):
        p,t=dls("S","G",lim);print(f"IDDFS limit={lim}: path={p}, trace={t}")
        if p:break
    print("BFS uses more frontier memory; DFS uses stack memory; IDDFS repeats shallow visits but retains low memory.")
