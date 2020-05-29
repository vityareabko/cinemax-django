


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

// var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url){
    var host = document.location.host;
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;

    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        !(/^(\/\/|http:|https:).*/.test(url));

}
                

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if(!(/http:.*/.test(settings.url) || /^https:.*/.test(settings.url))){
            xhr.setRequestHeader("X-CSRFToken",
                $('input[name="csrfmiddlewaretoken"]').val()
            );
        }
       
    }
});





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

