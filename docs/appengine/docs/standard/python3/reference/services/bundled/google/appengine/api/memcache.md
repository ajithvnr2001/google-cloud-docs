---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/
title: Module: google.appengine.api.memcache \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:29:10.751079+00:00
---

# Module: google.appengine.api.memcache  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.memcache Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py) Memcache API. Provides memcached-alike API to application developers to store data in memory when reliable storage via the DataStore API isn't required and higher performance is desired.

## Modules

[`memcache_stub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/memcache_stub) module: Stub version of the memcache API, keeping all data in process memory.

## Classes

[`class Client`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client): Memcache client object, through which one invokes all memcache operations. [`class ItemWithTimestamps`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/ItemWithTimestamps): A Memcache item with its relevant timestamps.

## Functions

[`add(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/add): Sets a key's value if the item is not already in memcache. [`add_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/add_multi): Set multiple keys' values if items are not already in memcache. [`create_rpc(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/create_rpc): Creates an RPC object for use with the memcache API. [`debuglog(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/debuglog): Logging function for debugging information. [`decr(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/decr): Atomically decrements a key's value. [`delete(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/delete): Deletes a key from memcache. [`delete_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/delete_multi): Delete multiple keys at once. [`disconnect_all(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/disconnect_all): Closes all connections to memcache servers. [`flush_all(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/flush_all): Deletes everything in memcache. [`forget_dead_hosts(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/forget_dead_hosts): Resets all servers to the alive status. [`get(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/get): Looks up a single key in memcache. [`get_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/get_multi): Looks up multiple keys from memcache in one operation. [`get_stats(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/get_stats): Gets memcache statistics for this application. [`incr(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/incr): Atomically increments a key's value. [`offset_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/offset_multi): Offsets multiple keys by a delta, incrementing and decrementing in batch. [`peek(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/peek): Gets an item from memcache along with its timestamp metadata. [`peek_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/peek_multi): Gets multiple items from memcache along with their timestamp metadata. [`replace(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/replace): Replaces a key's value, failing if item isn't already in memcache. [`replace_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/replace_multi): Replace multiple keys' values, failing if the items aren't in memcache. [`set(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/set): Sets a key's value, regardless of previous contents in cache. [`set_multi(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/set_multi): Set multiple keys' values at once, regardless of previous contents. [`set_servers(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/set_servers): Sets the pool of memcache servers used by the client. [`setup_client(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/setup_client): Sets the Client object instance to use for all module-level methods. | 

## Other Members  
  
---  
  
CAPABILITY |  Instance of [`google.appengine.api.capabilities.CapabilitySet`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/capabilities/CapabilitySet)  
DELETE_ITEM_MISSING |  `1`  
DELETE_NETWORK_FAILURE |  `0`  
DELETE_SUCCESSFUL |  `2`  
ERROR |  `3`  
EXISTS |  `4`  
FLAG_COMPRESSED |  `8`  
FLAG_TYPE_MASK |  `7`  
MAX_KEY_SIZE |  `250`  
MAX_VALUE_SIZE |  `1000000`  
NOT_STORED |  `2`  
STAT_BYTES |  `'bytes'`  
STAT_BYTE_HITS |  `'byte_hits'`  
STAT_HITS |  `'hits'`  
STAT_ITEMS |  `'items'`  
STAT_MISSES |  `'misses'`  
STAT_OLDEST_ITEM_AGES |  `'oldest_item_age'`  
STORED |  `1`  
TYPE_BOOL |  `5`  
TYPE_INT |  `3`  
TYPE_LONG |  `4`  
TYPE_PICKLED |  `2`  
TYPE_STR |  `0`  
TYPE_UNICODE |  `1`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
