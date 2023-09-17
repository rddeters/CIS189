class Game:
    # Game class constructor
    def __init__(self, team):
        self.team = team

    def __str__(self):
        return f"{self.team.name} ({self.team.abbreviation})"


class Team:
    # Team class constructor
    def __init__(self, tacronym, tschool, tmascot, tcity, tstate, nwin, nloss):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(tacronym) and name_characters.issuperset(tschool)
                and name_characters.issuperset(tmascot)):
            print('The input for the city or state the team is located in is incorrect')
            raise InvalidSchoolException
        if not (name_characters.issuperset(tcity) and name_characters.issuperset(tstate)):
            print('The input for the school abbreviation, name, or mascot is incorrect')
            raise InvalidLocationException
        self.school_acronym = tacronym
        self.team_school = tschool
        self.team_mascot = tmascot
        self.team_city = tcity
        self.team_state = tstate
        self.num_wins = nwin
        self.num_losses = nloss
        self.player_list = []
        self.player_position = {}
        self.team_array = [self.school_acronym, self.team_school, self.team_mascot, self.team_city,
                           self.team_state, self.num_wins, self.num_losses]

    def add_player(self, player):
        self.player_list.append(player)
        for player in self.player_list:
            if player.position not in self.player_position:
                self.player_position[player.position] = [player.first_name]
            else:
                self.player_position[player.position].append(player.first_name)

    def __str__(self):
        return "The " + self.school_acronym + " volleyball team from " \
            + self.team_school + ", known as the " + self.team_mascot + ", from " + self.team_city + ", " + \
            self.team_state + " has " + str(self.num_wins) + " wins and " + str(self.num_losses) + \
            " losses so far this season."

    def __repr__(self):
        return 'Team({},{},{},{},{},{},{})'.format(self.school_acronym, self.team_school, self.team_mascot,
                                                   self.team_city, self.team_state, self.num_wins, self.num_losses)

    def print_record(self):
        record = (self.num_wins, self.num_losses)
        return f'The record for {self.team_school} is: {record}'

    def team_cheer(self):
        return "Go " + self.school_acronym + " " + self.team_mascot + "!"


class Player (Team):
    # Player class constructor
    def __init__(self, tacronym, tschool, tmascot, tcity, tstate, nwin, nloss, lname, fname, pnum, pos):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            print('The input for first or last name is incorrect')
            raise InvalidNameException
        position_list = ["setter", "outside", "opposite", "middle blocker", "libero", "pinch server"]
        Team.__init__(self, tacronym, tschool, tmascot, tcity, tstate, nwin, nloss)
        self.last_name = lname
        self.first_name = fname
        self.player_number = pnum
        self.position = pos
        if self.position not in position_list:
            print('The input for the position the player plays is incorrect')
            raise InvalidPositionException

    def __str__(self):
        return self.first_name + " " + self.last_name + ", player #" + str(self.player_number) + ", " + \
            self.position + "."

    def __repr__(self):
        return 'Team({},{},{},{})'.format(self.last_name, self.first_name, self.player_number, self.position)

    def display(self):
        print(f'{self.first_name} {self.last_name}, player #{self.player_number}, '
              f'plays the position of {self.position}.')


class InvalidSchoolException(Exception):
    """InvalidSchoolException"""
    pass


class InvalidLocationException(Exception):
    """InvalidLocationException"""
    pass


class InvalidNumInputException(Exception):
    """InvalidNumInputException"""
    pass


class InvalidNameException(Exception):
    """InvalidNameException"""
    pass


class InvalidPositionException(Exception):
    """InvalidPositionException"""
    pass
