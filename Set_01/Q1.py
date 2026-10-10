from itertools import count

class VacuumAgent:
    def __init__(self, rooms, location):
        self.rooms = dict(rooms)
        self.location = location

    def step(self):
        percept = (self.location, self.rooms[self.location], tuple(self.rooms.items()))
        if all(state == "Clean" for state in self.rooms.values()):
            action = "NoOp"
        elif self.rooms[self.location] == "Dirty":
            action = "Suck"
            self.rooms[self.location] = "Clean"
        else:
            names = list(self.rooms)
            idx = names.index(self.location)
            action = "Right" if idx < len(names)-1 else "Left"
            self.location = names[idx+1] if action == "Right" else names[idx-1]
        print(f"percept={percept} -> action={action}; state={self.rooms}; location={self.location}")
        return action

if __name__ == "__main__":
    # Initial condition from Set 1: A dirty, B clean, agent starts in B.
    agent = VacuumAgent({"A":"Dirty", "B":"Clean"}, "B")
    for _ in range(10):
        if agent.step() == "NoOp":
            break
    print("\\nPEAS — University document-delivery robot")
    print("P: correct/fast delivery, low collisions, low energy, secure documents")
    print("E: offices, corridors, lifts, people, doors, obstacles, delivery points")
    print("A: wheels, motors, gripper/tray, display/speaker, door/lift interface")
    print("S: camera, lidar/depth, wheel odometry, IMU, RFID/QR, buttons")
