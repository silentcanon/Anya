/**
 * Created by Canon on 2015-08-08.
 */
function show_comments(comments, callback) {

    function _single_comment_as_html(comment, floorNum, $html_tmpl, id2floorNum) {
        var id = 'floor' + floorNum;
        $html_tmpl.attr('id',comment.id);
        $html_tmpl.find("span.floorNum").html("#"+floorNum.toString());
        $html_tmpl.find("span.username").html(comment.username);
        $html_tmpl.find("p.comment_content").html(comment.content);
        if(comment.parentCmt_id != null) {
            $receiver = $html_tmpl.find("p.comment_receiver");
            $receiver.find("span.floorNum").html("#"+id2floorNum[comment.parentCmt_id][0]);
            $receiver.find("span.username").html("#"+id2floorNum[comment.parentCmt_id][1]);
            $receiver.show();
        }
        var $reply_to = $html_tmpl.find("a.reply_comment");
        $reply_to.attr("comment_id",comment.id);
        $reply_to.attr("username",comment.username);
        $("#comments").append($html_tmpl);
        $html_tmpl.show();

    };

    var $html_tmpl = $(".single_comment_tmpl");
    var id2floorNum = {};
    for(var i=0; i<comments.length; i++) {
        id2floorNum[comments[i].id] = [i+1,comments[i].username];
    }
    for(var i=0; i<comments.length; i++) {
        _single_comment_as_html(comments[i], i+1, $html_tmpl.clone(), id2floorNum);
    }

    callback();


}