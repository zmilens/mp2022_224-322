char = '██'
w = int(input("Ширина? "))
h = int(input("Высота? "))
f = input("Закрасить? [y/n] ")
repeat = True
is_fill = f.lower() == "y"
char_fill = char if is_fill else " "



# for r in range(h):
#     print(char * w)
def paintRow(fill):
    if (fill):
        print(char * w)
    else:
        print(char + ("  " * (w-2)) + char)
        # print(" " * (w-2))
        # print(char)

while repeat == True:
    for r in range(h):
        paintRow(is_fill or r==(h-1) or r==0)
    exit = input("Повторить? [y/n] ")
    if exit == "n":
        repeat = False
