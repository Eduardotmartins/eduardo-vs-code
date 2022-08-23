 
# pergunte ao promp o tamanho da pilha de blocos
while True:
    blocks = int(input("Height: "))
    if blocks > 0 and blocks < 9:
        break

for i in range(0, blocks, 1):
    for j in range(0, blocks, 1):
        if (i+j < blocks-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()