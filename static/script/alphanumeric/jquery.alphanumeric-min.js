(function(a){a.fn.alphanumeric=function(b){b=a.extend({ichars:"!@#$%^&*()+=[]\\';,/{}|\":<>?~`.- ",nchars:"",allow:""},b);return this.each(function(){if(b.nocaps){b.nchars+="ABCDEFGHIJKLMNOPQRSTUVWXYZ";}if(b.allcaps){b.nchars+="abcdefghijklmnopqrstuvwxyz";}s=b.allow.split("");for(i=0;i<s.length;i++){if(b.ichars.indexOf(s[i])!=-1){s[i]="\\"+s[i];}}b.allow=s.join("|");var d=new RegExp(b.allow,"gi");var c=b.ichars+b.nchars;c=c.replace(d,"");a(this).keypress(function(f){if(!f.charCode){k=String.fromCharCode(f.which);}else{k=String.fromCharCode(f.charCode);}if(c.indexOf(k)!=-1){f.preventDefault();}if(f.ctrlKey&&k=="v"){f.preventDefault();}});a(this).bind("contextmenu",function(){return false;});});};a.fn.numeric=function(c){var b="abcdefghijklmnopqrstuvwxyz";b+=b.toUpperCase();c=a.extend({nchars:b},c);return this.each(function(){a(this).alphanumeric(c);});};a.fn.alpha=function(c){var b="1234567890";c=a.extend({nchars:b},c);return this.each(function(){a(this).alphanumeric(c);});};})(jQuery);