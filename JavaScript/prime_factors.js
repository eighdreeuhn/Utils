function primeFactors(n) {
    const factors = {}
    let   divisor = 2

    while (divisor <= n) {
      while (n % divisor == 0) {
        if (divisor in factors) {
            factors[divisor]++
            n /= divisor
        } else {
            factors[divisor] = 1
            n /= divisor
        }
    }
    divisor++
    }
    return factors
  }

  console.log(primeFactors(76))
  