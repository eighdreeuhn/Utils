// Transpose a 2d array //

function transpose(m) {
    return [...Array(m[0].length)].map((_,i) => [...Array(m.length)].map((__,j)=> m[j][i]))
}

const mat = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
console.log(transpose(mat))