from classes.Player import Player

class F9S:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.acc + self.player.pac + self.player.fin
        green = self.player.dri + self.player.fir + self.player.pas + self.player.tec + self.player.cmp + self.player.dec + self.player.otb + self.player.vis + self.player.agi
        blue = self.player.ant + self.player.fla + self.player.tea + self.player.bal

        return round(
            ((key * 5) + (green * 3) + blue) / 46, 1
        )