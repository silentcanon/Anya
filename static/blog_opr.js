/**
 * Created by Canon on 2015-08-25.
 */
function blog_remove(remove_prtcl_addr, callback) {
    $.ajax({
        url: remove_prtcl_addr,
        type: 'GET',
        success: function (response) {
            console.log(response);
            res_json = JSON.parse(response)
            if (res_json['success']) {
                alert("removed");
                callback();
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}