class Driver:

    def __init__(self, _name, _points, _wins, _podiums, _id=None):
        self.name = _name
        self.points = _points
        self.wins = _wins
        self.podiums = _podiums
        self.id = _id

    def race(self, result):
        self.points += result.score.points
        if result.score.win:
            self.wins += 1
        if result.score.podium:
            self.podiums += 1

    