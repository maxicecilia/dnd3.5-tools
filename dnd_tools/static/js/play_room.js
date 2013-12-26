/*!
* Add some doc here.
*/

function addRow(character, dex, mod, initiative) {
  total = getDexModificator(dex) + mod + initiative;

  $('#initiative-tracker-table > tbody:last').append('<tr class="dataRow" id="' + character +
    '"><td><button class="btn btn-default btn-sm delete-row">x</button></td><td>' + character +
    '</td><td class="dex-value">' + dex + '</td><td class="mod-value">' + mod +
    '</td><td class="init-value">' +
    '<input type="number" value="0" class="form-control input-sm width-sm initiativeInput"/>' +
    '</td><td class="total-value">' + total + '</td></tr>');
}

function initialize() {
  addRow('Sirius', 16, 4, 0);
  addRow('Thank', 18, 4, 0);
  addRow('Havoc', 21, 8, 0);
  addRow('K', 18, 6, 0);
  addRow('Haliax', 10, 4, 0);
}

function refreshTableSorter() {
  $.extend($.tablesorter.themes.bootstrap, {
    // these classes are added to the table. To see other table classes available,
    // look here: http://twitter.github.com/bootstrap/base-css.html#tables
    table      : 'table table-bordered',
    header     : 'bootstrap-header', // give the header a gradient background
    footerRow  : '',
    footerCells: '',
    icons      : '', // add "icon-white" to make them white; this icon class is added to the <i> in the header
    sortNone   : 'glyphicon-resize-small',
    sortAsc    : 'icon-chevron-up',
    sortDesc   : 'icon-chevron-down',
    active     : '', // applied when column is sorted
    hover      : '', // use custom css here - bootstrap class may not override it
    //filterRow  : '', // filter row class
    even       : '', // odd row zebra striping
    odd        : ''  // even row zebra striping
  });

  $("#initiative-tracker-table").tablesorter({
    theme : "bootstrap",
    widthFixed: true,
    headerTemplate : '{content} {icon}', // new in v2.7. Needed to add the bootstrap icon!
    widgets : [ "uitheme", "zebra" ],
    widgetOptions : {
      zebra : ["even", "odd"]
      // reset filters button
      //filter_reset : ".reset"
    }
  });
}

$(document).ready(function() {
  initialize();

  refreshTableSorter();

  $(".initiativeInput").change(function() {
    $( "tr.dataRow" ).each(function( index ) {
      total = getDexModificator(parseInt($(this).find('td.dex-value').html(), 10)) +
        parseInt($(this).find('td.mod-value').html(), 10) + parseInt($(this).find('td.init-value > input').val(), 10);
      $(this).find('td.total-value').html(total);

      $("#initiative-tracker-table").trigger("update")
        .trigger("sorton", [[0,5]])
        .trigger("appendCache")
        .trigger("applyWidgets");
    });
  });

  $("#add-new-row").click(function() {
    addRow($("#inputName").val(), parseInt($("#inputDex").val(), 10), parseInt($("#inputMod").val(), 10), 0);
    $("#initiative-tracker-table").trigger("update")
      .trigger("sorton", [[0,5]])
      .trigger("appendCache")
      .trigger("applyWidgets");
    });

  $(".delete-row").click(function() {
    $(this).parent().parent().remove();
  });

});


/* Life Tracker Tool - v2 */
$(document).ready(function() {

  $(".action-heal").click(function() {
    var hit_value = $(this).parent().find(".action-val").val();
    var parent = $(this).parent().parent().parent();
    var current_hp = parent.find("#current-hp");
    var hp = parseInt(current_hp.attr("data-hp"), 10) + parseInt(hit_value, 10);
    current_hp.text("Current HP: " + hp);
    current_hp.attr("data-hp", hp);
  });

  $(".action-hit").click(function() {
    var hit_value = $(this).parent().find(".action-val").val();
    var parent = $(this).parent().parent().parent();
    var current_hp = parent.find("#current-hp");
    var hp = parseInt(current_hp.attr("data-hp"), 10) - parseInt(hit_value, 10);
    current_hp.text("Current HP: " + hp);
    current_hp.attr("data-hp", hp);
  });
});
