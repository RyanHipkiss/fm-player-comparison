from classes.Player import Player

class BPDD:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.acc + self.player.pac + self.player.jum + self.player.cmp
        green = self.player.hea + self.player.mar + self.player.tck + self.player.pos + self.player.str
        blue = self.player.fir + self.player.tec + self.player.agg + self.player.ant + self.player.bra + self.player.cnt + self.player.dec + self.player.vis

        return round(
            (
            (key * 5) + (green * 3) + blue
            ) / 46,
            1
        )