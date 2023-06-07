const regexpModule = require('./regexp');

const validateEmail = regexpModule.validateEmail;
const validateUrls = regexpModule.validateUrls;

const emailTestCases = [
    'ben@test.com',
    'abc',
    'a@b.c',
    '@gmail.com',
    'google.com',
    'ben is cool@myspace.xyz',
    'nick@',
    'a@.com',
    'test@test.test'
];

for (const email of emailTestCases) {
    const result = validateEmail(email);
    if (result) {
        console.log(`${email} is a valid email`);
    } else {
        console.log(`${email} is an INVALID email`);
    }
}

const urlTestCases = [
    'http://www.example.com',
    'https://www.example.org',
    'www.example.com',
    'www.example.xyz',
    'http://www.example.',
    'https://example.org',
    'http:/www.example.org',
    'https://www..org',
];

for (const url of urlTestCases) {
    const result = validateUrls(url);
    if (result) {
        console.log(`${url} is a valid url`);
    } else {
        console.log(`${url} is an INVALID url`);
    }
}

