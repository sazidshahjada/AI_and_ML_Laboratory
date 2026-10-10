RULES=[({"TemperatureHigh"},"Hot"),({"Hot","Humid"},"Uncomfortable"),({"Uncomfortable"},"FanOn"),({"Rain"},"Humid")]
def forward(initial):
    facts=set(initial);given=set(initial);trace=[];changed=True
    while changed:
        changed=False
        for pre,con in RULES:
            if pre<=facts and con not in facts:
                facts.add(con);trace.append(f"{' AND '.join(sorted(pre))} -> {con}");changed=True
    return given,facts,trace
for initial in [{"TemperatureHigh"},{"TemperatureHigh","Humid"},{"TemperatureHigh","Rain"}]:
    given,facts,trace=forward(initial)
    print("\\nGiven facts:",sorted(given));print("Inference trace:",*trace,sep="\\n  ")
    print("Inferred facts:",sorted(facts-given));print("Final knowledge:",sorted(facts))
