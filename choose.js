import factorial from "./factorial";

function choose(m, k) {
    return factorial(m)/(factorial(k) * factorial(m - k))
}

console.log(choose(10,5))