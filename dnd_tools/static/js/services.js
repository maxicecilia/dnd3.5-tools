'use strict'; /*jslint node: true */

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('warRoom.services', []).
  value('version', '0.1');
