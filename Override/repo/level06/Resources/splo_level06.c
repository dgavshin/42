#include <string.h>
#include <stdio.h>
#include <fcntl.h>

int auth(char *login, int serial)
{
  int result; // eax
  int i; // [esp+14h] [ebp-14h]
  int v4; // [esp+18h] [ebp-10h]
  int login_len; // [esp+1Ch] [ebp-Ch]

  login[strcspn(login, "\n")] = 0;
  login_len = strnlen(login, 32);
  if ( login_len <= 5 )
    return 1;
  else
  {
    v4 = (login[3] ^ 0x1337) + 0x5EEDED;
    for ( i = 0; i < login_len; ++i )
    {
      if ( login[i] <= 31 )
        return 1;
      v4 += (v4 ^ (unsigned int)login[i]) % 0x539;
    }
    printf("expected: %d\n", v4);
    result = serial != v4;
  }
  return result;
}

int main() {
	auth(strdup("aaaaaa"), 222);
}
