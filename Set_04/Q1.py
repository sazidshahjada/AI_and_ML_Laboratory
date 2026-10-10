from collections import deque
def run(graph,start,goal,mode="bfs"):
    trace=[]; parent={start:None}
    if mode=="bfs":
        frontier=deque([start]); seen={start}
        pop=lambda:frontier.popleft()
        while frontier:
            u=pop(); trace.append(u)
            if u==goal: break
            for v in graph[u]:
                if v not in seen: seen.add(v); parent[v]=u; frontier.append(v)
    else:
        frontier=[start]; seen=set()
        while frontier:
            u=frontier.pop()
            if u in seen: continue
            seen.add(u); trace.append(u)
            if u==goal: break
            for v in reversed(graph[u]):
                if v not in seen and v not in parent: parent[v]=u; frontier.append(v)
    path=None
    if goal in trace:
        path=[]; n=goal
        while n is not None: path.append(n); n=parent[n]
        path.reverse()
    return path,trace
def bidirectional(graph,start,goal):
    reverse={u:[] for u in graph}
    for u,vs in graph.items():
        for v in vs: reverse[v].append(u)
    qf=deque([start]); qb=deque([goal]); pf={start:None}; pb={goal:None}; ef=[]; eb=[]; meet=None
    while qf and qb and meet is None:
        for q,par,g,trace in [(qf,pf,graph,ef),(qb,pb,reverse,eb)]:
            for _ in range(len(q)):
                u=q.popleft(); trace.append(u)
                if u in (pb if trace is ef else pf): meet=u; break
                for v in g[u]:
                    if v not in par: par[v]=u; q.append(v)
            if meet is not None: break
    if meet is None: return None,ef,eb
    left=[]; n=meet
    while n is not None: left.append(n); n=pf.get(n)
    left.reverse(); right=[]; n=pb.get(meet)
    while n is not None: right.append(n); n=pb.get(n)
    return left+right,ef,eb
if __name__=="__main__":
    graph={"P":["Q","R"],"Q":["S","T"],"R":["U"],"S":["V"],"T":["V"],"U":["V"],"V":[]}
    for mode in ["bfs","dfs"]:
        path,trace=run(graph,"P","V",mode)
        print(mode.upper(), "path=",path,"trace=",trace,"expanded=",len(trace))
    path,ef,eb=bidirectional(graph,"P","V")
    print("Bidirectional path=",path,"forward trace=",ef,"backward trace=",eb,"expanded total=",len(ef)+len(eb))
    changed={**graph,"Q":["T","S"]}
    for mode in ["bfs","dfs"]:
        print("Reversed Q children",mode.upper(),run(changed,"P","V",mode))
