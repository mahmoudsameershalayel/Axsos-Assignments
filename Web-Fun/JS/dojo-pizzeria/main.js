// Create a function called pizzaOven that returns a JavaScript (Pizza) Object
function pizzaOven(crust, sauce, cheeses, toppings) {
    var pizza = {};
    pizza.crust = crust;
    pizza.sauce = sauce;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// Create a pizza with: "deep dish", "traditional", ["mozzarella"], and ["pepperoni", "sausage"]
var p1 = pizzaOven(
    "deep dish",
    "traditional",
    ["mozzarella"],
    ["pepperoni", "sausage"]
);

console.log(p1);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// Create a pizza with: "hand tossed", "marinara", ["mozzarella", "feta"], and ["mushrooms", "olives", "onions"]
var p2 = pizzaOven(
    "hand tossed",
    "marinara",
    ["mozzarella", "feta"],
    ["mushrooms", "olives", "onions"]
);

console.log(p2);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// Create 2 more pizzas with any toppings we like!
var p3 = pizzaOven(
    "thin crust",
    "bbq",
    ["cheddar"],
    ["chicken", "corn"]
);

var p4 = pizzaOven(
    "stuffed crust",
    "alfredo",
    ["mozzarella", "parmesan"],
    ["shrimp", "spinach"]
);

console.log(p3);
console.log(p4);

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// Bonus Challenge: Create a function called randomPizza that uses Math.random() to create a random pizza!
function getRandom(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function randomPizza() {
    var crusts = ["deep dish", "thin", "hand tossed", "stuffed"];
    var sauces = ["traditional", "marinara", "bbq", "alfredo"];
    var cheeses = ["mozzarella", "cheddar", "feta", "parmesan"];
    var toppings = ["pepperoni", "mushrooms", "olives", "onions", "chicken"];


    var pizza = {
        crust: getRandom(crusts),
        sauce: getRandom(sauces),
        cheeses: [getRandom(cheeses)],
        toppings: [getRandom(toppings), getRandom(toppings)]
    };

    return pizza;
}

console.log(randomPizza());