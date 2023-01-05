// Basic recursive factorial function //

function factorial(x) {
    return x === 0 ? 1 : x * factorial(x - 1)
}

console.log(factorial(5))

export default factorial