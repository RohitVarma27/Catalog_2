from crop_management import CropManagement
from soil_management import SoilManagement
from pest_disease_management import PestDiseaseManagement
from task_scheduler import TaskScheduler

def main():
    crop_management = CropManagement()
    soil_management = SoilManagement()
    pest_disease_management = PestDiseaseManagement()
    task_scheduler = TaskScheduler()

    while True:
        print("\nCrop and Soil Management System")
        print("1. Crop Management")
        print("2. Soil Management")
        print("3. Pest and Disease Management")
        print("4. Task Scheduler")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            crop_management.manage_crops()
        elif choice == "2":
            soil_management.manage_soil()
        elif choice == "3":
            pest_disease_management.manage_pests_diseases()
        elif choice == "4":
            task_scheduler.schedule_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
