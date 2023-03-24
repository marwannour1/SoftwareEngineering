
$(document).ready(function(){
  
    // Increment and decrement item count
    $('.plus-btn').click(function() {
    var count = $(this).siblings('.count');
    var price = $(this).closest('.cart-item').find('.item-price');
    var currentCount = parseInt(count.text());
    count.text(currentCount + 1);
    price.text('$' + (currentCount + 1) * parseFloat(price.attr('data-price')));
    
    });
    
    $('.minus-btn').click(function() {
    var count = $(this).siblings('.count');
    var price = $(this).closest('.cart-item').find('.item-price');
    var currentCount = parseInt(count.text());
    if (currentCount > 0) {
    count.text(currentCount - 1);
    price.text('$' + (currentCount - 1) * parseFloat(price.attr('data-price')));
    updateTotalPrice();
    }
    });
    
    // Remove item from cart
    $('.remove-btn').click(function() {
    $(this).closest('.cart-item').remove();
    updateTotalPrice();
    });
    
    // Update total price
    function updateTotalPrice() {
    var totalPrice = $('#total-price');
    var sum = parseFloat(0);
    $('.cart-item').each(function() {
    sum += parseFloat($(this).find('.item-price').text().replace('$', ''));
    });
    totalPrice.text('$' + sum.toFixed(2));
    }
    
    });