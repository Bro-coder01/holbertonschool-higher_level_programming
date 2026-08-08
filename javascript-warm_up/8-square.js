#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let x = 0, row = ''; x < size; x++, row += 'X');
  for (x = 0; x < size; x++) {
    console.log(row);
}
}
