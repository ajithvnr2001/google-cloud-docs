---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/contextclass/
title: NDB Context class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:52.428085+00:00
---

# NDB Context class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/contextclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Context class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

An application can use a _Context_ to control its caching policy. `Context` also offers convenient asynchronous APIs for Memcache and URL Fetch integrated into NDB's asynchronous facilities; in particular, the Memcache API supports auto-batching. 

  * Cache Management Instance Methods 
    * `clear_cache()`
    * `flush()`
    * `get_cache_policy()`
    * `get_datastore_policy()`
    * `get_memcache_policy()`
    * `get_memcache_timeout_policy()`
    * `set_cache_policy()`
    * `set_datastore_policy()`
    * `set_memcache_policy()`
    * `set_memcache_timeout_policy()`
  * Memcache and Urlfetch Instance Methods 
    * `memcache_add()`
    * `memcache_cas()`
    * `memcache_decr()`
    * `memcache_delete()`
    * `memcache_get()`
    * `memcache_gets()`
    * `memcache_incr()`
    * `memcache_replace()`
    * `memcache_set()`
    * `urlfetch()`
  * Transaction Management Methods 
    * `call_on_commit()`
    * `in_transaction()`
  * Static Methods 
    * `default_cache_policy()`
    * `default_datastore_policy()`
    * `default_memcache_policy()`
    * `default_memcache_timeout_policy()`



## Cache Management Instance Methods

clear_cache()
    Clears the in-context cache.
flush()
    Flush all auto-batcher queues (sending their work to the servers). The flush happens asynchronously. 

Returns a `Future`. To wait for the flushing to finish, call this object's `wait()` method. 

get_cache_policy()
    Returns the cache policy function. This policy function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns a `bool` indicating whether the entity with this key should be cached in the in-context cache. May be `None` (meaning use ` default_cache_policy`). 
get_datastore_policy()
    Returns the current context Datastore policy function. This policy function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns a `bool` indicating if it should use the Datastore. May be `None` (meaning use ` default_datastore_policy`). 
get_memcache_policy()
    Returns the current memcache policy function. This policy function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns a `bool` indicating if it should be cached. May be `None` (meaning use ` default_memcache_policy`). 
get_memcache_timeout_policy()
    Returns the current memcache timeout policy function. This policy function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns the desired memcache timeout in seconds (or returns zero to use the default timeout). May be `None`, which uses ` default_memcache_timeout_policy`. 
set_cache_policy(func)
    Sets the cache policy function. 

**Arguments**

func
    This function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns a `bool` indicating whether the entity with this key should be cached in the in-context cache. May be `None`. 
set_datastore_policy(func)
    Sets the Datastore policy function. 

**Arguments**

func
    This function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns a `bool` indicating whether the entity with this key should be stored in the persistent Datastore. May be `None`. 
set_memcache_policy(func)
    Sets the memcache policy function. 

**Arguments**

func
    This function takes a [Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass) instance argument and returns a `bool` indicating whether the entity with this key should be cached in the in-context cache. May be `None`. 
set_memcache_timeout_policy(func)
    Sets the memcache timeout policy function. 

**Arguments**

func
    This function takes a `[Key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass)` instance argument and returns the desired memcache timeout in seconds (or returns zero to use the default timeout). May be `None`. 

## Memcache and Urlfetch Instance Methods

The full list of methods is found in the [ Memcache](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache) API reference. The list below highlights some of the more commonly used methods: 

memcache_add(key, value, time, namespace)
    Async auto-batching memcache `[ add()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#add)`.
memcache_cas(key, value, time, namespace)
    Async auto-batching memcache `Client` `[ cas()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#cas)` (compare-and-swap).
memcache_decr(key, delta, initial_value, namespace)
    Async auto-batching memcache `[ decr()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#decr)`.
memcache_delete(key, seconds, namespace)
    Async auto-batching memcache `[ delete()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#delete)`.
memcache_get(key, namespace, use_cache)
    Async auto-batching memcache `[ get()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#get)`. 

Returns a `Future` whose return value is the value retrieved from memcache or `None`.

memcache_gets(key, namespace, use_cache)
    Async auto-batching memcache `[ gets()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#gets)`.
memcache_incr(key, delta, initial_value, namespace)
    Async auto-batching memcache `[ incr()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#incr)`.
memcache_replace(key, value, time, namespace)
    Async auto-batching memcache `[ replace()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#replace)`.
memcache_set(key, value, time, namespace, use_cache)
    Async auto-batching memcache `[ set()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client#set)`.
urlfetch(url, payload, method, headers, allow_truncated, follow_redirects, validate_certificate, deadline, callback)
    Async auto-batching urlfetch `[ fetch()](https://docs.cloud.google.com/appengine/docs/standard/services/urlfetch/issue-requests).`

## Transaction Management Methods

call_on_commit(callback)
    Queues a callback to call upon successful commit of a transaction. 

If not in a transaction, the callback is called immediately. 

In a transaction, multiple callbacks may be registered and will be called once the transaction commits in the order in which they were registered. If the transaction fails, the callbacks will not be called. 

If a callback raises an exception, it bubbles up normally. This means: If the callback is called immediately, any exception it raises will bubble up immediately. If the call is postponed until commit, remaining callbacks will be skipped and the exception will bubble up through the `transaction()` call. (However, the transaction is already committed at that point.) 

**Arguments**

callback
    Callback function. This callback function takes no parameters and returns nothing. 
in_transaction()
    Returns `True` if this Context represents a transaction, `False` otherwise.

## Static Methods

default_cache_policy(key)
    Checks for a `[_use_cache](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model__use_cache)` class variable on the entity's model class; if there is one, return it. Otherwise, return `None`. 
default_datastore_policy(key)
    Checks for a `[_use_datastore](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model__use_datastore)` class variable on the entity's model class; if there is one, return it. Otherwise, return `None`. 
default_memcache_policy(key)
    Checks for a `[_use_memcache](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model__use_memcache)` class variable on the entity's model class; if there is one, return it. Otherwise, return `None`. 
default_memcache_timeout_policy(key)
    Checks for a `[_memcache_timeout](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass#Model__memcache_timeout)` class variable on the entity's model class; if there is one, return it. Otherwise, return `None`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
