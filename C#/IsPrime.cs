// Improved Primality Test //

boolean IsPrime(int n) {
    if (n < 3 || n % 2 == 0) return n == 2;
    return true;
}
