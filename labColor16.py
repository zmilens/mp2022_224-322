text = list(range(30, 38))
bg = list(range(40, 48))

for color in text:
    print("\033[2;{num}m {num} \033[0;0m".format(num=str(color)), end=' ')
print()    

for color in text:
    for bgcolor in bg:
        print("\033[2;{num};{bg}m {num}:{bg} \033[0;0m".format(num=str(color), bg=str(bgcolor)), end=' ')
    print()

