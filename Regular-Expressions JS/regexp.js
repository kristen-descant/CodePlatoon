// takes in a string as input and should return true if valid
function validateEmail(email) {
    let regex = /^[a-zA-Z0-9-_]+[@][a-zA-Z0-9-_]+[\.]/
    return regex.test(email)
}

// takes in a string as input and returns true if valud
function validateUrls(url) {
    let regex = /^(https?:\/\/)[/w-]+(\.)[\w]+(\.)[\w]+/
    return regex.test(url)
}

module.exports = {
    validateEmail,
    validateUrls
}