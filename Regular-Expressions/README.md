# Regular Expressions in Javascript

In this assignment, you will be using regular expressions to validate and manipulate strings in Javascript. 

## Task 1: Validate Email Addresses

Create a function `validateEmail(email)` that takes an email address as input and returns `true` if the email address is valid and `false` otherwise. An email address is considered valid if it meets the following criteria:

- It contains only one `@` symbol
- It contains at least one period (`.`) after the `@` symbol
- It does not contain any spaces
- It has at least one character before and after the `@` symbol

### Task 2: Find URLs

Create a function `findUrls(text)` that takes a string as input and returns an array of all URLs in the string. A URL is considered to be any string that begins with `http://` or `https://` and ends with a domain name like `.com` or `.org`. For example, `http://www.example.com` and `https://www.example.org` are both valid URLs, but `www.example.com` is not.