$(function() {
    return $(".carousel").on("slide.bs.carousel", function(ev) {
        $("iframe").lazyload();
    });
});