---
url: https://docs.cloud.google.com/storage/docs/rapid/rapid-cache/
title: Rapid Cache \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:57.435101+00:00
---

# Rapid Cache  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/rapid-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Rapid Cache Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Anywhere Cache is now renamed Rapid Cache. When using Rapid Cache with certain tools, you might still see the name Anywhere Cache being referenced in the tool's interface or surface. 

This page describes Rapid Cache, a feature that provides an SSD-backed zonal read cache for Cloud Storage buckets that can increase throughput and lower latency on your stored data. Rapid Cache provides storage capacity and bandwidth that automatically scale up or down to your needs. Rapid Cache is a fully managed service and returns consistent data.

Rapid Cache is helpful for improving read-heavy workload performance and reducing network costs. For more information, see Benefits.

See [Create and manage caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache) to learn how to create and manage caches using Rapid Cache.

## How does Rapid Cache work?

Rapid Cache lets you create caches in the same zone as your workloads. When you create a cache in a zone, data read requests originating from the zone are processed by the cache instead of the bucket. Each cache serves clients within the same zone as the cache.

Data from a bucket gets ingested into a cache when it's read by a VM that resides in the same zone as the cache. If you configure the ingest-on-write behavior, data is also ingested into the cache when it's written to the bucket.

Metadata is not cached. Requests for object metadata are always processed by the bucket instead of the cache.

For more information about how data gets ingested into a cache, see Data ingestion. You can configure a cache's Time to Live (TTL) and ingest-on-write behavior when you create or update the cache.

### Benefits

When you cache your data with Rapid Cache, you get the following benefits:

  * **Get faster data access** : Rapid Cache co-locates your data in the same zone as your compute resources and is fully backed by SSD. This enables your workloads to get up to 2.5 TB/s of throughput and reduces latency for faster reads.

  * **Reduce multi-region data transfer fees** : Data that's read from the cache is charged [reduced data transfer fees](https://docs.cloud.google.com/storage/pricing#rapid-cache) compared to data that's read directly from a multi-region bucket.

  * **Reduce retrieval fees** : Retrieval fees for buckets in Nearline storage, Coldline storage, and Archive storage don't apply for data reads from the cache.

  * **Accrue lower costs from read operations** : Read operations served from Rapid Cache are priced lower than Class B operations served from a bucket in Standard storage.

  * **Autoscale your cache size** : Rapid Cache's dynamic SSD caching scales automatically based on usage without you needing to specify a cache size.

  * **Use caches efficiently** : Rapid Cache can be enabled on existing buckets without requiring changes to your existing applications or APIs. Data stored within Rapid Cache is strongly consistent.




For details about pricing, see [Rapid Cache pricing](https://docs.cloud.google.com/storage/pricing#rapid-cache). For information about quotas, see [Rapid Cache quotas](https://docs.cloud.google.com/storage/quotas#rapid-cache).

### When should you use Rapid Cache?

Use Rapid Cache for data that's infrequently changed and frequently read to accelerate data reads for analytics workloads and AI/ML model training and loading.

Say you're training an AI model across many [Google Kubernetes Engine nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes), all repeatedly reading data that's stored in your Cloud Storage buckets and running in the same zone. When you create a cache in the zone where your workload is running, the cache provides extra bandwidth and helps you reduce the data transfer fees associated with reading data in multi-region buckets, letting you run larger, scaled workloads more efficiently.

## Cache size and bandwidth limit autoscaling

Rapid Cache provides temporary storage capacity and bandwidth that automatically scale up or down according to the amount of data stored in a cache.

The cache bandwidth limit starts at 100 Gbps and scales at the rate of 20 Gbps per 1 TiB of stored data. You can increase the starting bandwidth or total bandwidth limit by increasing the amount of data stored in the cache, creating more caches in a zone, or contacting your Technical Account Manager or Google representative.

To learn more about size and bandwidth limits for Rapid Cache, see [Cloud Storage quotas & limits](https://docs.cloud.google.com/storage/quotas#rapid-cache).

## Caching data in zones

When you create a cache for a bucket, the cache must be created in a zone within the location of your bucket. For example, if your bucket is located in the `us-east1` region, you can create a cache in `us-east1-b` but not `us-central1-c`. If your bucket is located in the `ASIA` dual-region, you can create a cache in any zones that make up the `asia-east1` and `asia-southeast1` regions.

For each bucket, you can create a maximum of one cache per zone. For example, if a bucket is located in the `us-east1` region, you could create a cache in `us-east1-b` and another cache in `us-east1-c`. If a bucket is located in a multi-region that encompasses `us-central1` and `us-east1`, you could create a cache in `us-central1-a` and another cache in `us-east1-b`.

You can create caches in zones as long as capacity is available for the zone. If the capacity for creating a cache is unavailable, Rapid Cache continues trying to create a cache until the capacity becomes available or the creation process is cancelled by the user. The capacity might remain unavailable for a long period of time.

You can use Rapid Cache in the following zones. These zones can be used depending on the location type of your bucket.

#### Asia

The following table shows the zones and location types that are available for Rapid Cache in the Asia geographical area.

Zone name | Region | Dual-region | Multi-region | Custom dual-region  
---|---|---|---|---  
`asia-east1-a` |  check |  |  check |  check  
`asia-east1-b` |  check |  |  check |  check  
`asia-east1-c` |  check |  |  check |  check  
`asia-northeast1-a` |  check |  check |  |   
`asia-northeast1-b` |  check |  check |  |   
`asia-northeast1-c` |  check |  check |  |   
`asia-south1-a` |  check |  |  |   
`asia-south1-b` |  check |  |  |   
`asia-south1-c` |  check |  |  |   
`asia-southeast1-a` |  check |  |  check |  check  
`asia-southeast1-b` |  check |  |  check |  check  
`asia-southeast1-c` |  check |  |  check |  check  
  
#### Europe

The following table shows the zones and location types that are available for Rapid Cache in the Europe geographical area.

Zone name | Region | Dual-region | Multi-region | Custom dual-region  
---|---|---|---|---  
`europe-north1-a` |  check |  check |  |   
`europe-north1-b` |  check |  check |  |   
`europe-north1-c` |  check |  check |  |   
`europe-west1-b` |  check |  check |  check |  check  
`europe-west1-c` |  check |  check |  check |  check  
`europe-west1-d` |  check |  check |  check |  check  
`europe-west3-a` |  check |  |  check |  check  
`europe-west3-b` |  check |  |  check |  check  
`europe-west3-c` |  check |  |  check |  check  
`europe-west4-a` |  check |  check |  check |  check  
`europe-west4-b` |  check |  check |  check |  check  
`europe-west4-c` |  check |  check |  check |  check  
`europe-west4-ai1a` ([AI zone](https://docs.cloud.google.com/storage/docs/ai-zones))  |  check |  |  |   
`europe-west6-a` |  check |  check |  |   
`europe-west6-b` |  check |  check |  |   
  
#### United States

The following table shows the zones and location types that are available for Rapid Cache in the United States geographical area.

Zone name | Region | Dual-region | Multi-region | Custom dual-region  
---|---|---|---|---  
`us-central1-a` |  check |  check |  check |  check  
`us-central1-b` |  check |  check |  check |  check  
`us-central1-c` |  check |  check |  check |  check  
`us-central1-f` |  check |  check |  check |  check  
`us-central1-ai1a` ([AI zone](https://docs.cloud.google.com/storage/docs/ai-zones))  |  check |  |  |   
`us-east1-b` |  check |  check |  check |  check  
`us-east1-c` |  check |  check |  check |  check  
`us-east1-d` |  check |  check |  check |  check  
`us-east4-a` |  check |  |  check |  check  
`us-east4-b` |  check |  |  check |  check  
`us-east4-c` |  check |  |  check |  check  
`us-east5-a` |  check |  |  check |  check  
`us-east5-b` |  check |  |  check |  check  
`us-east5-c` |  check |  |  check |  check  
`us-south1-a` |  check |  |  check |  check  
`us-south1-b` |  check |  |  check |  check  
`us-south1-c` |  check |  |  check |  check  
`us-south1-ai1b` ([AI zone](https://docs.cloud.google.com/storage/docs/ai-zones))  |  check |  |  |   
`us-west1-a` |  check |  |  check |  check  
`us-west1-b` |  check |  |  check |  check  
`us-west1-c` |  check |  |  check |  check  
`us-west2-a` |  check |  |  |   
`us-west3-a` |  check |  |  |   
`us-west3-b` |  check |  |  |   
`us-west3-c` |  check |  |  |   
`us-west4-a` |  check |  |  check |  check  
`us-west4-b` |  check |  |  check |  check  
`us-west4-c` |  check |  |  check |  check  
  
## Data ingestion for caches

By default, data is ingested into a cache after it's requested for the first time.

Because the cache is empty when this initial request arrives, the data can't be found inside the cache yet. This results in an **initial cache miss** , where the system retrieves the data from the backing Cloud Storage bucket instead. As the system delivers this retrieved data to the user, it simultaneously ingests the data into the cache.

Once this first request is complete, the data resides in the cache, allowing all subsequent reads to be served directly from the cache as high-speed **cache hits**. This behavior significantly reduces read latency and accelerates data retrieval. The ingested data resides in the cache until its TTL expires, after which the data gets evicted from the cache.

To avoid the slow initial request entirely, you can configure the cache to ingest data on write in addition to ingesting data after the first read.

### Ingesting data as chunks

When ingesting data into a cache, Rapid Cache breaks objects into smaller, fixed-size **chunks**. Breaking objects into chunks allows for more granular caching, especially for large files where only specific parts are accessed.

A chunk is a 2 MB block of data. When a request is made for an object, Rapid Cache identifies which 2 MB chunks cover the requested byte range and manages those chunks independently.

The data ingestion behavior differs depending on the size of the object being ingested into the cache:

  * For read requests to objects larger than 2 MB, only the chunks containing the requested byte range are ingested. For example, reading the first 1 MB of a 100 MB file ingests only the first 2 MB chunk.

  * For read requests to objects smaller than 2 MB (for example, a 500 KB image), the entire object is ingested into the cache.




### Ingesting data on write

When you enable a cache to ingest data on write, data is ingested into the cache the moment it's written to the bucket. This behavior can be optionally enabled in addition to the default cache behavior of ingesting data after the initial read.

The ingest-on-write capability removes initial cache misses and allows your workload to benefit from an immediate cache hit on the very first data read. Ingesting data on write accelerates read-after-write workloads, such as restoring system checkpoints or preparing data pipelines for model training.

You can enable a cache to ingest data on write when you [create](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#create-cache) or [update](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#update-cache) the cache. You can configure a cache to ingest all objects that are written to a bucket (also known as "bucket-level ingest-on-write") or selectively ingest objects that are written to the bucket under a specified [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) (also known as "prefix-level ingest-on-write").

For example, say you enable a cache to perform prefix-level ingest-on-write for objects in the bucket `my-bucket` that have the prefix `red/` in their name. You then upload three objects to `my-bucket`: the objects `red/my-dog.png`, `blue/my-cat.png`, and `red/my-goldfish.png`. As a result, only the objects `red/my-dog.png` and `red/my-goldfish.png` are ingested into the cache upon being uploaded to `my-bucket`.

When configuring prefix-level ingest-on-write using certain tools (like the Google Cloud console), a new managed folder is automatically created for you if you specify a prefix that isn't the name of an existing managed folder. However, when using the JSON API, you must manually create the managed folder and apply `ingestOnWrite` settings for each cache zone. You can find the instructions to enable or disable ingest-on-write using each tool in [Use Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache).

To understand how to enable or disable ingest-on-write at the bucket or prefix level when using the JSON API, expand the **Understanding how to enable ingest-on-write** section. The information in this section mostly pertains only to the JSON API; other tools, such as the Google Cloud console, obfuscate some of the settings to make it easier to enable and manage ingest-on-write.

#### Understanding how to enable ingest-on-write

This section helps you understand what JSON API settings to use to enable ingest-on-write for all objects written to a bucket, or only for selected objects that are written to the bucket under a managed folder prefix.

There are two settings that control whether a cache ingests data on write for all objects in a bucket or only selective objects under a prefix:

  * Bucket-level enablement of ingest-on-write is achieved by using the `ingestOnWrite` field of a [cache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache). The field looks like the following:
        
        {
        "zone": "us-east1-a",
        "ttl": "24h",
        "ingestOnWrite": true
        }

    * If set to `true`, ingest-on-write becomes enabled for all objects written to the bucket. This overrides any managed folder-level settings that enable ingest-on-write for selective objects by prefix.
    * If set to `false`, ingest-on-write becomes disabled on bucket-wide objects. This setting allows the enablement of ingest-on-write for selective objects by prefix through managed folder settings.
  * Prefix-level enablement of ingest-on-write is achieved by using [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders), which represent prefix paths ending in a trailing slash (for example: `my-prefix/`). When prefix-level ingest-on-write is enabled, a cache selectively ingests objects on write only if the object has the prefix in its name.

Prefix-level ingest-on-write is controlled through the `ingestOnWrite` field of the `rapidCacheConfig.policies` mapping in a [managed folder resource](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder). A cache instance must exist in order to be specified in the `rapidCacheConfig.policies` mapping.

The `rapidCacheConfig.policies` mapping of a managed folder looks like the following:
        
        "rapidCacheConfig": {
          "policies": {
            "us-east1-a": {
              "rapidCacheId": "us-east1-a",
              "ingestOnWrite": "unspecified"
            }
            "us-east1-b": {
              ...,
              ...
            }
          }
        }

    * Cache instances that are specified in the `policies` mapping must already exist in order for prefix-level ingest-on-write to work. For example, to specify `rapidCacheId: "us-east1-a"` in the `policies` mapping, you must first have a cache for the zone `us-east1-a`.
    * You can update multiple cache instances specified in the `policies` mapping in a single API call.
    * If `ingestOnWrite` is set to `enabled`, ingest-on-write is enabled for all objects written to the bucket under this managed folder prefix. Prefix-level ingest-on-write can only be enabled if the `ingestOnWrite` field of the cache resource is `false`.
    * If set to `unspecified` (default), the ingest-on-write enablement is inherited from the immediate parent resource, which can be either a parent managed folder or the bucket that contains the managed folder itself.
    * Any caches not specified in the policies mapping are treated as if its `ingestOnWrite` setting is set to `unspecified`.



The following is a summary of how to configure your cache and managed folder resources in order to enable or disable ingest-on-write at the bucket level or prefix level:

  * **Enabling bucket-level ingest-on-write (but not prefix-level)**

    * Configuration: Set the cache resource's `ingestOnWrite` field to `true`.

    * Behavior: Ingest-on-write is enabled for all objects written to the bucket. This bucket-wide setting overrides any managed folder-level configurations (meaning selective prefix-level configurations are bypassed).

  * **Enabling prefix-level ingest-on-write (but not bucket-level)**

    * Configuration:

      1. Set the cache resource's `ingestOnWrite` field to `false`.
      2. Configure a valid `policies` mapping (non-null) in the managed folder resource.
      3. Set the managed folder's `ingestOnWrite` field to `enabled` (or set it to `unspecified` if it is a child folder inheriting `enabled` from an enabled parent managed folder).
    * Behavior: Ingest-on-write only occurs for objects written under matching managed folder prefixes.

  * **Enabling prefix-level ingest-on-write on parent vs. child managed folders**

It's not possible to enable ingest-on-write for child managed folders without also enabling it on the parent managed folder.

  * **Disabling both bucket and prefix ingest-on-write**

    * Configuration:

      1. Set the cache resource's `ingestOnWrite` field to `false`.
      2. Set all managed folders' `ingestOnWrite` fields to `unspecified`, ensuring that no parent managed folders' `ingestOnWrite` field is `enabled`.

Alternatively, don't configure any policies by leaving the `policies` map `null` or omitting the `rapidCacheConfig` configuration altogether.

    * Behavior: Ingest-on-write is disabled globally for the bucket and all prefixes.




When you enable prefix-level ingest-on-write on a parent managed folder, ingest-on-write is enabled for all child managed folders that are nested under the parent managed folder. To learn more about how resources inherit the enablement and disablement of ingest-on-write, expand the **How ingest-on-write inheritance works** section.

#### How ingest-on-write inheritance works

When a managed folder doesn't explicitly enable ingest-on-write (where the managed folder's `ingestOnWrite` field is set to `unspecified`), the cache's ingest-on-write behavior is inherited from the parent resource of the managed folder, whether that's from the bucket or a parent managed folder.

When using ingest-on-write at the prefix level, the ingest-on-write setting that you configure on a parent managed folder is inherited by all child managed folders.

For example, consider the following scenario:

  * You have a managed folder `a/` whose parent resource is the bucket `my-bucket`.
  * You have a managed folder `a/b/` whose parent resource is the managed folder `a/` within `my-bucket`. 



When an object named `a/b/info.txt` is written, Rapid Cache evaluates the configuration hierarchy from top to bottom:

  1. **Check the immediate managed folder** : if `a/b/` is set to `enabled`, prefix-level ingest-on-write is enabled for objects written under `a/b/`. If `a/b/` is set to `unspecified`, Rapid Cache checks the immediate parent resource, which is the managed folder `a/`.
  2. **Check the parent managed folder** : if `a/` is set to `enabled`, prefix-level ingest-on-write is enabled for `a/` and `a/b/`. If `a/` is set to `unspecified`, Rapid Cache checks the parent bucket.
  3. **Check the bucket's cache-level`ingestOnWrite` setting**: If the cache's `ingestOnWrite` field is set to `true`, bucket-level ingest-on-write is enabled and overrides any managed folder that has prefix-level ingest-on-write configured. If the `ingestOnWrite` field of the cache is `false` and the `ingestOnWrite` field of both parent and child managed folders are `unspecified`, ingest-on-write is disabled for objects in the bucket that are under the parent and child managed folders. In this scenario, if there are no other managed folders in the bucket with ingest-on-write configured, ingest-on-write is disabled for all objects in the bucket.



### Time to live (TTL)

A cache's TTL governs how long data stays in the cache before the data gets evicted. The TTL is the duration of time that data remains in the cache from the last read. For example, if the TTL is set to 24 hours, a chunk of data that is last read at 11am on Monday with no subsequent reads is evicted from the cache at 11am on Tuesday.

You can set a cache's TTL when you [create](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#create-cache) or [update](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#update-cache) the cache. You can set a cache's TTL to a value between 24 hours and 7 days, inclusive. If unspecified, the TTL defaults to 24 hours.

## Cache operations

This section describes operations you can perform on Rapid Cache caches. Some operations are asynchronous and return a [long-running operation](https://google.aip.dev/151), while other operations are synchronous, where the operations are done immediately and return an [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

### Create a cache

You can set the location, TTL, and data ingestion behavior of a cache when you [create the cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#create-cache). The cache enters a _CREATING_ state as it's being created and enters a _RUNNING_ state when it becomes actively running. A cache creation operation can take up to 48 hours, after which the operation times out.

The AnywhereCaches Create API is asynchronous. A create operation causes a long-running operation to be returned. The long-running operation provides a status of the create operation and lets you cancel the operation before it's complete.

**Note:** if cancelling the create operation is attempted, the server makes a best effort to cancel the create operation, but success is not guaranteed.

### Update a cache

You can set the TTL or data ingestion behavior of a cache when you [update](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#update-cache) the cache. You can only update caches that are in a _RUNNING_ state. A cache in a _CREATING_ or _DISABLED_ state cannot be updated.

When a cache is in the process of being updated, the `pending_update` field evaluates to `true`. While the `pending_update` field evaluates to `true`, the cache cannot be updated again. When the TTL of a cache has finished updating, the new TTL is immediately applied to both existing and new data in the cache.

The AnywhereCaches Update API is asynchronous and returns a long-running operation.

### Get a cache

When you [get a cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#view-cache), Rapid Cache returns the state and configuration of the cache instance. The AnywhereCaches Get API is synchronous and returns an AnywhereCache resource.

### List caches

You can [return a list](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#list-caches) of associated caches for a given bucket. The AnywhereCaches List API is synchronous and supports [pagination](https://docs.cloud.google.com/storage/docs/paginate-results).

### Disable a cache

You can [disable a cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#disable-cache) to permanently remove the cache from your bucket's configuration. When you disable a cache, it enters a _DISABLED_ state. During this state, you can still read existing data from the cache but you can't ingest new data into the cache.

After you disable a cache, there's a 1-hour grace period during which you can cancel the disablement by resuming the cache. After this 1-hour grace period, the cache gets deleted. When the cache gets deleted, all the data within the cache gets evicted, and the cache is removed from the bucket.

During the 1-hour period before the cache gets deleted, you can revert the _DISABLED_ state by resuming the cache, at which point the cache resumes in the _RUNNING_ state.

The AnywhereCaches Disable API is synchronous and returns an AnywhereCache resource.

### Resume a cache

You can [resume caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#resume-cache) that are in a _DISABLED_ state, as long as the disabled cache is within the 1-hour grace period. After the 1-hour grace period, the resume operation is done at best effort, as the cache could be deleted at any point after the grace period. Once a cache has been resumed, it enters a _RUNNING_ state.

The AnywhereCaches Resume API is synchronous and returns an AnywhereCache resource.

## Rapid Cache recommender

The Rapid Cache recommender provides recommendations and insights for creating caches in bucket-zone pairs by analyzing your data usage and storage. For overview information and instructions on using the Rapid Cache recommender, see [Rapid Cache recommender](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache-recommender).

## Using Rapid Cache to accelerate reads for BigQuery

Rapid Cache can be used to serve data for object read requests issued by BigQuery. Using Rapid Cache, you can accelerate data reads for your applications while optimizing cost efficiency.

While BigQuery is a regional service, its underlying compute resources might occasionally shift between zones for load balancing. As a best practice, enable Rapid Cache for a BigQuery workload in all zones of a region to ensure there's an available cache to use in case the underlying compute resources change zones. If a cache in a zone is not used, it doesn't incur additional cost, as Rapid Cache is pay-per-use. Note that if a workload's resources change zones, the cache in the new zone will need to re-ingest the data, potentially incurring a one-time increase in data ingestion costs.

## Encryption of cached data

Data is stored in the cache in the data's original server-side encrypted format, providing compatibility with the [encryption options](https://docs.cloud.google.com/storage/docs/encryption) supported by Cloud Storage.

## Limitations and restrictions

  * To delete a bucket, you must first delete all its associated caches. The only exception is when deleting a bucket using the Google Cloud console, which deletes all associated caches along with the bucket.

  * When performing the cache create, disable, resume, or update operations, limit the rate of operations to no more than one operation per second. Performing more than one operation per second can result in failures.

  * Rapid Cache is not durable storage and data may be evicted from the cache in various scenarios. One scenario is when the cache gets automatically resized to ensure that sufficient resources are available for your workloads. In this scenario, some data might get evicted according to a least-recently-used (LRU) algorithm until the Rapid Cache service has finished increasing the cache size.

In any case, your data remains safely stored in your source bucket. When data gets dropped from the cache due to reasons besides TTL expiry, the Rapid Cache service will attempt to re-ingest the data into the cache transparently and at no cost to you. If the data cannot be transparently re-ingested or was dropped due to TTL expiry, the Rapid Cache service will re-ingest the data upon first read.

  * Recommendations and insights generated by the Rapid Cache recommender cannot be read using BigQuery.




## Performance considerations

  * **Chunk misses** : If a request covers multiple chunks and some chunks are in the cache while others are not, Rapid Cache transparently retrieves the missing chunks from the source bucket.

  * **TTL and eviction** : The Time to Live (TTL) and Least Recently Used (LRU) eviction policies also operate on chunks. Frequently used parts of a large file may remain in the cache while infrequently used parts are evicted.




## Pricing

For pricing for using Rapid Cache, see [Rapid Cache pricing](https://docs.cloud.google.com/storage/pricing#rapid-cache).

### Cost controls

Expand the following tips to learn how you can minimize the costs of running caches:

#### Bucket selection

You should only create caches for buckets that contain data you want to cache.

#### Zone selection

You should only create caches in zones where your workload will benefit from caching.

#### TTL setting

You should specify the minimal TTL you need to store data in the cache. The TTL can be changed non-disruptively. The default is 1 day.

#### Disabling the cache

You can disable a cache to permanently remove it from the service and stop all associated cache fees from accruing.

## Troubleshooting temporary resource shortages

The following sections describe how to troubleshoot when a temporary resource shortage occurs, where there isn't enough SSD capacity or serving capacity in a specified zone to create a cache, increase a cache's size, or increase a cache's bandwidth limit.

### Failure to create a new cache

Rapid Cache can fail to create a new cache in a specific zone due either to a lack of SSD capacity or throughput serving resources, which results in a temporary shortage of resources. During this time period, Rapid Cache attempts to create the new cache for up to 48 hours. If resources become available within the 48 hour timeframe, Rapid Cache completes the cache creation request successfully. If resources don't become available within the 48 hour timeframe, the cache creation request fails.

**How to troubleshoot** : To avoid disruption to your caching, you can manually cancel the cache creation operation and create a new cache in a different zone that might have capacity available. To monitor or cancel a cache creation operation, see [using long-running operations](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#manage-lros).

### Failure to increase cache size

Rapid Cache can fail to increase a cache's size when the required amount of SSD capacity isn't available in the cache's zone.

Although Rapid Cache offers automatic cache size increases on-demand, cache size increases are contingent upon SSD capacity availability. If SSD capacity isn't available when the automatic cache size increase request is made, Rapid Cache continues to submit the request until the temporary resource shortage ends or an increase in cache size is no longer needed.

During a temporary resource shortage, new data is ingested and existing data in the cache is evicted based on a least-recently-used basis. Caches that are large enough to store most of the hot data experience little to no impact to cache metrics. Caches with less capacity than the amount of hot data can evict data and re-ingest the same data more often than caches not affected by resource shortages. When the actual size of your cache is much smaller than the needed capacity, you might experience the following resource shortage-related behavior:

  * A lower cache bandwidth limit, lower cache throughput, higher data transfer bandwidth quota consumption, and a possible impact on other metrics
  * Billing might be affected in the following ways: 
    * Increased costs from the cache ingestion fee
    * Decreased costs from the cache storage fee
    * Decreased costs from the cache data transfer out fee
    * Decreased costs from the cache data transfer out operation fees
    * Increased costs from the multi-region data transfer fee
    * Increased costs from the usage of Class B operations



For information about these fees, see [Rapid Cache pricing](https://docs.cloud.google.com/storage/pricing#rapid-cache).

**How to troubleshoot** : For best results during a temporary resource shortage, we recommend monitoring your caches and disabling unnecessary caches or workloads based on your needs.

### Failure to scale up a cache's bandwidth limit

A cache bandwidth limit shortage can occur temporarily during a cache size increase when throughput serving resources in a specific zone are insufficient to scale the cache bandwidth limit of existing caches at 20 Gbps per TiB. During a shortage available of cache bandwidth, Rapid Cache doesn't allow the cache bandwidth limit to scale at 20 Gbps per TiB of data but the cache continues to serve read requests. You can request more cache bandwidth by contacting your Technical Account Manager or Google representative. During a shortage of available cache bandwidth, you might see an increase in your bucket's data egress bandwidth consumption.

**How to troubleshoot** : For best results during a temporary resource shortage, we recommend monitoring your caches and disabling unnecessary caches or workloads based on your needs.

## What's next

  * [Create and manage caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
