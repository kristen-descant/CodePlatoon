exports.factorial = function(num) {
    if (num === 0) {
        return 1
    }

    return exports.factorial(num - 1) * num
};
