---
url: https://docs.cloud.google.com/appengine/docs/standard/bundled-services-overview/
title: Overview of legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:46.192405+00:00
---

# Overview of legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/bundled-services-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Overview of legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Historically, the App Engine standard environment provided several scalable, proprietary services for app development. These services were bundled with [first-generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/runtimes) (also called App Engine _legacy runtimes_), which include Python 2, Java 8, Go 1.11, and PHP 5.5. Because several of the legacy runtimes are no longer maintained by their respective open-source communities, as an App Engine developer, you may face hard choices on whether to invest time and effort in migrating to a newer runtime or else incur growing costs to retain your app on a legacy runtime.

Recognizing this challenge, Google Cloud is committed to providing you with a more incremental migration path to newer runtimes. To reduce runtime migration complexity, Google Cloud now supports a set of App Engine legacy bundled services and their associated APIs on second-generation runtimes, which include [Python 3](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime), [Java 11+](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime), [Go 1.12+](https://docs.cloud.google.com/appengine/docs/standard/go/runtime), and [PHP 7+](https://docs.cloud.google.com/appengine/docs/standard/php-gen2/runtime). Your app can call legacy bundled services APIs for second-generation runtimes through language-idiomatic libraries.

![Accessing App Engine bundled services in first- and second generation runtimes](https://docs.cloud.google.com/static/appengine/docs/images/bundled-services.svg)**Figure 1.** How apps access the App Engine legacy bundled services

In runtime migration scenarios, you often also have the option to use Google Cloud products that offer similar functionality as the legacy bundled services. For the legacy bundled services that are not available as separate products in Google Cloud, such as image processing, search, and messaging, you can use third-party providers or other workarounds as suggested in the Runtimes guide.

To learn more about these options for migrating your app, see [Migrate off of legacy bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
