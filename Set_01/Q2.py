from collections import deque
import heapq

GRAPH = {"A":["B","C"], "B":["D","E"], "C":["F"], "D":["G"], "E":["G"], "F":["G"], "G":[]}
H = {"A":6,"B":4,"C":3,"D":2,"E":2,"F":1,"G":0}

def reconstruct(parent, goal):
    if goal not in parent: return None
    path=[]; node=goal
    while node is not None:
        path.append(node); node=parent[node]
    return path[::-1]

def bfs(start, goal):
    q=deque([start]); parent={start:None}; expanded=[]
    while q:
        u=q.popleft(); expanded.append(u)
        if u==goal: return reconstruct(parent,goal), expanded
        for v in GRAPH[u]:
            if v not in parent: parent[v]=u; q.append(v)
    return None,expanded

def dfs(start, goal, graph=None):
    graph=graph or GRAPH
    stack=[start]; parent={start:None}; seen=set(); expanded=[]
    while stack:
        u=stack.pop()
        if u in seen: continue
        seen.add(u); expanded.append(u)
        if u==goal: return reconstruct(parent,goal),expanded
        # reverse push preserves listed left-to-right order for expansion
        for v in reversed(graph[u]):
            if v not in seen and v not in parent: parent[v]=u; stack.append(v)
    return None,expanded

def greedy(start,goal):
    pq=[(H[start],0,start)]; tie=0; parent={start:None}; seen=set(); expanded=[]
    while pq:
        _,_,u=heapq.heappop(pq)
        if u in seen: continue
        seen.add(u); expanded.append(u)
        if u==goal: return reconstruct(parent,goal),expanded
        for v in GRAPH[u]:
            if v not in seen and v not in parent:
                parent[v]=u; tie+=1; heapq.heappush(pq,(H[v],tie,v))
    return None,expanded

if __name__=="__main__":
    for name,fn in [("BFS",bfs),("DFS",dfs),("Greedy Best-First",greedy)]:
        path,expanded=fn("A","G")
        print(f"{name}: path={path}, expanded={expanded}, expanded_count={len(expanded)}")
