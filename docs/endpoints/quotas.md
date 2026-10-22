---
url: https://docs.cloud.google.com/endpoints/quotas/
title: Quotas \u00a0|\u00a0 Cloud Endpoints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:26.741311+00:00
---

# Quotas  |  Cloud Endpoints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

This section describes the Service Control's quota limits.

### Request rate limits

A rate limit of 10,000,000 quota units per 100 seconds per service producer project is enforced by default. One quota unit is consumed for each call to [`services.check`](https://docs.cloud.google.com/service-control/reference/rest/v1/services/check) and for each operation reported by [`services.report`](https://docs.cloud.google.com/service-control/reference/rest/v1/services/report).

**Note:** Both ESP and Cloud Endpoints Frameworks employ efficient caching algorithms so they don't call Service Control every time your API is called. So while the default limit is 10,000,000 per 100 seconds, your API can support a much higher volume.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
