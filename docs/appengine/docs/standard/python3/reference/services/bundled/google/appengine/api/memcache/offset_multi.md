---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/offset_multi/
title: google.appengine.api.memcache.offset_multi \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:10:27.383425+00:00
---

# google.appengine.api.memcache.offset_multi  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/offset_multi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.offset_multi Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1607-L1631) Offsets multiple keys by a delta, incrementing and decrementing in batch.
    
    
    google.appengine.api.memcache.offset_multi(
        mapping, key_prefix='', namespace=None, initial_value=None
    )
    

| 

## Args  
  
---  
  
`mapping` |  Dictionary mapping keys to deltas (positive or negative integers) to apply to each corresponding key.   
`key_prefix` |  Prefix for to prepend to all keys.   
`initial_value` |  Initial value to put in the cache, if it doesn't already exist. The default value, None, will not create a cache entry if it doesn't already exist.   
`namespace` |  A string specifying an optional namespace to use in the request.   
  
## Returns  
  
---  
Dictionary mapping input keys to new integer values. The new value will be None if an error occurs, the key does not already exist, or the value was not an integer type. The values will wrap-around at unsigned 64-bit integer-maximum and underflow will be floored at zero.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
