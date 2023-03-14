#!/usr/bin/node
const tmp = process.argv[2];
if (!tmp) {
  console.log("No argument");
} else {
  console.log(tmp);
}
