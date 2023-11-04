

#include <stdio.h>
#include <cs50.h>

string name(void);

int main(void)
{
    string i = name();
    printf("Hello, %s\n", i);
}

string name(void)
{
    string n;
    n = get_string("What's your name? ");
    return n;
}

