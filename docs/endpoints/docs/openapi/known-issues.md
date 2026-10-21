---
url: https://docs.cloud.google.com/endpoints/docs/openapi/known-issues/
title: Known issues \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:22:56.602834+00:00
---

# Known issues  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This page contains known issues in Cloud Endpoints for OpenAPI.

## Paths with trailing slashes aren't supported

When you deploy an OpenAPI document by using the `gcloud endpoints services deploy` command, Cloud Endpoints rejects OpenAPI documents that include paths with trailing slashes.

See [OpenAPI feature limitations](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-limitations) for other unsupported OpenAPI features.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
