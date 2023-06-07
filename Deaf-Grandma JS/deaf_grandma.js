import * as readline from 'node:readline/promises';
import { stdin as input, stdout as output } from 'node:process';

// A readline interface which will prompt for command-line input and return said input.
// Don't worry about how this works right now. Focus on using it to solve the problem.
const rl = readline.createInterface({ input, output });

/**
 * Here is an example of how to get user input from the command line
 * and then do something with it.
 * 
 * We will learn more about `await` (and promises in JS) later. For now, use this guide code
 * to solve the problem.
 * 
 * Guide code borrowed from: https://nodejs.org/api/readline.html#readline
 */
// TODO: Once your program is working, comment this "guide code" out or delete it.
// let userInput = await rl.question('What do you think of Node.js? ');
// console.log(`Thank you for your valuable feedback: ${userInput}`);
// userInput = await rl.question(`Why do you think Node.js ${userInput}?`)


// TODO: Using the above code as a reference and a guide, implement the deaf grandma problem!
let goodbyeCount = 0
let goodbyeStr = 'GOODBYE!'
let grandChildInput = await rl.question('HEY, KID!\n');

let lowerCaseRegex = /[a-z]/


while (goodbyeCount < 2){
    if (grandChildInput == ''){
        grandChildInput = await rl.question('WHAT?\n')
    } else if (goodbyeCount === 0 && grandChildInput === goodbyeStr){
        goodbyeCount = 1
        grandChildInput = await rl.question('LEAVING SO SOON?\n')
    } else if (goodbyeCount === 1 && grandChildInput === goodbyeStr){
        console.log('LATER, SKATER!\n')
        goodbyeCount = 2
    } else if (lowerCaseRegex.test(grandChildInput)){
        grandChildInput = await rl.question('SPEAK UP, KID!\n')
    } else if (!lowerCaseRegex.test(grandChildInput)) {
        grandChildInput = await rl.question('NO, NOT SINCE 1946!\n')
    }
}

rl.close()





