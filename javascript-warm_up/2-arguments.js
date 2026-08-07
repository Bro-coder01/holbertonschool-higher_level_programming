#!/usr/bin/node
let long = process.argv.length - 2;
if (long === 0) {
  console.log('No argument');
} else if (long > 1) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}