#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<openssl/md5.h>

#define MAX_PASSWORD_LENGTH 128

void compute_md5_hash(const char *password, char *output_hash) {
    unsigned char hash[MAX_PASSWORD_LENGTH];
    MD5((unsigned char*) password, strlen(password), hash);

    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        sprintf(output_hash + (i * 2), "%02x", hash[i]);
    }
}

int main() {
    FILE *wordlist, *hash_table;

    char password[MAX_PASSWORD_LENGTH];
    // Each byte is 2 hex characters + null terminator
    char hash[MD%_DIGEST_LENGTH * 2 + 1];

    //open wordlist file
    wordlist = fopen("wordlist.txt", "r");
    if (wordlist == NULL) {
        perror("Error opening wordlist file");
        return 1;
    }

    //open hash table output file
    hash_table = fopen("hash_table.txt", "w");
    if(hash_table == NULL) {
        perror("Error opening hash table file");
        fclose(wordlist);
        return 1;
    }

    printf("Generating precomputed hashed...\n");

    // read passwords from wordlists and compute hash
    while(fgets(password, MAX_PASSWORD_LENGTH, wordlist)) {
        //remove newline char from password
        password[strcspn(password, "\n")] = '\0';

        compute_md5_hash(password, hash);

        fprintf(hash_table, "%s %s\n", password, hash);
    }

    printf("Precomputed hashed saved to hash_table.txt\n");

    fclose(wordlist);
    fclose(hash_table);

    return 0;


}

