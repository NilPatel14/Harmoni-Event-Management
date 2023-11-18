function toggleAdditionalImagesField() {
    var eventCategorySelect = document.getElementById("event-category-select");
    var additionalImagesField = document.getElementById("additional-images-field");
    var specialskillfield = document.getElementById("special-skill");
    var user_profile_pic = document.getElementById("user_profile_pic")
    var Discriotionfield = document.getElementById("Discriotion-field");
    var company_name = document.getElementById("company-name");
    var first_name =  document.getElementById("first_name");
    var last_name = document.getElementById("last_name");

    if (eventCategorySelect.value === "vendor") {
        Discriotionfield.style.display = "block";
        additionalImagesField.style.display = "block";
        company_name.style.display = "block";
        specialskillfield.style.display = "none";
        user_profile_pic.style.display = "none";
        first_name.style.display = "none";
        last_name.style.display = "none";
    } else {
        Discriotionfield.style.display = "none"
        additionalImagesField.style.display = "none";
        company_name.style.display = "none";
        specialskillfield.style.display = "block";
        user_profile_pic.style.display = "block";
        first_name.style.display = "block";
        last_name.style.display = "block";
    }
}

$(document).ready(function() {
    $("#state").change(function() {
        var state_id = $(this).val();
        var url = "/get-city/?state_id="+state_id;
        $.get(url, function(data,status){
            $("#city").html(data);
        });
    });
});