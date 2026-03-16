// 1. Display odd numbers
for (let i = 1; i <= 20; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}

// 2. Decreasing multiples of 3
for (let i = 100; i >= 0; i--) {
    if (i % 3 === 0) {
        console.log(i);
    }   
}
// 3. Print the given sequence
for (let i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
}

// 4. Sigma
let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum += i;
}
console.log(sum);

// 5. Factorial 
let product = 1;

for (let i = 1; i <= 12; i++) {
    product = product * i;
}

console.log(product);