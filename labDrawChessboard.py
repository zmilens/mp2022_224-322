import string
string.ascii_uppercase

whiteRect = "██"
blackRect = "  "
library = string.ascii_uppercase

linesCount = int(input('Количество строк: '))

lines = []

def fillSymbolLine():
    line = [' ']
    for symbol in [*library[0:linesCount]]:
        line.append(symbol+' ')
    line.append(' ')
    lines.append(line)

fillSymbolLine()

for lineNum in range(linesCount):
    line = [lineNum+1]
    for index in range(linesCount):
        if (lineNum % 2 == 0 and index % 2 == 0 or lineNum % 2 == 1 and index % 2 == 1):
            line.append(whiteRect)
        else:
            line.append(blackRect)
    line.append(lineNum+1)
    lines.append(line)

fillSymbolLine()

for line in lines:
    for char in line:
        print(char, end="")
    print()