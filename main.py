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
    output=[]
    f = open("result.txt", "x")
    while turns > 0:
        pandora.aggPunteggio()
        pandora.aggStamina()
        if pandora.stamina > 0:
            flag = True
            i = 0
            while flag and i < ndemons:
                if demons[i].sc < pandora.stamina and i not in output:
                    flag = False
                    pandora.nemicoSconfitto(demons[i])
                    output.append(i)
                    f.write(f"{i}\n")
                else:
                    i += 1
        turns -= 1
        ##implementare il modo in cui pandora sceglie i nemici
        # se un nemico non è affrontabile, aspetta un turno
        # se è affrontabile, scala la stamina a pandora e aggiorna le ricompense del demone
        # alla fine di ogni turno aggiungi le ricompense dai vettori di ricompense
        # e aggiorna le ricompense sulla stamina e sui fragments##
