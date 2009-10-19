/*!
 * Behavior for forms.
 * Copyright (C) 2009  Yesudeep Mangalapilly.
 *
 * The MIT License
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

String.prototype.startsWith = function(str)
{return (this.match("^"+str)==str)}

String.prototype.isUpperCase = function(){
   return !!this.match(/^[^a-z]*$/);
}
String.prototype.isLowerCase = function(){
   return !!this.match(/^[^A-Z]*$/);
}
String.prototype.isSameCase = function(){
   return (this.isLowerCase() || this.isUpperCase());
}
String.prototype.sanitizeCapitalization = function(){
   // Requires the titlecaps function by john resig.
   if(this && this.isSameCase()){
       return titleCaps(this.toLowerCase());
   } else {
       return this;
   }
}
String.prototype.lowerSanitizeCapitalization = function(){
   if(this && this.isLowerCase()){
       return titleCaps(this);
   } else {
       return this;
   }
}

jQuery(function(){
    var elements = {
        digitsFields: jQuery('form input.digits'),
        phoneFields: jQuery('form input.mobile, form input.phone'),
        forms: jQuery('form'),
        currencyFields: jQuery('form input.currency'),
        urlFields: jQuery('form input.url'),
        capitalizationFields: jQuery('form input.capitalize'),
        lowerCapitalizationFields: jQuery('form input.lower-capitalize')
    }, HTTP = "http://";

    elements.digitsFields.numeric();
    elements.phoneFields.numeric({allow: '+-() '});
    elements.currencyFields.numeric({allow: '+-.'});
    elements.urlFields.keyup(function(event){
        var elem = jQuery(this), value = elem.val();
        if (value == 'http:/'){
            elem.val(HTTP);
        } else if (!value.startsWith(HTTP)){
            elem.val(HTTP + value);
        }
    });
    elements.capitalizationFields.change(function(event){
       var elem = jQuery(this), value = jQuery.trim(elem.val());
       elem.val(value.sanitizeCapitalization());
    });
    elements.lowerCapitalizationFields.change(function(event){
        var elem = jQuery(this), value = jQuery.trim(elem.val());
        elem.val(value.lowerSanitizeCapitalization());
    });
    elements.forms.validate();
});

