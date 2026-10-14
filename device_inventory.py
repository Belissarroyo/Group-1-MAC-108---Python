"""
MAC 108 - IT Procurement Inventory Tracker

Scenario:
The IT Procurement and Deployment department manages a dynamic laptop stock.
Only pre-approved hardware models may be added to the inventory.

This program combines two data structures:
- Tuple (immutable): approved_models. It holds the fixed company policy and
  cannot be changed while the program runs, which protects data integrity.
- List (mutable): device_inventory. It starts empty and grows or shrinks as
  devices are added or removed.

It also uses three core techniques:
- while True: keeps the menu running until the user chooses Exit.
- .append() adds a device only after it passes validation against the tuple.
- if item in list: runs before .remove() so the program never raises a
  ValueError.
"""

# Requirement 1: Define pre-approved hardware models.
# Tuples are immutable (read-only), so the approved list cannot be
# accidentally overwritten or modified during execution.
approved_models = ("MacBook Pro", "Dell XPS", "ThinkPad")

# Requirement 2: Initialize an empty list for dynamic storage.
# This mutable list holds all deployed or stocked hardware.
device_inventory = []


def display_menu():
    """Print the interactive menu options."""
    print("\n--- INVENTORY MANAGEMENT ---")
    print("1: Add")
    print("2: Remove")
    print("3: View")
    print("4: Exit")


# Requirement 3: Persistent interactive menu loop.
# The infinite loop keeps the program running until an explicit exit.
while True:
    display_menu()
    choice = input("Enter choice (1-4): ")

    # Requirement 4: Option 1. Validate input before appending.
    if choice == "1":
        model = input("Enter device model: ")
        if model in approved_models:
            device_inventory.append(model)
            print(model + " added to inventory.")
        else:
            print("Error: Device model not approved for company use.")

    # Requirement 5: Option 2. Verify the item exists before removing it.
    elif choice == "2":
        # Prompt user for item to remove
        device = input("Enter device to remove: ")
        # Safe existence check before removal (prevents ValueError)
        if device in device_inventory:
            device_inventory.remove(device)
            print("Device removed.")
        else:
            # Graceful error handling
            print("Device not found.")

    # Requirement 4: Option 3. Display current device inventory.
    elif choice == "3":
        # Print active inventory list
        print("Current Active Stock:")
        print(device_inventory)

        # Show how many of each approved model are in stock
        print("Quantity by model:")
        for model in approved_models:
            print("  " + model + ": " + str(device_inventory.count(model)))
        print("Total devices: " + str(len(device_inventory)))

    # Option 4: Explicit exit signal ends the loop.
    elif choice == "4":
        print("Exiting Inventory Management. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
