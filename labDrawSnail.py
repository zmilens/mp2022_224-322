char = '█'
empty = " "
w = int(input("Ширина? "))
h = int(input("Высота? "))



for r in range(h):
    print(char * w)
    w-=1
    print(empty * w + char)
    if r % 4 == 0: 
        print(char * (w-2))



