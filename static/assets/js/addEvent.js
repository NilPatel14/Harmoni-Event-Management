$(document).ready(function() {
    $("#cat").change(function() {
        var cat_id = $(this).val();
        var url = "/get-subcat/?cat_id="+cat_id;
        $.get(url, function(data,status){
            $("#subcat").html(data);
        });
    });
});