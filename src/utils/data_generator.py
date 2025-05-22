import random
import os
from src.models.drone import Drone

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "data")

def generate_drones(num=5):
    drones = []
    for i in range(num):
        drone = Drone(
            id=i,
            max_weight=round(random.uniform(2.0, 10.0), 2),
            battery=random.randint(2000, 5000),
            speed=round(random.uniform(5.0, 20.0), 1),
            start_pos=(random.randint(0, 100), random.randint(0, 100))
        )
        drones.append(drone)
    return drones

def generate_deliveries(num=20):
    deliveries = []
    for i in range(num):
        delivery = {
            "id": i,
            "pos": (random.randint(0, 100), random.randint(0, 100)),
            "weight": round(random.uniform(0.5, 5.0), 2),
            "priority": random.randint(1, 5),
            "time_window": ("{:02d}:00".format(random.randint(9, 15)),
                            "{:02d}:00".format(random.randint(16, 20)))
        }
        deliveries.append(delivery)
    return deliveries

def generate_noflyzones(num=2):
    zones = []
    for i in range(num):
        x, y = random.randint(10, 80), random.randint(10, 80)
        width, height = random.randint(5, 15), random.randint(5, 15)
        zone = {
            "id": i,
            "coordinates": [(x, y), (x + width, y), (x + width, y + height), (x, y + height)],
            "active_time": ("{:02d}:{:02d}".format(random.randint(9, 12), 0),
                            "{:02d}:{:02d}".format(random.randint(13, 16), 0))
        }
        zones.append(zone)
    return zones

def save_to_txt(data, filename):
    filepath = os.path.join(DATA_PATH, filename)
    with open(filepath, "w") as f:
        for item in data:
            f.write(str(item) + "\n")

def generate_and_save_all(drones_n=5, deliveries_n=20, zones_n=2):
    os.makedirs(DATA_PATH, exist_ok=True)
    save_to_txt(generate_drones(drones_n), "drones.txt")
    save_to_txt(generate_deliveries(deliveries_n), "deliveries.txt")
    save_to_txt(generate_noflyzones(zones_n), "noflyzones.txt")

# Test çalıştırma
if __name__ == "__main__":
    generate_and_save_all()
