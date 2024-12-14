import csv
import pandas as pd
import numpy as np
class Garment:
    def __init__(self, Waist_Circumference, Limb_Circumference):
        self.Waist_Circumference = Waist_Circumference
        self.Limb_Circumference = Limb_Circumference

class Upper_Garment(Garment):
    def __init__(self, Bust_Length, Waist_Circumference, Limb_Circumference, Arm_Length, Chest_Width, Neck_Circumference, Shoulder_Width):
        super().__init__(Waist_Circumference, Limb_Circumference)
        self.Arm_Length = Arm_Length
        self.Bust_Length = Bust_Length
        self.Chest_Width = Chest_Width
        self.Neck_Circumference = Neck_Circumference
        self.Shoulder_Width = Shoulder_Width

class Pants(Garment):
    def __init__ (self, Waist_Circumference, Limb_Circumference, Leg_Length, Inseam, Calf_Circumference):
        super().__init__(Waist_Circumference, Limb_Circumference)
        self.Leg_Length = Leg_Length
        self.Inseam = Inseam
        self.Calf_Circumference = Calf_Circumference

# MULTILEVEL INHERITANCE

class Tshirt(Upper_Garment):
    def __init__ (self, Bust_Length, Waist_Circumference, Limb_Circumference,  Arm_Length, Chest_Width, Neck_Circumference, Shoulder_Width):
        super().__init__(Bust_Length, Waist_Circumference, Limb_Circumference,  Arm_Length, Chest_Width, Neck_Circumference, Shoulder_Width)

class Hoodie(Upper_Garment):
    def __init__(self, Bust_Length, Waist_Circumference, Limb_Circumference, Arm_Length, Chest_Width, Neck_Circumference, Shoulder_Width, Wrist_Circumference):
        super().__init__(Bust_Length, Waist_Circumference, Limb_Circumference, Arm_Length, Chest_Width, Neck_Circumference, Shoulder_Width)
        self.Wrist_Circumference = Wrist_Circumference

#  USER'S CLASS
class Customer:
    def __init__(self, Bust_Length = 0, Leg_Length = 0, Waist_Circumference = 0, Arm_Length = 0, Limb_Circumference = 0, Chest_Width = 0, Neck_Circumference = 0, Shoulder_Width = 0, Calf_Circumference = 0, Wrist_Circumference = 0) :
        self.Bust_Length = Bust_Length
        self.Leg_Length = Leg_Length
        self.Waist_Circumference = Waist_Circumference
        self.Arm_Length = Arm_Length
        self.Limb_Circumference = Limb_Circumference
        self.Chest_Width = Chest_Width
        self.Neck_Circumference = Neck_Circumference
        self.Shoulder_Width = Shoulder_Width
        self.Calf_Circumference = Calf_Circumference
        self.Wrist_Circumference = Wrist_Circumference

# OPENING THE FILE CSV WITH EXCEPTION HANDLING
try:
    file_path = "/Users/manfri/PycharmProjects/pythonProject4/Set_data_garment.csv"
    data = pd.read_csv(file_path, delimiter=';')
    data.columns = data.columns.str.strip()
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
    exit()
except pd.errors.ParserError:
    print("Error: There was a problem with parsing the CSV file.")
    exit()

# DIVIDING THE DATASET BASED ON CATEGORIES
try:
    hoodie_df = data[data["Category"] == "Hoodie"].dropna(how="all", axis=0)
    hoodie_df.to_csv("hoodie_table.csv", index=False)
    tshirt_df = data[data["Category"] == "Tshirt"].dropna(how="all", axis=0)
    tshirt_df.to_csv("tshirt_table.csv", index=False)
    pants_df = data[data["Category"] == "Pants"].dropna(how="all", axis=0)
    pants_df.to_csv("pants_table.csv", index=False)
except KeyError:
    print("Error: Missing 'Category' column in the data.")
    exit()

# PRINTING THE NEW TABLES
print("these are the sorted tables")
print("Hoodie Table:")
print(hoodie_df.head())
print("\nTshirt Table:")
print(tshirt_df.head())
print("\nPants Table:")
print(pants_df.head())
fits = []
class GarmentFitCalculator:
    @staticmethod
    def calculate_fit(user, garment_dict):
        user_attributes = vars(user)
        fits = {}
        for item_key, measures in garment_dict.items():
            total_difference = 0
            num_measures = 0
            for measure, garment_value in measures.items():
                try:
                    garment_value = float(garment_value)
                except ValueError:
                    continue

                user_value = user_attributes.get(measure)
                if user_value is None:
                    continue

                difference = abs(garment_value - user_value)
                percentage = (difference / garment_value) * 100
                total_difference += percentage
                num_measures += 1

            if num_measures > 0:
                mean_difference = total_difference / num_measures
                total_fit = 100 - mean_difference
                fits[item_key] = total_fit

        return fits


class UserInteraction:
    @staticmethod
    def get_valid_number(prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def start(hoodie_df, tshirt_df, pants_df):
        print("Hello, please enter your ID: ")
        user_id = input(" ")
        print(f"Welcome, user {user_id}!")

        # ASKING THE GARMENT CATEGORY
        while True:
            print("What type of garment are you looking for? (Options: Hoodie, Tshirt, Pants)")
            garment_type = input("Choose one: ").capitalize()
            if garment_type in ["Hoodie", "Tshirt", "Pants"]:
                print(f"You selected: {garment_type}")
                break
            else:
                print("Invalid garment type. Please try again.")

        # TAKING CUSTOMER MEASUREMENTS
        print(f"Please provide your {garment_type} measurements:")
        if garment_type == "Hoodie":
            user = Customer(
                Bust_Length=UserInteraction.get_valid_number("Bust Length: "),
                Waist_Circumference=UserInteraction.get_valid_number("Waist Circumference: "),
                Arm_Length=UserInteraction.get_valid_number("Arm Length: "),
                Limb_Circumference=UserInteraction.get_valid_number("Limb Circumference: "),
                Chest_Width=UserInteraction.get_valid_number("Chest Width: "),
                Neck_Circumference=UserInteraction.get_valid_number("Neck Circumference: "),
                Shoulder_Width=UserInteraction.get_valid_number("Shoulder Width: "),
                Wrist_Circumference=UserInteraction.get_valid_number("Wrist Circumference: ")
            )
        elif garment_type == "Tshirt":
            user = Customer(
                Bust_Length=UserInteraction.get_valid_number("Bust Length: "),
                Waist_Circumference=UserInteraction.get_valid_number("Waist Circumference: "),
                Limb_Circumference=UserInteraction.get_valid_number("Arm Circumference: "),
                Chest_Width=UserInteraction.get_valid_number("Chest Width: "),
                Neck_Circumference=UserInteraction.get_valid_number("Neck Circumference: "),
                Shoulder_Width=UserInteraction.get_valid_number("Shoulder Width: ")
            )
        elif garment_type == "Pants":
            user = Customer(
                Leg_Length=UserInteraction.get_valid_number("Leg Length: "),
                Waist_Circumference=UserInteraction.get_valid_number("Waist Circumference: "),
                Limb_Circumference=UserInteraction.get_valid_number("Leg Circumference: "),
                Calf_Circumference=UserInteraction.get_valid_number("Calf Circumference: ")
            )

        # Filtering the appropriate DataFrame
        if garment_type == "Hoodie":
            garment_df = hoodie_df
        elif garment_type == "Tshirt":
            garment_df = tshirt_df
        elif garment_type == "Pants":
            garment_df = pants_df
        else:
            print("Invalid garment type.")
            exit()

        garment_df = data[data["Category"] == garment_type].dropna(how="all", axis=0)
        garment_dict = {}
        for _, row in garment_df.iterrows():
            product_code = row['Product_Code']
            garment_dict[product_code] = {}

            for col in garment_df.columns:
                if col not in ["Product_Code", "Category"]:
                    try:
                        value = int(float(row[col]))
                    except (ValueError, TypeError):
                        value = None

                    if value is not None:
                        garment_dict[product_code][col] = value

        garment_fit = GarmentFitCalculator.calculate_fit(user, garment_dict)

        for product_code, fit_score in garment_fit.items():
            fits.append((product_code, fit_score))

        # SORTING THE FIT DICTIONARY
        keys = list(garment_fit.keys())

        def quicksort(fits, first_index, last_index):
            if first_index < last_index:
                partition_index = partition(fits, first_index, last_index)
                quicksort(fits, first_index, partition_index - 1)
                quicksort(fits, partition_index + 1, last_index)

        def partition(fits, first_index, last_index):
            pivot = fits[first_index][1]
            left_pointer = first_index + 1
            right_pointer = last_index
            while True:
                while fits[left_pointer][1] > pivot and left_pointer < last_index:
                    left_pointer += 1
                while fits[right_pointer][1] < pivot and right_pointer >= first_index:
                    right_pointer -= 1
                if left_pointer >= right_pointer:
                    break
                fits[left_pointer], fits[right_pointer] = fits[right_pointer], fits[left_pointer]
            fits[first_index], fits[right_pointer] = fits[right_pointer], fits[first_index]
            return right_pointer

        quicksort(fits, 0, len(fits) - 1)

        # PRINTING THE RESULTS
        if garment_type == "Hoodie":
            print(f"\nHere the best results in terms of fit for the available Hoodies:")
        elif garment_type == "Pants":
            print(f"\nHere the best results in terms of fit for the available Pants:")
        elif garment_type == "Tshirt":
            print(f"\nThese are the best results in terms of fit for the available Tshirt:")
        for keys, measures in fits:
            if isinstance(measures, (int, float)) and measures > 60:
                print(f"The {garment_type} {keys} has a fit of {round(measures, 2)}%")



# THE USE
file_path = "/Users/manfri/PycharmProjects/pythonProject4/Set_data_garment.csv"
data = pd.read_csv(file_path, delimiter=";")
data.columns = data.columns.str.strip()

hoodie_df = data[data["Category"] == "Hoodie"].dropna(how="all", axis=0)
tshirt_df = data[data["Category"] == "Tshirt"].dropna(how="all", axis=0)
pants_df = data[data["Category"] == "Pants"].dropna(how="all", axis=0)

UserInteraction.start(hoodie_df, tshirt_df, pants_df)