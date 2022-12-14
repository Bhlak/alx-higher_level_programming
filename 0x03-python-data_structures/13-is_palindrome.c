#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: Pointer to head node
 *
 * Return: 0 - Not a palindrome
 *         1 - Palindrome
 */

int is_palindrome(listint_t **head)
{
	int count = 0, i;
	listint_t *curr, *rev, *mid;

	if (*head == NULL || ((*head)->next == NULL))
		return (1);

	curr = *head;
	while (curr)
	{
		count++;
		curr = curr->next;
	}

	curr = *head;
	for (i = 0; i < ((count / 2) - 1); i++)
		curr = curr->next;
	if ((count % 2) == 0 && curr->n != curr->next->n)
		return (0);

	curr = curr->next->next;
	rev = reverse_listint(&curr);
	mid = rev;


	curr = *head;
	while (rev)
	{
		if (curr->n != rev->n)
			return (0);
		curr = curr->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
