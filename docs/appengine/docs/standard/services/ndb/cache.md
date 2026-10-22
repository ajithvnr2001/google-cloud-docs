---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/cache/
title: NDB Caching \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:41.406092+00:00
---

# NDB Caching  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Caching Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

NDB manages caches for you. There are two caching levels: an in-context cache and a gateway to App Engine's standard caching service, memcache. Both caches are enabled by default for all entity types, but can be configured to suit advanced needs. In addition, NDB implements a feature called auto-batching, which tries to group operations together to minimize server round trips. 

## Introduction

Caching helps most types of applications. NDB automatically caches data that it writes or reads (unless an application configures it not to). Reading from cache is faster than reading from the Datastore. 

You can alter caching behavior of many NDB functions by passing [Context Options](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions#context_options) arguments. For example, you might call `key.get(use_cache=False, use_memcache=False)` to bypass caching. You can also change default caching policy on an NDB context as described below. 

**Caution:** When you use the Administration Console's Datastore Viewer to modify the Datastore contents, the cached values will not be updated. Thus, your cache may be inconsistent. For the in-context cache this is generally not a problem. For Memcache, we recommend using the Administration Console to flush the cache. 

## Context Objects

Cache management uses a class named `[Context](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/contextclass)`: each thread and each transaction is executed in a new context. Because each incoming HTTP request starts a new thread, each request is executed with a new context as well. To access the current context, use the `ndb.get_context()` function. 

**Caution:** It makes no sense to share `Context` objects between multiple threads or requests. **Don't save the context as a global variable!** Storing it in a local or thread-local variable is fine. 

Context objects have methods for setting cache policies and otherwise manipulating the cache. 

## The In-Context Cache

The in-context cache persists only for the duration of a single thread. This means that each incoming HTTP request is given a new in-context cache and is "visible" only to the code that handles that request. If your application spawns any additional threads while handling a request, those threads will also have a new, separate in-context cache. 

The in-context cache is fast; this cache lives in memory. When an NDB function writes to the Datastore, it also writes to the in-context cache. When an NDB function reads an entity, it checks the in-context cache first. If the entity is found there, no Datastore interaction takes place. 

When an NDB function queries the Datastore, the result list is retrieved from the Datastore. However, if any individual result is in the in-context cache, it is used in place of the value retrieved from the Datastore query. Query results are written back to the in-context cache if the cache policy says so (but never to Memcache). 

With executing long-running queries in background tasks, it's possible for the in-context cache to consume large amounts of memory. This is because the cache keeps a copy of every entity that is retrieved or stored in the current context. To avoid memory exceptions in long-running tasks, you can disable the cache or set a policy that excludes whichever entities are consuming the most memory. 

## Memcache

[Memcache](https://docs.cloud.google.com/appengine/docs/standard/services/memcache) is App Engine's standard caching service, much faster than the Datastore but slower than the in-context cache (milliseconds vs. microseconds). 

By default, a nontransactional context caches all entities in memcache. All an application's contexts use the same memcache server and see a consistent set of cached values. 

Memcache does not support transactions. Thus, an update meant to be applied to both the Datastore and memcache _might_ be made to only one of the two. To maintain consistency in such cases (possibly at the expense of performance), the updated entity is deleted from memcache and then written to the Datastore. A subsequent read operation will find the entity missing from memcache, retrieve it from the Datastore, and then update it in memcache as a side effect of the read. Also, NDB reads inside transactions ignore the Memcache. 

When entities are written within a transaction, memcache is not used; when the transaction is committed, its context will attempt to delete all such entities from memcache. Note, however, that some failures may prevent these deletions from happening. 

## Policy Functions

Automatic caching is convenient for _most_ applications but maybe your application is unusual and you want to turn off automatic caching for some or all entities. You can control the behavior of the caches by setting policy functions. There is a policy function for the in-process cache, set with 
    
    
    context = ndb.get_context()
    context.set_cache_policy(func)

and another for memcache, set with 
    
    
    context = ndb.get_context()
    context.set_memcache_policy(func)

Each policy function accepts a key and returns a Boolean result. If it returns `False`, the entity identified by that key will not be saved in the corresponding cache. For example, to bypass the in-process cache for all `Account` entities, you could write 
    
    
    context = ndb.get_context()
    context.set_cache_policy(lambda key: key.kind() != 'Account')

(However, keep reading for an easier way to accomplish the same thing.) As a convenience, you can pass `True` or `False` instead of a function that always returns the same value. The default policies cache all entities. 

There is also a Datastore policy function governing which entities are written to the Datastore itself: 
    
    
    context = ndb.get_context()
    context.set_datastore_policy(func)

This works like the in-context cache and memcache policy functions: if the Datastore policy function returns `False` for a given key, the corresponding entity will not be written to the Datastore. (It may be written to the in-process cache or memcache if their policy functions allow it.) This can be useful in cases where you have entity-like data that you would like to cache, but that you don't need to store in the Datastore. Just as for the cache policies, you can pass `True` or `False` instead of a function that always returns the same value. 

Memcache [ automatically expires items](https://docs.cloud.google.com/appengine/docs/standard/services/memcache#how_cached_data_expires) when under memory pressure. You can set a memcache timeout policy function to determine an entity's maximum lifetime in the cache: 
    
    
    context = ndb.get_context()
    context.set_memcache_timeout_policy(func)

This function is called with a key argument and should return an integer specifying the maximum lifetime in seconds; 0 or `None` means indefinite (as long as the memcache server has enough memory). For convenience, you can simply pass an integer constant instead of a function that always returns the same value. See the memcache documentation for more information about timeouts. 

**Note:** There is no separate lifetime policy for the in-context cache: the cache's lifetime is the same as that of its context, a single incoming HTTP request. However, you can clear the in-process cache by calling 
    
    
    context = ndb.get_context()
    context.clear_cache()

A brand-new context starts out with an empty in-process cache. 

While policy functions are very flexible, in practice most policies are simple. For example, 

  * Don't cache entities belonging to a specific model class. 
  * Set the memcache timeout for entities in this model class to 30 seconds. 
  * Entities in this model class need not be written to the Datastore. 



To save you the work of writing and continually updating trivial policy functions (or worse, overriding the policies for each operation using context options), the default policy functions obtain the model class from the key passed to them and then look in the model class for specific class variables: 

Class Variable | Type | Description   
---|---|---  
`_use_cache `| `bool `| Specifies whether to store entities in in-process cache; overrides default in-process cache policy.   
`_use_memcache `| `bool `| Specifies whether to store entities in memcache; overrides default memcache policy.   
`_use_datastore `| `bool `| Specifies whether to store entities in datastore; overrides default Datastore policy.   
`_memcache_timeout `| `int `| Maximum lifetime for entities in memcache; overrides default memcache timeout policy.   
  
**Note:** This is a feature of the default policy function for each policy. If you specify your own policy function but also want to fall back to the default policy, call the default policy functions explicitly as static methods of class `Context`: 

  * `default_cache_policy(key)`
  * `default_memcache_policy(key)`
  * `default_datastore_policy(key)`
  * `default_memcache_timeout_policy(key)`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
