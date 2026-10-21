---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/caching-large/
title: Antipattern: Store data greater than 256 KB size in cache \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:09:05.014928+00:00
---

# Antipattern: Store data greater than 256 KB size in cache  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/caching-large/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Store data greater than 256 KB size in cache Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/caching-large) documentation._

Apigee provides the ability to store data in a cache at runtime for persistence and faster retrieval.

  * The data is initially stored in the Message Processor's in-memory cache, referred to as _L1 cache_.
  * The L1 cache is limited by the amount of memory reserved for it as a percentage of the JVM memory.
  * The cached entries are later persisted in _L2 cache_ , which is accessible to all Message Processors. More details can be found in the section below.
  * The L2 cache does not have any hard limit on the number of cache entries, however the maximum _size_ of the entry that can be cached is restricted to 256 KB. The cache size of 256 KB is the recommended size for optimal performance.



## Antipattern

This particular antipattern talks about the implications of exceeding the current cache size restrictions within Apigee.

When data > 256 KB is cached, the consequences are as follows:

  * API requests executed for the first time on each of the Message Processors need to get the data independently from the original source (policy or a target server), as entries > 256 KB are not available in L2 cache.
  * Storing larger data (> 256 KB) in L1 cache tends to put more stress on the platform resources. It results in the L1 cache memory being filled up faster and hence lesser space being available for other data. As a consequence, one will not be able to cache the data as aggressively as one would like to.
  * Cached entries from the Message Processors will be removed when the limit on the number of entries is reached. This causes the data to be fetched from the original source again on the respective Message Processors.



![Two flow diagrams.
  One for size<=512KB that shows flows between API Proxy and Message Processors
  and flows between Message Processors and Persistent Storage L2 Cache. One for size>512KB that shows
  flows between API Proxy and Message Processors and flows between Message Processors and Data/Response
  not stored in L2 Cache.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/antipatterns/256cache.png)

## Impact

  * Data of size > 256 KB will not be stored in L2/persistent cache.
  * More frequent calls to the original source (either a policy or a target server) leads to increased latencies for the API requests.



## Best practice

  * It is preferred to store data of size < 256 KB in cache to get optimum performance.
  * If there's a need to store data > 256 KB, then consider: 
    * Using any appropriate database for storing large data 

**OR**

    * Compressing the data



## Further reading

  * [Cache internals](https://docs.cloud.google.com/apigee/docs/api-platform/cache/cache-internals)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
