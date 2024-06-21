import tkinter as tk
import random
from PIL import Image, ImageTk
from team import Team
from player import Player
from game import play_inning
from utils import choose_batting_order, generate_commentary

class CricketSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Game Simulation")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="green")
        self.canvas.pack()

        self.commentary_text = tk.Text(root, height=10, width=100, bg="black", fg="white")
        self.commentary_text.pack()

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="black", fg="yellow")
        self.result_label.pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game, bg="blue", fg="white")
        self.start_button.pack()

        self.player_icon = self.load_icon('player.png')
        self.player_icons = {}

    def load_icon(self, file_name):
        try:
            image = Image.open(file_name)
            image = image.resize((10, 10), Image.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading icon {file_name}: {e}")
            return None

    def display_commentary(self, message, outcome):
        self.commentary_text.insert(tk.END, message + "\n", ("commentary",))
        self.commentary_text.see(tk.END)
        self.root.update()

    def start_game(self):
        self.canvas.delete("all")
        self.draw_game_board()

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

        # Simulate game with commentary
        self.simulate_game_with_commentary(team_a, 20)
        self.simulate_game_with_commentary(team_b, 20)

        # Determine the winner
        if team_a.total_score > team_b.total_score:
            result = "Team A wins!"
        elif team_a.total_score < team_b.total_score:
            result = "Team B wins!"
        else:
            result = "The match is a draw!"

        self.result_label.config(text=result)

    def draw_game_board(self):
        self.canvas.create_rectangle(50, 50, 750, 350, outline="white", width=2)
        self.canvas.create_line(400, 50, 400, 350, fill="white", dash=(5, 2))
        self.canvas.create_text(400, 30, text="Cricket Game Board", fill="white", font=("Helvetica", 16))

    def update_player_on_board(self, team, player, runs, balls_faced, wickets_lost):
        # Remove previous player icon if exists
        if player.name in self.player_icons:
            self.canvas.delete(self.player_icons[player.name])
            self.canvas.delete(self.player_icons[f"{player.name}_text"])

        # Calculate new position
        x = 100 + (runs * 5) % 600
        y = 70 + (wickets_lost * 25)
        player_text = f"{player.name}: {runs} ({balls_faced})"

        # Create player icon and text
        player_icon_id = self.canvas.create_image(x, y, image=self.player_icon, anchor=tk.CENTER)
        player_text_id = self.canvas.create_text(x, y + 20, text=player_text, fill="yellow", font=("Helvetica", 10))

        # Store the icon and text IDs to update later
        self.player_icons[player.name] = player_icon_id
        self.player_icons[f"{player.name}_text"] = player_text_id

    def simulate_game_with_commentary(self, team, overs):
        for over in range(overs):
            for ball in range(6):
                if team.wickets_lost == 10 or team.wickets_lost >= len(team.players):
                    return
                batsman = team.players[team.wickets_lost]
                bowler = team.players[-1]  # Assuming last player as bowler for simplicity
                outcome = self.simulate_ball_with_commentary(batsman, bowler)
                if outcome == 'wicket':
                    team.wickets_lost += 1
                else:
                    runs = {'dot': 0, 'single': 1, 'double': 2, 'triple': 3, 'four': 4, 'six': 6}[outcome]
                    batsman.runs_scored += runs
                    batsman.balls_faced += 1
                    team.total_score += runs
                    bowler.balls_bowled += 1
                    bowler.runs_conceded += runs
                self.update_player_on_board(team, batsman, batsman.runs_scored, batsman.balls_faced, team.wickets_lost)
                self.root.update()
                self.root.after(500)  # Delay to simulate real-time updates

    def simulate_ball_with_commentary(self, batsman, bowler):
        outcome = random.choices(
            ['dot', 'single', 'double', 'triple', 'four', 'six', 'wicket'],
            [0.4, 0.3, 0.1, 0.05, 0.1, 0.05, 0.1]
        )[0]
        commentary = generate_commentary(outcome, batsman, bowler)
        self.display_commentary(commentary, outcome)
        return outcome

if __name__ == "__main__":
    root = tk.Tk()
    app = CricketSimulator(root)
    root.mainloop()