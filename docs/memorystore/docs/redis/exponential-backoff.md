---
url: https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff/
title: Exponential backoff \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:03.931460+00:00
---

# Exponential backoff  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/exponential-backoff/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Exponential backoff Stay organized with collections  Save and categorize content based on your preferences. 

[Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) is a standard error handling strategy for network applications in which a client periodically retries a failed request with increasing delays between requests. Clients should use exponential backoff for all requests to Memorystore for Redis that return HTTP `5xx` and `429` response code errors.

Understanding how exponential backoff works is important if you are:

  * Building client applications that use the Memorystore for Redis [REST API](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest) directly.

  * Accessing Memorystore for Redis through a [client library](https://docs.cloud.google.com/memorystore/docs/redis/libraries). Note that some client libraries, such as the [Memorystore for Redis Client Library for Node.js](https://googleapis.dev/nodejs/redis/latest/index.html), have built-in exponential backoff.




If you are using the [Google Cloud console](https://console.cloud.google.com/), the console sends requests to Memorystore for Redis on your behalf and handles any necessary backoff.

## Example algorithm

An exponential backoff algorithm retries requests exponentially, increasing the waiting time between retries up to a maximum backoff time. An example is:

  1. Make a request to Memorystore for Redis.

  2. If the request fails, wait 1 + `random_number_milliseconds` seconds and retry the request.

  3. If the request fails, wait 2 + `random_number_milliseconds` seconds and retry the request.

  4. If the request fails, wait 4 + `random_number_milliseconds` seconds and retry the request.

  5. And so on, up to a `maximum_backoff` time.

  6. Continue waiting and retrying up to some maximum number of retries, but do not increase the wait period between retries.




where:

  * The wait time is min(((2^`n`)+`random_number_milliseconds`), `maximum_backoff`), with `n` incremented by 1 for each iteration (request).

  * `random_number_milliseconds` is a random number of milliseconds less than or equal to 1000. This helps to avoid cases where many clients get synchronized by some situation and all retry at once, sending requests in synchronized waves. The value of `random_number_milliseconds` should be recalculated after each retry request.

  * `maximum_backoff` is typically 32 or 64 seconds. The appropriate value depends on the use case.




It's okay to continue retrying once you reach the `maximum_backoff` time. Retries after this point do not need to continue increasing backoff time. For example, if a client uses an `maximum_backoff` time of 64 seconds, then after reaching this value, the client can retry every 64 seconds. At some point, clients should be prevented from retrying infinitely.

The maximum backoff and maximum number of retries that a client uses depends on the use case and network conditions. For example, mobile clients of an application may need to retry more times and for longer intervals when compared to desktop clients of the same application.

If the retry requests fail after you exceed the maximum number of retries, then report or log an error using one of the methods listed in [Get support](https://docs.cloud.google.com/memorystore/docs/redis/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
