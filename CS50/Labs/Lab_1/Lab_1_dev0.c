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
    printf("Years: %i\n", k);
}

int initial(void)
{
    int start_size;
    do
    {
        start_size = get_int("What is the Initial Population? ");
    } while (start_size < 9);
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
    time = 12 * (end_size - start_size) / ((float) start_size);
    return time;
}
