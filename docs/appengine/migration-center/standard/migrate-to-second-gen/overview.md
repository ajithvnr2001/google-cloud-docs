---
url: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/overview/
title: Overview \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:37.939624+00:00
---

# Overview  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

The App Engine first-generation legacy runtimes, such as Python 2.7, Java 8, Go 1.11, and PHP 5.5 runtimes have been deprecated on January 31, 2026. You won't be able to deploy these runtimes, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing applications will continue to run and receive traffic after their deprecation date. We recommend that you migrate to the latest supported version for your runtime as soon as possible. To migrate to the latest version for your runtime, see the following guides:

  * [Migrate to the latest supported version of Go](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/go-differences).
  * [Migrate to the latest supported version of Java](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/java-differences).
  * [Migrate to the latest supported version of PHP](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/php-differences).
  * [Migrate to the latest supported version of Python](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences).



You should also consider migrating to Cloud Run, the latest evolution of Google Cloud Serverless. Cloud Run is designed to improve upon the App Engine experience, incorporating many of the best features of both the App Engine standard environment and the App Engine flexible environment. To compare features and understand how to migrate, see the [App Engine and Cloud Run comparison guide](https://docs.cloud.google.com/appengine/migration-center/run/compare-gae-with-run).

If you used the App Engine legacy bundled services, you can either:

  * Upgrade your app to replace the bundled service with [Cloud Client Libraries](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services) and the equivalent Google Cloud service.
  * Migrate your app to use the App Engine legacy bundled services for second-generation runtimes where supported. See the [available App Engine legacy bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview).



The following diagram shows a simplified view of migrating from first-generation runtimes to second-generation runtimes.

![Overview of the migration paths for moving your apps to the second-generation runtimes in the standard environment.](https://docs.cloud.google.com/static/appengine/images/migrate-gen2-overview.svg)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
