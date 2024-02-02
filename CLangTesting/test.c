#include "test.h"

/* Return 0 if the variable has an even number of bits set
 * and 1 if it has an odd number of bits set.
 * Only use: ~ and &
 */
int has_odd_number_of_bits_set(int num) {
    int is_odd_or_even = 0;
    while (num) {
        // Tracking 
        is_odd_or_even += num & 1;
        // Incrementing by shifting bits
        num >>= 1;
    }
    return is_odd_or_even & 1;
}

/* Turn the k bit of n on
 * Only use: | and <<
 */
int turn_k_bit_on(const int n, const int k){
    int result = 1 << k; // Shifts all bits of n, k times to left
    return n | result; // Does turn on the kth but everything else is changed
}

/* Turn k bit of n off
 * Only use: &, ~ and <<
 */
int turn_k_bit_off(const int n, const int k){
    int result = 1 << k;
    return n & ~ result;
}

/* Return true if the k bit of n is on. False otherwise.
 * Only use: & and <<
 */
int k_bit_is_on(const int n, const int k) {
    int temp = 1 << k; // Location of that bit 

    return 0;
}

/* Turn on the k bit of n if it is off or turn it off if it
 * is on.
 * Only use: ^ and <<
 */
int toggle_k_bit(const int n, const int k) {
    return n ^ (1 << k);
}

/* Return 1 if the bit of n are palindrome
 * Only use: <<, |, & and >>
 */
int is_palindrome(const int n) {

    return 1;
}

int testing(int n, int k) {
    return 1 << k;
}