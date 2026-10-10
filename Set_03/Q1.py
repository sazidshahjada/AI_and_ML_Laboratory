from itertools import combinations
PARENT=[("Ali","Babu"),("Ali","Rina"),("Babu","Karim"),("Rina","Sumi"),("Karim","Nila")]
def children_of(x): return sorted({y for a,y in PARENT if a==x})
def grandparents():
    return sorted({(x,z) for x,y in PARENT for yy,z in PARENT if y==yy})
def siblings():
    out=set()
    for p1,c1 in PARENT:
        for p2,c2 in PARENT:
            if p1==p2 and c1!=c2: out.add(tuple(sorted((c1,c2))))
    return sorted(out)
people=sorted({x for pair in PARENT for x in pair})
print("Parent facts:",PARENT)
for p in people: print(f"children_of({p})={children_of(p)}")
print("Grandparent relations (x,z):",grandparents())
print("Sibling pairs:",siblings())
print("Tuple matching joins Parent(x,y) with Parent(y,z): the first relation's child y must equal the second relation's parent y.")
