/*
 * File: codigo.c
 * Author: 25760580
 * Description: Calculates VAL from NUM and V using a multiple selection.
 * Purpose: Practice switch, arithmetic expressions, and real output.
 */

#include <stdio.h>
#include <math.h>

int main(void)
{
    /* Declare the option, input value, and result */
    int NUM;
    int V;
    double VAL;

    /* Read the option and the value */
    printf("Enter NUM: ");
    scanf("%d", &NUM);
    printf("Enter V: ");
    scanf("%d", &V);

    /* Select the expression associated with NUM */
    switch (NUM)
    {
        case 1:
            VAL = 100 * V;
            break;
        case 2:
            VAL = pow(100, V);
            break;
        case 3:
            VAL = 100.0 / V;
            break;
        default:
            VAL = 0;
            break;
    }

    /* Display the calculated result */
    printf("VAL = %.2f\n", VAL);

    return 0;
}
