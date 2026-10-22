---
url: https://docs.cloud.google.com/error-reporting/docs/setup/cloud-functions/
title: Setting up on Cloud Run functions \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:25.501620+00:00
---

# Setting up on Cloud Run functions  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/cloud-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Setting up on Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Run functions](https://docs.cloud.google.com/functions/docs) lets you monitor and diagnose runtime errors by automatically writing unhandled exceptions to Cloud Logging. Error Reporting evaluates these logged stack traces without requiring a client library, and Cloud Run functions automatically grants default credentials if you use a client library.

**Note:** Error Reporting automatically creates an error event when a log entry contains a stack trace and the severity level of the log entry isn't set or is set to at least `ERROR`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
