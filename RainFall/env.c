#include <stdlib.h>
#include <stdio.h>

int main()
{
	void (*f)();
	f = getenv("shellcode");
	f += 1;
	f -= 1;
	f();
}
