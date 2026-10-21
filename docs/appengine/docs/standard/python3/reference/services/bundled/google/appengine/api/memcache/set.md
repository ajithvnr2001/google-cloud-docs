---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/set/
title: google.appengine.api.memcache.set \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:03.859212+00:00
---

# google.appengine.api.memcache.set  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.set Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L920-L943) Sets a key's value, regardless of previous contents in cache.
    
    
    google.appengine.api.memcache.set(
        key, value, time=0, min_compress_len=0, namespace=None
    )
    

Unlike `add()` and `replace()`, this method always sets (or overwrites) the value in memcache, regardless of previous contents. | 

## Args  
  
---  
  
`key` |  Key to set. See docs on Client for details.   
`value` |  Value to set. Any type. If complex, will be pickled.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`min_compress_len` |  Ignored option for compatibility.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
## Returns  
  
---  
`True` if set. `False` on error.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
