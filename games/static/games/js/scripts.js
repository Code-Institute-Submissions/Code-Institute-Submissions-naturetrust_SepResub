$(document).ready(function() {
    /* Hide section headers that do not have content */

    function hideEmptyHeaders() {
        var sectionContent = $('.active .section-content');
        for (i=0; i < sectionContent.length; i++) {
            var findString = $(sectionContent[i]).text().match(/[abcdefghijklmnopqrstuvwxyz]/g);
            if (!findString) {
                console.log('empty', sectionContent[i]);
                $(sectionContent[i]).prev('.section-header').addClass('hide');
            }
        }
    }
    hideEmptyHeaders(); 

    /* Change edition details section on edition button click */

    $('.select-edition a').on('click', function() {
        var edition = $(this).attr('id');
        var editionId = edition.split('Btn');
        editionId = editionId[1];

        $('.edition-details.active').removeClass('active').addClass('hide');
        $(`#editionDetails${editionId}`).removeClass('hide').addClass('active');
        hideEmptyHeaders();
    });
});