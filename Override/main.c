#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>

int main() 
{
	int password;
	int leet = 322424845;
	int b;
	char a;

	srand(time(0));
	printf("> ");
	scanf("%d", &password);
	b = leet - password;
	a = leet - password;
	printf("int - %d\n", b);
	printf("chr - %d\n", a);

}
