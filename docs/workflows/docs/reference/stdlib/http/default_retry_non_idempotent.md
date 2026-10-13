---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_non_idempotent/
title: Object: http.default_retry_non_idempotent \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:07.389717+00:00
---

# Object: http.default_retry_non_idempotent  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry_non_idempotent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Object: http.default_retry_non_idempotent Stay organized with collections  Save and categorize content based on your preferences. 

Simple default retry policy for non-idempotent targets.

If your target is idempotent, use [default_retry](https://docs.cloud.google.com/workflows/docs/reference/stdlib/http/default_retry) instead.

Retries on `429` (Too Many Requests) and `503` (Service Unavailable), as well as on `ConnectionFailedError`.

Uses `max_retries` of 5, and `backoff` as per `retry.default_backoff`.

For more information, see [Retry steps](https://docs.cloud.google.com/workflows/docs/reference/syntax/retrying).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
