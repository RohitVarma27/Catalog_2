import json
import os

class PestDiseaseManagement:
    def __init__(self):
        self.file_path = "data/pests_diseases.json"
        self.load_pests_diseases()

    def load_pests_diseases(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.pests_diseases = json.load(file)
        else:
            self.pests_diseases = []

    def save_pests_diseases(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.pests_diseases, file)

    def add_pest_disease(self):
        name = input("Enter pest or disease name: ")
        crop_affected = input("Enter crop affected: ")
        remedy = input("Enter remedy: ")

        pest_disease = {
            "name": name,
            "crop_affected": crop_affected,
            "remedy": remedy
        }

        self.pests_diseases.append(pest_disease)
        self.save_pests_diseases()
        print(f"Pest/Disease '{name}' added successfully!")

    def view_pests_diseases(self):
        if not self.pests_diseases:
            print("No pests or diseases recorded.")
        else:
            for pd in self.pests_diseases:
                print(f"Name: {pd['name']}, Crop Affected: {pd['crop_affected']}, Remedy: {pd['remedy']}")

    def manage_pests_diseases(self):
        while True:
            print("\nPest and Disease Management")
            print("1. Add Pest/Disease")
            print("2. View Pests/Diseases")
            print("3. Back")

            choice = input("Select an option: ")

            if choice == "1":
                self.add_pest_disease()
            elif choice == "2":
                self.view_pests_diseases()
            elif choice == "3":
                break
            else:
                print("Invalid choice, please try again.")
