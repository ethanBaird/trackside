class Constructor:

    def __init__(self, _name, _driver1, _driver2):
        self.name = _name
        self.drivers = [_driver1, _driver2]
        self.points = _driver1.points + _driver2.points

    