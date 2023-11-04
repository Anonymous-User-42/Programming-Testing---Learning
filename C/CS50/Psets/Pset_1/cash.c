

#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("How many cents are owed\n");
    } while (cents <= 0);
    
    return cents;
}

int calculate_quarters(int cents)
{
    int quarters;
    if (cents == 100)
    {
        quarters = 4;
    }
    else if (cents >= 75 && cents < 100)
    {
        quarters = 3;
    }
    else if (cents >= 50 && cents < 75)
    {
        quarters = 2;
    }
    else if (cents >= 25 && cents < 50)
    {
        quarters = 1;
    }
    else
    {
        quarters = 0;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes;
    if (cents >= 20 && cents <= 24)
    {
        dimes = 2;
    }
    else if (cents >= 10 && cents < 20)
    {
        dimes = 1;
    }
    else
    {
        dimes = 0;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickles;
    if (cents >= 5 && cents <= 9)
    {
        nickles = 1;
    }
    else
    {
        nickles = 0;
    }
    return nickles;
}

int calculate_pennies(int cents)
{
    int pennies;
    if (cents == 4)
    {
        pennies = 4;
    }
    else if (cents == 3)
    {
        pennies = 3;
    }
    else if (cents == 2)
    {
        pennies = 2;
    }
    else if (cents == 1)
    {
        pennies = 1;
    }
    else
    {
        pennies = 0;
    }
    return pennies;
}


