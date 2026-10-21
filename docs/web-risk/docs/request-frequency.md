---
url: https://docs.cloud.google.com/web-risk/docs/request-frequency/
title: Request Frequency \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:17.550181+00:00
---

# Request Frequency  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/request-frequency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request Frequency

## Update requests

To prevent server overload and to benefit from optimal protection, the Update API imposes time intervals for how often a client can send requests to the Web Risk server to perform URL checks ([`hashes.search`](https://docs.cloud.google.com/web-risk/docs/update-api#example-hashessearch)) or to update the local database ([`threatLists.computeDiff`](https://docs.cloud.google.com/web-risk/docs/update-api#example-threatlistsComputediff)).

The initial request for data must happen at a random interval between 0 and 1 minutes after the client starts or wakes up. Subsequent requests can happen only after the [minimum wait duration](https://docs.cloud.google.com/web-risk/docs/request-frequency#minimum_wait_duration) or [back-off mode](https://docs.cloud.google.com/web-risk/docs/request-frequency#back_off_mode) time limit has been observed.

## Minimum wait duration

Both the [hashes.search response](https://docs.cloud.google.com/web-risk/docs/update-api#http_post_response_2) and [threatLists.computeDiff response](https://docs.cloud.google.com/web-risk/docs/update-api#http_post_response) have a `minimumWaitDuration` field that clients must obey.

If the `minimumWaitDuration` field **is not set** in the response, clients can update as frequently as they want and send as many `threatListUpdates` or `fullHashes` requests as they want.

If the `minimumWaitDuration` field **is set** in the response, clients cannot update more frequently than the length of the wait duration. For example, if a `fullHashes` response contains a minimum wait duration of 1 hour, the client must not send send any `fullHashes` requests until that hour passes, even if the user is visiting a URL whose hash prefix matches the local database. (Note that clients can update less frequently than the minimum wait duration but this may negatively affect protection.)

## Back-off mode

For the recommended backoff procedure, read our [Service Level Agreement](https://cloud.google.com/web-risk/sla).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
