#include "lists.h"

/**
 * reverse_listint - reverses the singly linked of listint
 * @head: ponter the head of the list
 * Return: ponter to the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *forw, *prev = NULL;

	while (node)
	{
		forw = node->next;
		node->next = prev;
		prev = node;
		node = forw;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked is palindrome
 * @head: pointer to the head singly linked list
 * Return: 0 if linked list not a palindrome, else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *reversed, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	reversed = reverse_listint(&tmp);
	middle = reversed;

	tmp = *head;
	while (reversed)
	{
		if (tmp->n != reversed->n)
			return (0);
		tmp = tmp->next;
		reversed = reversed->next;
	}
	reverse_listint(&middle);

	return (1);
}
