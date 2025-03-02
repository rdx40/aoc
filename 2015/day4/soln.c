#include <stdio.h>
#include <string.h>
#include <openssl/md5.h>

// Function to compute the MD5 hash
void compute_md5(const char *input, unsigned char *output) {
    MD5_CTX md5_ctx;
    MD5_Init(&md5_ctx);
    MD5_Update(&md5_ctx, input, strlen(input));
    MD5_Final(output, &md5_ctx);
}

// Function to check if the hash starts with a specified number of zeroes
int hash_starts_with_zeroes(unsigned char *hash, int leading_zeroes) {
    char hex[33];
    for (int i = 0; i < 16; i++) {
        snprintf(&hex[i * 2], 3, "%02x", hash[i]);
    }
    // Check the first 'leading_zeroes' characters to see if they are all '0'
    for (int i = 0; i < leading_zeroes; i++) {
        if (hex[i] != '0') {
            return 0; // Not enough leading zeroes
        }
    }
    return 1; // Hash starts with the required number of zeroes
}

// Function to mine the advent coin with a given number of leading zeroes
long mine_adventcoin(const char *secret_key, int leading_zeroes) {
    unsigned char hash[MD5_DIGEST_LENGTH];
    char input[1024];
    long n = 1;

    while (1) {
        snprintf(input, sizeof(input), "%s%ld", secret_key, n); // Concatenate secret_key and number
        compute_md5(input, hash);

        if (hash_starts_with_zeroes(hash, leading_zeroes)) {
            return n; // Found the correct number
        }

        n++;
    }
}

int main() {
    const char *secret_key = "ckczppom";  // Secret key from the puzzle

    // Find the number that produces a hash with 5 leading zeroes
    long result_5_zeroes = mine_adventcoin(secret_key, 5);
    printf("The lowest number with 5 leading zeroes is: %ld\n", result_5_zeroes);

    // Find the number that produces a hash with 6 leading zeroes
    long result_6_zeroes = mine_adventcoin(secret_key, 6);
    printf("The lowest number with 6 leading zeroes is: %ld\n", result_6_zeroes);

    return 0;
}

