exports.calculateMode = function(inputList) {
    // Object to keep track of frequency
    let mostFreqObj = {};
    // Intialize a counter to keep track of highest value
    let mostFreqCounter = 0;
    // Initializae an answer array
    let answerArr = [];

    // Iterate through list and add items to object
    for (let elem of inputList) {
        if (mostFreqObj[elem]) {
            mostFreqObj[elem]++;
        } else {
            mostFreqObj[elem] = 1;
        }
    }

    // find the highest value in the object
    for (let elem in mostFreqObj) {
        if (mostFreqObj[elem] > mostFreqCounter) {
            mostFreqCounter = mostFreqObj[elem];
        }
    }

    // Add all elements that have the highest value to the answer array
    for (let elem in mostFreqObj) {
        if (mostFreqObj[elem] === mostFreqCounter) {
            answerArr.push(elem);
        }
    }
    
    return answerArr;

}
