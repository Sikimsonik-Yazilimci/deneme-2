
import time

# creating the variables/lists/dictionaries
menu_answers = ['1', '2', '3', '4', '5']


def menu():
    """
    Prints the menu
    """

    menu_items = ["Play Game",
                  "Game Description",
                  "List of Rewards",
                  "Teacher's Page",
                  "Quit"]
    print()
    print("-" * 20,
          "\n  ✖️ Math Game ➗")
    print("-" * 20)

    # A loop for iterating through the menu_answers and menu_items
    # list to print the menus options
    for i in range(len(menu_answers)):
        print(menu_answers[i].title() + ": " + menu_items[i])
    print("-" * 20)


def game_description():
    """
    Prints the game description (in bullet points)
    """
    rules_list = ["\nGame Description: ",
                  "    - This is a math game for kids in grades 2-4 ",
                  "    - You will choose from short (15s), medium (30s), "
                  "and long (60s) for the length of the game ",
                  "    - Depending on the level you choose, you will be "
                  "asked multiplication and division questions",
                  "    - You have to answer as many questions as you can "
                  "in the length of time you choose",
                  "    - You will earn points depending on the number of "
                  "questions you answer correctly",
                  "    - You can access your past scores through the menu "
                  "to see your performance\n"]

    # For loop prints the list of rules by iterating through the rules_list
    for rule in rules_list:
        print(rule)
        time.sleep(1)

    time.sleep(3)

    accepted_answers = ['1', '2', '3']
    options_list = ["Play game", "Return to main menu", "See the rewards"]

    # This for loop prints the user's list of navigational options
    for i in range(len(options_list)):
        print(str(i+1) + ": " + options_list[i])
    print("=" * 20)

    gd_page_input = 0

    # While loop takes user to desired page, or asks for a valid input
    while gd_page_input not in accepted_answers:
        gd_page_input = str(input("> Enter a choice: ")).strip()

        if gd_page_input in accepted_answers:
            if gd_page_input == '1':
                print("")
            elif gd_page_input == '2':
                menu()
            elif gd_page_input == '3':
                rewards()

        else:
            print("- ⛔️ Sorry, that is not a valid choice.\n")


def rewards():
    """
    Prints the list of rewards (in bullet points)
    """
    print("\nGame rewards:")
    rewards_list = ["    - +5% in your next test............15,000 points",
                    "    - Skip 1 class of your choice......20,000 points",
                    "    - +10% in your next test...........27,500 points",
                    "    - Get an early leave pass..........30,000 points",
                    "    - Get 1 day off of school..........50,000 points",
                    "    - Get 1 week off of school.........250,000 points\n"]

    # For loop prints the list of rewards by iterating through the rules_list
    for reward in rewards_list:
        print(reward)
        time.sleep(0.75)

    accepted_answers = ['1', '2', '3']
    options_list = ["Play game",
                    "Return to main menu",
                    "See the rules"]

    # This for loop prints the user's list of navigational options
    for i in range(len(options_list)):
        print(str(i + 1) + ": " + options_list[i])
    print("-" * 20)

    rewards_page_input = 0

    # While loop takes user to desired page, or asks for a valid input
    while rewards_page_input not in accepted_answers:
        rewards_page_input = str(input("> Enter a choice: ")).strip()

        if rewards_page_input in accepted_answers:
            if rewards_page_input == '1':
                print("")
            elif rewards_page_input == '2':
                menu()
            elif rewards_page_input == '3':
                game_description()

        else:
            print("- ⛔️ Sorry, that is not a valid choice.\n")


# Calls the menu function to print the menu, and asks for an input
menu()
menu_input = str(input("> Enter a choice: ")).strip()


# Loop executing code until user inputs "q" for exiting the code
while menu_input != menu_answers[-1]:

    # If input from the menu is valid, then executes code accordingly -
    # if not, asks for input again
    if menu_input.strip() in menu_answers:

        # If input is '1' then calls function to play game
        if menu_input == "1":
            print("")

        # If input is 2 then calls function to display game description
        elif menu_input == "2":
            game_description()

        # If input is 3 then calls function to display the rewards
        elif menu_input == "3":
            rewards()

        # If input is '4' then calls function to display teacher's page
        elif menu_input == "4":
            print("")

    # if input is not valid, then prints a message
    else:
        print("- ⛔️ Sorry, that is not a valid choice.\n")

    # calls menu function again as long as the while loop continues
    menu()
    menu_input = input("> Enter a choice: ")


print("\nThanks for playing!\n")


print("")
