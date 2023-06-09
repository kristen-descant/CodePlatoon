exports.palindrome = function(word) {
    // Create a regex to test each charcter. 
    // The character should only match letters and numbers.
    let edgeRegex = /\w/;
    // Split the word into an array
    let wordArr = String(word).split('');
    // Filter characters to eliminate any that don't pass regex
    wordArr = wordArr.filter(x => edgeRegex.test(x));
    // Create array to store reversed characters
    let reverseWordArr = [];
    // For loop adds characters to the front of array
    for (char of wordArr) {
        reverseWordArr.unshift(char);
    }
    // compare the two arrays
    if (wordArr.join('').toLowerCase() === reverseWordArr.join('').toLowerCase()) {
        return true;
    }

    return false;
};
