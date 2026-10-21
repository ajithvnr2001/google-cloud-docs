---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/peek_multi/
title: google.appengine.api.memcache.peek_multi \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:57:20.156950+00:00
---

# google.appengine.api.memcache.peek_multi  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/peek_multi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.peek_multi Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L733-L758) Gets multiple items from memcache along with their timestamp metadata.
    
    
    google.appengine.api.memcache.peek_multi(
        keys, key_prefix='', namespace=None
    )
    

This is the recommended way to do bulk peek() calls. | 

## Args  
  
---  
  
`keys` |  List of keys to look up. Keys may be strings or tuples of (hash_value, string). Google App Engine does the sharding and hashing automatically, though, so the hash value is ignored. To memcache, keys are just series of bytes, and not in any particular encoding.   
`key_prefix` |  Prefix to prepend to all keys when talking to the server; not included in the returned dictionary.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
## Returns  
  
---  
A dictionary of the keys and ItemWithTimestamps objects. Even if the key_prefix was specified, that key_prefix won't be on the keys in the returned dictionary. Each ItemWithTimestamps object contains the item corresponding to the key, along with timestamp metadata - expiration timestamp, last access timestamp and delete timestamp (if the item is delete locked).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
