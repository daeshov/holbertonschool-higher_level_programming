#!/usr/bin/node

const url = process.argv[2];
const filepath = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filepath, body, 'utf-8');
  }
});
