# Initialize choice variable
choice = ""

# Loop continues until user selects option 5
while choice != "5":
    # Display the menu
    print("\nSTUDENT RESULTS MANAGEMENT SYSTEM")
    print("1. Capture student information")
    print("2. Display student results")
    print("3. Save results to file")
    print("4. Read results from file")
    print("5. Exit")
    
    # Get user input
    choice = input("Enter your choice (1-5): ")
    
    # Branching statements to process the choice
    if choice == "1":
        print("Capturing student information...")
    elif choice == "2":
        print("Displaying student results...")
    elif choice == "3":
        print("Saving results to file...")
    elif choice == "4":
        print("Reading results from file...")
    elif choice == "5":
        print("Exiting the system. Goodbye!")
    else:
        # Error message for invalid choices
        print("Error: Invalid option. Please try again.")
