class Ship:
    def __init__(self, size):
        self.size = size
        self.damage = 0

    # self.points = points
    @property
    def is_destroyed(self):
        return self.damage == self.size

    def damage(self):
        if self.damage < self.size:
            self.damage += 1
