#₊˚ ✧ ━━━━⊱⋆⊰━━━━ ✧ ₊˚DEPENDENCIES₊˚ ✧ ━━━━⊱⋆⊰━━━━ ✧ ₊˚
#from time import time

#-----GLOBAL VARIABLES-----

desired_pH: float | None = None #global scope desired_pH updated by get_desired_pH()
desired_volume: float | None = None #global scope desired_volume updated by get_desired_volume()

#-----FUNCTIONS-----

def introduction():
    """Tells the user what the script calculates, what it will need, and how to enter info"""
    print("This script calculates the grams of reagents needed for a buffer solution at a " \
    "specific pH and volume using the pKa of the conjugate acid-base pair.")
    print("Please input quantities in the specified units.")
    
def get_desired_pH() -> float:
    """Prompts the user to enter the desired pH of the buffer solution."""
    while True:
        try:
            desired_pH = float(input("Enter the desired pH of your buffer solution: "))
        except ValueError: #fail case sends user back to pH question
            print("Please enter a numeric value!")
            continue
        if not 0 <= desired_pH <= 14: #pH cannot exceed 14 or be below 0, loop back to input
            print("Please enter a pH value between 0 and 14!")
            continue
        return desired_pH #return valid desired_pH to the manager function for storage in the global variable
    
def get_desired_volume() -> float:
    """Prompts the user to enter the desired volume of the buffer solution (in mL) and returns liters."""
    while True:
        try:
            volume_ml = float(input("Enter the desired volume of your buffer solution (in mL): ")) #user input
        except ValueError:
            print("Please enter a numeric value!")
            continue #fail case: user input is non-numeric
        if not 0 < volume_ml < float("inf"): #vol must be above 0
            print("Please enter a volume greater than 0!")
            continue #fail case: user input is not greater than 0
        volume_l = volume_ml / 1000  # convert mL to liters
        print(f"Your desired volume is {volume_l} liters")
        return volume_l #return valid volume in liters to the manager function for storage in the global variable

def main(): #manager function to avoid nested functios
    global desired_pH, desired_volume
    introduction()
    desired_pH = get_desired_pH()
    desired_volume = get_desired_volume()

if __name__ == "__main__": #entry point for the script
    main()
