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

    $('#loaderModal').modal({
        opacity: 0.8,
        endingTop: '45%',
    });

    // Initialize dropdown
    $('.dropdown-trigger').dropdown({
        aligment: 'right',
        coverTrigger: false,
        constrainWidth: false,
    });
});