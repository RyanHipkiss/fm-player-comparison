from classes.Player import Player

class SVA:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.wor + self.player.sta + self.player.acc + self.player.pac
        green = self.player.fin + self.player.lon + self.player.pas + self.player.tck + self.player.ant + self.player.otb + self.player.pos
        blue = self.player.fir + self.player.mar + self.player.cmp + self.player.cnt + self.player.dec + self.player.bal

        return round(
            ((key * 5) + (green * 3) + blue) / 47, 1
        )