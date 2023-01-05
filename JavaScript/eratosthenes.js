const eratosthenes = (n) => {
    const primes = new Array(n + 1).fill(true)
    primes[0] = primes[1] = false
    for (let i = 2; i <= Math.sqrt(n); i++) {
       for (let j = 2; i * j <= n; j++) {
           primes[i * j] = false
       }
    }
    return primes.reduce((acc, val, ind) => {
       if(val){
          return acc.concat(ind);
       }else{
          return acc;
       }
    },[])
 }

 console.log(eratosthenes(2000000))