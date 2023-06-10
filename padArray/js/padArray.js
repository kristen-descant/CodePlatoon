// REMEMBER TO PSEUDOCODE
const pad = (array, minSize, value=null) => {
    // code goes here : ) 
    // start at end of array and add the value to end of array 
    // until reaching the disred length
    for (let idx = array.length; idx < minSize; idx++) {
        array.push(value);
    }

    return array;
}

exports.pad = pad;
