---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.AsyncMemcacheService
title: Interface AsyncMemcacheService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:51:06.559647+00:00
---

# Interface AsyncMemcacheService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.AsyncMemcacheService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface AsyncMemcacheService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface AsyncMemcacheService extends BaseMemcacheService

An asynchronous version of [MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService). All methods return immediately and provide [Futures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) as their return values.

## Implements

[BaseMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService)

## Methods 

### <T>deleteAll(Collection<T> keys)
    
    
    public abstract Future<Set<T>> <T>deleteAll(Collection<T> keys)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>>` |   
  
### <T>deleteAll(Collection<T> keys, long millisNoReAdd)
    
    
    public abstract Future<Set<T>> <T>deleteAll(Collection<T> keys, long millisNoReAdd)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameters**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
`millisNoReAdd` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>>` |   
  
### <T>getAll(Collection<T> keys)
    
    
    public abstract Future<Map<T,Object>> <T>getAll(Collection<T> keys)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>>` |   
  
### <T>getIdentifiables(Collection<T> keys)
    
    
    public abstract Future<Map<T,MemcacheService.IdentifiableValue>> <T>getIdentifiables(Collection<T> keys)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)>>` |   
  
### <T>getItemsForPeek(Collection<T> keys)
    
    
    public abstract Future<Map<T,MemcacheService.ItemForPeek>> <T>getItemsForPeek(Collection<T> keys)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek)>>` |   
  
### <T>incrementAll(Collection<T> keys, long delta)
    
    
    public abstract Future<Map<T,Long>> <T>incrementAll(Collection<T> keys, long delta)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameters**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>>` |   
  
### <T>incrementAll(Collection<T> keys, long delta, Long initialValue)
    
    
    public abstract Future<Map<T,Long>> <T>incrementAll(Collection<T> keys, long delta, Long initialValue)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameters**  
---  
**Name** | **Description**  
`keys` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`initialValue` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>>` |   
  
### <T>incrementAll(Map<T,Long> offsets)
    
    
    public abstract Future<Map<T,Long>> <T>incrementAll(Map<T,Long> offsets)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`offsets` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>>` |   
  
### <T>incrementAll(Map<T,Long> offsets, Long initialValue)
    
    
    public abstract Future<Map<T,Long>> <T>incrementAll(Map<T,Long> offsets, Long initialValue)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameters**  
---  
**Name** | **Description**  
`offsets` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>`  
  
`initialValue` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>>` |   
  
### <T>putAll(Map<T,?> values, Expiration expires, MemcacheService.SetPolicy policy)
    
    
    public abstract Future<Set<T>> <T>putAll(Map<T,?> values, Expiration expires, MemcacheService.SetPolicy policy)

See Also: [MemcacheService#putAll(Map, Expiration, SetPolicy)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putAll_)

**Parameters**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,?>`  
  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
  
`policy` | `[MemcacheService.SetPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.SetPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>>` |   
  
### <T>putIfUntouched(Map<T,MemcacheService.CasValues> values)
    
    
    public abstract Future<Set<T>> <T>putIfUntouched(Map<T,MemcacheService.CasValues> values)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[CasValues](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.CasValues)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>>` |   
  
### <T>putIfUntouched(Map<T,MemcacheService.CasValues> values, Expiration expiration)
    
    
    public abstract Future<Set<T>> <T>putIfUntouched(Map<T,MemcacheService.CasValues> values, Expiration expiration)

See Also: <xref uid="com.google.appengine.api.memcache.MemcacheService.

**Parameters**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<T,[CasValues](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.CasValues)>`  
  
`expiration` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<T>>` |   
  
### clearAll()
    
    
    public abstract Future<Void> clearAll()

See Also: [MemcacheService#clearAll()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_clearAll__)

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### contains(Object key)
    
    
    public abstract Future<Boolean> contains(Object key)

See Also: [MemcacheService#contains(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_contains_java_lang_Object_)

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### delete(Object key)
    
    
    public abstract Future<Boolean> delete(Object key)

See Also: [MemcacheService#delete(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_delete_java_lang_Object_)

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### delete(Object key, long millisNoReAdd)
    
    
    public abstract Future<Boolean> delete(Object key, long millisNoReAdd)

See Also: [MemcacheService#delete(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_delete_java_lang_Object_long_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`millisNoReAdd` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### get(Object key)
    
    
    public abstract Future<Object> get(Object key)

See Also: [MemcacheService#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_)

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>` |   
  
### getIdentifiable(Object key)
    
    
    public abstract Future<MemcacheService.IdentifiableValue> getIdentifiable(Object key)

See Also: [MemcacheService#getIdentifiable(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getIdentifiable_java_lang_Object_)

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)>` |   
  
### getItemForPeek(Object key)
    
    
    public abstract Future<MemcacheService.ItemForPeek> getItemForPeek(Object key)

See Also: [MemcacheService#getItemForPeek(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getItemForPeek_java_lang_Object_)

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek)>` |   
  
### getStatistics()
    
    
    public abstract Future<Stats> getStatistics()

See Also: [MemcacheService#getStatistics()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getStatistics__)

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Stats](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Stats)>` |   
  
### increment(Object key, long delta)
    
    
    public abstract Future<Long> increment(Object key, long delta)

See Also: [MemcacheService#increment(Object, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` |   
  
### increment(Object key, long delta, Long initialValue)
    
    
    public abstract Future<Long> increment(Object key, long delta, Long initialValue)

See Also: [MemcacheService#increment(Object, long, Long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_java_lang_Object_long_java_lang_Long_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`delta` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`initialValue` | `[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` |   
  
### put(Object key, Object value)
    
    
    public abstract Future<Void> put(Object key, Object value)

See Also: [MemcacheService#put(Object, Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### put(Object key, Object value, Expiration expires)
    
    
    public abstract Future<Void> put(Object key, Object value, Expiration expires)

See Also: [MemcacheService#put(Object, Object, Expiration)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_com_google_appengine_api_memcache_Expiration_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### put(Object key, Object value, Expiration expires, MemcacheService.SetPolicy policy)
    
    
    public abstract Future<Boolean> put(Object key, Object value, Expiration expires, MemcacheService.SetPolicy policy)

See Also: [MemcacheService#put(Object, Object, Expiration, SetPolicy)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
  
`policy` | `[MemcacheService.SetPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.SetPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### putAll(Map<?,?> values)
    
    
    public abstract Future<Void> putAll(Map<?,?> values)

See Also: [MemcacheService#putAll(Map)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putAll_java_util_Map______)

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<?,?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### putAll(Map<?,?> values, Expiration expires)
    
    
    public abstract Future<Void> putAll(Map<?,?> values, Expiration expires)

See Also: [MemcacheService#putAll(Map, Expiration)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putAll_java_util_Map______com_google_appengine_api_memcache_Expiration_)

**Parameters**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<?,?>`  
  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue)
    
    
    public abstract Future<Boolean> putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue)

See Also: [MemcacheService#putIfUntouched(Object, IdentifiableValue, Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putIfUntouched_)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`oldValue` | `[MemcacheService.IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)`  
  
`newValue` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
### putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue, Expiration expires)
    
    
    public abstract Future<Boolean> putIfUntouched(Object key, MemcacheService.IdentifiableValue oldValue, Object newValue, Expiration expires)

See Also: MemcacheService#putIfUntouched(Object, IdentifiableValue, Object, Expiration)

**Parameters**  
---  
**Name** | **Description**  
`key` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`oldValue` | `[MemcacheService.IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)`  
  
`newValue` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
`expires` | `[Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
