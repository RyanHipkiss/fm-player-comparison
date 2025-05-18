from classes.Player import Player

class SKS:
    player: Player = None

    def __init__(self, player):
        self.player = player

    def getScore(self):
        key = self.player.agi + self.player.ref
        green = self.player.cmd + self.player.kic + self.player.one_v_one + self.player.ant + self.player.cnt + self.player.pos
        blue = self.player.aer + self.player.fir + self.player.han + self.player.pas + self.player.tro + self.player.dec + self.player.vis + self.player.acc

        score = ((key * 5) + (green * 3) + blue) / 36
        return round(score, 1)