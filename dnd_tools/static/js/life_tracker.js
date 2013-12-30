/* Life Tracker Tool - v2 */

$(document).ready(function() {

  $('#damage-input').tooltip({'trigger':'focus', 'title': 'Damage or dice pattern.'});

  $(".action-heal").click(function() {
    update_hp($(this), false);
  });

  $(".action-hit").click(function() {
    update_hp($(this), true);
  });

  $(".action-save").click(function() {
    var char_div = $(this).parent().parent();
    var character_id = char_div.attr('data-id');
    var current_hp = char_div.find('p').attr('data-current-hp');
    var total_hp = char_div.find('p').attr('data-total-hp');
    //Pull all information.
    //curl --dump-header - -H "Content-Type: application/json" -X PATCH --data '{"ecl": 21}' http://localhost:8000/v1/character/52bbb1a31238739e436e1dc1/

    $.ajax({
        headers : {
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
        },
        url : '/api/v1/character/' + character_id + '/',
        type : 'PATCH',
        data : JSON.stringify({hit_points: {current: current_hp, total: total_hp}}),
        success : function(response, textStatus, jqXhr) {
            $('.bottom-left').notify({
              message: { text: 'Your character has been saved!  ' }
            }).show();
        },
        error : function(jqXHR, textStatus, errorThrown) {
            $('.bottom-left').notify({
              message: { text: 'Error! ' + textStatus }
            }).show();
            console.log("The following error occured: " + textStatus, errorThrown);
        }
    });
  });

  function update_hp(obj, is_hit) {
    var parent = obj.parent().parent().parent();
    var hp_object = parent.find("#current-hp");
    var temp_check = $(parent.find(".temp-damage-checkbox")[0]).is(':checked');

    var dice = new DiceRoller();
    var damage = dice.roll(obj.parent().find(".action-val").val()).total;
    if (damage && is_hit) {
      damage = -1 * damage;
    } else if (!damage) {
      return;
    }

    var temp_hp = parseInt(hp_object.attr("data-temp-hp"), 10);
    var hp = parseInt(hp_object.attr("data-current-hp"), 10);
    var total_hp = hp_object.attr("data-total-hp");

    if (temp_check) {
      temp_hp -= damage;
    } else {
      hp += damage;
    }

    hp_object.text("Current HP: " + hp + " ("+ temp_hp + ")" + " / " + total_hp);
    hp_object.attr("data-current-hp", hp);
  }

  function get_damage(obj) {
    var hit_value = obj.val();

    if (!isNaN(hit_value)) {
      hit_value = parseInt(hit_value, 10);
    } else {
      var dice = new DiceRoller();
      hit_value = dice.roll(hit_value).total;
    }
    return hit_value;
  }

});
