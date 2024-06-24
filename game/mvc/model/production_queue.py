class ProductionQueue:
    def __init__(self):
        self.queue = []

    def add_to_queue(self, unit):
        self.queue.append({
            'unit': unit,
            'time_remaining': unit.production_time
        })
        print(f"Added {unit.name} to the queue.")

    def advance_turn(self):
        if not self.queue:
            print("Queue is empty.")
            return

        # Advance production for the unit at the front of the queue
        self.queue[0]['time_remaining'] -= 1

        # Check if the unit is completed
        if self.queue[0]['time_remaining'] <= 0:
            completed_unit = self.queue.pop(0)
            print(f"{completed_unit['unit'].name} has been produced.")

    def queue_status(self):
        if not self.queue:
            return "Queue: Empty"

        status = "Queue:\n"
        for idx, item in enumerate(self.queue):
            status += f"{idx + 1}. {item['unit'].name} (Turns remaining: {item['time_remaining']})\n"
        return status.strip()

