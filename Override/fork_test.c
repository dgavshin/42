#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>


int main() {

	int p = fork();

	if (p == 0) {
		wait()
		printf("It's the fork!\n");
	}
	else if (p > 0)
	{
	       printf("It's the parent process.. \n");	
	}
	
}
