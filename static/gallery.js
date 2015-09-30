/**
 * Created by Canon on 2015-09-29.
 */
var get_recent_images = function(next_max_id, callback) {
    url = "https://api.instagram.com/v1/users/425261701/media/recent/?count=10&client_id=44a3704cf42b4a2eb8329cba1054b450";
    if(next_max_id) {
        url = url + "&next_max_id=" + next_max_id;
        alert(url);
    }
    $.ajax({
        url: url,
        //data: data,
        success: function (response) {
            //update views
            callback(response)
            //alert();
        },
        dataType: 'json'
    });
};

var get_single_nail = function(img_info) {
    var info = {
        location: img_info["location"]["name"],
        img_src: img_info["link"],
        thumbnail_src: img_info["images"]["thumbnail"]["url"],
        standard_src: img_info["images"]["standard_resolution"]["url"],
        id: img_info["id"],
    };

    $img_comp = $("<img>", {'src': info.standard_src});
    $img_link_comp = $("<a>", {'href': info.img_src});
    $caption = $("<div>", {'class': 'caption'}).append($('<h3>test</h3>')).append($('<p>test</p>'));
    $thumbnail = $("<div>", {'class': 'thumbnail'});
    $thumbnail.append($img_link_comp).append($caption);

    return $thumbnail;
};






