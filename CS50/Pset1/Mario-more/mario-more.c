#include <stdio.h>
#include <cs50.h>

int main(void)
{   //using names to be more easy
    int height, row, collumn, space;
    do
    {
    height = get_int("Enter height here: ");
    }
    while(height < 1 || height > 8);

    for (row = 0; row < height; row++)
    {
        for (space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        for(collumn = 0; collumn <= row; collumn++)
        {
            printf("#");
        }
        printf("  ");
        for (collumn = 0; collumn <= row; collumn++)
        {
            printf("#");
        }
        printf("\n");
    }
}