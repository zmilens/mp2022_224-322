import random

wallSymbol = "██"
emptySymbol = "  "
optionalWallSymbol = "▦▦"


mapWidth = int(input("Ширина карты: "))
mapHeight = int(input("Высота карты: "))

paintLines = []


def fillWallLine():
    paintLines.append([*(wallSymbol*mapWidth)])

fillWallLine()



for lineNum in range(mapHeight-2):
    line = [ wallSymbol ]
    for index in range(mapWidth-2):
        if ( lineNum % 2 == 0 or lineNum % 2 == 1 and index % 2 == 0 or lineNum == (mapHeight-3) or index == (mapWidth-3) ):
            if ( ( random.randint(0, 10) < 2 ) ):
                line.append(optionalWallSymbol)
            else:
                line.append(emptySymbol)
        else:
            line.append(wallSymbol)
    line.append(wallSymbol)
    paintLines.append(line)


fillWallLine()


for line in paintLines:
    for char in line:
        print(char, end="")
    print()