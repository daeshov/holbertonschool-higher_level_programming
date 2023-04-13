#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
// process = node.js exec (0), pth > scrt(1)..
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
