class Pandora:
    def __init__(self, stamina, smax):
        self.stamina = stamina
        self.maxStamina = smax
        self.ricompenseStamina = []
        self.ricompenseFrammenti = []
        self.frammenti = 0

    def nemicoSconfitto(self, demone):
        if demone.tr<len(self.ricompenseStamina):
            self.ricompenseStamina[demone.tr-1] = self.ricompenseStamina[demone.tr-1] + demone.sr if self.ricompenseStamina[
                demone.tr-1] else demone.sr
        else:
            for _ in range(demone.tr-len(self.ricompenseStamina)):
                self.ricompenseStamina.append(0)
            self.ricompenseStamina[demone.tr - 1] = self.ricompenseStamina[demone.tr - 1] + demone.sr if self.ricompenseStamina[demone.tr - 1] else demone.sr

        if len(self.ricompenseFrammenti)>demone.na:
            for _ in range(demone.na-len(self.ricompenseFrammenti)):
                self.ricompenseFrammenti.append(0)
        for i in range(demone.na):
            self.ricompenseFrammenti[i] = self.ricompenseFrammenti + demone.values[i] if self.ricompenseFrammenti[
                i] else demone.values[i]

    def aggPunteggio(self):
        self.frammenti += self.ricompenseFrammenti.pop(0) if self.ricompenseFrammenti[0] else self.frammenti

    def aggStamina(self):
        pass
