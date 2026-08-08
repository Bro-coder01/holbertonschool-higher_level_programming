#!/usr/bin/node
const num = ParseInt(process.argv[2],10);
if (!num){
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
