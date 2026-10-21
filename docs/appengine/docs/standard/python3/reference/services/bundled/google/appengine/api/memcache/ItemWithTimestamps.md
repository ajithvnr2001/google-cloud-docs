---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/ItemWithTimestamps/
title: google.appengine.api.memcache.ItemWithTimestamps \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:51:35.893377+00:00
---

# google.appengine.api.memcache.ItemWithTimestamps  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/ItemWithTimestamps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.ItemWithTimestamps Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L124-L170) A Memcache item with its relevant timestamps. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.memcache.ItemWithTimestamps(
        value, expiration_time_sec, last_access_time_sec, delete_lock_time_sec=0
    )
    

| 

## Args  
  
---  
  
`value` |  The Memcache item. Set to "" if the item is delete locked.   
`expiration_time_sec` |  The absolute expiration timestamp of the item in unix epoch seconds. Set to 0 if no expiration time is set.   
`last_access_time_sec` |  The absolute last accessed timestamp of the item in unix epoch seconds.   
`delete_lock_time_sec` |  Absolute delete_time timestamp of the item in unix epoch seconds. Set to 0 if this item is not delete locked.   
  
## Methods

### `get_delete_lock_time_sec`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L165-L170)
    
    
    get_delete_lock_time_sec()
    

Returns the absolute delete_time timestamp in unix epoch seconds.

It is set to 0 if this item is not delete locked.

### `get_expiration_time_sec`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L154-L159)
    
    
    get_expiration_time_sec()
    

Returns the absolute expiration timestamp in unix epoch seconds.

It is set to 0 if this item has no expiration timestamp.

### `get_last_access_time_sec`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L161-L163)
    
    
    get_last_access_time_sec()
    

Returns the last accessed timestamp of the item in unix epoch seconds.

### `get_value`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L150-L152)
    
    
    get_value()
    

Returns the value of the item.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
