/**
 * Created by Canon on 2015-09-29.
 */
var get_recent_images = function() {
    if(isOver) {
        return;
    }
    url = "/gallery/instagram/?count=5&client_id=44a3704cf42b4a2eb8329cba1054b450";
    if(next_max_id) {
        url = url + "&max_id=" + next_max_id;
    }
    var update_gallery = function($thumbnail) {
        $('#nanshen').append($thumbnail);
    };
    $.ajax({
        url: url,
        //data: data,
        success: function (response) {

            info_list = response['data'];
            if(response.pagination.next_max_id == undefined) {
                isOver = true;
                next_max_id = null;
            } else {
                next_max_id = response.pagination.next_max_id;
            }
            info_list.map(get_single_nail).map(update_gallery);
            //update_gallery(response);
            //alert();
        },
        error: function() {
            next_max_id = null;
            console.log('Error');
        },
        dataType: 'json'
    });
};


var get_next_recent_images_maker = function() {
    next_max_id = null;
    isOver = false;
    return get_recent_images;
};

var get_single_nail = function(img_info) {
    var info = {
        img_src: img_info["link"],
        thumbnail_src: img_info["images"]["thumbnail"]["url"],
        standard_src: img_info["images"]["standard_resolution"]["url"],
        id: img_info["id"]
    };
    if(img_info.location) {
        info['location'] = img_info.location.name;
    } else {
        info['location'] = null;
    }


    $img_comp = $("<img>", {'src': info.standard_src});
    $img_link_comp = $("<a>", {'href': info.img_src, 'target': "_blank"}).append($img_comp);
    $caption = $("<div>", {'class': 'caption'}).append($('<h3>test</h3>')).append($('<p>test</p>'));
    $thumbnail = $("<div>", {'class': 'thumbnail'});
    $thumbnail.append($img_link_comp).append($caption);
    return $thumbnail;
};






