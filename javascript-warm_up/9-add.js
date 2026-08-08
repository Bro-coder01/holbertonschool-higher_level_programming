#!/usr/bin/node
let v1 = parseInt(process.argv[2], 10), v2 = parseInt(process.argv[3], 10);
function add(a, b) {
    return a + b;
}

if (isNaN(v1) || isNaN(v2)) {
  console.log('Invalid input');
} else {
console.log(add(a = v1, b = v2));
  }
  