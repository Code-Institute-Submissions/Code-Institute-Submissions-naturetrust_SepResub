$(document).ready(function() {
    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id-qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    };

    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    };

    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.qty-btn').find('.qty-val')[0];
        // Cache the value that's currently in it into a variable called currentValue
        var currentValue = parseInt($(closestInput).val());

        // Use that variable to set the input boxes new value to the current value plus one
        $(closestInput).val(currentValue + 1);
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);

        // Show update button when increment button is clicked
        itemId = $(this).attr('id');
        idNumber = itemId.split('qty_');
        idNumber = idNumber[1]
        $(`#updateQtyNav-${idNumber}`).fadeIn(400);
        $(`#updateQty-${idNumber}`).fadeIn(400);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.qty-btn').find('.qty-val')[0];
        // Cache the value that's currently in it into a variable called currentValue
        var currentValue = parseInt($(closestInput).val());

        if ($(closestInput).val() != 1) {
            // Use that variable to set the input boxes new value to the current value minus one
            $(closestInput).val(currentValue - 1);
            var itemId = $(this).data('item_id');
            handleEnableDisable(itemId);

            // Show update button when decrement button is clicked
            itemId = $(this).attr('id');
            idNumber = itemId.split('qty_');
            idNumber = idNumber[1]
            $(`#updateQtyNav-${idNumber}`).fadeIn(400);
            $(`#updateQty-${idNumber}`).fadeIn(400);
        };
    });
});