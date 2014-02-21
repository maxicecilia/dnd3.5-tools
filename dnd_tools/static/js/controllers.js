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
    });
  }]).
  controller('SidebarController', ['$scope', function($scope) {
    $scope.name = "Foobar";
  }]);
