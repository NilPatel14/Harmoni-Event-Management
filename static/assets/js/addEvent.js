$(document).ready(function() {
    $("#cat").change(function() {
        var cat_id = $(this).val();
        var url = "/get-subcat/?cat_id="+cat_id;
        $.get(url, function(data,status){
            $("#subcat").html(data);
        });
    });
});

document.getElementById("end_datetime").addEventListener("input", function() {
    var startDateTime = new Date(document.getElementById("start_datetime").value);
    var endDateTime = new Date(this.value);

    if (endDateTime <= startDateTime) {
        alert("End datetime should be greater than start datetime");
    }
});