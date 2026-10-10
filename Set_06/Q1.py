RULES=[({"Registered"},"Student"),({"Student"},"HasID"),({"Student","PaidFee"},"ExamEligible"),({"ExamEligible"},"CanEnterExamHall")]
def infer(initial):
    facts=set(initial); trace=[]; changed=True
    while changed:
        changed=False
        for pre,con in RULES:
            if pre<=facts and con not in facts:
                facts.add(con); trace.append(f"{' AND '.join(sorted(pre))} -> {con}"); changed=True
    return facts,trace
for initial in [{"Registered"},{"Registered","PaidFee"}]:
    facts,trace=infer(initial)
    print("\\nInitial:",sorted(initial)); print("Trace:",*trace,sep="\\n  ")
    print("Final facts:",sorted(facts))
print("\\nTruth table for P -> Q:")
for p in [False,True]:
    for q in [False,True]: print(f"P={p:<5} Q={q:<5} P->Q={((not p) or q)}")
print("Implication is false only when P is true and Q is false.")
