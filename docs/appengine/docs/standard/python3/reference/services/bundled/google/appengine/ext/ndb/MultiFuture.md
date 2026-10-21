---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/MultiFuture/
title: google.appengine.ext.ndb.MultiFuture \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:27:10.178687+00:00
---

# google.appengine.ext.ndb.MultiFuture  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/MultiFuture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.MultiFuture Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L561-L673) A Future that depends on multiple other Futures. Inherits From: [`Future`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Future), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.MultiFuture(
        info=None
    )
    

This is used internally by 'v1, v2, ... = yield f1, f2, ...'; the semantics (e.g. error handling) are constrained by that use case. The protocol from the caller's POV is:: mf = MultiFuture() mf.add_dependent() -OR- mf.putq() mf.add_dependent() -OR- mf.putq() . . (More mf.add_dependent() and/or mf.putq() calls) . mf.complete() # No more dependents will be added. . . (Time passes) . results = mf.get_result() Now, results is a list of results from all dependent Futures in the order in which they were added. It is legal to add the same dependent multiple times. Callbacks can be added at any point. From a dependent Future POV, there's nothing to be done: a callback is automatically added to each dependent Future which will signal its completion to the MultiFuture. Error handling: if any dependent future raises an error, it is propagated to mf. To force an early error, you can call mf.set_exception() instead of mf.complete(). After this you can't call mf.add_dependent() or mf.putq() any more. | 

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L655-L668)
    
    
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L617-L622)
    
    
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
    

### `putq`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L647-L653)
    
    
    putq(
        value
    )
    

### `set_exception`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/tasklets.py#L625-L627)
    
    
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
