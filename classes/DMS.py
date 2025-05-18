from classes.Player import Player

class DMS:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.wor + self.player.sta + self.player.acc + self.player.pac
        green = self.player.tck + self.player.ant + self.player.cnt + self.player.pos + self.player.tea
        blue = self.player.fir + self.player.mar + self.player.pas + self.player.agg + self.player.cmp + self.player.dec + self.player.str

        return round(
            ((key * 5) + (green * 3) + blue) / 42, 1
        )