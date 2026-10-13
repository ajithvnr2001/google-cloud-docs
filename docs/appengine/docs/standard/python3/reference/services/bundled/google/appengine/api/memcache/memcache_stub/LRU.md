---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/memcache_stub/LRU/
title: google.appengine.api.memcache.memcache_stub.LRU \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:15.453653+00:00
---

# google.appengine.api.memcache.memcache_stub.LRU  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/memcache_stub/LRU/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.memcache_stub.LRU Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L527-L610) Implements an `LRU` cache by intrusive chaining on elements. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.memcache.memcache_stub.LRU()
    

Also keeps track of the total size of the elements in bytes, as well as the length of the `LRU` chain. Heavily inspired by `//j/c/g/appengine/api/memcache/dev/LRU.java`. | 

## Attributes  
  
---  
  
`newest` |   
`oldest` |   
`total_byte_size` |   
  
## Methods

### `Clear`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L553-L558)
    
    
    Clear()
    

Clears the `LRU` chain.

### `IsEmpty`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L564-L566)
    
    
    IsEmpty()
    

Checks if the `LRU` chain is empty.

### `Remove`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L583-L606)
    
    
    Remove(
        element
    )
    

Removes an item from the `LRU` chain.

### `RemoveOldest`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L608-L610)
    
    
    RemoveOldest()
    

Removes the oldest item from the `LRU` chain.

### `Update`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L568-L581)
    
    
    Update(
        element
    )
    

Updates an item in the `LRU` chain.

### `__len__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/memcache_stub.py#L542-L543)
    
    
    __len__()
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
