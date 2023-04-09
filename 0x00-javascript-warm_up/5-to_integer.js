#!/usr/bin/node
// const num will covert arg through math/floor obj/method
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
