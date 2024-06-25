#write functions here, don't add input('') statements here!

#part 4.1

def get_day_of_week(day):
    if(int(day) == 1):
        dotw = "Monday"
    elif(int(day) == 2):
        dotw = "Tuesday"
    elif(int(day) == 3):
        dotw = "Wednesday"
    elif(int(day) == 4):
        dotw = "Thursday"
    elif(int(day) == 5):
        dotw = "Friday"
    elif(int(day) == 6):
        dotw = "Saturday"
    elif(int(day) == 7):
        dotw = "Sunday"
    else:
        dotw = "\nInvalid Number\n"
    
    print("\nThat is an",dotw,"")
    menu()


def exit_option():
    exit_choice = 0
    exit_choice = input("Do you want to exit the game? (yes/no):")
    if(exit_choice == "yes"):
        print("\nYou have left the game.\n")
    elif(exit_choice == "no"):
        menu()
    else:
        print("\nPlease type either yes or no\n")
        exit_option()

def menu():
    print("\nDays of the Week Game\n-----------------------------------------------------")
    print("Choose an option:\n")
    print("1- Days of the Week Game")
    print("2- Exit")
        
    user_option = input("Please select an option:\n")
        
    if(user_option == "1"):
        day = input("Pick a number and I'll tell you what day of the week it is:\n")
        get_day_of_week(day)

    elif user_option == "2":
        exit_option()

    else:
        print("\nPlease select a valid number input.")
        menu()
    