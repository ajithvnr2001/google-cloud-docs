---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/list-caching/
title: List caching in Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:52.916231+00:00
---

# List caching in Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/list-caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  List caching in Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

List caching in Cloud Storage FUSE accelerates directory listing operations by serving repeated listings of the same directory from an in-memory cache. List caching helps you speed up directory traversal for workloads that frequently list the entire contents of a directory, such as jobs that iterate over a large set of files at the beginning of processing.

## Benefits of list caching

  * **Faster directory listing operations** : list caching provides improved performance for operations that list the contents of directories. When list caching is enabled, the results of Cloud Storage object listings for a directory are cached in memory. Subsequent listings of the same directory can be served directly from this cache.

  * **Reduced latency** : by serving list results from the local cache, Cloud Storage avoids network round trips to Cloud Storage to fetch the object list, significantly reducing the latency of directory listing operations, especially for directories containing many objects or when network latency is high.

  * **Improved performance for repetitive workloads** : workloads that repeatedly scan the same directories, such as artificial intelligence and machine learning (AI/ML) training jobs, build processes, or file synchronization tools, can see performance gains.

  * **In-memory storage** : The list cache is kept in memory in the page cache, which is controlled by the kernel based on memory availability, as opposed to the stat cache, which is kept in your machine's memory and controlled by Cloud Storage FUSE.




## Configure list caching

You can enable list caching using one of the following methods:

  * `gcsfuse` option: [`--kernel-list-cache-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#kernel-list-cache-ttl-secs)
  * Configuration file field: [`file-system:kernel-list-cache-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file)



## List cache invalidation

List cache invalidation is set by specifying a value greater than `0` using one of the following methods:

  * `gcsfuse option`: `--kernel-list-cache-ttl-secs`
  * Configuration file field: `file-system:kernel-list-cache-ttl-secs`



The directory list response is kept in the kernel's page cache and remains valid for the amount of time you specified. When you specify a value of `-1`, Cloud Storage FUSE disables list cache expiration and returns the list response from the cache when it's available. Specifying a value of `0` disables the list cache.

## What's next

  * Review [considerations for caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#considerations).

  * Read more about [how to improve performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
