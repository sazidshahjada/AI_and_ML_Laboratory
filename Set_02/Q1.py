from collections import deque
RULES = [
    ({"Cloudy"}, "Rain"),
    ({"Rain"}, "WetGround"),
    ({"WetGround"}, "Slippery"),
    ({"Slippery"}, "DriveSlowly"),
    ({"Rain","Cold"}, "WearJacket"),
]
def forward_chain(initial):
    facts=set(initial); trace=[]; changed=True
    while changed:
        changed=False
        for premises,conclusion in RULES:
            if premises <= facts and conclusion not in facts:
                facts.add(conclusion); trace.append(f"{' AND '.join(sorted(premises))} -> {conclusion}")
                changed=True
    return facts,trace
for initial in [{"Cloudy"},{"Cloudy","Cold"}]:
    facts,trace=forward_chain(initial)
    print("\\nInitial facts:",sorted(initial))
    print("Rule firing sequence:")
    for t in trace: print("  ",t)
    print("Final inferred knowledge:",sorted(facts))
    print("WearJacket fires:", "WearJacket" in facts, "(requires both Rain and Cold)")
