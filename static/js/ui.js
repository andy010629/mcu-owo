document.addEventListener('DOMContentLoaded', function() {
    // nav menu
    const menus = document.querySelectorAll('.side-menu');
    var sidemenu = M.Sidenav.init(menus, { edge: 'right' });
    var elems = document.querySelectorAll('.login-page');
    var instances = M.Modal.init(elems);

    // var elems2 = document.querySelectorAll('.modal2');
    // var instances2 = M.Modal.init(elems2);

});