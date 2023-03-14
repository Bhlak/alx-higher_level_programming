#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv
    .splice(2)
    .map((e) => parseInt(e, 10))
    .sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
