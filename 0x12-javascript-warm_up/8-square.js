#!/usr/bin/node

const len = Math.floor(parseInt(process.argv[2]));

if (!Object.is(len, NaN) && process.argv.length > 2) {
  for (let i = 0; i < len; i++) {
    let tmp = '';
    for (let j = 0; j < len; j++) {
      tmp += 'X';
    }
    console.log(tmp);
  }
} else {
  console.log('Missing size');
}
