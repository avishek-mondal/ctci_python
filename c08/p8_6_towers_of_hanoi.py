class Tower:
    def __init__(self):
        self.disks = []

    def add(self, d):
        if len(self.disks) > 0 and self.disks[-1] <= d:
            raise ValueError

        self.disks.append[d]

    def move_top_to(self, tower: "Tower"):
        if len(self.disks) == 0:
            raise ValueError

        top = self.disks.pop()
        tower.add(top)

    def move_disks(
        self, num_disks: int, destination: "Tower", buffer: "Tower"
    ):
        if num_disks <= 0:
            return

        self.move_disks(num_disks - 1, destination=buffer, buffer=destination)
        self.move_top_to(destination)
        buffer.move_disks(num_disks - 1, destination=destination, buffer=self)
