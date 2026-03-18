let arr2 = [1, 2, 3, 4, 5];
let n = 2;
for (let i = 0; i < 2; i++) {
    let last = arr2.pop();
    arr2.unshift(last);
}
console.log(arr2);