---
url: https://docs.cloud.google.com/appengine/docs/deprecations/appstats-to-trace-migration/
title: Migrating from Appstats to Cloud Trace \u00a0|\u00a0 App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:56.371093+00:00
---

# Migrating from Appstats to Cloud Trace  |  App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/deprecations/appstats-to-trace-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)



Send feedback 

#  Migrating from Appstats to Cloud Trace Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Trace provides a feature set similar to Appstats. It is turned on automatically for all applications running in the App Engine standard environment. _You don't add or change any code or configuration to your application to support Trace!_

To migrate your Java application away from Appstats:

  1. Refer to the [Appstats](https://docs.cloud.google.com/appengine/docs/standard/java/tools/appstats) page for a listing of the files and the content that was added to support Appstats.
  2. Using that page as a guide, 
     * Remove the `appengine-apis-labs.jar` dependency from your build file (Maven or Gradle), so that it is removed from the `WEB-INF/lib` area of your web application. This removal applies to all versions of `appengine-apis-lab.jar`from the [Maven repository](https://mvnrepository.com/artifact/com.google.appengine/appengine-api-labs) or from the App Engine SDK.
     * From your `web.xml`, remove all `filter` and `filter-mapping` elements referring to `appstats`.
     * From your `web.xml`, remove all `servlet` and `servlet-mapping` elements referring to `appstats`.
     * Make sure all references to `AppstatsFilter` are deleted from your `web.xml`.
  3. Rebuild and redeploy your app.



At this point, your application no longer uses Appstats or the Appstats console, but you can find comparable information about your app in the Cloud Trace console. For more information about using Trace, see the [Cloud Trace Quickstart](https://docs.cloud.google.com/trace/docs/trace-app-latency).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
