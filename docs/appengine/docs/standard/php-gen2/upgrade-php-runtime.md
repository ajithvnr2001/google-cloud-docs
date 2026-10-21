---
url: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/upgrade-php-runtime/
title: Upgrade an existing application \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:34.250960+00:00
---

# Upgrade an existing application  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/php-gen2/upgrade-php-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Upgrade an existing application Stay organized with collections  Save and categorize content based on your preferences. 

You must upgrade your applications to the [latest supported runtime version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#php) to continue receiving security updates and be eligible for technical support.

The process of upgrading an existing app depends on the runtime version that your app currently uses:

  * **PHP 5.5 (first-generation runtime)** : You must migrate your app to the [latest supported PHP version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#php). PHP 5.5 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on January 30, 2024. Your existing PHP 5.5 applications will continue to run and receive traffic. However, App Engine might block re-deployment of applications that use runtimes [after their end of support date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#php). To migrate to the latest supported version of PHP, see [Migrate from PHP 5.5 to the latest PHP runtime](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/php-differences).

  * **PHP second-generation runtimes (after end of support)** : To upgrade to a [supported version of PHP](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#php), update the `app.yaml` file by specifying a version of PHP that you want your app to run. For example:
        
        runtime: phpVERSION
        

Where VERSION is the PHP `MAJOR` and `MINOR` version numbers. For example, to use the latest PHP version, PHP 8.5, specify `85`. For more information, see the [PHP runtime overview](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
