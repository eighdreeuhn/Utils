//----- Greatest common divisor -----//

function gcd(x,y) {
    let X = Math.abs(x);
    let Y = Math.abs(y);
  while(Y) {
    let t = Y
    Y = X % Y
    X = t
  }
  return X
}

console.log(gcd(120, 26))
