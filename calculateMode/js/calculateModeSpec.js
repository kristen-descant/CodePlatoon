var calc = require("./calculateMode");





// Write your own unit tests here!
console.log(calc.calculateMode([1,2,3,3]))         // => [3]
console.log(calc.calculateMode([4.5, 0, 0]))       // => [0]
console.log(calc.calculateMode([1.5, -1, 1, 1.5])) // => [1.5]
console.log(calc.calculateMode([1,1,2,2]))         // => [1,2]
console.log(calc.calculateMode([1,2,3]))          // => [1,2,3], because all occur with equal frequency
console.log(calc.calculateMode(["who", "what", "where", "who"])) // => ["who"]