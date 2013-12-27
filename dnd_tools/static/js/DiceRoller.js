/* 
 * Modified Version of this virtual dice roller that accepts standard dice notation
 * https://gist.github.com/thebinarypenguin/5811014 
 *
 * Dice Notation
 *
 *   [Num Dice] d <Num Sides> [Modifier][Droped Lowest or Highest Rolls][Droped Dices]
 *
 *
 * Num Dice  - Number of dice to roll (optional)
 *               Accepted Range : 0 - infinity
 *               Default        : 1
 *
 * Num Sides - Number of sides on each dice (required)
 *               Accepted Range : 1 - infinity
 *
 * Modifier  - Arithmetic modifier (optional)
 *               Accepted Range : -infinity - +infinity
 *               Default        : +0
 *
 * Droped Lower or Higher Rolls - Higher or Lower Dices Rolls are not added to the total (optional)
 *               Accepted Range : dh or dl (droped highest or droped lowest)
 *               Default        : +0
 *
 * Droped Dices - Number of Dices Rolls discarted (optional)
 *               Accepted Range : -infinity - +infinity
 *               Default        : +0
 *           
 * Examples
 *
 *   d6     - Roll 1 6-sided dice
 *   2d8    - Roll 2 8-sided dice
 *   d4+1   - Roll 1 4-sided dice and add 1
 *   3d10-5 - Roll 3 10-sided dice and subtract 5
 *   4d6dh4 - Roll 4 6-sided dice and does not add the 4 highest rolls to the total
 *   4d6dl4 - Roll 4 6-sided dice and does not add the 4 lowest rolls to the total
 *   4d4-1dl4 - Roll 4 4-sided dice and subtracts 1  it does not add the 4 lowest rolls to the total
 *
 *   The following are valid but stupid
 *
 *   0d6    - Roll 0 6-sided dice
 *   d1     - Roll 1 1-sided dic
 *   4d4dl4 - Roll 4 4-sided dice and does not add any roll to the total
 *   4d4dh4 - Roll 4 4-sided dice and does not add any roll to the total
 */
var DiceRoller = function() {

  // Private

  // Create a "data type" to represent the roll results
  var ResultSet = function() {
    this.rolls = [];
    this.modifier = 0;
    this.total = 0;
    this.drop = 0;
    this.dicesDroped = 0
  };

  // Add a toString method for convenience
  ResultSet.prototype.toString = function() {
    var rolls = this.rolls.join(' + ');
    var modifier = this.modifier;
    var total = this.total;

    if (modifier > 0) {
      return rolls + ' + ' + modifier + ' = ' + total;
    } else if (modifier < 0) {
      return rolls + ' - ' + Math.abs(modifier) + ' = ' + total;
    } else {
      return (rolls == total) ? total : rolls + ' = ' + total;
    }
  };

  /**
   * Parse formula into component parts
   * Returns object on success and null on failure
   */
  var parse = function(formula) {
    /* If formula is just a number, then treat it as a modifier */
    if (!isNaN(formula)) {
      return { rolls: 0, sides: 0, modifier: parseInt(formula, 10) };
    }

    var matches = formula.match(/^(\d+)?d(\d+)([+-]\d+)?(dl|dh)?(\d+)?$/i);

    if (matches === null || matches[2] === 0) {
      return null;
    }

    var rolls    = (matches[1] !== undefined) ? (matches[1] - 0) : 1;
    var sides    = (matches[2] !== undefined) ? (matches[2] - 0) : 0;
    var modifier = (matches[3] !== undefined) ? (matches[3] - 0) : 0;    
    var drop   =  (matches[4] !== undefined) ? (matches[4] =='dh'? 1 : -1 ) : 0;
    var dicesDroped = (matches[5] !== undefined) ? (matches[5] - 0) : 0;    

    return { rolls: rolls, sides: sides, modifier: modifier , drop : drop , dicesDroped : dicesDroped };
  };

  // Public

  /**
   * Roll the dice described in formula
   * Returns a ResultSet on success and null on failure
   */
  this.roll = function(formula) {
    var pieces = parse(formula);
    if (pieces === null) {
      return null;
    }

    var results = new ResultSet();

    // rolls
    for (var i = 0; i < pieces.rolls; i++) {
      results.rolls[i] = (1 + Math.floor(Math.random() * pieces.sides));
    }

    // sorts the rolls
    results.rolls.sort();    

    // modifier
    results.modifier = pieces.modifier;

    // total
    results.dicesDroped = pieces.dicesDroped;
    results.drop = pieces.drop;
    i = 0;
    var maxResult = results.rolls.length;
    var dropedDices = (results.drop)*(results.dicesDroped);

    // If higher or lower rolls are discarted it doesn't add them to the total
    if (dropedDices !== 0){
      (dropedDices > 0) ? maxResult = results.rolls.length - dropedDices :  i = Math.abs(dropedDices) ;
    }

    for (i; i < maxResult; i++) {
      results.total += results.rolls[i];
    }
    results.total += pieces.modifier;

    return results;
  };

  /**
   * Validates the format of formula
   * Returns true on success and false on failure
   */
  this.validate = function(formula) {
    return (parse(formula) === null) ? false : true ;
  };

};