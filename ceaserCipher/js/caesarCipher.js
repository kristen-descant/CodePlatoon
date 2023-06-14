exports.caesarCipher = function(string, shift_amount) {
    let answerStr = '';

    for (let letter of string) {
        let asciiValue = letter.charCodeAt(0);
        
        if (asciiValue < 65 || (asciiValue > 90 && asciiValue < 97) || asciiValue > 122) {
            answerStr += String.fromCharCode(asciiValue);
        } else if (asciiValue >= 65 && asciiValue <= 90 && asciiValue + shift_amount > 90) {
            asciiValue = asciiValue + shift_amount - 26;
            answerStr += String.fromCharCode(asciiValue);
        } else if (asciiValue >= 65 && asciiValue <= 90 && asciiValue + shift_amount < 65) {
            asciiValue = asciiValue + shift_amount + 26;
            answerStr += String.fromCharCode(asciiValue);
        } else if (asciiValue >= 97 && asciiValue <= 122 && asciiValue + shift_amount > 122) {
            asciiValue = asciiValue + shift_amount - 26;
            answerStr += String.fromCharCode(asciiValue);
        } else if (asciiValue >= 97 && asciiValue <= 122 && asciiValue + shift_amount < 97) {
            asciiValue = asciiValue + shift_amount + 26;
            answerStr += String.fromCharCode(asciiValue);
        } else {
            asciiValue = asciiValue + shift_amount
            answerStr += String.fromCharCode(asciiValue);
        }

    }

    return answerStr
};
