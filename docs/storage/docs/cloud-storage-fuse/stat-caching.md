---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching/
title: Stat caching in Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:53.497655+00:00
---

# Stat caching in Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Stat caching in Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

Stat caching in Cloud Storage FUSE accelerates file metadata operations for applications that frequently check file attributes, such as applications that repeatedly check whether a file has changed. By caching file metadata, stat caching helps reduce the number of `GetMetadata` calls to Cloud Storage.

## Benefits of stat caching

  * **Improved performance for file attribute operations** : stat caching stores object metadata such as file size, modification time, permissions, and other standard file attributes. Enabling stat caching significantly speeds up operations that query these attributes because Cloud Storage can often retrieve this information from the local cache.

  * **Reduced latency** : By serving metadata from the local stat cache, Cloud Storage FUSE avoids network round trips to Cloud Storage for a stat object request, lowering latency of metadata-heavy operations.

  * **Negative stat caching** : you can cache information about non-existent files or directories, meaning if an application frequently checks for a file that isn't there, the negative result can be cached for a short time to live (TTL), preventing repeated lookups to Cloud Storage for the same non-existent path.




## Configure stat caching

The stat cache is enabled by default. Configure it by using the `gcsfuse` command.

To set the maximum size of the cache, provide a value for one of the following:

  * `gcsfuse` option: [`--stat-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#stat-cache-max-size-mb)
  * Configuration file field: [`metadata-cache:stat-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#stat-cache-max-size-mb)

**Note:** This property is a mount-level limit, and actual memory usage might be lower than the value you specify. Alternatively, you can set the property to a value of `-1` to let the stat cache use as much memory as needed.

For more information about default and recommended values for configuring the stat cache, see the [Cloud Storage FUSE CLI reference](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#stat-cache-max-size-mb) and [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#stat-cache-max-size-mb) pages.

## Configure negative stat caching

Cloud Storage FUSE also offers a negative stat caching capability, which lets you set a TTL for stat cache entries for non-existent files, or negative results. The TTL of the negative stat cache is controlled using one the following methods:

  * `gcsfuse` option: [`--metadata-cache-negative-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#metadata-cache-negative-ttl-secs)
  * Configuration file field: [`metadata-cache:negative-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#negative-ttl-secs)



To learn more about stat caching, see [Cloud Storage FUSE semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md#caching) in the Cloud Storage FUSE GitHub documentation.

## What's next

  * Review [considerations for caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#considerations).

  * Read more about [how to improve performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
