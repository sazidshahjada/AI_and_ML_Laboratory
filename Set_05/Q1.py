import random
class ThreeRoomAgent:
    def __init__(self, states, location="A"):
        self.states=dict(states); self.location=location
    def run(self,max_steps=20):
        names=list(self.states)
        for _ in range(max_steps):
            sensed_location = self.location
            percept=self.states[sensed_location]
            if all(v=="Clean" for v in self.states.values()): action="NoOp"
            elif percept=="Dirty": action="Suck"; self.states[self.location]="Clean"
            else:
                idx=names.index(self.location)
                # Move to the next dirty room if possible; otherwise cycle.
                dirty=[n for n in names if self.states[n]=="Dirty"]
                target=min(dirty,key=lambda n:abs(names.index(n)-idx)) if dirty else self.location
                if target==self.location: action="NoOp"
                else:
                    nxt=idx+(1 if names.index(target)>idx else -1)
                    action="Right" if nxt>idx else "Left"; self.location=names[nxt]
            print(f"location={sensed_location}, percept={percept}, action={action}, environment_after_action={self.states}, next_location={self.location}")
            if action=="NoOp": break
if __name__=="__main__":
    ThreeRoomAgent({"A":"Dirty","B":"Dirty","C":"Clean"}).run()
    print("\\nPEAS: P=all rooms clean, few actions/time/energy; E=rooms A/B/C and connecting passages; A=suck/move; S=location and dirt sensor.")
