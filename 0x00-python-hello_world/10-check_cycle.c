#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @head: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
    listint_t *turtle = list;  // 'turtle' moves one node at a time
    listint_t *hare = list;    // 'hare' moves two nodes at a time

    while (turtle && hare && hare->next)
    {
        turtle = turtle->next;
        hare = hare->next->next;

        if (turtle == hare)
            return (1);  // There is a cycle
    }

    return (0);  // No cycle found
}


int main(void)
{

    listint_t *list = malloc(sizeof(listint_t));
    head->n = 1;

    list->next = malloc(sizeof(listint_t));
    list->next->n = 2;

    list->next->next = malloc(sizeof(listint_t));
    list->next->next->n = 3;

    // Create a cycle
    list->next->next->next = list;

    // Test the function
    int result = check_cycle(list);

    // Output the result
    if (result)
        printf("The linked list has a cycle.\n");
    else
        printf("The linked list does not have a cycle.\n");

    // Clean up memory
    free(list->next->next);
    free(list->next);
    free(list);

    return 0;
}
