import Classes as c

valid_actions = ["Add", "Edit", "View List", "Completed", "Plan to Watch", "Watching", "Dropped", "Ranking", "Remove", "Clear", "Exit"]

def request_action():
    user_action = input("What would you like to do?\n")
    try:
        if user_action in valid_actions:
            return user_action
    except ValueError:
        print("Invalid Action. Please Enter A Valid Action:\n")
        print("To view your full list of shows, enter 'View List'.\n")
        print("To view your list by status, enter one of the statuses ('Completed', 'Watching', 'Plan to Watch', 'Dropped')\n")
        print("To view your finished and dropped shows sorted by rank, enter 'Ranking'\n")
        print("To remove a show, enter 'Remove'. And to delete your entire list, enter 'Clear'\n")

def action(tv_list: c.TVList):
    user_action = request_action()
    if user_action == "Add":
        tv_list.get_and_add_show()
    if user_action == "View List":
        tv_list.print_full_list()
    if user_action == "Completed":
        tv_list.print_completed()
    if user_action == "Watching":
        tv_list.print_watching()
    if user_action == "Plan to Watch":
        tv_list.print_plan_to_watch()
    if user_action == "Remove":
        tv_list.remove_show()
    if user_action == "Clear":
        tv_list.clear_list()
    if user_action == "Exit":
        exit()

print("Welcome to MyTVShows\n")
MyTVShows = c.TVList()
while True:
    action(MyTVShows)