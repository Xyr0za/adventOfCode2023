import re


def retrieve(x, y):
    ly, uy = y - 3, y + 4

    return [
        cont[x - 1][ly:uy],
        cont[x][ly:uy],
        cont[x + 1][ly:uy],
    ]


# retrieving Data
cont = [i.strip() for i in open("input.txt", "r").readlines()]

# Locating all the parts, returns a tuple (x, y)
loc = []
for i, v in enumerate(cont):
    for s in re.finditer(r'[-/*#&=%@$+]', cont[i]):
        loc.append((i, int(s.start())))

# Locating numbers
nums = []
for i, v in enumerate(cont):
    for s in re.finditer(r'\d', cont[i]):
        nums.append((i, int(s.start())))

print(nums)

# returning string for regex comparison
for i in loc:
    x = i[0]
    y = i[1]
    print(retrieve(x, y))
    print("")

#      0011100
#      001@100
#      0011100

# ..664..
# ...*...
# 407...5
