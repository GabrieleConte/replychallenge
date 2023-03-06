class Pandora:
    def __init__(self, stamina, smax):
        self.stamina = stamina
        self.maxStamina = smax
        self.ricompenseStamina = [0]
        self.ricompenseFrammenti = [0]
        self.frammenti = 0

    def nemicoSconfitto(self, demone):
        if demone.tr < len(self.ricompenseStamina):
            self.ricompenseStamina[demone.tr - 1] = self.ricompenseStamina[demone.tr - 1] + demone.sr if \
            self.ricompenseStamina[
                demone.tr - 1] else demone.sr
        else:
            for _ in range(demone.tr - len(self.ricompenseStamina)):
                self.ricompenseStamina.append(0)
            self.ricompenseStamina[demone.tr - 1] = self.ricompenseStamina[demone.tr - 1] + demone.sr if \
            self.ricompenseStamina[demone.tr - 1] else demone.sr

        if len(self.ricompenseFrammenti) < demone.na:
            for _ in range(demone.na - len(self.ricompenseFrammenti)):
                self.ricompenseFrammenti.append(0)
        for i in range(demone.na):
            self.ricompenseFrammenti[i] = self.ricompenseFrammenti[i] + demone.values[i] if self.ricompenseFrammenti[
                i] else demone.values[i]
        self.stamina -= demone.sc

    def aggPunteggio(self):
        self.frammenti = self.frammenti + self.ricompenseFrammenti.pop() if self.ricompenseFrammenti[
            0] else self.frammenti

    def aggStamina(self):
        print(self.ricompenseStamina)
        self.stamina = self.stamina + self.ricompenseStamina.pop() if self.ricompenseStamina[0] else self.stamina
        if self.stamina > self.maxStamina:
            self.stamina = self.maxStamina
