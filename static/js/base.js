$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $('select').formSelect();
    $('.modal').modal();
    // $('.datepicker').datepicker({
    //     'format': 'yyyy-mm-dd',
    // });
    $('.collapsible').collapsible();
    setTimeout(function() {
        $('.messages').fadeOut('fast');
    }, 3000);
});


