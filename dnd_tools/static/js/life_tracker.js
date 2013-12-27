/* Life Tracker Tool - v2 */

$(document).ready(function() {

  $('#damage-input').tooltip({'trigger':'focus', 'title': 'Damage or dice pattern.'});

  $(".action-heal").click(function() {
    update_hp($(this), false);
  });

  $(".action-hit").click(function() {
    update_hp($(this), true);
  });

  function update_hp(obj, is_hit) {
    var parent = obj.parent().parent().parent();
    var hp_object = parent.find("#current-hp");

    var dice = new DiceRoller();
    var damage = dice.roll(obj.parent().find(".action-val").val()).total;
    if (is_hit) {
      damage = -1 * damage;
    }

    var hp = parseInt(hp_object.attr("data-current-hp"), 10) + damage;
    var total_hp = hp_object.attr("data-total-hp");

    hp_object.text("Current HP: " + hp + " / " + total_hp);
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
