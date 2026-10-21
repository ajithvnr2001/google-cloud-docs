---
url: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions/
title: NDB Functions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:52.743662+00:00
---

# NDB Functions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/ndb/functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  NDB Functions Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

## Functions

ndb.add_flow_exception(exc)
    Specify that an exception should _not_ be logged, but is just part of normal program flow. (Normally, raising an exception writes a warning message to the application's logs.) 

**Arguments**

exc
    Exception class that should not be logged. 

By default, the following exceptions are not logged: 

  * `webob.exc.HTTPException` (and its subclasses) 
  * `ndb.Rollback`


ndb.delete_multi(keys, **ctx_options)
    Deletes entities identified by the passed sequence of keys. 

**Arguments**

keys
    Sequence of [keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass)
**ctx_options
    Context options
ndb.delete_multi_async(keys, **ctx_options)
    Asynchronously deletes entities identified by the passed sequence of keys. 

**Arguments**

keys
    Sequence of [keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass)
**ctx_options
    Context options

Returns a list of `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` objects. Each future's result will be `None`. 

ndb.get_multi(keys, **ctx_options)
    Fetches entities identified by the passed sequence of keys. 

**Arguments**

keys
    Sequence of [keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass)
**ctx_options
    Context options

Returns a list. Each list item is either a [Model](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass) instance or `None` if the key wasn't found. 

ndb.get_multi_async(keys, **ctx_options)
    Asynchronously fetches entities identified by the passed sequence of keys. 

**Arguments**

keys
    Sequence of [keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass)
**ctx_options
    Context options

Returns a list of `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` objects. Each future's result is a [Model](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass) instance or `None` if the key wasn't found. 

ndb.in_transaction()
    Returns a Boolean indicating whether a transaction is currently active. 
@ndb.non_transactional  
@ndb.non_transactional(allow_existing=True)
    Decorator to ensure that a function runs _outside_ a transaction. 

**Arguments:**

allow_existing
    If `True` (the default) and if the decorated function is called by code in a transaction, the function runs independent of the transaction. If `False` and if the decorated function is called by code in a transaction, it raises an exception. 
ndb.put_multi(entities, **ctx_options)
    Stores a sequence of [Model](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass) instances. 

**Arguments**

entities
    Sequence of [Model](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass) instances
**ctx_options
    Context options

Returns a list with the stored [keys](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass). 

ndb.put_multi_async(entities, **ctx_options)
    Asynchronously stores a sequence of [Model](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass) instances. 

**Arguments**

entities
    Sequence of [Model](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/modelclass) instances
**ctx_options
    Context options

Returns a list of `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)` objects. Each future's result will be a stored [key](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/keyclass). 

ndb.transaction(callback, **ctx_options)
    Run a callback in a transaction. 

**Arguments**

callback
    Function or tasklet to be called
**ctx_options
    Transaction options

Returns whatever callback returns. Raises whatever callback raises or a `TransactionFailedError` exception if the transaction fails. 

To pass arguments to a callback function, use a lambda. For example, 
    
    
    def my_callback(key, inc):
      ...
    
    transaction(lambda: my_callback(Key(...), 1))

ndb.transaction_async(callback, **ctx_options)
    Asynchronously run a callback in a transaction. 

**Arguments**

callback
    Function or tasklet to be called
**ctx_options
    Transaction options

Returns a `[Future](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/futureclass)`. The future returns whatever callback returns, or raises whatever callback raises or a `TransactionFailedError` if the transaction fails. 

To pass arguments to a callback function, use a lambda. For example, 
    
    
    def my_callback(key, inc):
      ...
    
    transaction(lambda: my_callback(Key(...), 1))

@ndb.transactional  
@ndb.transactional(**ctx_options)
    Decorator to make a function automatically run in a transaction. 

**Arguments:**

This decorator can have transaction options. 

## Context Options, Transaction Options

Context options allow you to run specific datastore operations with different configurations. For example, you might want to vary the read policy or the RPC deadline for individual requests. You can do this by passing _context options_ to almost any operation. Some transaction-related functions take _transaction options_ , which include additional options on top of a set of context options. 

Here are a few examples using context options. To set the RPC deadline to 1 second when reading an entity, you can use: 
    
    
    key.get(deadline=1)

To set the memcache timeout to 30 seconds when writing an entity, you can use: 
    
    
    ent.put(ndb_memcache_timeout=30)

To delete an item that has been cached and force its reload, you can use: 
    
    
    key.delete(use_datastore=False)

The special keyword arguments `options` and `config` (which have identical meanings for historical reasons) allow one to specify several options as a Configuration object. This can be an `ndb.ContextOptions` object or (for the transactional functions and decorator) an `ndb.TransactionOptions` object. For example, `key.get(options=ndb.ContextOptions(use_cache=True))` is equivalent to `key.get(use_cache=True)`. The options set in such an options object can be overridden by keyword parameters. 

The following **context options** are available: 

Option | Type | Description   
---|---|---  
`deadline` | `float` | Datastore call deadline, specified as a number of seconds. (By default, the call is only interrupted by the request handler deadline.)   
`read_policy` | `ndb.EVENTUAL_CONSISTENCY` | Set this to `ndb.EVENTUAL_CONSISTENCY` if, instead of waiting for the Datastore to finish applying changes to all returned results, you wish to get possibly-not-current results faster.   
`force_writes` | `bool` | Specifies whether a write request should succeed even if the app is read-only. (This only applies to user controlled read-only periods.)   
`use_cache `| `bool `| Specifies whether to store entities in in-process cache; overrides in-process cache policy for this operation.   
`use_memcache `| `bool `| Specifies whether to store entities in memcache; overrides memcache policy for this operation.   
`use_datastore `| `bool `| Specifies whether to store entities in Datastore; overrides Datastore policy for this operation.   
`memcache_timeout `| `int `| Maximum lifetime for entities in memcache; overrides memcache timeout policy for this operation.   
`max_memcache_items `| `int ` | Maximum batch size for the auto-batching feature of the [Context](https://docs.cloud.google.com/appengine/docs/standard/services/ndb/contextclass) memcache methods. For example, with the default size of `max_memcache_items` (100), up to 100 memcache set operations will be combined into a single `set_multi` operation.   
For some transaction-related functions, the following **transaction options** are available (along with the inherited context options listed above):   
Option | Type | Description   
`xg` | `bool` | Allow cross-group (`XG`) transactions. `False` by default.   
`propagation` | `int` | NDB provides limited support for transactions within transactions, which are known as "nested transactions". The propagation parameter controls what happens if your code tries to start a nested transaction. The propagation policy for `@ndb.transactional` defaults to `ALLOWED`. The propagation policy for `ndb.transaction()` defaults to `NESTED`. The `NESTED` policy is not supported by NDB so your code will throw a `BadRequestError` exception. NDB sets an unsupported default value, in this case, so that programmers are explicitly aware of the limitations of nested transactions. The propagation parameter can be one of the following values:

`ndb.TransactionOptions.NESTED`
    The `NESTED` propagation policy would commit all changes in the outer and inner transactions together when the outer policy commits. However, if an exception is thrown in the inner transaction all changes there would get thrown out but allow the outer transaction to optionally recover and continue. The `NESTED` policy is not supported. If you use this policy, your code will throw a `BadRequestError` exception. 
`ndb.TransactionOptions.MANDATORY`
    Always propagate an existing transaction; throw an exception if there is no existing transaction. If a function that uses this policy throws an exception, it's probably not safe to catch the exception and commit the outer transaction; the function may have left the outer transaction in a bad state. 
`ndb.TransactionOptions.ALLOWED`
    If there is an existing transaction, propagate it. If a function that uses this policy throws an exception, it's probably not safe to catch the exception and commit the outer transaction; the function may have left the outer transaction in a bad state. 
`ndb.TransactionOptions.INDEPENDENT`
    Always use a new transaction, "pausing" any existing transactions. A function that uses this policy should not return any entities read in the new transaction, as the entities are not transactionally consistent with the caller's transaction.   
`retries` | `int` | How many times to retry automatically in case of transaction failures. Zero means to try once but not _re_ -try.   
  
In some cases, options are ignored because of caching. For example, if you specify an RPC deadline for a read operation that is satisfied from the in-context cache, the deadline is ignored. On the other hand, unrecognized options cause `TypeError` to be raised. 

Operations with different options are grouped together when auto-batching applies. For example, if you use `put_async()` to write some entities with `deadline = 5` and some without specifying a deadline, and all are eligible for auto-batching, the auto-batcher will make two separate RPC calls—one for the group of entities with `deadline = 5` and one for the other group—even though the default RPC deadline is also 5! This applies even if the option specified is irrelevant to the RPC operation (for example, `ndb_should_cache`). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
