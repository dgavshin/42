#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	long puts_addr = 456624;

	printf("%#x", &puts - puts_addr);
	return 2;
}

