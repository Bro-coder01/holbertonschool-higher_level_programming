#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const mapArgs = args.map(x => parseInt(x, 10));
  const sorted = [...new Set(mapArgs)].sort((a, b) => a - b);

  if (sorted.length < 2) {
    console.log(0);
  } else {
    console.log(sorted[sorted.length - 2]);
  }
}
