class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.total_score = 0
        self.wickets_lost = 0

    def add_player(self, player):
        self.players.append(player)
