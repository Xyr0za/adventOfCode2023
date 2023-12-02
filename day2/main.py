import re


def intC(array):
    return [int(i) if i != "" else 0 for i in array]


class Game:
    def __init__(self, unfstr : str):
        self.unfstr = unfstr
        self.fstr = None
        self.id = None

        self.array = None

        self.rv = None
        self.gv = None
        self.bv = None

        self.mbr = None
        self.mbg = None
        self.mbb = None

    def clean(self):
        array = self.unfstr.replace("Game", "G")
        array = array.replace(";", ":").split(":")
        self.id = int(''.join(re.findall(r'\d+', array[0])))

        self.array = tuple(array[1:])

    def fbounds(self):
        self.rv = intC([''.join(re.findall(r'\d+r', i))[:-1] for i in self.array])
        self.gv = intC([''.join(re.findall(r'\d+g', i))[:-1] for i in self.array])
        self.bv = intC([''.join(re.findall(r'\d+b', i))[:-1] for i in self.array])

        self.mbr = max(self.rv)
        self.mbg = max(self.gv)
        self.mbb = max(self.bv)

    def cbounds(self, rb, gb, bb):
        if (self.mbr > rb) or (self.mbg > gb) or (self.mbb > bb):
            return 0
        return self.id

    def cpower(self):
        return self.mbr * self.mbg * self.mbb


cont = [i.strip().replace(" ", "").replace("Game", "G") for i in open("input.txt", "r").readlines()]
games = [Game(i) for i in cont]

C = 0
P = 0

for g in games:
    g.clean()
    g.fbounds()
    C += g.cbounds(12, 13, 14)
    P += g.cpower()

print(f"First: {C}")
print(f"Second: {P}")
