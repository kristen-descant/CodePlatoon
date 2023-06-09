exports.charCount = function(str) {
    const charObj = {};
    charArr = [];

    for (let char of str){
        if (char === ' ') {
            continue;
        } else if (charObj[char]) {
            charObj[char]++;
        } else {
            charObj[char] = 1;
        }
    }

    for ([key, value] of Object.entries(charObj)) {
        charArr.push([key, value]);
    }
    
    charArr.sort((a,b) => b[1] - a[1]);
    
    for (let subList = 0; subList < charArr.length; subList++) {
        for (let idx = 0; idx < charArr.length - 1; idx++) {
            if (charArr[idx][1] === charArr[idx+1][1]) {
                if (charArr[idx][0] > charArr[idx+1][0]) {
                    let temp = charArr[idx];
                    charArr[idx] = charArr[idx+1];
                    charArr[idx+1] = temp;
                }
            }
        }
    }
    return charArr


};
