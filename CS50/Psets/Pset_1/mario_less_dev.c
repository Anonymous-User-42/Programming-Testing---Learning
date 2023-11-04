

#include <stdio.h>
#include <cs50.h>

int input(void);
void output(int input);

int main(void)
{
    int i = input();
    output(i);
}

int input(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    } while (!(h > 0 && h < 9));
    return h;
}

void output(int input)
{
    for (int i = 0; i < input; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

