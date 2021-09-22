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
        color: "#FF1744",
        iconColor: "#FF1744"
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = $('#card-errors');
    if (event.error) {
        var html = `
        <div class="col s12 center">
            <p class="center red-text text-accent-3">${event.error.message}</p>
        </div>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    };
});

// Handle form submit
var form = document.getElementById('paymentForm');

form.addEventListener('submit', function(ev) {

    // disable card element and submit button to prevent multiple submissions.
    ev.preventDefault();
    card.update({'disabled': true});
    $('#make-payment').attr('disabled', true);

    $('#loaderModal').modal('open');


    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    }

    var url = '/checkout/cache_checkout_data/';

    // Post data to the view

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(`${form.first_name.value} ${form.last_name.value}`),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address.value),
                        line2: $.trim(form.street_address_2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(`${form.first_name.value} ${form.last_name.value}`),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address.value),
                    line2: $.trim(form.street_address_2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            }
        }).then(function(result) {
            if (result.error) {
                var errorDiv = $('#card-errors');
                var html = `
                    <div class="col s12 center">
                        <span class="center red-text text-accent-3">${result.error.message}</span>
                    </div>`;
                $(errorDiv).html(html);

                $('#loaderModal').modal('close');
                card.update({'disabled': false});
                $('#make-payment').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    });
});