from classes.Player import Player

class CFS:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.acc + self.player.pac + self.player.fin
        green = self.player.dri + self.player.fir + self.player.hea + self.player.tec + self.player.ant + self.player.cmp + self.player.otb + self.player.agi + self.player.str
        blue = self.player.lon + self.player.pas + self.player.dec + self.player.tea + self.player.vis + self.player.wor + self.player.bal + self.player.jum + self.player.sta

        return round(
            (
            (
            (key * 5) + (green * 3) + blue
            ) / 51
            ),
            1
        )