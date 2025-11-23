def get_int_input(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return None
