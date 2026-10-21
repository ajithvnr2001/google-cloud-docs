---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService
title: Interface MemcacheService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:36:15.421805+00:00
---

# Interface MemcacheService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface MemcacheService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface MemcacheService extends BaseMemcacheService

The Java API for the App Engine Memcache service. This offers a fast distributed cache for commonly-used data. The cache is limited both in duration and also in total space, so objects stored in it may be discarded at any time.

Note that `null` is a legal value to store in the cache, or to use as a cache key. Although the API is written for [Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)s, both keys and values should be [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html), although future versions may someday accept specific types of non-`Serializable` `Objects`.

The values returned from this API are mutable copies from the cache; altering them has no effect upon the cached value itself until assigned with one of the [put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_) methods. Likewise, the methods returning collections return mutable collections, but changes do not affect the cache.

Methods that operate on single entries, including [#increment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_), are atomic, while batch methods such as #getAll, #putAll, and #deleteAll do not provide atomicity. Arbitrary operations on single entries can be performed atomically by using [#putIfUntouched](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putIfUntouched_) in combination with [#getIdentifiable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getIdentifiable_).

[Increment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_) has a number of caveats to its use; please consult the method documentation.

An [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler) configures how errors are treated. The default error handler is an instance of [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler). In most cases this will log the underlying error condition and emulate cache-miss behavior instead of throwing an error to the calling code. For example, it returns `null` from [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_).

A less permissive alternative is [StrictErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.StrictErrorHandler), which will instead throw a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) to expose any errors for application code to resolve.

To guarantee that all [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) are directed to the error handler use a [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) such as [ErrorHandlers#getConsistentLogAndContinue(Level)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getConsistentLogAndContinue_java_util_logging_Level_) or [ErrorHandlers#getStrict()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getStrict__).

## Implements

[BaseMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService)

## Methods 

### <T>deleteAll(Collection<T> keys)
    
    
    public abstract Set<T> <T>deleteAll(Collection<T> keys)

Batch version of [#delete(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_delete_java_lang_Object_).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of keys for entries to delete  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>` | the Set of keys deleted. Any keys in `keys` but not in the returned set were not found in the cache. The iteration order of the returned set matches the iteration order of the provided `keys`.  
  
### <T>deleteAll(Collection<T> keys, long millisNoReAdd)
    
    
    public abstract Set<T> <T>deleteAll(Collection<T> keys, long millisNoReAdd)

Batch version of [#delete(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_delete_java_lang_Object_long_).

**Parameters**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of keys for entries to delete  
`millisNoReAdd` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
time during which calls to put using SetPolicy#ADD_ONLY_IF_NOT_PRESENT should be denied.  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>` | the Set of keys deleted. Any keys in `keys` but not in the returned set were not found in the cache. The iteration order of the returned set matches the iteration order of the provided `keys`.  
  
### <T>getAll(Collection<T> keys)
    
    
    public abstract Map<T,Object> <T>getAll(Collection<T> keys)

Performs a get of multiple keys at once. This is more efficient than multiple separate calls to [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_), and allows a single call to both test for [#contains(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_contains_java_lang_Object_) and also fetch the value, because the return will not include mappings for keys not found.

If an error deserializing the value occurs, this passes an [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of keys for which values should be retrieved  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>` | a mapping from keys to values of any entries found. If a requested key is not found in the cache, the key will not be in the returned Map.  
  
### <T>getIdentifiables(Collection<T> keys)
    
    
    public abstract Map<T,MemcacheService.IdentifiableValue> <T>getIdentifiables(Collection<T> keys)

Performs a getIdentifiable for multiple keys at once. This is more efficient than multiple separate calls to [#getIdentifiable(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getIdentifiable_java_lang_Object_).

If an error deserializing the value occurs, this passes an [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of keys for which values should be retrieved  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)>` | a mapping from keys to values of any entries found. If a requested key is not found in the cache, the key will not be in the returned Map.  
  
### <T>getItemsForPeek(Collection<T> keys)
    
    
    public default Map<T,MemcacheService.ItemForPeek> <T>getItemsForPeek(Collection<T> keys)

Performs a getItemForPeek for multiple keys at once. This is more efficient than multiple separate calls to [#getItemForPeek(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getItemForPeek_java_lang_Object_).

If an error deserializing the value occurs, this passes an [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of keys for which values should be retrieved  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek)>` | a mapping from keys to [ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek) of any entries found. If a requested key is not found in the cache, the key will not be in the returned Map.  
  
### <T>incrementAll(Collection<T> keys, long delta)
    
    
    public abstract Map<T,Long> <T>incrementAll(Collection<T> keys, long delta)

Like normal increment, but increments a batch of separate keys in parallel by the same delta. See Also: [#increment(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_)

**Parameters**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | mapping keys to their new values; values will be null if they could not be incremented or were not present in the cache  
  
### <T>incrementAll(Collection<T> keys, long delta, Long initialValue)
    
    
    public abstract Map<T,Long> <T>incrementAll(Collection<T> keys, long delta, Long initialValue)

Like normal increment, but increments a batch of separate keys in parallel by the same delta and potentially sets a starting value. See Also: [#increment(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_)

**Parameters**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`initialValue` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
value to insert into the cache if the key is not present  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | mapping keys to their new values; values will be null if they could not be incremented for whatever reason  
  
### <T>incrementAll(Map<T,Long> offsets)
    
    
    public abstract Map<T,Long> <T>incrementAll(Map<T,Long> offsets)

Like normal increment, but accepts a mapping of separate controllable offsets for each key individually. Good for incrementing by a sum and a count in parallel. See Also: [#increment(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_)

**Parameter**  
---  
**Name** | **Description**  
`offsets` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | mapping keys to their new values; values will be null if they could not be incremented for whatever reason  
  
### <T>incrementAll(Map<T,Long> offsets, Long initialValue)
    
    
    public abstract Map<T,Long> <T>incrementAll(Map<T,Long> offsets, Long initialValue)

Like normal increment, but accepts a mapping of separate controllable offsets for each key individually. Good for incrementing by a sum and a count in parallel. Callers may also pass an initial value for the keys to take on if they are not already present in the cache. See Also: [#increment(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_)

**Parameters**  
---  
**Name** | **Description**  
`offsets` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>`  
  
`initialValue` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | mapping keys to their new values; values will be null if they could not be incremented for whatever reason  
  
### <T>putAll(Map<T,?> values, Expiration expires, MemcacheService.SetPolicy policy)
    
    
    public abstract Set<T> <T>putAll(Map<T,?> values, Expiration expires, MemcacheService.SetPolicy policy)

A batch-processing variant of [#put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_). This is more efficiently implemented by the service than multiple calls.

**Parameters**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,?>`  
the key/value mappings to add to the cache  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
the expiration time for all `values`, or `null` for no time-based expiration.  
`policy` | `[MemcacheService.SetPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.SetPolicy)`  
what to do if the entry is or is not already present  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>` | the set of keys for which entries were created. Keys in `values` may not be in the returned set because of the `policy` regarding pre-existing entries.  
  
### <T>putIfUntouched(Map<T,MemcacheService.CasValues> values)
    
    
    public abstract Set<T> <T>putIfUntouched(Map<T,MemcacheService.CasValues> values)

Convenience shortcut, equivalent to <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[CasValues](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.CasValues)>`  
the key/values mappings to compare and swap  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>` | the set of keys for which the new value was stored.  
  
### <T>putIfUntouched(Map<T,MemcacheService.CasValues> values, Expiration expiration)
    
    
    public abstract Set<T> <T>putIfUntouched(Map<T,MemcacheService.CasValues> values, Expiration expiration)

A batch-processing variant of #putIfUntouched(Object, IdentifiableValue,Object,Expiration). This is more efficient than multiple single value calls.

**Parameters**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[CasValues](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.CasValues)>`  
the key/values mappings to compare and swap  
`expiration` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
an [Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration) object to set time-based expiration for a [value](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.CasValues) with a `null` [expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration) value. `null` may be used to indicate no specific expiration.  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>` | the set of keys for which the new value was stored.  
  
### clearAll()
    
    
    public abstract void clearAll()

Empties the cache of all values across all namespaces. Statistics are not affected.

### contains(Object key)
    
    
    public abstract boolean contains(Object key)

Tests whether a given value is in cache, even if its value is `null`.

Note that, because an object may be removed from cache at any time, the following is not sound code:
    
    
       if (memcache.contains("key")) {
         foo = memcache.get("key");
         if (foo == null) {
           // continue, assuming foo had the real value null
         }
       }
      

The problem is that the cache could have dropped the entry between the call to [#contains](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_contains_) and [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_). This is a sounder pattern:
    
    
       foo = memcache.get("key");
       if (foo == null) {
         if (memcache.contains("key")) {
           // continue, assuming foo had the real value null
         } else {
           // continue; foo may have had a real null, but has been dropped now
         }
       }
      

Another alternative is to prefer <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key object used to store the cache entry  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the cache contains an entry for the key  
  
### delete(Object key)
    
    
    public abstract boolean delete(Object key)

Removes `key` from the cache.

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key of the entry to delete.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if an entry existed, but was discarded  
  
### delete(Object key, long millisNoReAdd)
    
    
    public abstract boolean delete(Object key, long millisNoReAdd)

Removes the given key from the cache, and prevents it from being added under the SetPolicy#ADD_ONLY_IF_NOT_PRESENT policy for `millisNoReAdd` milliseconds thereafter. Calls to a [#put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_) method using SetPolicy#SET_ALWAYS are not blocked, however.

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
key to delete  
`millisNoReAdd` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
time during which calls to put using ADD_IF_NOT_PRESENT should be denied.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if an entry existed to delete  
  
### get(Object key)
    
    
    public abstract Object get(Object key)

Fetches a previously-stored value, or `null` if unset. To distinguish a `null` value from unset use [MemcacheService#contains(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_contains_java_lang_Object_).

If an error deserializing the value occurs, this passes an [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key object used to store the cache entry  
**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)` | the value object previously stored, or `null`  
  
### getIdentifiable(Object key)
    
    
    public abstract MemcacheService.IdentifiableValue getIdentifiable(Object key)

Similar to [#get](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_), but returns an object that can later be used to perform a [#putIfUntouched](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putIfUntouched_) operation.

If an error deserializing the value occurs, this passes an [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key object used to store the cache entry  
**Returns**  
---  
**Type** | **Description**  
`[MemcacheService.IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)` | an [IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue) object that wraps the value object previously stored. `null` is returned if `key` is not present in the cache.  
  
### getItemForPeek(Object key)
    
    
    public default MemcacheService.ItemForPeek getItemForPeek(Object key)

Similar to [#get](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_), but returns an object that can provide extra timestamp metadata.

If an error deserializing the value occurs, this passes an [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key object used to store the cache entry  
**Returns**  
---  
**Type** | **Description**  
`[MemcacheService.ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek)` | an [ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek) object that wraps the value object stored as well as extra meta data timestamps. `null` is returned if `key` is not present in the cache.  
  
### getStatistics()
    
    
    public abstract Stats getStatistics()

Fetches some statistics about the cache and its usage.

**Returns**  
---  
**Type** | **Description**  
`[Stats](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Stats)` | statistics for the cache. Note that this method returns aggregated [Stats](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Stats) for all namespaces. Response will never be `null`.  
  
### increment(Object key, long delta)
    
    
    public abstract Long increment(Object key, long delta)

Atomically fetches, increments, and stores a given integral value. "Integral" types are Byte, Short, [Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html), [Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html), and in some cases [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html). The entry must already exist, and have a non-negative value.

Incrementing by positive amounts will reach signed 64-bit max ( `2^63 - 1`) and then wrap-around to signed 64-bit min (`-2^63` ), continuing increments from that point.

To facilitate use as an atomic countdown, incrementing by a negative value (i.e. decrementing) will not go below zero: incrementing `2` by `-5` will return `0`, not `-3`.

Note: The actual representation of all numbers in Memcache is a string. This means if you initially stored a number as a string (e.g., "10") and then increment it, everything will work properly.

When you [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_) a key for a string value, wrapping occurs after exceeding the max value of an unsigned 64-bit number (`2^64 - 1`). When you [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_) a key for a numerical type, wrapping occurs after exceeding the type max value.

If a service error occurs, this passes a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) to the service's [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler). See [BaseMemcacheService#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key of the entry to manipulate  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the size of the increment, positive or negative  
**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` | the post-increment value, as a long. However, a [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_) of the key will still have the original type ( Byte, Short, etc.). If there is no entry for `key`, returns `null`.  
  
### increment(Object key, long delta, Long initialValue)
    
    
    public abstract Long increment(Object key, long delta, Long initialValue)

Like normal increment, but allows for an optional initial value for the key to take on if not already present in the cache.

Note, the provided initial value can be negative, which allows incrementing negative numbers. This is in contrast to the base version of this method, which requires a pre-existing value (e.g. one stored with [#put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_)) to be non-negative prior to being incremented. See Also: [#increment(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`initialValue` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
value to insert into the cache if the key is not present  
**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### put(Object key, Object value)
    
    
    public abstract void put(Object key, Object value)

A convenience shortcut, equivalent to put(key, value, null, SetPolicy.SET_ALWAYS).

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
key of the new entry  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
value for the new entry  
  
### put(Object key, Object value, Expiration expires)
    
    
    public abstract void put(Object key, Object value, Expiration expires)

Convenience put, equivalent to put(key, value, expiration, SetPolicy.SET_ALWAYS).

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
key of the new entry  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
value for the new entry  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
time-based [Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration), or `null` for none  
  
### put(Object key, Object value, Expiration expires, MemcacheService.SetPolicy policy)
    
    
    public abstract boolean put(Object key, Object value, Expiration expires, MemcacheService.SetPolicy policy)

Store a new value into the cache, using `key`, but subject to the `policy` regarding existing entries.

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the key for the new cache entry  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
the value to be stored  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
an [Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration) object to set time-based expiration. `null` may be used indicate no specific expiration.  
`policy` | `[MemcacheService.SetPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.SetPolicy)`  
Requests particular handling regarding pre-existing entries under the same key. This parameter must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if a new entry was created, `false` if not because of the `policy`  
  
### putAll(Map<?,?> values)
    
    
    public abstract void putAll(Map<?,?> values)

Convenience multi-put, equivalent to putAll(values, expires, SetPolicy.SET_ALWAYS).

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<?,?>`  
key/value mappings for new entries to add to the cache  
  
### putAll(Map<?,?> values, Expiration expires)
    
    
    public abstract void putAll(Map<?,?> values, Expiration expires)

Convenience multi-put, equivalent to putAll(values, expires, SetPolicy.SET_ALWAYS).

**Parameters**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<?,?>`  
key/value mappings to add to the cache  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
expiration time for the new values, or `null` for no time-based expiration  
  
### putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue)
    
    
    public abstract boolean putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue)

Convenience shortcut, equivalent to put(key, oldValue, newValue, null).

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
key of the entry  
`oldValue` | `[MemcacheService.IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)`  
identifier for the value to compare against newValue  
`newValue` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
new value to store if oldValue is still there  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if `newValue` was stored, `false` otherwise.  
  
### putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue, Expiration expires)
    
    
    public abstract boolean putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue, Expiration expires)

Atomically, store `newValue` only if no other value has been stored since `oldValue` was retrieved. `oldValue` is an [IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue) that was returned from a previous call to [#getIdentifiable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getIdentifiable_).

If another value in the cache for `key` has been stored, or if this cache entry has been evicted, then nothing is stored by this call and `false` is returned.

Note that storing the same value again _does_ count as a "touch" for this purpose.

Using [#getIdentifiable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getIdentifiable_) and [#putIfUntouched](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putIfUntouched_) together constitutes an operation that either succeeds atomically or fails due to concurrency (or eviction), in which case the entire operation can be retried by the application.

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
key of the entry  
`oldValue` | `[MemcacheService.IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)`  
identifier for the value to compare against newValue  
`newValue` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
new value to store if oldValue is still there  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
an [Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration) object to set time-based expiration. `null` may be used to indicate no specific expiration.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if `newValue` was stored, `false` otherwise  
  
### setNamespace(String newNamespace) (deprecated)
    
    
    public abstract void setNamespace(String newNamespace)

**Deprecated.** _use[MemcacheServiceFactory#getMemcacheService(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceFactory#com_google_appengine_api_memcache_MemcacheServiceFactory_getMemcacheService_java_lang_String_) instead._

**Parameter**  
---  
**Name** | **Description**  
`newNamespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
