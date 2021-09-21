$(document).ready(function () {
    // Initialize sidenav
    $('.sidenav').sidenav({
        inDuration: 450,
        outDuration: 350,
    });

    $('.sidenav-right').sidenav({
        edge: 'right',
        inDuration: 450,
        outDuration: 350,
    });

    // Initialize parallax
    $('.parallax').parallax();

    // Initialize form select
    $('select').formSelect();
});