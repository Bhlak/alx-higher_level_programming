#include "lists.h"

/**
 * *insert_node - Inserts a node into a sorted linked list
 *
 * @head: Head node of linked list
 *
 * @number: Value of node
 *
 * Return: Address of the new node (On Success)
 *         Null (On Failure)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *temp, *current;

	temp = malloc(sizeof(listint_t));
	if (!temp || !number)
		return (NULL);

	temp->n = number;
	temp->next = NULL;

	if (!(*head))
	{
		(*head) = temp;
		return (*head);
	}
	else
	{
		current = (*head);
		if (current->n > number)
		{
			temp->next = current;
			*head = temp;
			return (temp);
		}
		while (current->next)
		{
			prev = current;
			current = current->next;
			if (prev->n <= number && current->n > number)
			{
				prev->next = temp;
				temp->next = current;
				return (temp);
			}
		}
		current->next = temp;
		return (temp);
	}
}
