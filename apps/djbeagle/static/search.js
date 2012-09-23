$('html').ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        // Only send the token to relative URLs i.e. locally.
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$(function(){
    $('.delete-search').on('click', function(){
        var $row    = $(this).parent().parent(),
            id      = $row.data('id');

        $.ajax({ 
            url     : '/search/' + id,
            type    : 'DELETE'
        }).success(function(data){
            $row.remove();
        }).error(function(){
            console.log('error');
        });
    });

    $('#combine').on('click', function(){
        var id = $(this).data('id');

        $.ajax({ 
            url     : '/search/' + id + '/combined/',
            type    : 'POST',
            dataType: 'json'
        }).success(function(data){
            console.log(data);
        }).error(function(){
            console.log('error');
        });
    });

    $(document).on('click', '#add_criterion', function(){
        var $elem = $('<div class="controls"><input type="text" name="criterion"/>' +
          '</div>')
        .insertAfter($(this).parent());
        
        $(this).remove();
        $(this).insertAfter($elem.find('input'));
    });
});
