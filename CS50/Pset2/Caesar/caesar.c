#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{   //If any of the characters is not a decimal digit, print the message:
    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key");
            return 1;
        }
    }
        //prompt the user for a string of plaintext (using get_string)
        int k = atoi(argv[1]);

        string plaintext = get_string("Plaintext:  ");
        printf("ciphertext: ");
        //using the same code of scrabble in my git
        for (int j = 0; j < strlen(plaintext); j++)
        {
            if (isupper(plaintext[j]))
            {
                printf("%c", (plaintext[j] - 65 + k) % 26 + 65);
            }

            else if (islower(plaintext[j]))
            {
                printf("%c", (plaintext[j]- 97 + k) % 26 + 97);
            }

            else
            {
                printf("%c", plaintext[j]);
            }
        }
        printf("\n");
}