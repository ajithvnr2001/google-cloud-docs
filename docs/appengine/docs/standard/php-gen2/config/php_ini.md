---
url: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/config/php_ini/
title: The php.ini File \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:32:13.103866+00:00
---

# The php.ini File  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/config/php_ini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  The php.ini File Stay organized with collections  Save and categorize content based on your preferences. 

You can include a `php.ini` file with your App Engine application. This file lets you customize the behavior of the PHP interpreter directives.

See an example of the [default `php.ini` configuration](http://php72-ini.appspot.com/).

## Using a custom php.ini file

Place the `php.ini` file in your application's base directory where your `app.yaml` file is located. It is loaded when the PHP interpreter is initialized, before running your application code.

The file follows the same syntax as [other `.ini` files](https://en.wikipedia.org/wiki/INI_file). A simple example might look like:
    
    
    ; This is a simple php.ini file on App Engine
    ; It enables output buffering for all requests by overriding the
    ; default setting of the PHP interpreter.
    output_buffering = "On"
    

A list of the core directives, along with their changeable mode values, is [published on php.net](http://php.net/manual/en/ini.list.php).

You can override any PHP directive that has one of the following changeable mode values:

  * `PHP_INI_SYSTEM`
  * `PHP_INI_ALL`
  * `PHP_INI_PERDIR`



You can enable a set of [dynamically loadable extensions](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime#dynamically_loadable_extensions) by using the `extension` directive.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
