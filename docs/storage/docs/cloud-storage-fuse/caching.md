---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching/
title: Overview of caching in Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:56.585210+00:00
---

# Overview of caching in Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Overview of caching in Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage FUSE offers three types of optional caching that help you improve the performance of data retrieval: file caching, list caching, and stat caching. This document describes each cache type and how you can configure it.

The following table describes each type of caching:

Caching type | Description  
---|---  
[File caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching) | Accelerates file data reads for read-heavy workloads that repetitively access data, especially artificial intelligence and machine learning training where the same large files are read multiple times, significantly reducing latency.  
[List caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/list-caching) | Accelerates directory listing operations for workloads that frequently list the entire contents of a directory, such as iterating over a large set of files at the beginning of a processing job, improving the speed of directory traversal.  
[Stat caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching) | Accelerates file metadata operations for applications that frequently check file attributes, which is common for many applications that repeatedly check if a file has changed, reducing the number of `GetMetadata` calls for Cloud Storage.  
**Note:** Starting Cloud Storage FUSE [v3.8.0](https://github.com/GoogleCloudPlatform/gcsfuse/releases/tag/v3.8.0), Type cache has been merged into Stat cache.

## Considerations

  * Enabling caching can increase performance but reduce consistency, which usually occurs when you access the same bucket using multiple clients with a high change rate. To reduce the impact on consistency, we recommend mounting buckets as read-only. To learn more about caching behavior, see [Cloud Storage FUSE semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md#caching) in the Cloud Storage FUSE GitHub documentation.

  * To avoid cache thrashing, ensure that your entire dataset fits into the cache capacity. Also, consider the maximum capacity and performance that your cache media can provide. If you hit the provisioned cache's maximum performance, capacity limit, or both, it's beneficial to read directly from Cloud Storage which has much higher limits than Cloud Storage FUSE.




## Read path for cached data

The Cloud Storage FUSE cache accelerates repeat reads after they've been ingested to the cache. Both first-time reads and cache misses go directly to Cloud Storage and are subject to normal Cloud Storage network latencies. To improve first-time read performance, see [Pre-populate the metadata cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#pre-populate-the-metadata-cache).

## What's next

  * Learn more about each caching type:

    * [File caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching)

    * [List caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/list-caching)

    * [Stat caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
