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

const sudoku = [[1,1,1,1,1,1,1,1,1],
[2,2,2,2,2,2,2,2,2],
[3,3,3,3,3,3,3,3,3],
[4,4,4,4,4,4,4,4,4],
[5,5,5,5,5,5,5,5,5],
[6,6,6,6,6,6,6,6,6],
[7,7,7,7,7,7,7,7,7],
[8,8,8,8,8,8,8,8,8],
[9,9,9,9,9,9,9,9,9]]
console.log(transpose(sudoku))
console.log(transpose(mat))
