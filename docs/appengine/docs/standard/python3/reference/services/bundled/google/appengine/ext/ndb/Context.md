---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Context/
title: google.appengine.ext.ndb.Context \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:57:44.349654+00:00
---

# google.appengine.ext.ndb.Context  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/Context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.ext.ndb.Context Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L292-L1337) Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.ext.ndb.Context(
        conn=None,
        auto_batcher_class=[google.appengine.ext.ndb.AutoBatcher](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/AutoBatcher),
        config=None,
        parent_context=None
    )
    

## Methods

### `allocate_ids`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L890-L894)
    
    
    allocate_ids(
        key, size=None, max=None, **ctx_options
    )
    

### `call_on_commit`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1096-L1119)
    
    
    call_on_commit(
        callback
    )
    

Call a callback upon successful commit of a transaction. If not in a transaction, the callback is called immediately. In a transaction, multiple callbacks may be registered and will be called once the transaction commits, in the order in which they were registered. If the transaction fails, the callbacks will not be called. If the callback raises an exception, it bubbles up normally. This means:

  * If the callback is called immediately, any exception it raises will bubble up immediately.
  * If the call is postponed until commit, remaining callbacks will be skipped and the exception will bubble up through the `transaction()` call. However, the transaction is already committed at that point.



### `clear_cache`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1121-L1126)
    
    
    clear_cache()
    

Clears the in-memory cache. NOTE: This does not affect memcache.

### `default_cache_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L419-L441)
    
    
    @staticmethod
    default_cache_policy(
        key
    )
    

Default cache policy. This defers to `_use_cache` on the `Model` class. | Args  
---  
  
`key` |  Key instance.   
  
Returns  
---  
A bool or `None`.   
  
### `default_datastore_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L553-L575)
    
    
    @staticmethod
    default_datastore_policy(
        key
    )
    

Default Datastore policy.

This defers to `_use_datastore` on the `Model` class.

Args  
---  
  
`key` |  Key instance.   
  
Returns  
---  
A bool or `None`.   
  
### `default_memcache_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L486-L508)
    
    
    @staticmethod
    default_memcache_policy(
        key
    )
    

Default Memcache policy.

This defers to `_use_memcache` on the `Model` class.

Args  
---  
  
`key` |  Key instance.   
  
Returns  
---  
A bool or `None`.   
  
### `default_memcache_timeout_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L620-L642)
    
    
    @staticmethod
    default_memcache_timeout_policy(
        key
    )
    

Default Memcache timeout policy.

This defers to `_memcache_timeout` on the `Model` class.

Args  
---  
  
`key` |  Key instance.   
  
Returns  
---  
Memcache timeout to use (integer), or `None`.   
  
### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L872-L888)
    
    
    delete(
        key, **ctx_options
    )
    

### `flush`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L347-L357)
    
    
    flush()
    

### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L715-L811)
    
    
    get(
        key, **ctx_options
    )
    

Returns a `Model` instance given the entity key.

It will use the context cache if the cache policy for the given key is enabled.

Args  
---  
  
`key` |  Key instance.   
`**ctx_options` |  Context options.   
  
Returns  
---  
A `Model` instance if the key exists in the datastore; `None` otherwise.   
  
### `get_cache_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L445-L452)
    
    
    get_cache_policy()
    

Return the current context cache policy function.

Returns  
---  
A function that accepts a `Key` instance as argument and returns a bool indicating if it should be cached. May be `None`.   
  
### `get_datastore_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L579-L586)
    
    
    get_datastore_policy()
    

Return the current context datastore policy function.

Returns  
---  
A function that accepts a `Key` instance as argument and returns a bool indicating if it should use the datastore. May be `None`.   
  
### `get_indexes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L896-L900)
    
    
    get_indexes(
        **ctx_options
    )
    

### `get_memcache_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L512-L519)
    
    
    get_memcache_policy()
    

Return the current memcache policy function.

Returns  
---  
A function that accepts a `Key` instance as argument and returns a bool indicating if it should be cached. May be `None`.   
  
### `get_memcache_timeout_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L661-L663)
    
    
    get_memcache_timeout_policy()
    

Return the current policy function for memcache timeout (expiration).

### `in_transaction`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1092-L1094)
    
    
    in_transaction()
    

Return whether a transaction is currently active.

### `iter_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L964-L969)
    
    
    iter_query(
        query, callback=None, pass_batch_into_callback=None, options=None
    )
    

### `map_query`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L902-L941)
    
    
    map_query(
        query,
        callback,
        pass_batch_into_callback=None,
        options=None,
        merge_future=None
    )
    

### `memcache_add`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1255-L1263)
    
    
    memcache_add(
        key, value, time=0, namespace=None, deadline=None
    )
    

### `memcache_cas`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1275-L1283)
    
    
    memcache_cas(
        key, value, time=0, namespace=None, deadline=None
    )
    

### `memcache_decr`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1309-L1322)
    
    
    memcache_decr(
        key, delta=1, initial_value=None, namespace=None, deadline=None
    )
    

### `memcache_delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1285-L1292)
    
    
    memcache_delete(
        key, seconds=0, namespace=None, deadline=None
    )
    

### `memcache_get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1207-L1232)
    
    
    memcache_get(
        key, for_cas=False, namespace=None, use_cache=False, deadline=None
    )
    

An auto-batching wrapper for [`memcache.get()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/get) or `.get_multi()`.

Args  
---  
  
`key` |  Key to set. This must be a string; no prefix is applied.   
`for_cas` |  If `True`, request and store CAS ids on the Context.   
`namespace` |  Optional namespace.   
`deadline` |  Optional deadline for the RPC.   
  
Returns  
---  
A Future (!) whose return value is the value retrieved from memcache, or `None`.   
  
### `memcache_gets`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1236-L1238)
    
    
    memcache_gets(
        key, namespace=None, use_cache=False, deadline=None
    )
    

### `memcache_incr`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1294-L1307)
    
    
    memcache_incr(
        key, delta=1, initial_value=None, namespace=None, deadline=None
    )
    

### `memcache_replace`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1265-L1273)
    
    
    memcache_replace(
        key, value, time=0, namespace=None, deadline=None
    )
    

### `memcache_set`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1240-L1253)
    
    
    memcache_set(
        key, value, time=0, namespace=None, use_cache=False, deadline=None
    )
    

### `put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L813-L870)
    
    
    put(
        entity, **ctx_options
    )
    

### `set_cache_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L454-L465)
    
    
    set_cache_policy(
        func
    )
    

Set the context cache policy function.

Args  
---  
  
`func` |  A function that accepts a `Key` instance as argument and returns a bool indicating if it should be cached. May be `None`.   
  
### `set_datastore_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L588-L599)
    
    
    set_datastore_policy(
        func
    )
    

Set the context datastore policy function.

Args  
---  
  
`func` |  A function that accepts a `Key` instance as argument and returns a bool indicating if it should use the datastore. May be `None`.   
  
### `set_memcache_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L521-L532)
    
    
    set_memcache_policy(
        func
    )
    

Set the memcache policy function.

Args  
---  
  
`func` |  A function that accepts a Key instance as argument and returns a bool indicating if it should be cached. May be None.   
  
### `set_memcache_timeout_policy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L646-L659)
    
    
    set_memcache_timeout_policy(
        func
    )
    

Set the policy function for memcache timeout (expiration).

If the function returns `0`, it implies the default timeout.

Args  
---  
  
`func` |  A function that accepts a key instance as argument and returns an integer indicating the desired memcache timeout. May be `None`.   
  
### `transaction`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L971-L1090)
    
    
    transaction(
        callback, **ctx_options
    )
    

### `urlfetch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/ndb/context.py#L1324-L1337)
    
    
    urlfetch(
        url,
        payload=None,
        method='GET',
        headers={},
        allow_truncated=False,
        follow_redirects=True,
        validate_certificate=None,
        deadline=None,
        callback=None
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
