/*
 * File: codigo.c
 * Author: 25760580
 * Description: Adds two times written in HH:MM:SS format.
 * Purpose: Practice sequential structures, integer division, and modulo.
 */

#include <stdio.h>

int main(void)
{
    /* Declare the components of the two input times */
    int h1, m1, s1;
    int h2, m2, s2;

    /* Declare variables for totals, carries, and final values */
    int totalSeconds;
    int carriedMinutes;
    int finalSeconds;
    int totalMinutes;
    int carriedHours;
    int finalMinutes;
    int finalHours;

    /* Read the first time */
    printf("Enter the first time (HH:MM:SS): ");
    scanf("%d:%d:%d", &h1, &m1, &s1);

    /* Read the second time */
    printf("Enter the second time (HH:MM:SS): ");
    scanf("%d:%d:%d", &h2, &m2, &s2);

    /* Add seconds and carry complete minutes */
    totalSeconds = s1 + s2;
    carriedMinutes = totalSeconds / 60;
    finalSeconds = totalSeconds % 60;

    /* Add minutes and carry complete hours */
    totalMinutes = m1 + m2 + carriedMinutes;
    carriedHours = totalMinutes / 60;
    finalMinutes = totalMinutes % 60;

    /* Add hours and the carried hours */
    finalHours = h1 + h2 + carriedHours;

    /* Display the result with two digits for minutes and seconds */
    printf("Sum: %d:%02d:%02d\n", finalHours, finalMinutes, finalSeconds);

    return 0;
}
