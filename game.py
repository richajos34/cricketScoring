import random
from utils import generate_commentary

def simulate_ball(batsman, bowler):
    outcome = random.choices(
        ['dot', 'single', 'double', 'triple', 'four', 'six', 'wicket'],
        [0.4, 0.3, 0.1, 0.05, 0.1, 0.05, 0.1]
    )[0]
    print(generate_commentary(outcome, batsman, bowler))
    return outcome

def play_inning(team, overs):
    for over in range(overs):
        for ball in range(6):
            if team.wickets_lost == 10 or team.wickets_lost >= len(team.players):
                return
            batsman = team.players[team.wickets_lost]
            bowler = team.players[-1]
            outcome = simulate_ball(batsman, bowler)
            if outcome == 'wicket':
                team.wickets_lost += 1
            else:
                runs = {'dot': 0, 'single': 1, 'double': 2, 'triple': 3, 'four': 4, 'six': 6}[outcome]
                batsman.runs_scored += runs
                batsman.balls_faced += 1
                team.total_score += runs
                bowler.balls_bowled += 1
                bowler.runs_conceded += runs
