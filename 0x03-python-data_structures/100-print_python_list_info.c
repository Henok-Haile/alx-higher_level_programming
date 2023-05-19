#include <stdio.h>

/**
 * print_python_list_info - prints python list info
 * @p: pyhton object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	printf("Python Lists are one of 4 built-in data types in Python used to store collections of data");
}

/**
 * main - entry code
 * Return: 0 on success
 */
int main(void)
{
	print_python_list_info();
	return (0);
}
