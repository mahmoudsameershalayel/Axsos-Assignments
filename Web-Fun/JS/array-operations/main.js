

// 1. Accessing Elements
let colors = ["red", "blue", "green", "yellow", "purple"];

// Print the first and last elements of the array
var firstElement = colors[0];
var lastElement = colors[colors.length - 1];

console.log("First element:", firstElement);
console.log("Last element:", lastElement);

// Print the element at the second position.
var secondElement = colors[1];
console.log("Second element:", secondElement);

// Update the third element to orange and print the updated array
colors[2] = "orange";
console.log("Updated array:", colors);


// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 2. Traversing an Array
let numbers = [10, 20, 30, 40, 50];

// a. write a program to print each element using a for loop.
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i])
}

// b. Write a for loop to print the elements in reverse order.
for(var i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 3. Searching in an Array
let numbers2 = [5, 10, 15, 20, 25];

var isExist = false;
for (let i = 0; i < numbers2.length; i++) {
    if(numbers2[i] === 25) {
        console.log("Element found at index:", i);
        isExist = true;
        break;
    }
}

if(isExist === false)
{
    console.log("Not Found");
}

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 4. Sorting an Array
let scores = [50, 20, 70, 10, 40];

var ascendingOrder = scores.sort((a,b) => a - b);
console.log("Ascending order:", ascendingOrder);

var descendingOrder = scores.sort((a,b) => b - a);
console.log("Descending order:", descendingOrder);

let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
var alphabeticalOrder = names.sort();
console.log("Alphabetical order:", alphabeticalOrder);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 5. Inserting Elements
let animals = ["dog", "cat", "rabbit"];
animals.push("elephant");
animals.unshift("lion");
animals.splice(2, 0, "tiger");
console.log("Updated array:", animals);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 6. Deleting Elements
let fruits = ["apple", "banana", "cherry", "date"];
fruits.shift(); 
fruits.pop(); 
fruits.splice(0, 1);
console.log("Updated array:", fruits);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 7. Combining Arrays
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let combinedArray = array1.concat(array2);
console.log("Combined array:", combinedArray);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 8. Splitting an Array
let items = ["a", "b", "c", "d", "e"];
let firstPart = items.slice(0, 3);
let secondPart = items.slice(3);
console.log("First part:", firstPart);
console.log("Second part:", secondPart)

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 9. Filtering Elements
let numbers3 = [1, 5, 10, 15, 20, 25, 30];
let filteredNumbers = numbers3.filter(num => num > 15);
console.log("Filtered numbers:", filteredNumbers);  

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 10. Advanced Challenge

let arr = [1, 2, 2, 3, 4, 4, 5];
let uniqueArray = arr.filter((value, index, self) => 
    { return self.indexOf(value) === index; }
);
console.log("Unique array:", uniqueArray);

let arr2 = [1, 2, 3, 4, 5];
let n = 2;
for (let i = 0; i < 2; i++) {
    let last = arr2.pop();
    arr2.unshift(last);
}
console.log(arr2);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
// Bonus Challenge
var firstArray = [1, 3, 5]
var secondArray = [2, 4, 6]

let merged = [];

let i = 0;
let j = 0;

while (i < firstArray.length && j < secondArray.length) {

    if (firstArray[i] < secondArray[j]) {
        merged.push(firstArray[i]);
        i++;
    } else {
        merged.push(secondArray[j]);
        j++;
    }

}

while (i < firstArray.length) {
    merged.push(firstArray[i]);
    i++;
}

while (j < secondArray.length) {
    merged.push(secondArray[j]);
    j++;
}

console.log(merged);