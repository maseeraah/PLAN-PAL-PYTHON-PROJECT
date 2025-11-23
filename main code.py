from plants import add_plant, list_plants, water_plant, plants
from reminders import check_reminders
from utils import get_int_input

def show_menu():
    while True:
        print("\n--- BloomBuddy Plant Watering Reminder ---")
        print("1. Add Plant")
        print("2. Water Plant")
        print("3. Check Reminders")
        print("4. List Plants")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter plant name: ").strip()
            frequency = get_int_input("Enter watering frequency (days): ")
            if frequency is not None:
                add_plant(name, frequency)
        elif choice == "2":
            list_plants()
            index = get_int_input("Enter the number of the plant to water (starting from 0): ")
            if index is not None:
                water_plant(index)
        elif choice == "3":
            check_reminders()
        elif choice == "4":
            list_plants()
        elif choice == "5":
            print("👋 Goodbye! Keep your plants healthy!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()
