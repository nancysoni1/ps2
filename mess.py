import threading
import time

class Tablet:
    def __init__(self, tablet_id):
        self.tablet_id = tablet_id

    def record_meal(self):
        # Simulating the process of recording a meal
        meal_data = f"Meal recorded by Tablet {self.tablet_id} at {time.strftime('%H:%M:%S')}"
        return meal_data

class Server:
    def __init__(self):
        self.meal_records = []  # List to store meal records
        self.lock = threading.Lock()  # Lock for thread safety

    def add_meal_record(self, tablet_id):
        tablet = Tablet(tablet_id)
        meal_data = tablet.record_meal()

        with self.lock:
            self.meal_records.append(meal_data)

    def send_updates_to_tablet(self, tablet_id):
        # Simulating sending updates to the tablet
        tablet = Tablet(tablet_id)

        with self.lock:
            tablet_updates = self.meal_records[:]
        
        # Simulating the tablet receiving and processing updates
        print(f"Tablet {tablet_id} received updates: {tablet_updates}")

# Example usage
if __name__ == "__main__":
    server = Server()

    # Simulating tablets recording meals
    tablet_ids = [1, 2, 3]

    for tablet_id in tablet_ids:
        threading.Thread(target=server.add_meal_record, args=(tablet_id,)).start()

    # Simulating tablets requesting updates
    for tablet_id in tablet_ids:
        threading.Thread(target=server.send_updates_to_tablet, args=(tablet_id,)).start()
