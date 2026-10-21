---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/AutoBatcher/
title: google.appengine.ext.ndb.AutoBatcher \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:19:50.017181+00:00
---

# google.appengine.ext.ndb.AutoBatcher  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/AutoBatcher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.AutoBatcher Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L148-L289) Batches multiple async calls if they share the same RPC options. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.AutoBatcher(
        todo_tasklet, limit
    )
    

Here is an example to explain what this class does. Life of a `key.get_async(options)` API call:

  * `Key` gets the singleton `Context` instance and invokes [`Context.get`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Context#get).
  * [`Context.get`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Context#get) calls `Context._get_batcher.add(key, options)`. This returns a future `fut` as the return value of `key.get_async`. At this moment, `key.get_async` returns.
  * When more than "limit" number of `_get_batcher.add()` was called, `_get_batcher` invokes its `self._todo_tasklet`, `Context._get_tasklet`, with the list of keys seen so far.
  * `Context._get_tasklet` fires a MultiRPC and waits on it.
  * Upon MultiRPC completion, `Context._get_tasklet` passes on the results to the respective `fut` from `key.get_async`.
  * If user calls `fut.get_result()` before "limit" number of `add()` was called, `fut.get_result()` will repeatedly call `eventloop.run1()`.
  * After processing immediate callbacks, `eventloop` will run idlers. `AutoBatcher._on_idle` is an idler.
  * `_on_idle` will run the `todo_tasklet` before the batch is full.

So the engine is `todo_tasklet`, which is a proxy tasklet that can combine arguments into batches and passes along results back to respective futures. This class is mainly a helper that invokes `todo_tasklet` with the right arguments at the right time. | 

## Args  
  
---  
  
`todo_tasklet` |  The tasklet that actually fires RPC and waits on a MultiRPC. It should take a list of (future, arg) pairs and an "options" as arguments. "options" are rpc options.   
`limit` |  Max number of items to batch for each distinct value of "options".   
  
## Methods

### `action`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L258-L264)
    
    
    action()
    

### `add`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L224-L247)
    
    
    add(
        arg, options=None
    )
    

Returns back an instance of future after adding an arg.

Args  
---  
  
`arg` |  One argument for `_todo_tasklet`.   
`options` |  RPC options.   
  
Return  
---  
An instance of future, representing the result of running `_todo_tasklet` without batching.   
  
### `add_once`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L249-L256)
    
    
    add_once(
        arg, options=None
    )
    

### `flush`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L285-L289)
    
    
    flush()
    

### `run_queue`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L204-L211)
    
    
    run_queue(
        options, todo
    )
    

Actually run the `_todo_tasklet`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
