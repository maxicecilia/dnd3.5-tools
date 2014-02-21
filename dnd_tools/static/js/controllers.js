'use strict'; /*jslint node: true */

/* Controllers */

angular.module('warRoom.controllers', []).
  controller('WarRoomController', ['$scope', '$http', function($scope, $http) {
    $http.get('/api/v1/character/?format=json').success(function(data) {
        data.objects.forEach(function( character ) {
            character['initiative'] = 0 + character['initiative_mod'];
        });
        $scope.characters = data.objects;

        $scope.heal = function(character) {
            var dice = new DiceRoller();
            var damage = dice.roll(character.damage).total;
            character.hit_points.current += damage;
        };

        $scope.addCharacter = function(new_char) {
          var dice = new DiceRoller();
          new_char.hit_points = {
            current: parseInt(new_char.hitpoints, 10),
            temp_damage: 0,
            total: parseInt(new_char.hitpoints, 10)
          };
          var count = parseInt($('#inputClone').val(), 10);
          if (isNaN(count)) {
            count = 1;
          }
          for (var i = 1; i <= count; i++) {
            var x = angular.copy(new_char);
            x.initiative = dice.roll(x.initiative).total;
            if (i > 1) {
              x.name = x.name + "_" + i;
            }
            $scope.characters.push(x);
          }
        };

        $scope.removeCharacter = function(character) {
          $scope.characters.splice( $scope.characters.indexOf(character), 1 );
        };
    });
  }]).
  controller('SidebarController', ['$scope', function($scope) {
    $scope.name = "Foobar";
  }]);
