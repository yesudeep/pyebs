(function(a){jQuery.validator.addMethod("mobile",function(d,b){var c=new RegExp("^[+]?[0-9- ]+$","g");return c.test(d);},"Please enter a valid mobile number (eg. +1 650 555 1212).");jQuery.validator.addMethod("phone",function(b,c){var d=new RegExp("^[+]?[0-9- ]+$","g");return d.test(b);},"Please enter a valid phone number (eg. 011 91 22 2765 4585).");})(jQuery);