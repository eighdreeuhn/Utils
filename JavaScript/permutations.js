//--- Generates all permutations of an array with duplicates ---//


function permutations(a) {
    const res = []
    function permute(arr, memo=[]) {
      for (let i = 0; i < arr.length; i++) {
        const cur = arr.splice(i,1)
        if (!arr.length) res.push(memo.concat(cur))
        permute([...arr], memo.concat(cur))
        arr.splice(i, 0, cur[0])
      }
      return res
    }
    return permute(a)
  }

  const array = [1,2,3]
  console.dir(permutations(array))