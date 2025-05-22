class Drone:
    def __init__(self, id, max_weight, battery, speed, start_pos):
        self.id = id                       # (int)
        self.max_weight = max_weight       # max kg for shipping item for drone able to take it (float)
        self.battery = battery             # mAh (int)
        self.speed = speed                 # m\s (int)
        self.start_pos = start_pos         # (x,y) tuple
        self.battery_level = battery       # current battery level (int)
        self.charging_time = 0             # charging time (minute,int)
        self.current_pos = start_pos       # current position (at the beggining start_pos)

    def __repr__(self):
        return f"Drone(id={self.id}, max_weight={self.max_weight}, battery={self.battery}, speed={self.speed}, start_pos={self.start_pos})"
