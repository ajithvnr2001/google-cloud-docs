---
url: https://docs.cloud.google.com/appengine/docs/standard/services/users/php/get_current_user.txt
title: https://docs.cloud.google.com/appengine/docs/standard/services/users/php/get_current_user.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:54:12.497403+00:00
---

# https://docs.cloud.google.com/appengine/docs/standard/services/users/php/get_current_user.txt

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/users/php/get_current_user.txt

getNickname(); if (UserService::isCurrentUserAdmin()) { echo 'Go to admin area'; } } // [END adminurl] // [START loginurl] if (isset($user)) { echo sprintf('Welcome, %s! ([sign out](https://docs.cloud.google.com/appengine/docs/standard/services/users/php/%s))', $user->getNickname(), UserService::createLogoutUrl('/')); } else { echo sprintf('[Sign in or register](https://docs.cloud.google.com/appengine/docs/standard/services/users/php/%s)', UserService::createLoginUrl('/')); } // [END loginurl] // [START getuser] if (!isset($user)) { // The user is not logged in } else { echo 'Hello, ' . $user->getNickname(); } // [END getuser] // [START createuser] $user = new User("Albert.Johnson@example.com"); // [END createuser] // [START createuser_fed] $user = new User(null, "http://example.com/id/ajohnson"); // [END createuser_fed] 
