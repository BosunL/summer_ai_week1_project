# Various import statements can go here
from social_network_classes import SocialNetwork, Person
import social_network_ui

ai_social_network = SocialNetwork()
current_person = None

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")

    while True:
        choice = social_network_ui.mainMenu()

        if choice == "1":
            print("\nYou are now in the create account menu")
            current_person = ai_social_network.create_account()

        elif choice == "2":
            while True:
                inner_menu_choice = social_network_ui.manageAccountMenu()
                if inner_menu_choice == "1":
                    print("\nYou are now in the edit details menu")
                    # Implement edit details functionality here
                    name = input("Enter your new name: ")
                    age = input("Enter your new age: ")
                    current_person.id = name
                    current_person.year = age
                    print("Details updated successfully.")
                elif inner_menu_choice == "2":
                    person_id = input("Enter the ID of the person you want to add as a friend: ")
                    person = ai_social_network.get_person(person_id)
                    if person:
                        current_person.add_friend(person_id)
                    else:
                        print("Person not found.")
                elif inner_menu_choice == "3":
                    current_person.view_friends()
                elif inner_menu_choice == "4":
                    person_id = input("Enter the ID of the person you want to send a message to: ")
                    message = input("Enter your message: ")
                    current_person.send_message(person_id, message)
                elif inner_menu_choice == "5":
                    person_id = input("Enter the ID of the person you want to block: ")
                    current_person.block_friend(person_id)
                elif inner_menu_choice == "6":
                    current_person.view_messages()
                elif inner_menu_choice == "7":
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")