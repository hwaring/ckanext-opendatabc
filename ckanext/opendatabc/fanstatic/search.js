$( document ).ready( function() {
	$('.total-view-count, .last-modified').tooltip();

	$('.isotope').isotope({
		itemSelector : '.isotope-item',
		masonry:{isFitWidth:true },
		
		getSortData : {
		    total_count : function ( elem ) {
		    	return parseInt ($( elem ).find('.total-view-count').text(), 10 )
		    },
		    recent_count : function ( elem ) {
		    	return parseInt( $( elem ).find('.recent-view-count').text(), 10 )
		    },
		    title : function ( elem ) {
		      return $( elem ).find('.title').text();
		    },
		    last_modified: function (elem) {
		    	return $( elem ).find('.last-modified a').attr('ckan-modified');
		    }
	  	}
	});

	$('.isotope').ckan_isotope({
		default_facet_operator: {
			groups: 'or',
			res_format: 'and',
			tags: 'and',
		}
	})

	$(window).bind( 'hashchange', function() { 
		$('[data-toggle="dropdown"]').parent().removeClass('open'); 
	}).trigger('hashchange');


	$('.tagbox .iso-toggle-facet, .tagbox .iso-clear-facet').tooltip()
	$('.toolbar .facet.groups .iso-toggle-category span, .group-icon-list a').tooltip();
	$('.dataset-metadata a').tooltip();

	
});
