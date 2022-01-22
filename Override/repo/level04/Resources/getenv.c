#include <stdlib.h>
#include <stdio.h>

/* gcc -m32 env.c */
int main(int argc, char **argv) {
    printf("%p\n", getenv(argv[1]));
}