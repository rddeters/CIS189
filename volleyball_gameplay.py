import random
import tkinter as tk
from final_definitions.volleyball_definitions import Player
from final_definitions.volleyball_definitions import Team
from final_definitions.volleyball_definitions import Game
from final_definitions.volleyball_definitions import InvalidNumInputException


def create_gui():
    def create_team():
        global team  # declare team as nonlocal
        abbreviation = entry_abbreviation.get()
        name = entry_name.get()
        mascot = entry_mascot.get()
        city = entry_city.get()
        state = entry_state.get()
        losses = entry_losses.get()
        wins = entry_wins.get()
        team = Team(abbreviation, name, mascot, city, state, losses, wins)  # update team
        game = Game(team)
        print(game.team.__dict__)

    def add_player(team):
        team_array = team.team_array
        fname = entry_player_fname.get()
        lname = entry_player_lname.get()
        number = entry_player_number.get()
        position = entry_player_position.get()
        player = Player(team_array[0], team_array[1], team_array[2], team_array[3],
                        team_array[4], team_array[5], team_array[6], lname, fname, number, position)
        team.add_player(player)  # add player to the team
        print(team.player_list)

    root = tk.Tk()
    root.title("Team & Player Information")
    root.geometry("400x400")

    # Labels for team information
    tk.Label(root, text="Team Abbreviation: ").grid(row=0, column=0)
    tk.Label(root, text="School Name: ").grid(row=1, column=0)
    tk.Label(root, text="School Mascot: ").grid(row=2, column=0)
    tk.Label(root, text="School City: ").grid(row=3, column=0)
    tk.Label(root, text="School State: ").grid(row=4, column=0)
    tk.Label(root, text="Season Losses: ").grid(row=5, column=0)
    tk.Label(root, text="Season Wins: ").grid(row=6, column=0)

    # Entry fields for team information
    entry_abbreviation = tk.Entry(root)
    entry_abbreviation.grid(row=0, column=1)
    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1)
    entry_mascot = tk.Entry(root)
    entry_mascot.grid(row=2, column=1)
    entry_city = tk.Entry(root)
    entry_city.grid(row=3, column=1)
    entry_state = tk.Entry(root)
    entry_state.grid(row=4, column=1)
    entry_losses = tk.Entry(root)
    entry_losses.grid(row=5, column=1)
    entry_wins = tk.Entry(root)
    entry_wins.grid(row=6, column=1)

    # Buttons for team information and player information
    tk.Button(root, text="Create Team", command=create_team).grid(row=7, column=0, columnspan=2)

    tk.Label(root, text="First Name: ").grid(row=8, column=0)
    tk.Label(root, text="Last Name: ").grid(row=9, column=0)
    tk.Label(root, text="Number: ").grid(row=10, column=0)
    tk.Label(root, text="Position: ").grid(row=11, column=0)
    entry_player_fname = tk.Entry(root)
    entry_player_fname.grid(row=8, column=1)
    entry_player_lname = tk.Entry(root)
    entry_player_lname.grid(row=9, column=1)
    entry_player_number = tk.Entry(root)
    entry_player_number.grid(row=10, column=1)
    entry_player_position = tk.Entry(root)
    entry_player_position.grid(row=11, column=1)

    tk.Button(root, text="Create Player", command=lambda: add_player(team)).grid(row=12, column=0, columnspan=2)

    def create_game():
        if team:
            play(team.school_acronym, team.player_position, team)
        else:
            print("Error creating team")

    start_game_button = tk.Button(root, text="Start Game", command=lambda: create_game())
    start_game_button.grid(row=14, column=1)

    root.mainloop()


def play(team1, player_positions, team):

    def determine_order(team1_play):
        order_of_play = random.randint(1, 2)
        if order_of_play == 1:
            team1_play = True
        return team1_play

    def select_player(action_name, player_position):
        if action_name == "serve":
            if "pinch server" in player_positions:
                action_player = player_position["pinch server"][0]
            else:
                action_player = "None"
        elif action_name == "set":
            if "setter" in player_positions:
                action_player = player_position["setter"][0]
            else:
                action_player = "None"
        elif action_name == "spike":
            if "outside" in player_positions:
                action_player = player_position["outside"][0]
            elif "opposite" in player_positions:
                action_player = player_position["opposite"][0]
            else:
                action_player = "None"
        elif action_name == "block":
            if "middle blocker" in player_positions:
                action_player = player_position["middle blocker"][0]
            else:
                action_player = "None"
        else:
            if "libero" in player_positions:
                action_player = player_positions["libero"][0]
            else:
                action_player = "None"
        return action_player

    def action(team1_play, action_name, player_positions):
        if action_name != "block":
            rand_num = random.randint(1, 20)
            rand2_num = random.randint(1, 20)
            if team1_play:
                try:
                    position_player = select_player(action_name, player_positions)
                    if not position_player == 'None':
                        action = int(input(f'Please enter a number between 1 and 20'
                                           f' to determine if {position_player} successfully {action_name}s: '))
                    else:
                        action = int(input(f'Please enter a number between 1 and 20'
                                           f' to determine if your team successfully {action_name}s: '))
                    if action < 1 or action > 20:
                        raise InvalidNumInputException("Your input was out of range.")
                except InvalidNumInputException as n:
                    print(n)
                    position_player = select_player(action_name, player_positions)
                    action = int(input(f'Please enter a VALID number between 1 and 20'
                                       f' to determine if the user team successfully {action_name}s: '))
                except ValueError:
                    position_player = select_player(action_name, player_positions)
                    action = int(input(f'Please enter a NUMBER between 1 and 20'
                                       f' to determine if the user team successfully {action_name}s: '))
                if not (action == rand_num):
                    action_complete = True
                    if not position_player == 'None':
                        print(f'{position_player} successfully {action_name}s the ball!')
                else:
                    action_complete = False
            else:
                if not (rand2_num == rand_num):
                    action_complete = True
                else:
                    action_complete = False
        else:
            rand_num = random.randint(1, 5)
            rand2_num = random.randint(1, 5)
            if not team1_play:
                try:
                    position_player = select_player(action_name, player_positions)
                    if not position_player == 'None':
                        action = int(input(f'Please enter a number between 1 and 5'
                                           f' to determine if {position_player} successfully {action_name}s: '))
                    else:
                        action = int(input(f'Please enter a number between 1 and 5'
                                           f' to determine if your team successfully {action_name}s: '))
                    if action < 1 or action > 5:
                        raise InvalidNumInputException("Your input was out of range.")
                except InvalidNumInputException as n:
                    print(n)
                    position_player = select_player(action_name, player_positions)
                    action = int(input(f'Please enter a VALID number between 1 and 5'
                                       f' to determine if the user team successfully {action_name}s: '))
                except ValueError:
                    position_player = select_player(action_name, player_positions)
                    action = int(input(f'Please enter a NUMBER between 1 and 5'
                                       f' to determine if the user team successfully {action_name}s: '))

                if action == rand_num:
                    action_complete = True
                    if not position_player == 'None':
                        print(f'{position_player} successfully {action_name}ed the ball!')
                else:
                    action_complete = False
            else:
                if rand2_num == rand_num:
                    action_complete = True
                else:
                    action_complete = False
        return action_complete

    def play_set(user_team, computer_team, user_points, computer_points, user_play, player_positions):

        has_served = False
        has_received = False
        has_set = False
        has_spiked = False
        has_blocked = False
        continue_rally = True

        has_served = action(user_play, "serve", player_positions)

        if has_served and not user_play:
            user_play = True
            has_received = action(user_play, "receive", player_positions)
        elif has_served and user_play:
            user_play = False
            has_received = action(user_play, "receive", player_positions)
        elif user_play and not has_served:
            computer_points += 1
            user_play = False
            print(
                f'{computer_team} wins the rally, as {user_team} did not successfully serve!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            continue_rally = False
        else:
            user_points += 1
            user_play = True
            print(
                f'{user_team} wins the rally as {computer_team} did not successfully serve!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            continue_rally = False

        if has_received and continue_rally:
            has_set = action(user_play, "set", player_positions)
        elif user_play and continue_rally and not has_received:
            computer_points += 1
            user_play = False
            print(
                f'{computer_team} wins the rally, as {user_team} did not successfully receive!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            continue_rally = False
        elif continue_rally:
            user_points += 1
            user_play = True
            print(
                f'{user_team} wins the rally as {computer_team} did not successfully receive!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            continue_rally = False

        if has_set and continue_rally:
            has_spiked = action(user_play, "spike", player_positions)
        elif user_play and continue_rally and not has_set:
            computer_points += 1
            user_play = False
            print(
                f'{computer_team} wins the rally, as {user_team} did not successfully set the ball!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            continue_rally = False
        elif continue_rally:
            user_points += 1
            user_play = True
            print(
                f'{user_team} wins the rally as {computer_team} did not successfully set the ball!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            continue_rally = False

        if has_spiked and continue_rally:
            has_blocked = action(user_play, "block", player_positions)
        elif user_play and continue_rally and not has_spiked:
            computer_points += 1
            user_play = False
            continue_rally = False
            print(
                f'{computer_team} wins the rally, as {user_team} did not successfully spike!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
        elif continue_rally:
            user_points += 1
            continue_rally = False
            user_play = True
            print(
                f'{user_team} wins the rally as {computer_team} did not successfully spike!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')

        if has_blocked and continue_rally:
            if user_play:
                computer_points += 1
                user_play = False
                print(
                    f'{computer_team} wins the rally, as they successfully blocked the ball!'
                    f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
            else:
                user_points += 1
                user_play = True
                continue_rally = False
                print(
                    f'{user_team} wins the rally, as they successfully blocked the ball!'
                    f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
        elif user_play and not has_blocked and continue_rally:
            user_points += 1
            user_play = True
            continue_rally = False
            print(
                f'{user_team} wins the rally as {computer_team} did not successfully block!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')
        elif continue_rally and not user_play:
            computer_points += 1
            user_play = False
            print(
                f'{computer_team} wins the rally, as {user_team} did not successfully block!'
                f' The score is now {user_points} points for {user_team} and {computer_points} for {computer_team}')

        return user_points, computer_points, user_play

    user_team = team1
    user_play = False
    computer_team = "Computer"
    user_points = 0
    computer_points = 0
    user_play = determine_order(user_play)
    while (user_points < 25) and (computer_points < 25):
        user_points, computer_points, user_play = \
            play_set(user_team, computer_team, user_points, computer_points, user_play, player_positions)

    if user_points >= 25:
        print(f'{user_team} wins the set!')
    elif computer_points >= 25:
        print(f'{computer_team} wins the set!')


if __name__ == '__main__':
    create_gui()
