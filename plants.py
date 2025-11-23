import datetime

plants = []

def add_plant(name, frequency):
    plant = {
        "name": name.strip(),
        "frequency": frequency,
        "last_watered": datetime.date.today()
    }
    plants.append(plant)
    print(f"✅ Added {name} (water every {frequency} days).")

def list_plants():
    if not plants:
        print("🌱 No plants added yet.")
    else:
        print("\n📋 Your Plants:")
        for plant in plants:
            print(f"- {plant['name']} (every {plant['frequency']} days, last watered {plant['last_watered']})")

def water_plant(index):
    if 0 <= index < len(plants):
        plants[index]["last_watered"] = datetime.date.today()
        print(f"💧 You watered {plants[index]['name']} today!")
    else:
        print("⚠️ Invalid plant index.")