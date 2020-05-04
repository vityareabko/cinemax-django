$(document).ready(function () {
    var tabsItem = $('.tabs-item');
    
    tabsItem.on('click', function(e){
        e.preventDefault();
        var activContent = $(this).attr('href');
        $('.active').toggleClass('active');
        $(this).toggleClass('active');
        $('.visible').toggleClass('visible');
        $(activContent).toggleClass('visible');
    });
});
