/*!
 * Behavior for payment page for Python EBS Integration Kit.
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

jQuery(function(){
    var elements = {
        returnUrlField: jQuery('#form_payment input[name="return_url"]'),
        returnUrlDisplay: jQuery('#display_return_url'),
        modeField: jQuery('#form_payment select[name="mode"]'),
        modeDisplay: jQuery('#display_mode'),
        accountIdField: jQuery('#form_payment input[name="account_id"]')
    };

    /*
     * Return URL input form field handler for keyup and change events.
     */
    function returnUrlFieldHandler(event){
        elements.returnUrlDisplay.text(jQuery(this).val());
    }
    elements.returnUrlField.keyup(returnUrlFieldHandler).change(returnUrlFieldHandler);
    
    function onModeChanged(event){
        jQuery.post('/update/mode', {mode: jQuery(this).val()}, function(data, textStatus){
            elements.modeDisplay.text('Mode has been set to: ' + data.mode).css({display: 'block'});
            elements.accountIdField.val(data.account_id);
        }, 'json');
    }
    elements.modeField.change(onModeChanged);
});

