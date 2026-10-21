---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Future/
title: google.appengine.ext.ndb.Future \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:51:27.692529+00:00
---

# google.appengine.ext.ndb.Future  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Future/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Future Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L247-L547) A Future has 0 or more callbacks. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Future(
        info=None
    )
    

The callbacks will be called when the result is ready. NOTE: This is somewhat inspired but not conformant to the Future interface defined by PEP 3148. It is also inspired (and tries to be somewhat compatible with) the App Engine specific UserRPC and MultiRpc classes. | 

## Attributes  
  
---  
  
`state` |   
  
## Methods

### `add_callback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L322-L326)
    
    
    add_callback(
        callback, *args, **kwds
    )
    

### `add_immediate_callback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L328-L332)
    
    
    add_immediate_callback(
        callback, *args, **kwds
    )
    

### `check_success`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L391-L394)
    
    
    check_success()
    

### `done`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L359-L360)
    
    
    done()
    

### `dump`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L310-L312)
    
    
    dump()
    

### `dump_stack`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L314-L320)
    
    
    dump_stack()
    

### `get_exception`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L383-L385)
    
    
    get_exception()
    

### `get_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L396-L398)
    
    
    get_result()
    

### `get_traceback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L387-L389)
    
    
    get_traceback()
    

### `set_exception`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L345-L357)
    
    
    set_exception(
        exc, tb=None
    )
    

### `set_result`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L334-L343)
    
    
    set_result(
        result
    )
    

### `wait`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L371-L381)
    
    
    wait()
    

### `wait_all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L414-L421)
    
    
    @classmethod
    wait_all(
        futures
    )
    

### `wait_any`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L401-L411)
    
    
    @classmethod
    wait_any(
        futures
    )
    

## Class Variables  
  
---  
  
FINISHING |  `2`  
IDLE |  `0`  
RUNNING |  `1`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
