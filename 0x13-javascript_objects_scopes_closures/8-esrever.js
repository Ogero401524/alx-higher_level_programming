#!/usr/bin/node
exports.esrever = function (list) {
  let lent = list.length - 1;
  let j = 0;
  while ((lent - j) > 0) {
    const a = list[lent];
    list[lent] = list[j];
    list[j] = a;
    j++;
    lent--;
  }
  return list;
};
