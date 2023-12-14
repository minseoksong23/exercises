//ex 7.9; two implementations of isupper 1) save space 2) save time

//save space
int isupper(int c) {
    return c >= 'A' && c <= 'Z';
}

//save time
static const char upper_table[256] = {
    0, 0, ..., 0,  // 0-64 not uppercase
    1, 1, ..., 1,  // 'A'-'Z' are uppercase
    0, 0, ..., 0   // 91-255 not uppercase
};

int isupper(int c) {
    return upper_table[(unsigned char)c];
}
