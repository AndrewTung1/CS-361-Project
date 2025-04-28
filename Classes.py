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

    def print_full_list(self):
        """Method to print the current list of shows"""
        for show in self._list:
            print("Show Name: ", show.name, "Status: ", show.status, "Rating: ", show.rating)
            print("\n")

    def print_completed(self):
        """Method to print all the completed shows"""
        for show in self._list:
            if show.status == "Completed":
                print("Show Name: ", show.name, "Status: ", show.status, "Rating: ", show.rating)
                print("\n")

    def print_watching(self):
        """Method to print all the currently watching shows"""
        for show in self._list:
            if show.status == "Watching":
                print("Show Name: ", show.name, "Status: ", show.status, "Rating: ", show.rating)
                print("\n")

    def print_plan_to_watch(self):
        """Method to print all the plan to watch shows"""
        for show in self._list:
            if show.status == "Plan to Watch":
                print("Show Name: ", show.name, "Status: ", show.status, "Rating: ", show.rating)
                print("\n")

    def print_dropped(self):
        """Method to print all the dropped shows"""
        for show in self._list:
            if show.status == "Dropped":
                print("Show Name: ", show.name, "Status: ", show.status, "Rating: ", show.rating)
                print("\n")

    def get_show_name(self):
        """Method to request the name of a show the user would like to add"""
        while True:
            show_name = input("What is the name of the show you would like to add?\n")
            if show_name == "Cancel":
                print("Action canceled.")
                return
            if self.exist_already(show_name) is True:
                print("Error: TV Show is already in your list.\n")
            else:
                return show_name

    def get_show_rating(self):
        """Method to request the rating of a show from the user"""
        while True:
            try:
                user_rating = int(input("How would you rate this show from 1 to 10?\n"))
                if user_rating == "Cancel":
                    print("Action canceled.")
                    return
                if 1 <= user_rating <= 10:
                    return user_rating
                else:
                    print("Error: Number must be between 1 and 10.\n")
            except ValueError:
                print("Error: Invalid input. Please enter an integer between 1 and 10.\n")

    def get_show_status(self):
        """Method to request the status of a show"""
        while True:
            try:
                status = input("Enter the status of this show ('Completed', 'Watching', 'Plan to Watch', 'Dropped':\n")
                if status == "Cancel":
                    print("Action canceled.")
                    return
                if status == "Completed" or status == "Watching" or status == "Plan to Watch" or status == "Dropped":
                    return status
            except ValueError:
                print("Invalid Status. Please Enter One of the Following: 'Completed', 'Watching', 'Plan to Watch', 'Dropped'\n")

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
        elif show_status == "Plan to Watch" or show_status == "Watching":
            new_show = TVShow(show_name, show_status)
            self.add_show(new_show)

    def get_remove_name(self):
        while True:
            show_name = input("What is the name of the show you would like to remove?\n")
            if show_name == "Cancel":
                print("Action canceled.")
                return
            if self.exist_already(show_name) is False:
                print("Error: The TV show you entered is not currently in your list. Please enter a different show or enter 'Cancel' to cancel the action.\n")
            else:
                return show_name

    def remove_show(self):
        """Method to remove a show from the list"""
        show_name = self.get_remove_name()
        if show_name is None:
            print("Action canceled.")
            return
        user_input = input("Are you sure you would like to remove this show? This action cannot be undone. (Y/N)")
        if user_input == "Y":
            for show in self._list:
                if show.name == show_name:
                    self._list.remove(show)
            print(show_name, "has been removed.")
        else:
            print("Action canceled.")

    def clear_list(self):
        """Method to remove all shows from the list"""
        user_input = input("Are you sure you would like to remove all shows from your list? This action cannot be undone. (Y/N)")
        if user_input == "Y":
            for show in self._list:
                self._list.remove(show)
            print("Your list of shows has been cleared.")
        else:
            print("Action canceled.")

