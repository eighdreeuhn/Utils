// Imporoved Primality test //

function isPrime(x) {
    if (x < 3 || !(x % 2)) return x === 2
    for (let i = 3; i <= Math.sqrt(x); i += 2) 
        if (!(x % i)) 
            return false
    return true
}
