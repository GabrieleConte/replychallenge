from Demon import Demon
from Pandora import Pandora

with open("file.txt") as f:
    frow = f.readline(0).split(" ")
    frow = [eval(i) for i in frow]
    rows = f.readlines()
    pandora = Pandora(frow[0], frow[1])
    turns = frow[2]
    ndemons = frow[3]
    demons = []
    for i in range(1, len(rows)):
        statsDemone = rows[i].split(" ")
        statsDemone = [eval(i) for i in statsDemone]
        x = []
        for j in range(statsDemone[3]):
            x.append(statsDemone[j + 3])
        demone = Demon(statsDemone[0], statsDemone[1], statsDemone[2], statsDemone[3], x)
        demons.append(demone)
    i = 0
    while turns >= 0:
        turns -= 1
        if demons[i].sc > pandora.stamina:
            turns -= 1
            i += 1
        else:
            pass
        ##implementare il modo in cui pandora sceglie i nemici
        # se un nemico non è affrontabile, aspetta un turno
        # se è affrontabile, scala la stamina a pandora e aggiorna le ricompense del demone
        # alla fine di ogni turno aggiungi le ricompense dai vettori di ricompense
        # e aggiorna le ricompense sulla stamina e sui fragments##