---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/cannot-find-fromimage-field/
title: Can't find the fromImage migration plan field \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:12.511440+00:00
---

# Can't find the fromImage migration plan field  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/cannot-find-fromimage-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Can't find the fromImage migration plan field

If you're customizing a migration plan for a Tomcat server and can't find the `fromImage` migration plan field of type `string`, then this is because starting from Migrate to Containers modernization plugins version 1.4.0, the `fromImage` field has been replaced by the `baseImage.name` property of type `string`.

If you've upgraded to Migrate to Containers modernization plugins version 1.4.0 or later, then to specify the Docker community image or provide your own Docker image to use as the base image for the migration, use the `baseImage.name` property instead.

For more information, see the [Migrate to Containers modernization plugins release notes](https://docs.cloud.google.com/migrate/containers/docs/release-notes#November_29_2023).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
