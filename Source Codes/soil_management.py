import json
import os

class SoilManagement:
    def __init__(self):
        self.file_path = "data/soil.json"
        self.load_soil_data()

    def load_soil_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.soil_data = json.load(file)
        else:
            self.soil_data = []

    def save_soil_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.soil_data, file)

    def add_soil_data(self):
        soil_type = input("Enter soil type: ")
        pH_level = input("Enter pH level: ")
        nutrient_level = input("Enter nutrient level: ")

        soil = {
            "soil_type": soil_type,
            "pH_level": pH_level,
            "nutrient_level": nutrient_level
        }

        self.soil_data.append(soil)
        self.save_soil_data()
        print(f"Soil data for '{soil_type}' added successfully!")

    def view_soil_data(self):
        if not self.soil_data:
            print("No soil data available.")
        else:
            for soil in self.soil_data:
                print(f"Soil Type: {soil['soil_type']}, pH Level: {soil['pH_level']}, Nutrient Level: {soil['nutrient_level']}")

    def manage_soil(self):
        while True:
            print("\nSoil Management")
            print("1. Add Soil Data")
            print("2. View Soil Data")
            print("3. Back")

            choice = input("Select an option: ")

            if choice == "1":
                self.add_soil_data()
            elif choice == "2":
                self.view_soil_data()
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
