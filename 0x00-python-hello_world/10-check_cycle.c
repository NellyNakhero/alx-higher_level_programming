#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *s;
  listint_t *m;

  if (list == NULL)
    return (0);
  s = list;
  m = list;
  while (m->next != NULL && m->next->next != NULL)
  {
    s = s->next;
    m = m->next->next;
    if (s == m)
    {
      s = list;
      while (s != m)
      {
        s = s->next;
        m = m->next;
      }
      return (1);
    }
  }
  return (0);
}
