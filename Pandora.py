class Pandora:
    def __init__(self, stamina, smax):
        self.stamina = stamina
        self.maxStamina = smax
        self.ricompenseStamina = []
        self.ricompenseFrammenti = []
        self.enemies = []
        self.frammenti = 0

    def nemicoSconfitto(self, demone):
        self.enemies.append(demone)
        self.ricompenseStamina[demone.tr] = self.ricompenseStamina[demone.tr] + demone.sr if self.ricompenseStamina[
            demone.tr] else demone.sr

        for i in range(demone.na):
            self.ricompenseFrammenti[i] = self.ricompenseFrammenti + demone.values[i] if self.ricompenseFrammenti[
                i] else demone.values[i]

    def aggPunteggio(self):
        pass