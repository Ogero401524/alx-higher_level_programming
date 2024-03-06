#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @head: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *head)
{
	listint_t *turtle = head;	// 'turtle' moves one node at a time
	listint_t *hare = head;		// 'hare' moves two nodes at a time

	if (!head)
		return (0);

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);	//yes
	}

	return (0);	// No
}
