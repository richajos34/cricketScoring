from team import Team
from player import Player
from game import play_inning
from utils import (
    display_scoreboard_gui,
    optimal_batting_order,
    display_scoreboard,
    choose_batting_order,
    generate_commentary
)

def main():
    team_a = Team("Team A")
    team_b = Team("Team B")

    # Add players to teams
    team_a.add_player(Player("Player A1", "batsman", 45.0, 0.0))
    team_a.add_player(Player("Player A2", "bowler", 15.0, 25.0))
    team_a.add_player(Player("Player A3", "all-rounder", 35.0, 30.0))
    team_a.add_player(Player("Player A4", "batsman", 40.0, 0.0))
    team_a.add_player(Player("Player A5", "bowler", 10.0, 20.0))
    team_a.add_player(Player("Player A6", "batsman", 50.0, 0.0))
    team_a.add_player(Player("Player A7", "bowler", 12.0, 22.0))
    team_a.add_player(Player("Player A8", "all-rounder", 28.0, 18.0))
    team_a.add_player(Player("Player A9", "batsman", 37.0, 0.0))
    team_a.add_player(Player("Player A10", "bowler", 14.0, 24.0))
    team_a.add_player(Player("Player A11", "batsman", 42.0, 0.0))

    team_b.add_player(Player("Player B1", "batsman", 40.0, 0.0))
    team_b.add_player(Player("Player B2", "bowler", 20.0, 20.0))
    team_b.add_player(Player("Player B3", "all-rounder", 30.0, 35.0))
    team_b.add_player(Player("Player B4", "batsman", 38.0, 0.0))
    team_b.add_player(Player("Player B5", "bowler", 12.0, 22.0))
    team_b.add_player(Player("Player B6", "batsman", 47.0, 0.0))
    team_b.add_player(Player("Player B7", "bowler", 17.0, 19.0))
    team_b.add_player(Player("Player B8", "all-rounder", 29.0, 23.0))
    team_b.add_player(Player("Player B9", "batsman", 35.0, 0.0))
    team_b.add_player(Player("Player B10", "bowler", 16.0, 21.0))
    team_b.add_player(Player("Player B11", "batsman", 43.0, 0.0))

    # Choose batting order for both teams
    choose_batting_order(team_a)
    choose_batting_order(team_b)

    # Play the game
    play_inning(team_a, 20)
    play_inning(team_b, 20)

    display_scoreboard_gui(team_a)
    display_scoreboard_gui(team_a)

    # Determine the winner
    if team_a.total_score > team_b.total_score:
        print("\nTeam A wins!")
    elif team_a.total_score < team_b.total_score:
        print("\nTeam B wins!")
    else:
        print("\nThe match is a draw!")

if __name__ == "__main__":
    main()
