---
url: https://docs.cloud.google.com/error-reporting/docs/setup/cloud-run/
title: Setting up on Cloud Run \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:25.102759+00:00
---

# Setting up on Cloud Run  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Setting up on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Error Reporting lets you monitor and diagnose application crashes in Cloud Run by automatically detecting stack traces written to `stdout` or `stderr`. If exceptions aren't detected, then you can [instrument your service](https://docs.cloud.google.com/error-reporting/docs/setup#libraries) with Error Reporting client libraries or [manually format error messages](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages) in Cloud Logging.

## Viewing errors

To view exception logs in Cloud Run, go to the **Metrics** tab of the [service detail page](https://docs.cloud.google.com/run/docs/managing/services#details). It includes a table showing the top errors for Cloud Run that Error Reporting has detected and aggregated.

For instructions on viewing error and exception data for your application in the Google Cloud console, go to [Viewing errors](https://docs.cloud.google.com/error-reporting/docs/viewing-errors).

**Note** : If you see the message "Set up Error Reporting" on the **Error Reporting** page, then your Google Cloud project has no error groups to display.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
