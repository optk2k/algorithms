"use strict";
// обход в глубину
// итеративный подход


let tree =  [1,2,3,4, 5, [34, 55, [123, [1234]], 11, 245], [6,5,4,3,4,56], [1,2,234], 4,5,6];

while (tree.length){
    let element = tree.shift();
    if (element.constructor.name == "Array") {
        tree.unshift(...element);
    } else {
        console.log(element);
    }
}
