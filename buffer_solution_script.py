def introduction():
    """Tells the user what the script calculates, what it will need, and how to enter info"""
    print("This script calculates the grams of reagents needed for a buffer solution at a" \
    "specific pH and volume using the pKa of the conjugate acid-base pair.")
    print("Please input quantities in the specified units.")
    get_desired_pH()
    
def get_desired_pH() -> float:
    """Prompts the user to enter the desired pH of the buffer solution."""
    while True:
        try:
            desired_pH = float(input("Enter the desired pH of your buffer solution: "))
        except ValueError: #fail case sends user back to pH question
            print("Invalid input. Please enter a numeric value.")

def main():
    introduction()

main()