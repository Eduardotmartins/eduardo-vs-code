#include <cs50.h>
#include <stdio.h>

void print_credit_card_brand(long long credit_card);
bool check_validity(long long credit_card_num);
int find_length(long long n);
bool checksum(long long credit_card);

int main(void)
{
    long long credit_card_num;
    do
    {   //get the number from the promp
        credit_card_num = get_long_long("number: ");
    } while (credit_card_num < 0);

    if (check_validity(credit_card_num))
        print_credit_card_brand(credit_card_num);
    else
        printf("INVALID\n");
}
// check if card is valid about the numbers of companies
bool check_validity(long long credit_card_num)
{   //here i ask for the length of card for each company
    int len = find_length(credit_card_num);
    return (len == 13 || len == 15 || len == 16) && checksum(credit_card_num);
}

int find_length(long long n)
{
    int len;
    for (len = 0; n != 0; n /= 10, len++);
    return len;
}

bool checksum(long long credit_card)
{
    int sum = 0;
    for (int i = 0; credit_card != 0; i++, credit_card /= 10)
    {   // check index number
        if (i % 2 == 0)
            sum += credit_card % 10;
        else
        {
            int digit = 2 * (credit_card % 10);
            sum += digit / 10 + digit % 10;
        }
    }
    return (sum % 10) == 0;
}
// print witch credit card is, validity by line 17
void print_credit_card_brand(long long credit_card)
{
    if ((credit_card >= 34e13 && credit_card < 35e13) || (credit_card >= 37e13 && credit_card < 38e13))
        printf("AMEX\n");
    else if (credit_card >= 51e14 && credit_card < 56e14)
        printf("MASTERCARD\n");
    else if ((credit_card >= 4e12 && credit_card < 5e12) || (credit_card >= 4e15 && credit_card < 5e15))
        printf("VISA\n");
    else
        printf("INVALID\n");
}