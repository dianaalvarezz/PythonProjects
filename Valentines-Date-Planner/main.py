from random import choice

def suggest_date_activity():
    while True:  # Ensures the function keeps running until a valid choice is made
        user_choice = input("Would you prefer a restaurant, an activity, or something else to start? ").strip().lower()
        
        if user_choice == "restaurant":
            restaurants = ['Applebees', 'La Salsa', 'Olive Garden', 'Texas Roadhouse']
            print("How about going to", choice(restaurants), "for dinner?")
            break  # Exit the loop after a valid choice
        elif user_choice == "activity":
            activities = ['a romantic walk', 'a picnic', 'minigolf', 'a movie']
            print("How about", choice(activities), "for some fun?")
            break  # Exit the loop after a valid choice
        elif user_choice == "something else":
            others = ['a spa day', 'a cooking class', 'visiting a museum', 'attending a concert']
            print("How about", choice(others), "?")
            break  # Exit the loop after a valid choice
        else:
            print("Sorry, that's not a valid choice. Let's start over.")

def suggest_single_activity():
    activities = ['a spa day just for you', 'a marathon of your favorite movies', 'visiting a museum', 'attending a workshop']
    print("Since it's all about self-love today, how about", choice(activities), "?")

def main():
    print("Happy Valentine's Day!")

    while True:  # Main loop
        response = input("\nAre you ready to plan your surprise day? (Yes/No): ")
        if response.strip().lower() == "yes":
            response = input("Do you have a date? (Yes/No): ")
            if response.strip().lower() == "yes":
                print("\nHow romantic! Let's generate the perfect date night!")
                suggest_date_activity()
            elif response.strip().lower() == "no":
                print("\nNo problem! There's no better day for some self-love!")
                suggest_single_activity()
            else:
                print("\nSorry, I didn't understand that. Please start over.")
        elif response.strip().lower() == "no":
            print("\nYou chose no, bummer.")
            break  # Exit the main loop if the user is not ready or wants to stop
        else:
            print("\nSorry, I didn't understand that. Please start over.")
        
        # Ask the user if they want to continue planning another surprise day
        another_round = input("\nWould you like to plan another day? (Yes/No): ").strip().lower()
        if another_round != "yes":
            print("Thank you for using the Valentine's Day Planner. Have a great day!")
            break  # Break the loop and exit the program

if __name__ == "__main__":
    main()
