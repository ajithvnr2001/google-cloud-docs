---
url: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/
title: Memcache API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:50.061342+00:00
---

# Memcache API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Memcache API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page provides an overview of the App Engine memcache service. High performance scalable web applications often use a distributed in-memory data cache in front of or in place of robust persistent storage for some tasks. App Engine includes a memory cache service for this purpose. To learn how to configure, monitor, and use the memcache service, read [Using Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/using).

**Note:** The cache is global and is shared across the application's frontend, backend, and all of its services and versions.

## When to use a memory cache

One use of a memory cache is to speed up common datastore queries. If many requests make the same query with the same parameters, and changes to the results do not need to appear on the web site right away, the application can cache the results in the memcache. Subsequent requests can check the memcache, and only perform the datastore query if the results are absent or expired. Session data, user preferences, and other data returned by queries for web pages are good candidates for caching.

Memcache can be useful for other temporary values. However, when considering whether to store a value solely in the memcache and not backed by other persistent storage, be sure that your application behaves acceptably when the value is suddenly not available. Values can expire from the memcache at any time, and can be expired prior to the expiration deadline set for the value. For example, if the sudden absence of a user's session data would cause the session to malfunction, that data should probably be stored in the datastore in addition to the memcache.

## Service levels

App Engine supports two levels of the memcache service:

  * **Shared memcache** is the free default for App Engine applications. It provides cache capacity on a best-effort basis and is subject to the overall demand of all the App Engine applications using the shared memcache service.

  * **Dedicated memcache** provides a fixed cache capacity assigned exclusively to your application. It's billed by the GB-hour of cache size and requires billing to be enabled. Having control over cache size means your app can perform more predictably and with fewer reads from more costly durable storage.




Both memcache service levels use the same API. To configure the memcache service for your application, see [Using Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/using#configuring_memcache).

**Note:** Whether shared or dedicated, memcache is not durable storage. Keys can be evicted when the cache fills up, according to the cache's LRU policy. Changes in the cache configuration or datacenter maintenance events can also flush some or all of the cache.

The following table summarizes the differences between the two classes of memcache service:

Feature | Dedicated Memcache | Shared Memcache  
---|---|---  
Price | $0.06 per GB per hour | Free  
Capacity | 

us-central
    1 to 100GB
asia-northeast1, europe-west, europe-west3, and us-east1:
    1 to 20GB
other regions:
    1 to 2GB
| No guaranteed capacity  
Performance | Up to 10k reads or 5k writes (exclusive) per second per GB (items < 1KB). For more details, see Cache statistics. | Not guaranteed  
Durable store | No | No  
SLA | None | None  
  
Dedicated memcache billing is charged in 15 minute increments. If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply. 

If your app needs more memcache capacity, [contact our Sales team](https://cloud.google.com/contact/).

## Limits

The following limits apply to the use of the memcache service:

  * The maximum size of a cached data value is 1 MB (10^6 bytes).
  * A key cannot be larger than 250 bytes. In the Python runtime, keys that are strings longer than 250 bytes will be hashed. 
  * The "multi" batch operations can have any number of elements. The total size of the call and the total size of the data fetched must not exceed 32 megabytes.
  * A memcache key cannot contain a null byte.
  * Usage of the shared tier Memcache API is subject to limits defined by [Shared Centi Memcache Compute Units Per Region Per Minute](https://docs.cloud.google.com/appengine/docs/standard/quotas#Memcache).



## Recommendations and best practices

When using Memcache, we recommend that you design your applications to:

  * **Handle the case where a cached value is not always available.**

    * _Memcache is not durable storage_. According to the eviction policy, keys are evicted when the cache fills up. Changes in the cache configuration or datacenter maintenance events can also flush some or all of the cache.
    * _Memcache may experience temporary unavailability._ Memcache operations can fail for various reasons including changes in cache configuration or datacenter maintenance events. Applications should be designed to catch failed operations without exposing these errors to end users. This guidance applies especially to Set operations.
  * **Use the batching capability of the API when possible.**

    * Doing so increases the performance and efficiency of your app, especially for small items.
  * **Distribute load across your memcache keyspace.**

    * Having a single or small set of memcache items represent a disproportionate amount of traffic will hinder your app from scaling. This guidance applies to both operations/sec and bandwidth. You can often alleviate this problem by explicitly sharding your data.

For example, you can split a frequently updated counter among several keys, reading them back and summing only when you need a total. Likewise, you can split a 500K piece of data that must be read on every HTTP request across multiple keys and read them back using a single batch API call. (Even better would be to cache the value in instance memory.) For dedicated memcache, the peak access rate on a single key should be 1-2 orders of magnitude less than the per-GB rating.

  * **Retain your own keys in order to retrieve values from the cache.**

    * _Memcache does not provide a method to list keys._ Due to the nature of the cache, it is not possible to list keys without disrupting the cache. Additionally, some languages, like Python, hash long keys, and the original keys are only known to the application.



## How cached data expires

Memcache contains key/value pairs. The pairs in memory at any time change as items are written and retrieved from the cache.

By default, values stored in memcache are retained as long as possible. Values can be evicted from the cache when a new value is added to the cache and the cache is low on memory. When values are evicted due to memory pressure, the least recently used values are evicted first.

The app can provide an expiration time when a value is stored, as either a number of seconds relative to when the value is added, or as an absolute Unix epoch time in the future (a number of seconds from midnight January 1, 1970). The value is evicted no later than this time, though it can be evicted earlier for other reasons. Incrementing the value stored for an existing key does not update its expiration time.

Under rare circumstances, values can also disappear from the cache prior to expiration for reasons other than memory pressure. While memcache is resilient to server failures, memcache values are not saved to disk, so a service failure can cause values to become unavailable.

In general, an application should not expect a cached value to always be available.

You can erase an application's entire cache via the API or in the memcache section of [Google Cloud console](https://console.cloud.google.com/appengine/memcache).

**Note:** The actual removal of expired cache data is handled lazily. An expired item is removed when someone unsuccessfully tries to retrieve it. Alternatively, the expired cache data falls out of the cache according to LRU cache behavior, which applies to all items, both live and expired. This means when the cache size is reported in statistics, the number can include live and expired items.

## Cache statistics

### Operations per second by item size

**Note:** This information applies to dedicated memcache only.

Dedicated memcache is rated in operations per second per GB, where an operation is defined as an individual cache item access, such as a `get`, `set`, or `delete`. The operation rate varies by item size approximately according to the following table. Exceeding these ratings might result in increased API latency or errors.

The following tables provide the maximum number of sustained, exclusive `get-hit` or `set` operations per GB of cache. Note that a `get-hit` operation is a `get` call that finds that there is a value stored with the specified key, and returns that value.

Item Size (KB) | Maximum `get-hit` ops/s | Maximum `set` ops/s  
---|---|---  
≤1 | 10,000 | 5,000  
100 | 2,000 | 1,000  
512 | 500 | 250  
  
An app configured for multiple GB of cache can in theory achieve an aggregate operation rate computed as the number of GB multiplied by the per-GB rate. For example, an app configured for 5GB of cache could reach 50,000 memcache operations/sec on 1KB items. Achieving this level requires a good distribution of load across the memcache keyspace.

For each IO pattern, the limits listed above are for reads _or_ writes. For simultaneous reads _and_ writes, the limits are on a sliding scale. The more reads being performed, the fewer writes can be performed, and vice versa. Each of the following are example IOPs limits for simultaneous reads and writes of 1KB values per 1GB of cache:

Read IOPs | Write IOPs  
---|---  
10000 | 0  
8000 | 1000  
5000 | 2500  
1000 | 4500  
0 | 5000  
  
### Memcache compute units (MCU)

**Note:** This information applies to dedicated memcache only.

Memcache throughput can vary depending on the size of the item you are accessing and the operation you want to perform on the item. You can roughly associate a cost with operations and estimate the traffic capacity that you can expect from dedicated memcache using a unit called Memcache Compute Unit (MCU). MCU is defined such that you can expect 10,000 MCU per second per GB of dedicated memcache. The Google Cloud console shows how much MCU your app is currently using.

Note that MCU is a rough statistical estimation and also it's not a linear unit. Each cache operation that reads or writes a value has a corresponding MCU cost that depends on the size of the value. The MCU for a `set` depends on the value size: it is 2 times the cost of a successful `get-hit` operation.

**Note:** The way that Memcache Compute Units (MCU) are computed is subject to change.Value item size (KB) | MCU cost for `get-hit` | MCU cost for `set`  
---|---|---  
≤1 | 1.0 | 2.0  
2 | 1.3 | 2.6  
10 | 1.7 | 3.4  
100 | 5.0 | 10.0  
512 | 20.0 | 40.0  
1024 | 50.0 | 100.0  
  
Operations that do not read or write a value have a fixed MCU cost:

Operation | MCU  
---|---  
`get-miss` | 1.0  
`delete` | 2.0  
`increment` | 2.0  
`flush` | 100.0  
`stats` | 100.0  
  
Note that a `get-miss` operation is a `get` that finds that there is no value stored with the specified key.

## Compare and set

Compare and set is a feature that allows multiple requests that are being handled concurrently to update the value of the same memcache key atomically, avoiding race conditions.

**Note:** For a complete discussion of the compare and set feature for Python, see Guido van Rossum's blog post [Compare-And-Set in Memcache](http://neopythonic.blogspot.com/2011/08/compare-and-set-in-memcache.html).

### Key logical components of compare and set

If you're updating the value of a memcache key that might receive other concurrent write requests, you must use the memcache `Client` object, which stores certain state information that's used by the methods that support compare and set. You cannot use the memcache functions `get()` or `set()`, because they are stateless. The `Client` class itself is not thread-safe, so you should not use the same `Client` object in more than one thread.

When you retrieve keys, you must use the memcache `Client` methods that support compare and set: `gets()` or `get_multi()` with the `for_cas` parameter set to `True`.

When you update a key, you must use the memcache `Client` methods that support compare and set: `cas()` or `cas_multi()`.

The other key logical component is the App Engine memcache service and its behavior with regard to compare and set. The App Engine memcache service itself behaves atomically. That is, when two concurrent requests (for the same app id) use memcache, they will go to the same memcache service instance, and the memcache service has enough internal locking so that concurrent requests for the same key are properly serialized. In particular this means that two `cas()` requests for the same key do not actually run in parallel -- the service handles the first request that came in until completion (that is, updating the value and timestamp) before it starts handling the second request.

To learn how to use compare and set in Python, read [Handling concurrent writes](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/using#handling_concurrent_writes).

## What's next

  * Learn how to configure, monitor, and use memcache in [Using Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/using).
  * Refer to the [Memcache Examples](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/examples). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
