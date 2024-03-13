#!/usr/bin/node
const Squareer = require('./5-square');
class Square extends Squareer {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let xs = '';
      for (let j = 0; j < this.width; j++) {
        xs += c;
      }
      console.log(xs);
    }
  }
}
module.exports = Square;
