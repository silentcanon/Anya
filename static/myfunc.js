/**
 * Created by Canon on 2015-08-08.
 */
function show_comments(comments) {

    function _single_comment_as_html(comment, floorNum) {
        var id = 'floor' + floorNum;
        var html = "<div class='row'>" +
            "<div class='col-sm-1 gravatar'>" +
            "<img src='http://gravatar.com/avatar/729e26a2a2c7ff24a71958d4aa4e5f35?s=60&d=identicon'>" +
            "</div>" +
            "<div class='col-sm-5 commnent_body'>" +
            "<p><span class='label label-primary'>" +
            floorNum.toString() + "</span>" +
            "<span class='label label-primary'>" + comment.username + "</spam>" + "</p>" +"</div></div>";
        return html;
    }
    var html = "";
    for(var i=0; i<comments.length; i++) {
        html += _single_comment_as_html(comments[i], i+1);

    }
    return html;

}