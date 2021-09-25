# Testing

## Contents

- [Automated Testing](#automated-testing)

    - [W3C Markup Validation Service](#w3c-markup-validation-service)

    - [W3C CSS Validation Service](#w3c-css-validation-service)
    
    - [JSHint](#jshint)

    - [PEP8](#pep8)

- [Testing User Stories](#testing-user-stories)

    - [Viewing and Navigation](#viewing-and-navigation)

    - [Registration and User Accounts](#registration-and-user-accounts)

    - [Making a Purchase at Checkout](#making-a-purchase-at-checkout)


------

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



------

## Testing User Stories


### Viewing and Navigation

1. As a shopper/site user I want to be able to find information about the site so that I can understand what the site is about, what products it sells, and why I should make my purchases here.

![Testing user stories](documentation/media/test-userstories-1.png)

![Testing user stories](documentation/media/test-userstories-1-2.png)


- The homepage gives information about the site, its purpose and the products its sells.

- An About Us page can also be accessed via the sidenav, which gives a more detailed insight into what the site is.


2. As a shopper/site user I want to be able to view all products so that I can select some item(s) to purchase.

![Testing user stories](documentation/media/test-userstories-2.png)

![Testing user stories](documentation/media/test-userstories-2-2.png)

![Testing user stories](documentation/media/test-userstories-2-3.png)


- A 'Buy Games' button is accessible via the navbar, which directs users to the games page, where they can choose a game to purchase.

- When scrolling down on the home page, users will find two buttons: an 'adopt' button and a 'buy games' button. Each buttons allow users to access the two product types that the site sells - games and adoption packs. All products belonging to these two categories can be accessed easily and quickly.


3. As a shopper/site user I want to be able view all products by category so that I can quickly pinpoint the type of product that I want to purchase.

![Testing user stories](documentation/media/test-userstories-3.png)

- When scrolling down on the home page, users will find two buttons: an 'adopt' button and a 'buy games' button. Each buttons allow users to access the two product types that the site sells - games and adoption packs. All products belonging to these two categories can be accessed easily and quickly.


4. As a shopper/site user I want to be able to view the content of my shopping cart at any time so that I can review the items within my shopping cart. I want to see prices, item quantity and total price so that I can see how much I am spending.

![Testing user stories](documentation/media/test-userstories-4.png)


- Users can access their shopping cart via the shopping cart side nav or via the view cart page, which they can access via the 'view cart' button within the shopping cart sidenav.


5. As a shopper/site user I want to be able to find delivery information so that I can see if the store delivers to my area and if so how long it will take and how much it will cost.

- Delivery information has not yet, as of right now the store only handles orders via product keys that customers would access via their email. These product keys would allow users to redeem their game via a code and download it on an appropriate platform. Delivery options and costs will be added in the future to account for the items listed in the adoption pack packages. 



### Registration and User Accounts

6. As a site user I want to be able to easily register an account so that I can have a personal account and profile.

![Testing user stories](documentation/media/test-userstories-6.png)

- Users can sign up for an account easily and quickly by clicking the profile icon in the navbar. This will direct users to the log in page, which also provides a clear link for users to create an account if they do not already have one. 


7. As a site user I want to be able to easily log in and out so that I can access my personal account and sign out when finished.

![Testing user stories](documentation/media/test-userstories-6.png)

![Testing user stories](documentation/media/test-userstories-7.png)

- Users can log in easily and quickly by clicking the profile icon in the navbar, which will direct them to the log in page.

- Once logged in, the profile icon in the navbar will change to a dropdown menu. Clicking this will allow them to either navigate to their profile or sign out.



8. As a site user I want to be able to easily recover my password incase I forget it so that I can recover access to my account.

![Testing user stories](documentation/media/test-userstories-8.png)

![Testing user stories](documentation/media/test-userstories-8-2.png)

- Users can click the 'forgot password' link on the log in page to reset their password. 



9. As a site user I want to be able to recive a confirmation email after registering so that I can confirm that the registration was successful and validate that the site is trusted.

![Testing user stories](documentation/media/test-userstories-9.png)

![Testing user stories](documentation/media/test-userstories-9-2.png)

![Testing user stories](documentation/media/test-userstories-9-3.png)

![Testing user stories](documentation/media/test-userstories-9-4.png)

- Once registered, users will recieve an email confirmation and be asked to verify their email address in order to complete their registration. This was tested with a tempory email as shown above, and demonstrates full functionality.


10. As a site user I want to be able to have a personal profile so that I can view my order history, order confirmations and save my payment and delivery information.

![Testing user stories](documentation/media/test-userstories-10.png)

![Testing user stories](documentation/media/test-userstories-10-2.png)

![Testing user stories](documentation/media/test-userstories-10-3.png)

![Testing user stories](documentation/media/test-userstories-10-4.png)

![Testing user stories](documentation/media/test-userstories-10-5.png)

![Testing user stories](documentation/media/test-userstories-10-6.png)


- Once logged in users can navigate to their profile by click on the profile icon in the navbar, which will trigger a dropdown menu where they can click the link to navigate to their profile.

- Within their profile, users can view their order history, and see which product types they have purchased. This is represented with 'my games' and 'my adoptions'.

- Users can also view and update their personal information and billing/delivery details, which can be used on checkout.



### Making a Purchase at Checkout

11. As a shopper/site user I want to be able to easily select a package/edition for a product when making a purchase so that I can make a purchase easily and ensure that I do not accidentally purchase the wrong product.

![Testing user stories](documentation/media/test-userstories-11.png)

- When clicking on a game or adoption pack via the games page or adoptions page, users will be directed to the product details page. From here they can choose which package they would like to purchase and add that package to their shopping cart.


12. As a shopper/site user I want to be able to view items in my shopping cart so that I can identify the total cost and all the items I will recieve upon checkout.

![Testing user stories](documentation/media/test-userstories-4.png)

![Testing user stories](documentation/media/test-userstories-12.png)


- Users can access their shopping cart via the shopping cart side nav or via the view cart page, which they can access via the 'view cart' button within the shopping cart sidenav.

- The shopping cart displays each item price and quantity and calculates the total cost for the order. 



13. As a shopper/site user I want to be able to adjust the individual items in my shopping cart so that I can make adjustments to any items in my shopping cart, such as quantity. before proceeding to checkout.

![Testing user stories](documentation/media/test-userstories-13.png)

![Testing user stories](documentation/media/test-userstories-13-2.png)

- Item quantity can be adjusted by clicking on the increment/decrement buttons within the shopping cart. This will prompt an 'update' button to appear, which will save the new quantity value to session storage once clicked.



14. As a shopper/site user I want to be able to remove any item from my shopping cart so that I can ensure that I won't be charged for any items that I no longer wish to buy.

![Testing user stories](documentation/media/test-userstories-12.png)

![Testing user stories](documentation/media/test-userstories-13.png)


- Items can be removed from the shopping cart by clicking the bin icon within the cart item card. Removing the item will trigger a toast message to notify the user that the item has been successfully removed. 


15. As a shopper/site user I want to be able to easily enter my payment information and delivery/billing address details so that I can checkout quickly and easily.

![Testing user stories](documentation/media/test-userstories-15.png)

- Upon checkout, users can easily enter their payment and billing information via the checkout form.



16. As a shopper/site user I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes and that my payment was successful.

![Testing user stories](documentation/media/test-userstories-16.png)


- Once an order is processed, and successful, the user will be redirected to a checkout success page, where they will see an order confirmation page, listing the details of their order. Additionally, this will trigger a toast message to notify the user that the order was successful and that an order confirmation will be sent to their email. 


17. As a shopper/site user I want to be able to recieve an email confirmation after completing a purchase so that I can keep a record of my order in case I need it later.

![Testing user stories](documentation/media/test-userstories-16.png)

- Upon a successful checkout, users will be notified that an order confirmation will be sent to their email.



18. As a shopper/site user I want to be able to make a purchase without registering an account so that I can purchase a product without the need of signing up and making an account.

![Testing user stories](documentation/media/test-userstories-16.png)

- It is not neccessary for users to make an account in order to complete a purchase. As long as they fill out the checkout form correctly, their order will processed normally and with no issues. They will be redirected to a checkout success page displaying their order confirmation when checkout is complete and will recieve an order confirmation to the email.

- However, users who are not logged into an account are not able to save their details on checkout. This functionality is only available to those who are signed in.


-----


### C-R-U-D Testing

| No. |   Action    |   Input   |   Expected Output |   Actual Output   |   Result |  Further Comments |
| --- | ----------- | --------- | ----------------- | ----------------- | ---------| ----------------- |
| 1 | Add to cart | Navigate to a [games details page](https://naturetrust.herokuapp.com/games/buy/reddeadredemption2/) and click 'buy now' on one of the packages | The item should add to cart | The game item is added to the shopping cart | Pass |
| 2 | Update item quantity in shopping cart | Open the shopping cart sidenav and update the quantity by clicking on the increment/decrement buttons. Click 'update' once the button appears | The quantity value should update to the new value | The quantity updates | Pass |
|  3  | Remove item from shopping cart |  Open the shopping cart sidenav and click the bin icon on one of the items | The item should be removed from the shopping cart | The item is removed and a toast message is triggered, which says 'Removed <order name> from your cart' | Pass |
|  4  | Checkout | Add an item to your shopping cart, open the shopping cart and click 'secure checkout' to go to checkout. Fill in all required details and submit the form by clicking the 'place order' button | If successful you should see an order confirmation at the checkout success page | Checkout successful. I am redirected to the checkout success page where I can see a confirmation of my order which contains my order and information. On page load a toast message is triggered which says 'Order Successfully Processed! Your order number is <order number>. A confirmation email will be sent to <email>' | Pass |
| 5 | Save details at Checkout | Make an account if you haven't done so already and log in. Take all the required steps to go to checkout and once there ensure that 'Save this delivery information to my profile' is checked. Proceed with checkout and then navigate to your profile by clicking on the profile icon in the navbar | Your personal details should have saved and present with the account information and address book cards on the first page of your profile | All information is there | Pass |
| 6 | Update personal information | Make an account if you haven't done so already and log in. Navigate to your profile by clicking on the profile icon in the navbar and click 'edit information' in the first card. Update the content of an input field, or several, and click 'update details' | Your new data is saved | The new values are saved and can be seen on the profile page | Pass |


-----

## Further Testing

### Desktop

- Hardware 
    - Desktop PC with a AOC 2560 x 1440 monitor
    - MSI GE72MVR Apache Pro 17'3" Laptop
    - HP Spectre x360 15'6" Laptop 

- Operating Sytems 
    - Windows 10

- Browsers 
    - Google Chrome
    - Brave
    - Microsoft Edge


### Mobile Devices

- Hardware
    - Honor 20 Pro
    - Sony Xperia Z3 Plus
    - Realme x50 Pro
    - Samsung A20

- Operating Systems
    - Android

- Browsers
    - Google Chrome
    - Brave
    - Opera 
    - Microsoft Edge

-----
