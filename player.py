class Player:
    def __init__(self, name, role, batting_avg, bowling_avg):
        self.name = name
        self.role = role
        self.batting_avg = batting_avg
        self.bowling_avg = bowling_avg
        self.runs_scored = 0
        self.balls_faced = 0
        self.wickets_taken = 0
        self.runs_conceded = 0
        self.balls_bowled = 0
