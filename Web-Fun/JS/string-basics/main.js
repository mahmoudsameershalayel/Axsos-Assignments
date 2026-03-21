// 1. Remove Blanks
function removeBlanks(str) {
    var strWithoutBlanks = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            strWithoutBlanks += str[i];
        }
    }
    return strWithoutBlanks;
}

console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));


// 2. Get Digits
function getDigits(str) {
    var digits = "";
    for (var i = 0; i < str.length; i++) {
        if (isNaN(str[i])) {
            continue;
        }
        digits += str[i];
    }
    return Number(digits);
}

console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"));

// 3. Acronyms
function acronym(str) {
    var words = str.split(" ");
    var acro = "";
    for (word of words) {
        if(word !== ""){
            acro += word[0];
        }
    }
    return acro.toUpperCase(); 
}

console.log(acronym(" there's no free lunch - gotta pay yer way. "));

// 4. Count Non-Spaces
function countNonSpaces(str) {
    var count = 0;
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            count++;
        }
    }
    return count;   
}
console.log(countNonSpaces("Hello world !"));

// 5. Remove Shorter Strings
function removeShorterStrings(arr, minLength) {
    var newArr = [];
    for(var i = 0; i < arr.length; i++){
        if(arr[i].length >= minLength){
            newArr.push(arr[i]);
        }
    }
    return newArr;
}

console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3));

