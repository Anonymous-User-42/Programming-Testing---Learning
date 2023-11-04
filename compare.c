

#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int x = get_int("Enter first value ");
    int y = get_int("Enter second value ");

    if (x < y)
    {
        printf("The first value is smaller than the second value\n");
    }

    else if (x > y)
    {
        printf("The first value is bigger than the secon value\n");
    }

    else
    {
        printf("The first and second values are equal\n");
    }
}

