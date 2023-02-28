from Demon import Demon
from Pandora import Pandora

with open("file.txt") as f:
    frow = f.readline(0).split(" ")
    frow = [eval(i) for i in frow]
    rows = f.readlines()
    game = Pandora(int(frow[0]), int(frow[1]), int(frow[2]), int(frow[3]))
    demons = []
    for i in range(1, len(rows)):
        statsDemone = rows[i].split(" ")
        statsDemone = [eval(i) for i in statsDemone]
        x = []
        for j in range(statsDemone[3]):
            x.append(statsDemone[j + 3])
        demone = Demon(statsDemone[0], statsDemone[1], statsDemone[2], statsDemone[3], x)
        demons.append(demone)
