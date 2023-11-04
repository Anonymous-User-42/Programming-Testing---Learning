//  Population Growth

#include <stdio.h>
#include <cs50.h>

int initial(void);
int final(int start_size);
float years(int start_size, int end_size);

int main(void)
{
    int i = initial();
    int j = final(i);
    float k = years(i, j);
    printf("The number of years is %.2f\n", k);
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

float years(int start_size, int end_size)
{
    float time;
    float increase = start_size / 3;
    float decrease = start_size / 4;
    int rate = increase - decrease;
    time = (end_size - start_size) / (rate);
    return time;
}
