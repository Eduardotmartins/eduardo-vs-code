while True:
    blocks = int(input("Height: "))
    if blocks > 0 and blocks < 9:
        break

for i in range(0, blocks, 1):
    for j in range(0, blocks+i+3, 1):
        if (j==blocks or j==blocks+1 or i+j<blocks-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()