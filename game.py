import random

def simulate_ball(batsman, bowler):
    outcome = random.choices(
        ['dot', 'single', 'double', 'triple', 'four', 'six', 'wicket'],
        [0.4, 0.3, 0.1, 0.05, 0.1, 0.05, 0.1]
    )[0]
    return outcome

def play_inning(team, overs):
    for over in range(overs):
        for ball in range(6):
            if team.wickets_lost == 10 or team.wickets_lost >= len(team.players):
                return
            batsman = team.players[team.wickets_lost]
            bowler = team.players[-1]  # Assuming last player as bowler for simplicity
            outcome = simulate_ball(batsman, bowler)
            if outcome == 'wicket':
                team.wickets_lost += 1
            else:
                runs = {'dot': 0, 'single': 1, 'double': 2, 'triple': 3, 'four': 4, 'six': 6}[outcome]
                batsman.runs_scored += runs
                team.total_score += runs

