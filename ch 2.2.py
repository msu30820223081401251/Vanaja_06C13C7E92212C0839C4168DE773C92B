# batsman and bowler 

class CricketMatch:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print(f"{self.player1} is batting, and {self.player2} is bowling")

# Create two instances of CricketMatch
match1 = CricketMatch("Batman", "Bowler1")
match2 = CricketMatch("Superman", "Bowler2")

# Call play() method on each object
match1.play()
match2.play()