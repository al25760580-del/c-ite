/*
 * File: codigo.c
 * Author: 25760580
 * Description: Reads four integer values and prints them in reverse order.
 * Purpose: Practice input, output, variables, and sequential execution.
 */

#include <stdio.h>

int main(void)
{
    /* Declare the four input values */
    int A, B, C, D;

    /* Read the values in their original order */
    printf("Enter four integers separated by spaces: ");
    scanf("%d %d %d %d", &A, &B, &C, &D);

    /* Print the values in reverse order */
    printf("Reversed order: %d %d %d %d\n", D, C, B, A);

    return 0;
}
