---
url: https://docs.cloud.google.com/appengine/docs/flexible/php/customizing-the-php-runtime/
title: Customizing the PHP Runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:09.479901+00:00
---

# Customizing the PHP Runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/php/customizing-the-php-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Customizing the PHP Runtime Stay organized with collections  Save and categorize content based on your preferences. 

You can use [custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) to add additional functionality to a PHP app running in the App Engine flexible environment. To configure a custom runtime, replace the following line in your [`app.yaml` file](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml):
    
    
    runtime: php
    

with this line:
    
    
    runtime: custom
    

You must also [specify a base image](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base) by adding a Dockerfile in the same directory that contains the `app.yaml` file.

Visit the [Custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) documentation to learn how to define a Dockerfile in a custom runtime.

## Health checking

By default, all programs running in the flexible environment receive [health check requests](https://docs.cloud.google.com/appengine/docs/flexible/how-instances-are-managed). Make sure to write your own code to handle health check request, or disable health checks if needed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
