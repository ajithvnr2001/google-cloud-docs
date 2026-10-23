---
url: https://docs.cloud.google.com/web-risk/docs/status-codes/
title: HTTP status codes \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:15.960931+00:00
---

# HTTP status codes  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/status-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HTTP status codes

HTTP status codes the server can generate in response to HTTP requests:

  * `200 OK`: Successful request.
  * `400 Bad Request`: Invalid argument (invalid request payload).
  * `403 Forbidden`: Permission denied (e.g. invalid API key).
  * `429 Resource Exhausted`: Either out of resource quota or reaching rate limiting.
  * `500 Internal Server Error`: Internal server error (retry your request).
  * `503 Service Unavailable`: Unavailable.
  * `504 Gateway Timeout`: Deadline exceeded (retry your request).

**Note:** Clients that receive an unsuccessful HTTP response (that is, any HTTP status code other than `200 OK`) must enter [back-off mode](https://docs.cloud.google.com/web-risk/docs/request-frequency#back-off-mode).

Possible reasons for receiving HTTP status code `400 Bad Request`:

  * [`hashes.search`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/hashes/search): Invalid hash.
  * [`threatLists.computeDiff`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/threatLists/computeDiff): Empty update request, or invalid configuration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
