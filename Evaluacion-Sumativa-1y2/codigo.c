/*
 * File: codigo.c
 * Author: 25760580
 * Description: Calculates fuel usage and total cost from distance,
 *              fuel efficiency, and price.
 * Purpose: Practice sequential input, arithmetic expressions, and output.
 */

#include <stdio.h>

int main(void)
{
    /* Declare input values and calculated results */
    int D;
    int R;
    int P;
    int LITROS;
    int COSTO;

    /* Read the distance */
    printf("Enter distance\n");
    scanf("%d", &D);

    /* Read the fuel efficiency */
    printf("Enter efficiency\n");
    scanf("%d", &R);

    /* Read the fuel price */
    printf("Enter price\n");
    scanf("%d", &P);

    /* Calculate the liters used and the total cost */
    LITROS = D / R;
    COSTO = LITROS * P;

    /* Display both results in one output section */
    printf("Liters used\n%d\nTotal cost\n%d\n", LITROS, COSTO);

    return 0;
}
