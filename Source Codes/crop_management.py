import json
import os

class CropManagement:
    def __init__(self):
        self.file_path = "data/crops.json"
        self.load_crops()

    def load_crops(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.crops = json.load(file)
        else:
            self.crops = []

    def save_crops(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.crops, file)

    def add_crop(self):
        crop_name = input("Enter crop name: ")
        season = input("Enter suitable season: ")
        soil_type = input("Enter suitable soil type: ")

        crop = {
            "name": crop_name,
            "season": season,
            "soil_type": soil_type
        }

        self.crops.append(crop)
        self.save_crops()
        print(f"Crop '{crop_name}' added successfully!")

    def view_crops(self):
        if not self.crops:
            print("No crops added yet.")
        else:
            for crop in self.crops:
                print(f"Crop: {crop['name']}, Season: {crop['season']}, Soil Type: {crop['soil_type']}")

    def manage_crops(self):
        while True:
            print("\nCrop Management")
            print("1. Add Crop")
            print("2. View Crops")
            print("3. Back")

            choice = input("Select an option: ")

            if choice == "1":
                self.add_crop()
            elif choice == "2":
                self.view_crops()
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
