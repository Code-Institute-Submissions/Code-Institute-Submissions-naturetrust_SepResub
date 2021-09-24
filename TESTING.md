# Testing

## Contents

- [Automated Testing](#automated-testing)

    - [W3C Markup Validation Service](#w3c-markup-validation-service)

    - [W3C CSS Validation Service](#w3c-css-validation-service)
    
    - [JSHint](#jshint)

    - [PEP8](#pep8)


## Automated Testing


[W3C Markup Validation Service](https://validator.w3.org/), [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and [JShint](https://jshint.com/) were used to validate the project's HTML, CSS and JS files.


### W3C Markup Validation Service

All pages passed the HTML validation checker with the following results:

|  Page url  |  Validation Results  | Fix |
| ---------- | -------------------- | ----- |
| home/      | The validator flagged an error for the cart-item card in the shopping cart sidenav: `div not allowed as child of element ul` | I updated the shopping cart sidenav to only use ul and li elements as parents of the cart-item div elements to fix the issue |
| home/      | `Warning: The type attribute is unnecessary for JavaScript resources` | I removed the type attributes from all script tags to fix the issue |
| games/     | Pass ||
| games/<game_title>/ | Pass ||
| games/buy/<game_title>/ | `Error: Stray end tag a` | Removed stray anchor tags to fix the issue |
| adoption/  | Pass ||
| adoption/adopt/<animal>  | Pass ||
| profile/  | Pass ||
| profile/my-orders/  | Pass ||
| profile/my-games/  | Pass ||
| profile/my-adoptions/  | Pass ||
| profile/update-details/  | Pass ||
| cart/  | `Error: Duplicate ID` for shopping cart item quantity buttons. `Error: element h6 must not appear as a descendant of the th element`. Errors were also flagged for having a form inside the the table | Any duplicate id's were address and h6 elements were replaced with span elements. The update quantity form was moved outside the table and the form attribute was added to input fields in order to pass the validation check. I used [this source](https://stackoverflow.com/questions/5967564/form-inside-a-table) to find the solution for this issue |
| checkout/ | `Error element option without attribute label must not be empty` | Added `blank_label` to the CountryField in the models to fix this issue |
| checkout/success/  | Pass | |


### W3C CSS Validation Service

Found no errors in my code.

![CSS Validator screenshot](documentation/media/css-validator.png)


### JSHint

JShint gave the following warnings in relation to the syntax of my code:

`'template literal syntax' is only available in ES6 (use 'esversion: 6').

`'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').`

`sessionStorage['addedToCart'] is better written in dot notation.`

I updated my JavaScript code to use `sessionStorage.getItem()` and `sessionStorage.setItem()`, however other warnings were ignored as they were undetrimental to the overall functionality of my project.


### PEP8

All of the Python code was run through a [PEP8 validator](http://pep8online.com/). 

The only errors that was flagged was `line too long`. When able, this was promptly corrected.