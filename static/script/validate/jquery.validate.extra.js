(function($){
    jQuery.validator.addMethod("mobile", function(mobile_number, element){
        var re = new RegExp("^[+]?[0-9- ]+$", "g");
        return re.test(mobile_number);
    }, "Please enter a valid mobile number (eg. +1 650 555 1212).");

    jQuery.validator.addMethod("phone", function(phone_number, element){
        var re = new RegExp("^[+]?[0-9- ]+$", "g");
        return re.test(phone_number);
    }, "Please enter a valid phone number (eg. 011 91 22 2765 4585).");
})(jQuery);

