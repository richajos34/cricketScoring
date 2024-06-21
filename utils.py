import random
import tkinter as tk
import json

from team import Team

def optimal_batting_order(team):
    team.players.sort(key=lambda player: player.batting_avg, reverse=True)

def optimal_bowling_change(team, current_bowler):
    # Choose next bowler based on current game situation and player stats
    next_bowler = min(
        [p for p in team.players if p.role in ['bowler', 'all-rounder'] and p != current_bowler],
        key=lambda p: (p.bowling_avg, p.balls_bowled)
    )
    return next_bowler


def choose_batting_order(team):
    print("Choose batting order for", team.name)
    for i, player in enumerate(team.players):
        print(f"{i + 1}. {player.name} (Role: {player.role}, Batting Avg: {player.batting_avg})")
    order = input("Enter the player numbers in desired batting order, separated by spaces: ")
    order = [int(x) - 1 for x in order.split()]
    team.players = [team.players[i] for i in order]

def display_scoreboard(team):
    print(f"\nTeam {team.name} Score: {team.total_score}/{team.wickets_lost} in {team.overs_faced} overs")
    print(f"{'Player':<15} {'Runs Scored':<10} {'Balls Faced':<10} {'Strike Rate':<10}")
    for player in team.players:
        if player.balls_faced > 0:
            strike_rate = round((player.runs_scored / player.balls_faced) * 100, 2)
        else:
            strike_rate = 0.0
        print(f"{player.name:<15} {player.runs_scored:<10} {player.balls_faced:<10} {strike_rate:<10}")


def display_scoreboard_gui(team):
    window = tk.Tk()
    window.title(f"{team.name} Scoreboard")

    tk.Label(window, text=f"Team {team.name} Score: {team.total_score}/{team.wickets_lost}").pack()
    
    for player in team.players:
        tk.Label(window, text=f"{player.name}: {player.runs_scored} runs").pack()

    window.mainloop()



def save_game_state(teams, filename="game_state.json"):
    with open(filename, "w") as file:
        json.dump([team.__dict__ for team in teams], file)

def load_game_state(filename="game_state.json"):
    with open(filename, "r") as file:
        team_dicts = json.load(file)
        return [Team(**team_dict) for team_dict in team_dicts]

def generate_commentary(outcome, batsman, bowler):
    commentary = {
        'dot': f"{bowler.name} bowls to {batsman.name}, no run.",
        'single': f"{bowler.name} bowls to {batsman.name}, single taken.",
        'double': f"{bowler.name} bowls to {batsman.name}, good running, they get two.",
        'triple': f"{bowler.name} bowls to {batsman.name}, excellent running, three runs.",
        'four': f"{bowler.name} bowls to {batsman.name}, it's a boundary! Four runs.",
        'six': f"{bowler.name} bowls to {batsman.name}, what a shot! Six runs.",
        'wicket': f"{bowler.name} to {batsman.name}, out! Great delivery."
    }
    return commentary[outcome]

def simulate_ball(batsman, bowler):
    outcome = random.choices(
        ['dot', 'single', 'double', 'triple', 'four', 'six', 'wicket'],
        [0.4, 0.3, 0.1, 0.05, 0.1, 0.05, 0.1]
    )[0]
    print(generate_commentary(outcome, batsman, bowler))
    return outcome
