#include <stdio.h>
#include <stdlib.h>

#include "test.h"

int main(void) {
    // Call functions from the other file
    int result = has_odd_number_of_bits_set(5);
    printf("(has odd number ) Result: %d\n", result); // Return 1 (True)

    int result2 = turn_k_bit_on(5,2); // Return 13
    printf("(turn k bit on) Result: %d\n", result2);

    int result3 = turn_k_bit_off(5,1);
    printf("(turn_k_bit_off) Result: %d\n", result3);

    int result4 = k_bit_is_on(5,2);
    printf("(k_bit_is_on) Result: %d\n", result4);

    int result5 = toggle_k_bit(5,2);
    printf("(toggle_k_bit) Result: %d\n", result5);

    int result6 = is_palindrome(5);
    printf("palindrom) Result: %d\n", result6);

    int test = testing(5,0); 
    printf("Test: %d\n", test);

    return 0;
}

/*

Qs :




*/


