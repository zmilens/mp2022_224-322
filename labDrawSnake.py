
char = '█'
empty = " "
w = int(input("Ширина? "))
h = int(input("Высота? "))



for r in range(h):
    if r % 2 == 1:
        print(char * w)
    elif r % 4 == 0:
        print(empty * (h-1) + char)
    else:
        print(char + empty)
    

