# Group-1-MAC-108---Python


name = input("Enter your hacker alias: ")
print(f"\nWelcome, {name}. You're locked in a secure server room.")
print("Alarms start in 60 seconds. Find a way out.\n")

choice = input("Do you (1) hack the terminal, (2) check the vent, or (3) inspect the door? ")

if choice == "1":
    print("Triggered the alarm! You have 60 seconds until the police")
elif choice == "2":
    print("")
elif choice == "3":
    print("")
else:
    print("Invalid choice, must pick 1, 2, or 3 to proceed.")

    
