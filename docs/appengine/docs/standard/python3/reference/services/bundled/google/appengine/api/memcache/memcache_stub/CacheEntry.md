---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/memcache_stub/CacheEntry/
title: google.appengine.api.memcache.memcache_stub.CacheEntry \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:47:03.702582+00:00
---

# google.appengine.api.memcache.memcache_stub.CacheEntry  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/memcache_stub/CacheEntry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.memcache_stub.CacheEntry Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L87-L151) An entry in the cache. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.memcache.memcache_stub.CacheEntry(
        value, expiration, flags, cas_id, gettime, namespace, key
    )
    

| 

## Args  
  
---  
  
`value` |  String containing the data for this entry.   
`expiration` |  Number containing the expiration time or offset in seconds for this entry.   
`flags` |  Opaque flags used by the memcache implementation.   
`cas_id` |  Unique Compare-And-Set ID.   
`gettime` |  Used for testing. Function that works like `time.time()`.   
`namespace` |  String namespace that this entry is stored under.   
`key` |  String key used to retrieve the item from the namespace.   
  
## Attributes  
  
---  
  
`byte_size` |   
  
## Methods

### `CheckExpired`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L132-L134)
    
    
    CheckExpired()
    

Returns `True` if this entry has expired; `False` otherwise.

### `CheckLocked`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L149-L151)
    
    
    CheckLocked()
    

Returns `True` if this entry was deleted but has not yet timed out.

### `ExpireAndLock`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L136-L147)
    
    
    ExpireAndLock(
        timeout
    )
    

Marks this entry as deleted and locks it for the expiration time.

Used to implement memcache's delete timeout behavior.

Args  
---  
  
`timeout` |  Parameter originally passed to memcache.delete or memcache.delete_multi to control deletion timeout.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
