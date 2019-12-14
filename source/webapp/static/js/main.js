const baseUrl = 'http://localhost:8000/api/v1/';

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

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}

function makeRequest(path, method, auth=true, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json'
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    if (auth) {
        settings.headers = {'X-CSRFToken': getCookie('csrftoken')};
    }
    return $.ajax(settings);
}


let likes, like, dislike

function setUpGlobalVars() {
    likes = $('#likes');
    like = $('#like');
    dislike = $('#dislike');

}
// /photos/2/like_up/
function likesUp(id) {
    let request = makeRequest('photos/' + id + '/like_up', 'post');
    request.done(function(data, status, response) {
        console.log('Rated up quote with id ' + id + '.');
    }).fail(function(response, status, message) {
        console.log('Could not rate up quote with id ' + id + '.');
        console.log(response.responseText);
    });
}

function likesDown(id) {
    let request = makeRequest('photos/' + id + '/likes_down', 'post');
    request.done(function(data, status, response) {
        console.log('Rated up quote with id ' + id + '.');
    }).fail(function(response, status, message) {
        console.log('Could not rate up quote with id ' + id + '.');
        console.log(response.responseText);
    });
}

function checkLikes(){
    photo = likes.data('photo')
    user = likes.data('user')
    let request = makeRequest('likes/', 'get');
    console.log(request)
}



$(document).ready(function() {
    setUpGlobalVars();
    setUpAuth();
    checkAuth();
    getQuotes();
});