---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/SerialQueueFuture/
title: google.appengine.ext.ndb.SerialQueueFuture \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:30:47.218092+00:00
---

# google.appengine.ext.ndb.SerialQueueFuture  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/SerialQueueFuture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.SerialQueueFuture Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L793-L908) Like QueueFuture but maintains the order of insertion. Inherits From: [`Future`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Future), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.SerialQueueFuture(
        info=None
    )
    

This class is used by Query operations.

#### Invariants:

  * At least one of _queue and _waiting is empty.
  * The Futures in _waiting are always pending.

(The Futures in _queue may be pending or completed.) In the discussion below, add_dependent() is treated the same way as putq(). If putq() is ahead of getq(), the situation is like this:
    
    
                       putq()
                       v
    

_queue: [f1, f2, ...]; _waiting: [] ^ getq() Here, putq() appends a Future to the right of _queue, and getq() removes one from the left. If getq() is ahead of putq(), it's like this:
    
    
            putq()
            v
    

_queue: []; _waiting: [f1, f2, ...] ^ getq() Here, putq() removes a Future from the left of _waiting, and getq() appends one to the right. When both are empty, putq() appends a Future to the right of _queue, while getq() appends one to the right of _waiting. The _full flag means that no more calls to putq() will be made; it is set by calling either complete() or set_exception(). Calling complete() signals that no more putq() calls will be made. If getq() is behind, subsequent getq() calls will eat up _queue until it is empty, and after that will return a Future that passes EOFError (note that getq() itself never raises EOFError). If getq() is ahead when complete() is called, the Futures in _waiting are all passed an EOFError exception (thereby eating up _waiting). If, instead of complete(), set_exception() is called, the exception and traceback set there will be used instead of EOFError. | 

## Attributes  
  
---  
  
`state` |   
  
## Methods

### `add_callback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L322-L326)
    
    
    add_callback(
        callback, *args, **kwds
    )
    

### `add_dependent`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L881-L891)
    
    
    add_dependent(
        fut
    )
    

### `add_immediate_callback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L328-L332)
    
    
    add_immediate_callback(
        callback, *args, **kwds
    )
    

### `check_success`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L391-L394)
    
    
    check_success()
    

### `complete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L854-L861)
    
    
    complete()
    

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
    

### `getq`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L893-L908)
    
    
    getq()
    

### `putq`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L869-L879)
    
    
    putq(
        value
    )
    

### `set_exception`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L863-L867)
    
    
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
