---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/decr/
title: google.appengine.api.memcache.decr \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:01:23.752338+00:00
---

# google.appengine.api.memcache.decr  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/decr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.decr Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1449-L1483) Atomically decrements a key's value.
    
    
    google.appengine.api.memcache.decr(
        key, delta=1, namespace=None, initial_value=None
    )
    

Internally, the value is a unsigned 64-bit integer. Memcache caps decrementing below zero to zero. The key must already exist in the cache to be decremented. See docs on `incr()` for details. | 

## Args  
  
---  
  
`key` |  Key to decrement. If an iterable collection, each one of the keys will be offset. See Client's docstring for details.   
`delta` |  Non-negative integer value (int or long) to decrement key by, defaulting to 1.   
`namespace` |  a string specifying an optional namespace to use in the request.   
`initial_value` |  initial value to put in the cache, if it doesn't already exist. The default value, None, will not create a cache entry if it doesn't already exist.   
  
## Returns  
  
---  
If key was a single value, the new long integer value, or None if key was not in the cache, could not be decremented for any other reason, or a network/RPC/server error occurred. If key was an iterable collection, a dictionary will be returned mapping supplied keys to values, with the values having the same meaning as the singular return value of this method.   
  
## Raises  
  
---  
  
`ValueError` |  If number is negative.   
`TypeError` |  If delta isn't an int or long.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
