from classes.Player import Player

class WBS:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.acc + self.player.pac + self.player.sta + self.player.wor
        green = self.player.cro + self.player.dri + self.player.mar + self.player.tck + self.player.otb + self.player.tea
        blue = self.player.fir + self.player.pas + self.player.tec + self.player.ant + self.player.cnt + self.player.dec + self.player.pos + self.player.agi + self.player.bal

        score = ((key * 5) + (green * 3) + blue) / 47
        return round(score, 1)