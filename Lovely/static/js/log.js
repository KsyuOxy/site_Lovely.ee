$(document).ready(function () {

    $('#log_btn').click(function () {
        let _login = $('#login_field').val();
        let _password = $('#password_field').val();
        $.ajax({
            url: '/ajax_log_passwd',
            data: {password_field:_password, login_field:_login},
            success: function(result){
                if (result.message_user === 'ok'){
                    $('.form-group').attr( 'onsubmit', 'return true');
                    alert('Welcome!');
                }else{
                    alert('Error');
                }
            }
        })
    })
    //----------------------------------------------------------------

    $('#check_btn').click(function () {
        let _login = $('#login_field').val();
        let _password = $('#password_field').val();
        $.ajax({
            url: '/ajax_log_passwd',
            data: {password_field:_password, login_field:_login},
            success: function(result){
                if (result.message_user === 'ok'){
                $('.form-group').attr( 'onsubmit', 'return true');
                    alert('The data was successfully authenticated');
                }else{
                    alert('Wrong data');
                }
            }
        })
    })
    //----------------------------------------------------------------
})
