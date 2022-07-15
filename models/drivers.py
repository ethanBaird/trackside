class Driver:

    def __init__(self, _name, _points, _wins, _podiums):
        self.name = _name
        self.points = _points
        self.wins = _wins
        self.podiums = _podiums

    def add_points(self, points, constructor):
        self.points += points
        constructor.points += points
    


    def add_wins(self, wins):
        self.wins += wins

    def add_podiums(self, podiums):
        self.podiums += podiums

    