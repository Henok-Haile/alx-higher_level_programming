#include "lists.h"

/**
 * check_cycle - checks if there is a loop
 * @list: lists
 * Return: 1 if there is cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *Ntrav = list;
	listint_t *Dtrav = list;

	while (Ntrav && Dtrav && Dtrav->next)
	{
		Ntrav = Ntrav->next;
		Dtrav = Dtrav->next->next;

		if (Ntrav == Dtrav)
		{
			return (1);
		}
	}

	return (0);
}
