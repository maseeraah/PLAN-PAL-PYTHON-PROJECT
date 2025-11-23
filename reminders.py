import datetime
from plants import plants

def check_reminders():
    today = datetime.date.today()
    print("\n🌿 Plant Watering Reminders:")
    if not plants:
        print("No plants added yet.")
        return
    for plant in plants:
        days_since = (today - plant["last_watered"]).days
        if days_since >= plant["frequency"]:
            print(f"👉 Water {plant['name']} today! (Last watered {days_since} days ago)")
        else:
            print(f"✅ {plant['name']} is fine (next in {plant['frequency'] - days_since} days).")
