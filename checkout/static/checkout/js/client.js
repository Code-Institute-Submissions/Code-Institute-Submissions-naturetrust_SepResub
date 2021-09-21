/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/


var StripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);


// Set up Stripe

var stripe = Stripe(StripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: "#000",
        fontFamily: 'Agency, Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "18px",
        textTransform: "uppercase",
        letterSpacing: "2px",
        fontWeight: "500",
        "::placeholder": {
            color: "#aab7c4"
        }
    },
    invalid: {
        fontFamily: 'Agency, Helvetica, sans-serif',
        color: "#dc3545",
        iconColor: "#dc3545"
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');
