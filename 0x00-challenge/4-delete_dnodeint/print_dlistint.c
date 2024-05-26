#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 *
 * @h: pointer to the head of the list
 *
 * Return: The number of element printed
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count;

	count = 0;
	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}