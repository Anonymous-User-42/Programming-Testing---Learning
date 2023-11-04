//  Population Growth

#include <stdio.h>
#include <cs50.h>

int initial(void);
int final(int start_size);
int years(int start_size, int end_size);

int main(void)
{
    int i = initial();
    int j = final(i);
    int k = years(i, j);
    printf("The number of years is %i\n", k);
}

int initial(void)
{
    int start_size;
    do
    {
        start_size = get_int("What is the Initial Population? ");
    } while (start_size <= 9);
    printf("\n");
    return start_size;
}

int final(int start_size)
{
    int end_size;
    do
    {
        end_size = get_int("What is the Final Population? ");
    } while (start_size > end_size);
    printf("\n");
    return end_size;
}

int years(int start_size, int end_size)
{
    int time;
    int rate = start_size / 12;
    time = (end_size - start_size) / (rate);
    return time;
}
