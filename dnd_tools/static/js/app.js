'use strict'; /*jslint node: true */

// Declare app level module which depends on filters, and services
angular.module('warRoom', [
  'ngRoute',
  'warRoom.filters',
  'warRoom.services',
  'warRoom.directives',
  'warRoom.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/war', {templateUrl: '/static/partials/war_room.html', controller: 'WarRoomController'});
  //$routeProvider.when('/view2', {templateUrl: 'partials/partial2.html', controller: 'MyCtrl2'});
  $routeProvider.otherwise({redirectTo: '/war'});
}]);
