def optimal_batting_order(team):
    team.players.sort(key=lambda player: player.batting_avg, reverse=True)

def optimal_bowling_change(team, current_bowler):
    next_bowler = min(
        [p for p in team.players if p.role in ['bowler', 'all-rounder'] and p != current_bowler],
        key=lambda p: p.bowling_avg
    )
    return next_bowler

def display_scoreboard(team):
    print(f"Team {team.name} Score: {team.total_score}/{team.wickets_lost}")
    for player in team.players:
        print(f"{player.name}: {player.runs_scored} runs")
