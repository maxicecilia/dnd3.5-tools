'use strict'; /*jslint node: true */

/* Filters */

angular.module('warRoom.filters', []).
  filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    };
  }]).
  filter('orderObjectBy', function(){
    return function(input, attribute) {
        if (!angular.isObject(input)) return input;

        var array = [];
        for(var objectKey in input) {
            array.push(input[objectKey]);
        }

        array.sort(function(a, b){
            a = parseInt(a[attribute], 10);
            b = parseInt(b[attribute], 10);
            return b - a;
        });
        return array;
    };
});