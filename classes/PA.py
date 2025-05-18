from classes.Player import Player

class PA:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.acc + self.player.pac + self.player.fin
        green = self.player.ant + self.player.cmp + self.player.otb
        blue = self.player.fir + self.player.hea + self.player.tec + self.player.dec

        score = ((key * 5) + (green * 3) + blue) / 28
        return round(score, 1)