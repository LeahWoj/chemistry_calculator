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
    
def validate_pH(raw_pH: str) -> float:  
    try:
        pH_value = float(raw_pH)
    except ValueError:
        raise ValueError("Please enter a numeric value!")
    if not 0 <= pH_value <= 14:
        raise ValueError("Please enter a pH between 0 and 14!")
    return pH_value
     
def validate_pKa(raw_pKa: str) -> float:  
    """Validates the pKa value entered by the user."""
    try:
        pKa_value = float(raw_pKa)
    except ValueError:
        raise ValueError("Please enter a numeric value!")
    if pKa_value < 0:
        raise ValueError(f"A negative pKa for a conjugate acid-base pair " 
            "requires a non-aqueous solvent. The Henderson-Hasselbalch equation " 
            "is altered in this case, and out of the scope of this calculator."
            )
    return pKa_value
        
def pKa_warning(value: float) -> str | None:
    """Issues a warning if the pKa value is outside the common range for buffers."""
    if value > 14:
        return("Although pKas above 14 are possible, they are less common in buffers. Please proceed with caution.")
    return None

def validate_number(raw_number: str, name: str = "Value") -> float:
    """Convert text to a finite number greater than 0, or raise ValueError."""
    try:
        number = float(raw_number)
    except ValueError:
        raise ValueError(f"{name} must be a number!")
    if not 0 < number < float("inf"):
        raise ValueError(f"{name} must be greater than 0!")
    return number

def get_desired_pH() -> float:
    """Prompts the user to enter the desired pH of the buffer solution."""
    while True:
        raw_pH = input("Enter the desired pH of your buffer solution: ")
        try:
            return validate_pH(raw_pH)
        except ValueError as e:
            print(e)
    
def get_desired_pKa() -> float:
    """Prompts the user to enter the pKa of the conjugate acid-base pair."""
    while True:
        raw_pKa = input("Enter the pKa of the conjugate acid-base pair: ")
        try:
            pKa_value = validate_pKa(raw_pKa)
        except ValueError as e:
            print(e)
            continue
        warning = pKa_warning(pKa_value)
        if warning:
            print(warning)
        return pKa_value
    
def get_desired_volume() -> float:
    """Prompts for the desired volume in mL and returns it in liters."""
    while True:
        raw_volume = input("Enter the desired volume of your buffer solution (in mL): ")
        try:
            volume_ml = validate_number(raw_volume, "Volume")
        except ValueError as e:
            print(e)
            continue
        volume_l = volume_ml / 1000
        print(f"Your desired volume is {volume_l} liters")
        return volume_l
    
def get_desired_molarity() -> float:
    """Prompts for the desired molarity in M"""
    while True:
        raw_molarity = input("Enter the desired molarity of your buffer solution (in M): ")
        try:
            molarity = validate_number(raw_molarity, "Molarity")
        except ValueError as e:
            print(e)
            continue
        print(f"Your desired molarity is {molarity} ")
        return molarity

def main(): #manager function to avoid nested functios
    global desired_pH, desired_volume
    introduction()
    desired_pH = get_desired_pH()
    desired_pKa = get_desired_pKa()
    desired_volume = get_desired_volume()
    molarity = get_desired_molarity()

if __name__ == "__main__": #entry point for the script
    main()

