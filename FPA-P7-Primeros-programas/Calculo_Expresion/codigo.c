/*
 * File: codigo.c
 * Author: 25760580
 * Description: Calculates the expression (A + B) raised to the power 2/3.
 * Purpose: Practice real-valued expressions and the math library.
 */

#include <stdio.h>
#include <math.h>

int main(void)
{
    /* Declare integer inputs and a real result */
    int A, B;
    double RES;

    /* Read the two integer values */
    printf("Enter A and B: ");
    scanf("%d %d", &A, &B);

    /* Calculate the expression using a real exponent */
    RES = pow((double)(A + B), 2.0 / 3.0);

    /* Display the result with two decimal places */
    printf("RES = %.2f\n", RES);

    return 0;
}
