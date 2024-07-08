$(document).ready(function() {
    $('#messages .message').each(function() {
        var message = $(this).text();
        var messageType = $(this).hasClass('success') ? 'success' : 'info';
        toastr[messageType](message);
    });
});