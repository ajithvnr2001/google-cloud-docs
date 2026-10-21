---
url: https://docs.cloud.google.com/binary-authorization/docs/ga-migration-guide/
title: GA migration guide \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:09.530991+00:00
---

# GA migration guide  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/ga-migration-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  GA migration guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** **Binary Authorization Beta API users:** Support for the Binary Authorization Beta API was discontinued on September 16, 2019. As a result, **the Binary Authorization Beta API will stop working after March 16, 2020. To prevent service interruption, you must take actions outlined in this page to migrate to the GA version.**

If you do not have workloads that use the Binary Authorization Beta version, no action is required on your part.

**Note:** **Artifact Analysis Beta API users:** Use the GA version of the [Artifact Analysis API](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest).

[Binary Authorization is now generally available](https://docs.cloud.google.com/binary-authorization/docs/release-notes#September_16_2019). If your workloads use the Binary Authorization Beta API, perform the following steps to migrate to the GA version.

## Migration steps

The GA version of Binary Authorization provides an updated REST API and `gcloud` command set. Update any scripts or automations that access these interfaces as follows:

  * **REST API**

Use GA REST API endpoints relative to the following URL `https://binaryauthorization.googleapis.com/v1/` instead of `https://binaryauthorization.googleapis.com/v1beta1`.

When you [create a new attestor](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-rest) when calling the GA version of the REST API, you send a JSON message that describes the attestor as part of the request. In the Beta version of the API, the JSON message contained a field named `UserOwnedDrydockNote`. In the GA version, the name of this field is `UserOwnedGrafeasNote`.

  * **Google Cloud CLI**

Use GA `gcloud` commands in `gcloud container binauthz` instead of `gcloud beta container binauthz`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
