#!/usr/bin/node
function add (a, b) {
  const ab = a + b;
  console.log(ab);
}

add(Number(process.argv[2]), Number(process.argv[3]));
