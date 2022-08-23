#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{   //ask for the promp the text using a string
    string text = get_string("Text: ");

    // denominating what you use in your code
    int letters = 0;
    int words = 0;
    int sentences = 0;

    //calculate the length of a string
    for (int i = 0; i < strlen(text); i++)
    {   //check whether a character is alphabetical
        if (isalpha(text[i]))
        {
            letters++;
        }
        //creating a variable with letters,words and sentences
        else if (text[i] == ' ')
        {
            words++;
        }

        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }

    }   // after all, make this float
    float L = (float)letters / (float)words * 100;
    float S = (float)sentences / (float)words * 100;

    //round a number to the nearest integer
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // print again a variable if
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}
