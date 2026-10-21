---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client/
title: google.appengine.api.memcache.Client \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:45:40.242205+00:00
---

# google.appengine.api.memcache.Client  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.memcache.Client Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L364-L1702) Memcache client object, through which one invokes all memcache operations. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.memcache.Client(
        servers=None,
        debug=0,
        pickleProtocol=six.moves.cPickle.HIGHEST_PROTOCOL,
        pickler=six.moves.cPickle.Pickler,
        unpickler=six.moves.cPickle.Unpickler,
        pload=None,
        pid=None,
        make_sync_call=None,
        _app_id=None
    )
    

Several methods are no-ops to retain source-level compatibility with the existing popular Python memcache library. Any method that takes a 'key' argument will accept that key as a string (unicode or not) or a tuple of `(hash_value, string)` where the hash_value, normally used for sharding onto a memcache instance, is instead ignored, as Google App Engine deals with the sharding transparently. Keys in memcache are just bytes, without a specified encoding. All such methods may raise `TypeError` if provided a bogus key value and a `ValueError` if the key is too large. Any method that takes a 'value' argument will accept as that value any `string` (unicode or not), `int`, `long`, or pickle-able Python object, including all native types. You'll get back from the cache the same type that you originally put in. The `Client` class is not thread-safe with respect to the `gets()`, `cas()` and `cas_multi()` methods (and other compare-and-set-related methods). Therefore, `Client` objects should not be used by more than one thread for CAS purposes. Note that the global `Client` for the module-level functions is okay because it does not expose any of the CAS methods. | 

## Arguments  
  
---  
  
`servers` |  Ignored; only for compatibility.   
`debug` |  Ignored; only for compatibility.   
`pickleProtocol` |  Pickle protocol to use for pickling the object.   
`pickler` |  pickle.Pickler sub-class to use for pickling.   
`unpickler` |  pickle.Unpickler sub-class to use for unpickling.   
`pload` |  Callable to use for retrieving objects by persistent id.   
`pid` |  Callable to use for determine the persistent id for objects, if any.   
`make_sync_call` |  Ignored; only for compatibility with an earlier version.   
  
## Methods

### `add`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L945-L964)
    
    
    add(
        key, value, time=0, min_compress_len=0, namespace=None
    )
    

Sets a key's value if the item is not already in memcache.

Args  
---  
  
`key` |  Key to set. See docs on Client for details.   
`value` |  Value to set. Any type. If complex, will be pickled.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`min_compress_len` |  Ignored option for compatibility.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
`True` if added. `False` on error.   
  
### `add_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1234-L1263)
    
    
    add_multi(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None
    )
    

Set multiple keys' values if items are not already in memcache.

Args  
---  
  
`mapping` |  Dictionary of keys to values.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`key_prefix` |  Prefix for to prepend to all keys.   
`min_compress_len` |  Unimplemented compatibility option.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
A list of keys whose values were NOT set because they already exist in memcache. On total success, this list should be empty.   
  
### `add_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1265-L1283)
    
    
    add_multi_async(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None,
        rpc=None
    )
    

Async version of `add_multi()` \-- note different return value.

Returns  
---  
See `_set_multi_async_with_policy()`.   
  
### `cas`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L987-L1027)
    
    
    cas(
        key, value, time=0, min_compress_len=0, namespace=None
    )
    

Compare-And-Set update.

This requires that the key has previously been successfully fetched with `gets()` or `get(..., for_cas=True)`, and that no changes have been made to the key since that fetch. Typical usage is:

key = ... client = memcache.Client() value = client.gets(key) # `OR` client.get(key, for_cas=True)  ok = client.cas(key, value)

If two processes run similar code, the first one calling `cas()` will succeed (`ok == True`), while the second one will fail (`ok == False`). This can be used to detect race conditions.

NOTE: Some state (the CAS id) is stored on the `Client` object for each key ever used with `gets()`. To prevent ever-increasing memory usage, you must use a `Client` object when using `cas()`, and the lifetime of your `Client` object should be limited to that of one incoming HTTP request. You cannot use the global-function-based API.

Args  
---  
  
`key` |  Key to set. See docs on `Client` for details.   
`value` |  The new value.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`min_compress_len` |  Ignored option for compatibility.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
`True` if updated. `False` on RPC error or if the CAS id didn't match.   
  
### `cas_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1336-L1367)
    
    
    cas_multi(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None
    )
    

Compare-And-Set update for multiple keys.

See `cas()` docstring for an explanation.

Args  
---  
  
`mapping` |  Dictionary of keys to values.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`key_prefix` |  Prefix for to prepend to all keys.   
`min_compress_len` |  Unimplemented compatibility option.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
A list of keys whose values were NOT set because the compare failed. On total success, this list should be empty.   
  
### `cas_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1369-L1387)
    
    
    cas_multi_async(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None,
        rpc=None
    )
    

Async version of `cas_multi()` \-- note different return value.

Returns  
---  
See `_set_multi_async_with_policy()`.   
  
### `cas_reset`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L431-L433)
    
    
    cas_reset()
    

Clear the remembered CAS ids.

### `debuglog`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L507-L512)
    
    
    debuglog()
    

Logging function for debugging information.

This is purely a compatibility method. In Google App Engine, it's a no-op.

### `decr`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1449-L1483)
    
    
    decr(
        key, delta=1, namespace=None, initial_value=None
    )
    

Atomically decrements a key's value.

Internally, the value is a unsigned 64-bit integer. Memcache caps decrementing below zero to zero.

The key must already exist in the cache to be decremented. See docs on `incr()` for details.

Args  
---  
  
`key` |  Key to decrement. If an iterable collection, each one of the keys will be offset. See Client's docstring for details.   
`delta` |  Non-negative integer value (int or long) to decrement key by, defaulting to 1.   
`namespace` |  a string specifying an optional namespace to use in the request.   
`initial_value` |  initial value to put in the cache, if it doesn't already exist. The default value, None, will not create a cache entry if it doesn't already exist.   
  
Returns  
---  
If key was a single value, the new long integer value, or None if key was not in the cache, could not be decremented for any other reason, or a network/RPC/server error occurred. If key was an iterable collection, a dictionary will be returned mapping supplied keys to values, with the values having the same meaning as the singular return value of this method.   
  
Raises  
---  
  
`ValueError` |  If number is negative.   
`TypeError` |  If delta isn't an int or long.   
  
### `decr_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1485-L1503)
    
    
    decr_async(
        key, delta=1, namespace=None, initial_value=None, rpc=None
    )
    

Async version of `decr()`.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns the same kind of value as `decr()` returns.   
  
### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L809-L835)
    
    
    delete(
        key, seconds=0, namespace=None
    )
    

Deletes a key from memcache.

Args  
---  
  
`key` |  Key to delete. See docs on Client for detils.   
`seconds` |  Optional number of seconds to make deleted items 'locked' for 'add' operations. Value can be a delta from current time (up to 1 month), or an absolute Unix epoch time. Defaults to 0, which means items can be immediately added. With or without this option, a 'set' operation will always work. Float values will be rounded up to the nearest whole second.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
`DELETE_NETWORK_FAILURE (0)` on network failure, `DELETE_ITEM_MISSING (1) if the server tried to delete the item but didn't have it, or`DELETE_SUCCESSFUL (2)` if the item was actually deleted. This can be used as a boolean value, where a network failure is the only bad condition.   
  
### `delete_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L837-L859)
    
    
    delete_multi(
        keys, seconds=0, key_prefix='', namespace=None
    )
    

Delete multiple keys at once.

Args  
---  
  
`keys` |  List of keys to delete.   
`seconds` |  Optional number of seconds to make deleted items 'locked' for 'add' operations. Value can be a delta from current time (up to 1 month), or an absolute Unix epoch time. Defaults to 0, which means items can be immediately added. With or without this option, a 'set' operation will always work. Float values will be rounded up to the nearest whole second.   
`key_prefix` |  Prefix to put on all keys when sending specified keys to memcache. See docs for `get_multi()` and `set_multi()`.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
`True` if all operations completed successfully. `False` if one or more failed to complete.   
  
### `delete_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L861-L892)
    
    
    delete_multi_async(
        keys, seconds=0, key_prefix='', namespace=None, rpc=None
    )
    

Async version of `delete_multi()` \-- note different return value.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns `None` if there was a network error, or a list of status values otherwise, where each status corresponds to a key and is either `DELETE_SUCCESSFUL`, `DELETE_ITEM_MISSING`, or `DELETE_NETWORK_FAILURE` (see `delete()` docstring for details).   
  
### `disconnect_all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L493-L498)
    
    
    disconnect_all()
    

Closes all connections to memcache servers.

This is purely a compatibility method. In Google App Engine, it's a no-op.

### `flush_all`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L581-L588)
    
    
    flush_all()
    

Deletes everything in memcache.

Returns  
---  
`True` on success, `False` on RPC or server error.   
  
### `flush_all_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L590-L601)
    
    
    flush_all_async(
        rpc=None
    )
    

Async version of `flush_all()`.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns `True` on success, `False` on RPC or server error.   
  
### `forget_dead_hosts`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L500-L505)
    
    
    forget_dead_hosts()
    

Resets all servers to the alive status.

This is purely a compatibility method. In Google App Engine, it's a no-op.

### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L610-L633)
    
    
    get(
        key, namespace=None, for_cas=False
    )
    

Looks up a single key in memcache.

If you have multiple items to load, though, it's much more efficient to use `get_multi()` instead, which loads them in one bulk operation, reducing the networking latency that'd otherwise be required to do many serialized `get()` operations.

Args  
---  
  
`key` |  The key in memcache to look up. See docs on Client for details of format.   
`namespace` |  a string specifying an optional namespace to use in the request.   
`for_cas` |  If `True`, request and store CAS ids on the client (see `cas()` operation below).   
  
Returns  
---  
The value of the key, if found in memcache, else `None`.   
  
### `get_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L639-L662)
    
    
    get_multi(
        keys, key_prefix='', namespace=None, for_cas=False
    )
    

Looks up multiple keys from memcache in one operation.

This is the recommended way to do bulk loads.

Args  
---  
  
`keys` |  List of keys to look up. Keys may be strings or tuples of `(hash_value, string)`. Google App Engine does the sharding and hashing automatically, though, so the hash value is ignored. To memcache, keys are just series of bytes, and not in any particular encoding.   
`key_prefix` |  Prefix to prepend to all keys when talking to the server; not included in the returned dictionary.   
`namespace` |  a string specifying an optional namespace to use in the request.   
`for_cas` |  If `True`, request and store CAS ids on the client.   
  
Returns  
---  
A dictionary of the keys and values that were present in memcache. Even if the key_prefix was specified, that key_prefix won't be on the keys in the returned dictionary.   
  
### `get_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L664-L688)
    
    
    get_multi_async(
        keys, key_prefix='', namespace=None, for_cas=False, rpc=None
    )
    

Async version of `get_multi()`.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns {} if there was a network error, otherwise a `dict` just like `get_multi()` returns.   
  
### `get_stats`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L514-L539)
    
    
    get_stats()
    

Gets memcache statistics for this application.

All of these statistics may reset due to various transient conditions. They provide the best information available at the time of being called.

Returns  
---  
Dictionary mapping statistic names to associated values. Statistics and their associated meanings: hits: Number of cache get requests resulting in a cache hit. misses: Number of cache get requests resulting in a cache miss. byte_hits: Sum of bytes transferred on get requests. Rolls over to zero on overflow. items: Number of key/value pairs in the cache. bytes: Total size of all items in the cache. oldest_item_age: How long in seconds since the oldest item in the cache was accessed. Effectively, this indicates how long a new item will survive in the cache without being accessed. This is _not_ the amount of time that has elapsed since the item was created. On error, returns `None`.   
  
### `get_stats_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L541-L553)
    
    
    get_stats_async(
        rpc=None
    )
    

Async version of `get_stats()`.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns `None` if there was a network error, otherwise a `dict` just like `get_stats()` returns.   
  
### `gets`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L635-L637)
    
    
    gets(
        key, namespace=None
    )
    

An alias for `get(..., for_cas=True)`.

### `incr`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1389-L1427)
    
    
    incr(
        key, delta=1, namespace=None, initial_value=None
    )
    

Atomically increments a key's value.

Internally, the value is a unsigned 64-bit integer. Memcache doesn't check 64-bit overflows. The value, if too large, will wrap around.

Unless an initial_value is specified, the key must already exist in the cache to be incremented. To initialize a counter, either specify initial_value or `set()` it to the initial value, as an ASCII decimal integer. Future `get()`s of the key, post-increment, will still be an ASCII decimal value.

Args  
---  
  
`key` |  Key to increment. If an iterable collection, each one of the keys will be offset. See Client's docstring for details.   
`delta` |  Non-negative integer value (int or long) to increment key by, defaulting to 1.   
`namespace` |  a string specifying an optional namespace to use in the request.   
`initial_value` |  initial value to put in the cache, if it doesn't already exist. The default value, None, will not create a cache entry if it doesn't already exist.   
  
Returns  
---  
If key was a single value, the new long integer value, or None if key was not in the cache, could not be incremented for any other reason, or a network/RPC/server error occurred. If key was an iterable collection, a dictionary will be returned mapping supplied keys to values, with the values having the same meaning as the singular return value of this method.   
  
Raises  
---  
  
`ValueError` |  If number is negative.   
`TypeError` |  If delta isn't an int or long.   
  
### `incr_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1429-L1447)
    
    
    incr_async(
        key, delta=1, namespace=None, initial_value=None, rpc=None
    )
    

Async version of `incr()`.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns the same kind of value as `incr()` returns.   
  
### `offset_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1607-L1631)
    
    
    offset_multi(
        mapping, key_prefix='', namespace=None, initial_value=None
    )
    

Offsets multiple keys by a delta, incrementing and decrementing in batch.

Args  
---  
  
`mapping` |  Dictionary mapping keys to deltas (positive or negative integers) to apply to each corresponding key.   
`key_prefix` |  Prefix for to prepend to all keys.   
`initial_value` |  Initial value to put in the cache, if it doesn't already exist. The default value, None, will not create a cache entry if it doesn't already exist.   
`namespace` |  A string specifying an optional namespace to use in the request.   
  
Returns  
---  
Dictionary mapping input keys to new integer values. The new value will be None if an error occurs, the key does not already exist, or the value was not an integer type. The values will wrap-around at unsigned 64-bit integer-maximum and underflow will be floored at zero.   
  
### `offset_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1633-L1682)
    
    
    offset_multi_async(
        mapping,
        key_prefix='',
        namespace=None,
        initial_value=None,
        rpc=None
    )
    

Async version of `offset_multi()`.

Returns  
---  
A `UserRPC` instance whose `get_result()` method returns a dict just like `offset_multi()` returns.   
  
### `peek`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L710-L731)
    
    
    peek(
        key, namespace=None
    )
    

Gets an item from memcache along with its timestamp metadata.

Peeking at items will update stats, but will not alter the eviction order of the item. Unlike get(), an item is fetched even if it is delete locked.

Args  
---  
  
`key` |  The key in memcache to look up. See docs on Client for details of format.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
An ItemWithTimestamps object which contains the value of the item along with timestamp metadata - expiration timestamp, last access timestamp and delete timestamp (if the item is delete locked).   
  
### `peek_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L733-L758)
    
    
    peek_multi(
        keys, key_prefix='', namespace=None
    )
    

Gets multiple items from memcache along with their timestamp metadata.

This is the recommended way to do bulk peek() calls.

Args  
---  
  
`keys` |  List of keys to look up. Keys may be strings or tuples of (hash_value, string). Google App Engine does the sharding and hashing automatically, though, so the hash value is ignored. To memcache, keys are just series of bytes, and not in any particular encoding.   
`key_prefix` |  Prefix to prepend to all keys when talking to the server; not included in the returned dictionary.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
A dictionary of the keys and ItemWithTimestamps objects. Even if the key_prefix was specified, that key_prefix won't be on the keys in the returned dictionary. Each ItemWithTimestamps object contains the item corresponding to the key, along with timestamp metadata - expiration timestamp, last access timestamp and delete timestamp (if the item is delete locked).   
  
### `peek_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L760-L774)
    
    
    peek_multi_async(
        keys, key_prefix='', namespace=None, rpc=None
    )
    

Async version of peek_multi().

### `replace`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L966-L985)
    
    
    replace(
        key, value, time=0, min_compress_len=0, namespace=None
    )
    

Replaces a key's value, failing if item isn't already in memcache.

Args  
---  
  
`key` |  Key to set. See docs on Client for details.   
`value` |  Value to set. Any type. If complex, will be pickled.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`min_compress_len` |  Ignored option for compatibility.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
`True` if replaced. `False` on RPC error or cache miss.   
  
### `replace_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1285-L1314)
    
    
    replace_multi(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None
    )
    

Replace multiple keys' values, failing if the items aren't in memcache.

Args  
---  
  
`mapping` |  Dictionary of keys to values.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`key_prefix` |  Prefix for to prepend to all keys.   
`min_compress_len` |  Unimplemented compatibility option.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
A list of keys whose values were NOT set because they already existed in memcache. On total success, this list should be empty.   
  
### `replace_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1316-L1334)
    
    
    replace_multi_async(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None,
        rpc=None
    )
    

Async version of `replace_multi()` \-- note different return value.

Returns  
---  
See `_set_multi_async_with_policy()`.   
  
### `set`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L920-L943)
    
    
    set(
        key, value, time=0, min_compress_len=0, namespace=None
    )
    

Sets a key's value, regardless of previous contents in cache.

Unlike `add()` and `replace()`, this method always sets (or overwrites) the value in memcache, regardless of previous contents.

Args  
---  
  
`key` |  Key to set. See docs on Client for details.   
`value` |  Value to set. Any type. If complex, will be pickled.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`min_compress_len` |  Ignored option for compatibility.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
`True` if set. `False` on error.   
  
### `set_multi`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1183-L1212)
    
    
    set_multi(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None
    )
    

Set multiple keys' values at once, regardless of previous contents.

Args  
---  
  
`mapping` |  Dictionary of keys to values.   
`time` |  Optional expiration time, either relative number of seconds from current time (up to 1 month), or an absolute Unix epoch time. By default, items never expire, though items may be evicted due to memory pressure. Float values will be rounded up to the nearest whole second.   
`key_prefix` |  Prefix for to prepend to all keys.   
`min_compress_len` |  Unimplemented compatibility option.   
`namespace` |  a string specifying an optional namespace to use in the request.   
  
Returns  
---  
A list of keys whose values were NOT set. On total success, this list should be empty.   
  
### `set_multi_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L1214-L1232)
    
    
    set_multi_async(
        mapping,
        time=0,
        key_prefix='',
        min_compress_len=0,
        namespace=None,
        rpc=None
    )
    

Async version of `set_multi()` \-- note different return value.

Returns  
---  
See `_set_multi_async_with_policy()`.   
  
### `set_servers`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/memcache/__init__.py#L486-L491)
    
    
    set_servers(
        servers
    )
    

Sets the pool of memcache servers used by the client.

This is purely a compatibility method. In Google App Engine, it's a no-op.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
