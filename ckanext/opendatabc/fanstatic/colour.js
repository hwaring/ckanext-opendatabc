var stringToColour = function(str) {
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
        hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    var colour = '#';
    for (var i = 0; i < 3; i++) {
        var value = (hash >> (i * 8)) & 0xFF;
        colour += ('00' + value.toString(16)).substr(-2);
    }
    return colour;
}

 $('.dataset-organization').each(function(value, index) {
                                var selectorObj = $(this);
                                var org = selectorObj.attr('class').split(' ')[1];

				$("."+org).css('background-color', stringToColour(org));
				$("._"+org).css('border-color', stringToColour(org));
			  				 
                        });

