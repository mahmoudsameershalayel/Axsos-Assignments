// 1. Reverse a String
var name = "Hello";

function reverseString(str){
    var newString = "";
    for(var i = str.length-1 ; i>=0 ; i--){
        newString += str[i];
    }
    return newString;
}

var newString = reverseString(name);

console.log(newString)

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 2. Count Vowels
var vowels = "aeiouAEIOU"

function vowelsCount(str){
    var counter = 0;
    for(var i =0; i<str.length;i++){
        if(vowels.includes(str[i])){
            counter++;
        }
    }
    console.log("The Count of vowels in our string is : " + counter);
}

vowelsCount("hello");

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 3. Check Palindrome
function palindromeCheck(string){
    var revers = reverseString(string);
    return revers === string;
}

var result = palindromeCheck("madam");
console.log(result)

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

// 4. Longest Word in a Sentence
function longestWord(sentance){
    var words = sentance.split(" ");

    var longestWord = "";
    for(word of words){
        if(word.length > longestWord.length){
            longestWord = word;
        }
    }
    return longestWord;
}
console.log(longestWord("I love solving algorithms"))

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

function feedBack(grade){
    var result = "";
    switch(grade){
        case 'A':
            result = "Excellent";
            break;
        case 'B' :
            result = "Good job";
            break;
        case 'C' :
            result = "You passed";
            break;
        case 'D' :
            result = "Need improvement";
            break;
        case 'D' :
            result = "Failed";
            break;
        default:
            result = "Invalid grade";
    }
    return result;
}

console.log(feedBack("A"))

// <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

function charTypesCount(str){
    var vowelsCounter = 0;
    var digitsCounter = 0;
    var spacesCounter = 0;
    var othersCounter = 0;

    for(char of str){
        switch(char){
            case " ":
                spacesCounter++;
                break;
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                vowelsCounter++;
                break;
            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                digitsCounter++;
                break;
            default:
                othersCounter++;
        }
    }

   return  {vowelsCounter : vowelsCounter , DigitsCounter : digitsCounter , SpacesCounter : spacesCounter , OthersCounter : othersCounter };
}

console.log(charTypesCount("Hi 123!"));


