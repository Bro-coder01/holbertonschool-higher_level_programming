#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
let x, row;
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (x = 0, row = ''; x < size; x++, row += 'X');
  for (x = 0; x < size; x++) {
    console.log(row);
}
}
