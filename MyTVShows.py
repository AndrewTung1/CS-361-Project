import Classes as c
import os

valid_actions = ["Add", "Edit", "View List", "Completed", "Plan to Watch", "Watching", "Dropped", "Ranking", "Remove", "Clear", "Exit", "Home"]

line = "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

def test(tv_list):
    tv_list.add_show(c.TVShow("The Blacklist", "Completed", 6))
    tv_list.add_show(c.TVShow("Black Mirror", "Completed", 8))
    tv_list.add_show(c.TVShow("Severance", "Watching"))
    tv_list.add_show(c.TVShow("Game of Thrones", "Dropped", 4))
    tv_list.add_show(c.TVShow("Santa Clarita Diet", "Dropped", 5))
    tv_list.add_show(c.TVShow("Arcane", "Watching"))
    tv_list.add_show(c.TVShow("The Wire", "Watching"))
    tv_list.add_show(c.TVShow("Friends", "Plan to Watch"))
    tv_list.add_show(c.TVShow("The Sopranos", "Plan to Watch"))

def request_action():
    while True:
        user_action = input("What would you like to do?\n")
        if user_action in valid_actions:
                return user_action
        else:
            print(line)
            print("Invalid Action. Please Enter A Valid Action:\n")
            print("To view your full list of shows, enter 'View List'.\n")
            print("To view your list by status, enter one of the statuses ('Completed', 'Watching', 'Plan to Watch', 'Dropped')\n")
            print("To view your finished and dropped shows sorted by rank, enter 'Ranking'\n")
            print("To remove a show, enter 'Remove'. And to delete your entire list, enter 'Clear'\n")
            print("To clear the terminal and refresh the screen, enter 'Home'")
            print(line,"\n")

def action(tv_list: c.TVList):
    user_action = request_action()
    if user_action == "Home":
        tv_list.refresh()
    if user_action == "Add":
        tv_list.get_and_add_show()
    if user_action in ["View List", "Completed", "Watching", "Plan to Watch", "Dropped"]:
        tv_list.print_list(user_action)
    if user_action == "Ranking":
        tv_list.print_ranked()
    if user_action == "Remove":
        tv_list.remove_show()
    if user_action == "Edit":
        tv_list.edit_show()
    if user_action == "Clear":
        tv_list.clear_list()
    if user_action == "Exit":
        exit()


os.system('cls')
print("Welcome to MyTVShows!\n")
print("Keep track of your shows by adding them to your own personalized list with your viewing status and personal rating!\n")
print(line)
print("To view your full list of shows, enter 'View List'.\n")
print("To view your list by status, enter one of the statuses ('Completed', 'Watching', 'Plan to Watch', 'Dropped')\n")
print("To view your finished and dropped shows sorted by rank, enter 'Ranking'\n")
print("To remove a show, enter 'Remove'. And to delete your entire list, enter 'Clear'\n")
print("To clear the terminal and refresh the screen, enter 'Home'")
print(line, "\n")
MyTVShows = c.TVList()
while True:
    action(MyTVShows)