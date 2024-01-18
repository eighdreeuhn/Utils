const fibos = [0, 1]

function fibonacci(n) {
    if (fibos.length >= n) return fibos[n]
    while (fibos.length <= n) {
        fibos.push(fibos[fibos.length - 1] + fibos[fibos.length - 2])
    }
    return fibos[n]
}

console.log(fibonacci(3))
console.log(fibos)
console.log(fibonacci(73))
console.log(fibos)
console.log(fibonacci(53))