---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview/
title: FlexCache overview \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:01.990541+00:00
---

# FlexCache overview  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  FlexCache overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the FlexCache feature. The volume instructions provided on this page don't apply to Flex Unified ONTAP-mode. You can't create, view, update, or delete ONTAP-mode volumes using the Google Cloud console or Google Cloud CLI.

## About FlexCache

NetApp FlexCache accelerates data access, reduces WAN latency, and lowers WAN bandwidth costs for read-intensive workloads, especially when clients repeatedly access the same data. When you create a FlexCache volume, it acts as a remote cache of an existing (origin) volume. This cache stores only frequently accessed hot data of the origin volume.

When a FlexCache volume receives a read request for hot data it contains, it responds faster than the origin volume because the data has a shorter distance to travel to the client. If a FlexCache volume receives a read request for infrequently accessed cold data, it retrieves the required data from the origin volume, stores it, and then serves the client request. Subsequent read requests for that data are then served directly from the FlexCache volume. After the first request, the data no longer needs to travel across the network, or be served from a heavily loaded system.

While applications can write to a FlexCache volume, these writes are sent to the origin volume to maintain cache coherence.

The integration of FlexCache with Google Cloud NetApp Volumes lets you provision cache volumes within your Google network to improve performance for hybrid cloud environments. This feature supports the transition of workloads to the hybrid cloud by caching data from an on-premises data center to the cloud.

Volumes in NetApp Volumes can only serve as cache volumes, except for Flex Unified ONTAP-mode volumes, which can also act as origin volumes.

FlexCache has the following characteristics:

  * Write behavior

  * Cache invalidation due to access time updates

  * Global file locking

  * CIFS change notifications

  * Cache prepopulation




### Write behavior

FlexCache ensures that data you read from the origin or any of its caches is always up to date. To manage writes in environments where data can be written to the origin or any cache, FlexCache provides the following strategies to handle these write operations.

  * Write-around

  * Write-back




#### Write-around

Write-around is the default cache setting. It is recommended for environments with read-intensive workloads or where only small files are written.

When data is written to a FlexCache volume, the write operation is passed to the origin volume. The cache acknowledges the write once the origin confirms it. Writing to a file invalidates its cached copy, and the cache retrieves it again upon the next access.

This strategy provides LAN-like read latency for cached data. However, write throughput depends on the network connection to the origin. If the network between the origin and a cache fails, users can still access data in the cache.

#### Write-back

Write-back is suitable only for specific workloads. It provides fast write speed for heavy writes to large files. Write-back isn't recommended for workloads with many small writes to multiple files, because the overhead of managing data consistency between the origin and all caches reduces performance significantly.

Before enabling write-back for FlexCache, first review the [ONTAP FlexCache write-back guidelines](https://docs.netapp.com/us-en/ontap/flexcache-writeback/flexcache-write-back-guidelines.html), understand the [architecture](https://docs.netapp.com/us-en/ontap/flexcache-writeback/flexcache-write-back-architecture.html) implications, and check if your environment matches the documented [workload profile](https://docs.netapp.com/us-en/ontap/flexcache-writeback/flexcache-write-back-use-cases.html). Write-around is the recommended option unless you can verify that your workload is appropriate for write-back.

Users can optionally enable write-back support. When write-back is enabled, clients can write large amounts of data to a cache with LAN-like performance. The cache then sends these changes to the origin. Because a client's write speed to the cache might exceed the rate at which data is sent to the origin, the cache temporarily stores the changes until they are completely flushed to the origin. During the period a client is writing to a file, the origin and all other caches block read calls for that file until the write operation is completed.

The write-back strategy provides LAN-like read and write performance to cached data. However, if either the caches or the origin lose connectivity, all read and write operations are blocked.

### Cache invalidation due to access time updates

ONTAP provides a volume-level field called `-atime-update` to manage access time updates on files and directories that are read using `READ`, `READLINK`, and `READDIR`.

Access time updates on either origin or cache volumes can trigger file invalidations that reduce cache effectiveness and cause slow performance and high latency for file access. To prevent this, disable access time updates on the origin volume using the ONTAP [`volume modify -atime-update`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-modify.html#description) command. In the scenarios where you need access time to reflect recent reads, use the [`volume modify -atime-update-period`](https://docs.netapp.com/us-en/ontap-cli-9131/volume-modify.html#description) command to define a period during which access time updates are stopped. For example, setting it to `86400` seconds results in access time updates only once a day.

FlexCache volumes in NetApp Volumes inherit the `-atime-update` setting from the origin, which can increase cache invalidations. Therefore, we recommend that you disable access time updates on the origin volume.

### Global file locking

Global file locking enforces deny-read and exclusive byte-range locks on files across all caches and the origin volume. If these locks must be strictly enforced in your workflow to maintain data consistency or prevent access conflicts, enable global file locking.

**Note:** This feature is disabled by default.

#### Considerations

Enable global file locking only if you have reliable connectivity between the cache and the origin. Unstable connections can delay or suspend modifications, or result in timeouts if FlexCache volumes are offline.

  * **Performance impact** : enabling global file locking increases latency because every cache read triggers a request to the origin for lock validation, increasing the round-trip time (RTT).

  * **Availability impact** : if a cache volume goes offline, reads of its files are blocked across all other cache volumes, and modifications to the origin volume are suspended until all FlexCache volumes are back online.




As global file locking can affect system performance and reliability, keep it disabled unless your workflow explicitly requires it.

### CIFS change notifications

The SMB protocol provides a mechanism to notify SMB clients of changes made to a volume by other clients. This allows applications, such as Windows File Explorer, to update their views without polling the volume. This optional feature is useful for caches where interactive users access files on SMB volumes through Windows Explorer. Otherwise, it should be disabled to reduce notification load.

**Note:** The feature is disabled by default.

### Cache prepopulation

FlexCache accelerates read access by caching data upon first read from an origin and helps ensure cache coherency, keeping the origin and all caches synchronized. As a result, the initial file access has WAN-like read performance, but subsequent reads are as fast as local reads.

If you know what specific data is required in your cache, you can use cache prepopulation. Prepopulation lets you instruct the cache to fetch specific files and folders before their first use, to accelerate reads on first access.

To start a [prepopulation](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/prepopulate-flexcache-volume) job, you must provide the cache with a list of file or directory paths. You also have the option to enable recursion, which can fetch all content within sub-directories.

A prepopulation job's execution time can vary depending on the amount of data to prepopulate and the network speed between the cache and origin. FlexCache lets you monitor the status of a prepopulation job whether it is still running or completed.

## What's next

[Plan FlexCache volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/plan-flexcache-volumes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
