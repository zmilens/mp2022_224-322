# def colors_256(color_):
#     num1 = str(color_) 
#     num2 = str(color_).ljust(3, ' ')
#     if color_ % 16 == 0:
#         return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
#     else:
#         return(f"\033[38;5;{num1}m {num2} \033[0;0m")

# print(' '.join([colors_256(x) for x in range(256)]))

colors = list(range(0, 256))

for color in colors:
    print("\033[48;5;{0}m Text \033[0m".format(color), end=" ")