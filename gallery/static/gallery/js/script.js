const slider = document.querySelectorAll('.slider')
M.Slider.init(slider, {
    indicators: false,
    height: 400,
})

M.AutoInit();


$(document).ready(function () {
    $('.sidenav')
        .sidenav()
        .on('click tap', 'li a', () => {
            $('.sidenav').sidenav('close');
        });
});

$(document).ready(function () {

    $(window).scroll(function () {

        if ($(window).scrollTop() > 300) {
            $('nav').addClass('teal');
        } else {
            $('nav').removeClass('teal');
        }

    });

});
