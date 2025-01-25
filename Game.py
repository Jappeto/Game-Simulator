

# ----------------------------------------------------------------------
# Game.py
# Jacob Reppeto
# 11/16/2024
# ----------------------------------------------------------------------

import random

class Game:
    """A Game/Score tracker for a game between two teams"""

    # ------------------------------------------------------------------

    def __init__(self, team1: str, team2: str):
        """
        :param team1: name of team 1
        :param team2: name of team 2
        """
        self._team1Name: str = team1
        self._team2Name: str = team2
        self._team1Points: int = 0
        self._team2Points: int = 0
        self._team1Wins: int = 0
        self._team2Wins: int = 0

    # ------------------------------------------------------------------

    def addPoints(self, team: str, points: int):
        """
        add specified number of points to the specified team
        :param team: name of team to add the points to
        :param points: number of points to add to the specified team
        :return: None
        """
        if self._team1Name == team:
            self._team1Points += points
        else:
            self._team2Points += points

    def score(self) -> str:
        """
        name of first team followed by a colon and space followed by their score followed by a dash
        followed by a space and then name of second team, a colon and dash, and their score
        for example if the teams were named "Team1" and "Team2", it would return a string such as:
        "Team1: 25 - Team2: 27"
        :return: string showing score as specified above
        """
        return f"{self._team1Name}: {self._team1Points} - {self._team2Name}: {self._team2Points}"

    def winner(self) -> str:
        """
        :return: the name of the winning team based on who has more points, or "tie" if score is tied
        """
        if self._team1Points > self._team2Points:
            return self._team1Name
        elif self._team1Points < self._team2Points:
            return self._team2Name
        else:
            return "tie"

    # ------------------------------------------------------------------

    def startNewGame(self):
        """
        updates the number of wins for the winning team (ties are not counted as either team winning)
        and resets the score for each team to zero
        :return:
        """
        if self._team1Points > self._team2Points:
            self._team1Wins += 1
        elif self._team1Points < self._team2Points:
            self._team2Wins += 1
        self._team1Points = 0
        self._team2Points = 0



    def seriesLead(self) -> str:
        """
        a string indicating who is winning the series for the games played so far
        the leading team is always listed first with their number of wins and then
        the number of wins by the other team. Here are two examples (second one shows
        what to do in case of a tie):
        Team1 leads 3 - 2
        series tied 3 - 3
        :return: string as specified above
        """
        if self._team1Wins > self._team2Wins:
            return f"{self._team1Name} leads {self._team1Wins} - {self._team2Wins}"
        elif self._team1Wins < self._team2Wins:
            return f"{self._team2Name} leads {self._team2Wins} - {self._team1Wins}"
        else:
            return f"series tied {self._team1Wins} - {self._team2Wins}"

# ----------------------------------------------------------------------

def main():
    game = Game("Capital", "Otterbein")
    numGames = int(input("Enter number of games in each series: "))
    for _ in range(7):
        for _ in range(numGames):
            scorer = random.random()
            if scorer <= 0.5:
                team = "Capital"
            else:
                team = "Otterbein"
            game.addPoints(team, 1)
            print(game.score())
        print(game.winner())
        print()
        game.startNewGame()
        print(game.seriesLead())

# ----------------------------------------------------------------------


if __name__ == "__main__":
    main()