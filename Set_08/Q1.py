GRAPH={"A":["B","C"],"B":["D","E"],"C":["F"],"D":["H"],"E":["I"],"F":["G"],"G":[],"H":[],"I":[]}
def dls(limit):
    trace=[]; path=["A"]
    def rec(u,d):
        trace.append((u,d))
        if u=="G":return "FOUND"
        if d==limit:return "CUTOFF"
        cutoff=False
        for v in GRAPH[u]:
            path.append(v);r=rec(v,d+1)
            if r=="FOUND":return r
            path.pop()
            cutoff|=(r=="CUTOFF")
        return "CUTOFF" if cutoff else "FAILURE"
    r=rec("A",0)
    return (path.copy() if r=="FOUND" else None),trace,r
for lim in [2,3]:
    p,t,r=dls(lim);print(f"DLS limit={lim}: path={p}, trace={t}, result={r}")
root_visits=0
for lim in range(5):
    p,t,r=dls(lim);root_visits+=sum(1 for n,d in t if n=="A" and d==0)
    print(f"IDDFS iteration limit={lim}: trace={t}, result={r}")
    if r=="FOUND":break
print("Root A visited",root_visits,"times across IDDFS iterations.")
print("Repeated shallow work is the price paid for low memory and finding a shallow solution.")
