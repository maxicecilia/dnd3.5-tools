'use strict'; /*jslint node: true */

/* Directives */


angular.module('warRoom.directives', []).
  directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
      elm.text(version);
    };
  }]);