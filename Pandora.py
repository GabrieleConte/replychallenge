class Pandora:
    def __init__(self, stamina, smax):
        self.stamina = stamina
        self.maxStamina = smax
        self.ricompenseStamina = [0]
        self.ricompenseFrammenti = [0]
        self.frammenti = 0

    def nemicoSconfitto(self, demone):
        if demone.tr < len(self.ricompenseStamina):
            self.ricompenseStamina[demone.tr] = self.ricompenseStamina[demone.tr] + demone.sr if \
            self.ricompenseStamina[
                demone.tr] else demone.sr
        else:
            for _ in range(demone.tr - len(self.ricompenseStamina)+1):
                self.ricompenseStamina.append(0)
            self.ricompenseStamina[demone.tr] = self.ricompenseStamina[demone.tr] + demone.sr if \
            self.ricompenseStamina[demone.tr] else demone.sr

        if len(self.ricompenseFrammenti) < demone.na:
            for _ in range(demone.na - len(self.ricompenseFrammenti)+1):
                self.ricompenseFrammenti.append(0)
        for i in range(1,demone.na):
            self.ricompenseFrammenti[i] = self.ricompenseFrammenti[i] + demone.values[i] if self.ricompenseFrammenti[
                i] else demone.values[i]
        self.stamina -= demone.sc
        print(self.ricompenseStamina)
        print(self.ricompenseFrammenti)
    def aggPunteggio(self):
        self.frammenti = self.frammenti + self.ricompenseFrammenti.pop(0) if self.ricompenseFrammenti[
            0] is not None else self.frammenti

    def aggStamina(self):
        print(self.ricompenseStamina)
        self.stamina = self.stamina + self.ricompenseStamina.pop(0) if self.ricompenseStamina[0] is not None else self.stamina
        if self.stamina > self.maxStamina:
            self.stamina = self.maxStamina
