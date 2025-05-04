import os

line = "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
class TVShow:
    """A TV Show with three attributes: name, status, and user rating for the show"""
    def __init__(self, name, status, rating=None):
        self.name = name
        self.status = status
        self.rating = rating

class TVList:
    """Class for the list of tv shows with its various methods"""
    def __init__(self):
        self._list = []

    def refresh(self):
        """Method to go back to the home page by clearing the terminal"""
        os.system('cls')
        print("Welcome to MyTVShows\n")
        print("Keep track of your shows by adding them to your own personalized list with your viewing status and personal rating!\n")
        print(line)
        print("To view your full list of shows, enter 'View List'.\n")
        print("To view your list by status, enter one of the statuses ('Completed', 'Watching', 'Plan to Watch', 'Dropped')\n")
        print("To view your finished and dropped shows sorted by rank, enter 'Ranking'\n")
        print("To remove a show, enter 'Remove'. And to delete your entire list, enter 'Clear'\n")
        print("To clear the terminal and refresh the screen, enter 'Home'\n")
        print(line)

    def get_list(self):
        """Method for returning the current list"""
        return self._list

    def add_show(self, inputted_show: TVShow):
        """Method to add a TV show object to the list"""
        self._list.append(inputted_show)

    def exist_already(self, inputted_show_name: str):
        """Method to check if the user's inputted show already exists in the list"""
        for show in self._list:
            if show.name == inputted_show_name:
                return True
        return False

    def print_list(self, status: str):
        """Method to print the current list of shows"""
        if status == "View List":
            print(line, "\n\n")
            for show in self._list:
                print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
                print("\n")
            print(line, "\n")
        else:
            print(line, "\n")
            for show in self._list:
                if show.status == status:
                    print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
                    print("\n")
            print(line, "\n")

    def print_ranked(self):
        """Method to print the list of finished or dropped shows by rank"""
        print(line, "\n")
        ranked_shows = []
        for show in self._list:
            if type(show.rating) is int:
                ranked_shows.append(show)
        ranked_list = sorted(ranked_shows, key=lambda x: x.rating, reverse=True)
        for show in ranked_list:
            print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
            print("\n")
        print(line, "\n")

    def print_completed(self):
        """Method to print all the completed shows"""
        print(line, "\n")
        for show in self._list:
            if show.status == "Completed":
                print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
                print("\n")
        print(line, "\n")

    def print_watching(self):
        """Method to print all the currently watching shows"""
        print(line, "\n")
        for show in self._list:
            if show.status == "Watching":
                print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
                print("\n")
        print(line, "\n")

    def print_plan_to_watch(self):
        """Method to print all the plan to watch shows"""
        print(line, "\n")
        for show in self._list:
            if show.status == "Plan to Watch":
                print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
                print("\n")
        print(line, "\n")

    def print_dropped(self):
        """Method to print all the dropped shows"""
        print(line, "\n")
        for show in self._list:
            if show.status == "Dropped":
                print("Show Name:", show.name, " Status:", show.status, " Rating:", show.rating)
                print("\n")
        print(line, "\n")

    def get_show_name(self):
        """Method to request the name of a show the user would like to add"""
        while True:
            show_name = input("What is the name of the show you would like to add?\n")
            if show_name == "Cancel":
                print("Action canceled.\n")
                return
            if self.exist_already(show_name) is True:
                print("Error: TV Show is already in your list.\n")
            else:
                return show_name

    def get_show_rating(self):
        """Method to request the rating of a show from the user"""
        while True:
            user_rating = input("How would you rate this show from 1 to 10?\n")
            if user_rating == "Cancel":
                print("Action canceled.\n")
                return
            elif user_rating.isdigit() is False:
                print("Error: Invalid input. Please enter an integer between 1 and 10.\n")
            else:
                if int(user_rating) > 10 or int(user_rating) < 1:
                    print("Error: Invalid input. Please enter an integer between 1 and 10.\n")
                else:
                    return int(user_rating)

    def get_show_status(self):
        """Method to request the status of a show"""
        while True:
            status = input("Enter the status of this show ('Completed', 'Watching', 'Plan to Watch', 'Dropped':\n")
            if status == "Cancel":
                print("Action canceled.\n")
                return
            if status in ["Completed", "Watching", "Plan to Watch", "Dropped"]:
                return status
            else:
                print("Invalid Status. Please enter one of the following: 'Completed', 'Watching', 'Plan to Watch', 'Dropped'\n")

    def get_and_add_show(self):
        """Method that combines the get and add methods"""
        show_name = self.get_show_name()
        if show_name is None:
            return
        show_status = self.get_show_status()
        if show_status is None:
            return
        if show_status == "Completed" or show_status == "Dropped":
            show_rating = self.get_show_rating()
            if show_rating is None:
                return
            new_show = TVShow(show_name, show_status, show_rating)
            self.add_show(new_show)
            print(show_name, " has been added!\n")
        elif show_status == "Plan to Watch" or show_status == "Watching":
            new_show = TVShow(show_name, show_status)
            self.add_show(new_show)
            print(show_name, "has been added!\n")

    def get_edit_remove_name(self):
        """Method to get the name of the edited or removed show"""
        while True:
            show_name = input("What is the name of the show you would like to edit or remove?\n")
            if show_name == "Cancel":
                return
            if self.exist_already(show_name) is False:
                print("Error: The TV show you entered is not currently in your list. Please enter a different show or enter 'Cancel' to cancel the action.\n")
            else:
                return show_name

    def remove_show(self):
        """Method to remove a show from the list"""
        show_name = self.get_edit_remove_name()
        if show_name is None:
            print("Action canceled.\n")
            return
        else:
            user_input = input("Are you sure you would like to remove this show? This action cannot be undone. (Y/N)\n")
            if user_input == "Y":
                for show in self._list:
                    if show.name == show_name:
                        self._list.remove(show)
                print(show_name, "has been removed.\n")
            else:
                print("Action canceled.\n")

    def get_edited_status(self):
        """Method to get the status of the edited show"""
        while True:
            new_status = input("What is the new status of this show?\n")
            if new_status == "Cancel":
                return
            elif new_status not in ["Completed", "Watching", "Plan to Watch", "Dropped"]:
                print("Invalid Status. Please enter one of the following: 'Completed', 'Watching', 'Plan to Watch', 'Dropped'\n")
            else:
                return new_status

    def get_edited_rating(self):
        """Method to get the rating of the edited show"""
        while True:
            user_rating = input("What is your new rating of this show?\n")
            if user_rating == "Cancel":
                return
            elif user_rating.isdigit() is False:
                print("Error: Invalid input. Please enter an integer between 1 and 10.\n")
            else:
                if int(user_rating) > 10 or int(user_rating) < 1:
                    print("Error: Invalid input. Please enter an integer between 1 and 10.\n")
                else:
                    return int(user_rating)

    def edit_show(self):
        """Method to edit a show from the list"""
        show_name = self.get_edit_remove_name()
        if show_name is None:
            print("Action canceled.\n")
            return
        else:
            user_input = input("Are you sure you would like to edit this show? This action cannot be undone. (Y/N)\n")
            if user_input == "Y":
                for show in self._list:
                    if show.name == show_name:
                        new_status = self.get_edited_status()
                        if new_status is None:
                            print("Action canceled.\n")
                            return
                        elif new_status == "Watching" or new_status == "Plan to Watch":
                            show.status = new_status
                            show.rating = None
                        elif new_status == "Completed" or new_status == "Dropped":
                            new_rating = self.get_edited_rating()
                            if new_rating is None:
                                print("Action canceled.\n")
                                return
                            show.status = new_status
                            show.rating = new_rating
                print(show_name, "has been edited.\n")
            else:
                print("Action canceled.\n")

    def clear_list(self):
        """Method to remove all shows from the list"""
        user_input = input("Are you sure you would like to remove all shows from your list? This action cannot be undone. (Y/N)\n")
        if user_input == "Y":
            for show in self._list:
                self._list.remove(show)
            print("Your list of shows has been cleared.\n")
        else:
            print("Action canceled.\n")

