#include <string.h>
#include <stdio.h>

int win() {
	printf("win\n");
}

int main() {
	char buf[20];

	gets(buf);
	return 1;
}
