var searchTerms = Array();
jQuery.expr[':'].icontains = function(a,i,m){
    return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase())>=0;
};

      
function qrcode() {
    $("#content").css({opacity: '0.1'});
    $( "#qrcode" ).dialog({
	    modal: true,
		buttons: {
		Ok: function() {
		    $( this ).dialog( "close" );
		    $("#content").css({opacity: '1.0'});
		}
	    }
        });
    return false;
}

function showNode(el) {
    el.addClass("expanded");
    el.removeClass("collapsed");
    el.next().show('fast');
}

function hideNode(el) {
    el.addClass("collapsed");
    el.removeClass("expanded");
    el.next().hide('fast');
}
      
function toggleNode(el) {
    var dd = el.next();
    if ($(dd).is(":visible")) {
	hideNode(el);
    } else {
	showNode(el);
    }
}
      
function showHideNode() {
    toggleNode($(this));
}

function showHideNodeFromMenu() {
    toggleNode($('a[name="' + $(this)[0].href.split('#')[1] +'"]').parent());
}

function showNodes(els) {
    els.each(function() {showNode($(this));});
}

function collapseAll() {
    $('dt.expanded').each( function() {hideNode($(this));} );
}

function showSearchResults() {
    collapseAll();
    stext = $("#searchbox p input")[0].value;
    var contains = ':icontains("' + stext + '")';
    showNodes($('dt' + contains));
    showNodes($('dd' + contains).prev('*.collapsed'));
    showNodes($('td' + contains).prev('*.collapsed'));
    showNodes($('li' + contains).prev('*.collapsed'));
}

$(document).ready(function() {
        jQuery('#findmeonlogos').jqDock({align: 'bottom', labels: 'bc'});
        $("ul.jd_menu").jdMenu();
        $("#jobhistorybody dd").hide();
        $("#specialskills dd").hide();
        $("#projecthistory dd").hide();
        $("#jobhistorybody dt").bind('click', showHideNode).addClass("collapsed").addClass("link");
        $("#specialskills dt").bind('click', showHideNode).addClass("collapsed").addClass("link");
        $("#projecthistory dt").bind('click', showHideNode).addClass("collapsed").addClass("link");
        $("ul.jd_menu li ul li a").bind('click', showHideNodeFromMenu);
        $(".backtotop").hide();
        $("span.mailme").mailme();
        $("#qrcodelink").bind('click', qrcode);
        $("#searchbox").show();
        $("#specialskills dd table tbody tr td:nth-child(1)").each(function(idx){searchTerms.push($(this).text().replace(/^\s+|\s+$/g, ''))});
        $("#projecthistory dt").each(function(idx){searchTerms.push($(this).text().replace(/^\s+|\s+$/g, ''))});
        $("#jobhistorybody dt span.jobname").each(function(idx){searchTerms.push($(this).text().replace(/^\s+|\s+$/g, ''))});
        searchTerms.sort();
        $("#searchbox p input[name=searchvalue]").autocomplete(searchTerms);
        $("#searchbox p input[type=submit]").bind('click', showSearchResults);
        $("#searchbox p input[type=reset]").bind('click', collapseAll);
    });
