#!/usr/bin/node
function factorialofint (nam) {
  if (nam < 0) {
    return (-1);
  }
  if (nam === 0 || isNaN(nam)) {
    return (1);
  }
  return (nam * factorial(nam - 1));
}

console.log(factorialofint(Number(process.argv[2])));
