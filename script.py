import time
from datetime import datetime

# Define feeding schedule (24-hour format)
FEEDING_TIMES = {
    "morning": "08:00",
    "afternoon": "14:00",
    "evening": "19:00"
}

# Function to check if it's feeding time
def is_feeding_time():
    current_time = datetime.now().strftime("%H:%M")
    for meal, feed_time in FEEDING_TIMES.items():
        if current_time == feed_time:
            return meal
    return None

# Function to dispense food
def dispense_food(meal):
    print(f"Dispensing food for {meal} meal... 🐶🍖")

# Main loop to check feeding time
def dog_feeding_scheduler():
    print("Dog feeding scheduler running... Press Ctrl+C to stop.")
    while True:
        meal_time = is_feeding_time()
        if meal_time:
            dispense_food(meal_time)
            time.sleep(60)  # Wait for a minute to prevent multiple feedings at the same time
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    dog_feeding_scheduler()
