#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * infinite_while - infinite sleep loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 zombie processes
 *
 * Return: infinite_while zombies
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}

	infinite_while();
	return (EXIT_SUCCESS);
}
