/** -----------------------------------------------------
 * All the script here it will extends to all the pages
------------------------------------------------------- */

// 1) Script to validate all inputs
function validateEmail(email) {

    let regex = /^([a-zA-Z0-9 .+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}
function validateAll() {

    let name = $("#name").val();
    let phone = $("#phone").val();
    let email = $("#email").val();
    let dateofbirth = $("#dateofbirth").val();
    let gender = $("#gender").val();
    let grade = $("#grade").val();

    if (name == '') {
        swal("OoPss !! ", "Name field cannot be empty.", "error");
        return false;
    }
    else if (phone == '') {
        swal("OoPss !! ", "Phone field cannot be empty.", "error");
        return false;
    }
    else if (email == '') {
        swal("OoPss !! ", "Email field cannot be empty.", "error");
        return false;
    }
    else if (!(validateEmail(email)) ) {
        swal("OoPss !! ", "Put a validate address.", "error");
        return false;
    }
    else if (dateofbirth == '') {
        swal("OoPss !! ", "Date of Birth field cannot be empty.", "error");
        return false;
    }  
    else if (dateofbirth > 99999999999) {
        swal("Denied !! ", "The maximum value is 99999999999 years old.", "error");
        $("#dateofbirth").val("");
        return false;
    }
    else if (gender == '') {
        swal("OoPss !! ", "Gender field cannot be empty.", "error");
        return false;
    }
    else if (grade == '') {
        swal("OoPss !! ", "Grade field cannot be empty.", "error");
        return false;
    }
    else {
        return true;
    }
}
$("#btn-add").bind("click", validateAll); 

// 2) script (Name field) only letter is allowed
$(document).ready(function() {
    // only letter
    jQuery('input[name="name').keyup(function() {
        
        let letter = jQuery(this).val();
        let allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
          
    });
    // prevent starting with space 첫 문자 공백 금지 
    $("input").on("keypress", function(e) {

           if(e.which === 32 && ! this.value.length)
           e.preventDefault(); 
    });
            
}); 

// 3) Script to put first letter capitalized
$("#name").keyup(function() {
    let txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){ return $1.toUpperCase( ); }));
});
// 4) Script to Lowercase input email
$(document).ready(function(){
    $('#email').keyup(function(){
        this.value = this.value.toLowerCase();
    });
});

// 5) Script to allow only number in date of birth
$("#dateofbirth").keyup(function(){
    if(!/^[0-9]*$/.test(this.value)) {
         this.value = this.value.split(/[^ 0-9.]/).join('');
    };
});

// 6) date of birth Mask
$(document).ready(function() {
    $("#dateofbirth").inputmask("9999-99-99", { "onlycomplete": function() {
        swal("Opsss !", "Incomplete Date of Birth. Review.", "error");
        return false;

    } });

});
// 7) Phone Mask
$(document).ready(function() {
    $("#phone").inputmask("999-9999-9999", { "onlycomplete": function() {
        swal("Opsss !", "Incomplete phone. Review.", "error");
        return false;

    } });

});

// 8) 시간
setInterval(function() {
    const date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500); 


//9) if no student, show message
let verify = $("#chk_td").length;
    if (verify == 0) {
        $("#no-data").text("No Student Found!!!");
    }



