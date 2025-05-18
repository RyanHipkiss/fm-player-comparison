from classes.Player import Player

class AMA:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
       key = self.player.acc + self.player.pac + self.player.sta + self.player.wor
       green = self.player.fir + self.player.pas + self.player.tec + self.player.cmp + self.player.dec + self.player.otb + self.player.tea + self.player.vis
       blue = self.player.dri + self.player.ant + self.player.fla + self.player.agi

       return round(
           (
            (
                (key * 5) + (green * 3) + blue
            )
           ) / 48,
           1
       )