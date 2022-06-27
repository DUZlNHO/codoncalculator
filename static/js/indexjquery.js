$(document).ready(function(){
    $('#loading').hide();

    $('#submit').click(function(){
        $('#loading').fadeIn(600);
    });

    $("#seq").on("keydown", function(e) {
        if(e.code === "Enter") {
            e.preventDefault();
            $("#submit").trigger("click");
            $('#loading').fadeIn(600);
        }
    });

    $("#seq").on("keydown", function(e) {
        if(e.code === "KeyA" || e.code === "KeyC" || e.code === "KeyG" || e.code === "KeyU" || e.code === "KeyT"
        || e.code === "Backspace" || e.code === "Delete" || e.code === "ArrowLeft" || e.code === "ArrowRight"
        || (e.ctrlKey && e.code === "KeyV")) {
            e.allowDefault();
        }
        else {
            e.preventDefault();
        }
    });
});