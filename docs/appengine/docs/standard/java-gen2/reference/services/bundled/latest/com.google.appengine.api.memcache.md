---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache
title: Package com.google.appengine.api.memcache (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:02:14.839907+00:00
---

# Package com.google.appengine.api.memcache (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.memcache (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides fast but unreliable data storage, also accessible via a [JCache](http://jcp.org/en/jsr/detail?id=107) interface. Objects may be stored in the cache with an explicit expiration time, but may also be evicted before that expiration to make room for newer, more active entries.

The cache is accessed via a MemcacheService object, obtained from the MemcacheServiceFactory. It offers the cache as a map from key Object to value Object.

In the Development Server, the system property `memcache.maxsize` can be set to limit the available cache, taking values like "100M" (the default), "10K", or "768" (bytes).

Because the cache offers best-effort data storage, by default most errors are treated as a cache miss. More explicit error handling can be installed via MemcacheService#setErrorHandler(ErrorHandler). See Also: [com.google.appengine.api.memcache.MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService), [The Memcache Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/memcache/)., [JCache API](http://jcp.org/en/jsr/detail?id=107)

## Classes 

### [ConsistentLogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentLogAndContinueErrorHandler)

Similar to the deprecated [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler) but consistently handles all back-end related errors.

### [ErrorHandlers](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers)

Static utility for getting built-in [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler)s.

### [Expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration)

Expiration specifications on [MemcacheService#putAll(Map , Expiration)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putAll_) and [MemcacheService#put(Object, Object, Expiration)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_com_google_appengine_api_memcache_Expiration_) operations. 

`Expiration` has resolution to one second, although a milliseconds factory constructor is provided for convenience.

### [IMemcacheServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.IMemcacheServiceFactoryProvider)

Factory provider for [IMemcacheServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.IMemcacheServiceFactory).

**Note:** This class is not intended for end users.

### [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler)

The default error handler, which will cause most service errors to behave as though there were a cache miss, not an error.

To guarantee that all [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) are directed to the error handler use a [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) instead such as [ErrorHandlers#getConsistentLogAndContinue(Level)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getConsistentLogAndContinue_java_util_logging_Level_).

### [MemcacheSerialization](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheSerialization)

Static serialization helpers used by MemcacheServiceImpl

This class is thread-safe.

### [MemcacheSerialization.ValueAndFlags](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheSerialization.ValueAndFlags)

Tuple of a serialized byte array value and associated flags to interpret that value. Used as the return from [MemcacheSerialization#serialize](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheSerialization#com_google_appengine_api_memcache_MemcacheSerialization_serialize_).

### [MemcacheService.CasValues](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.CasValues)

A holder for compare and set values. [expiration](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Expiration) and `newValue` can be null.

### [MemcacheServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceFactory)

The factory by which users acquire a handle to the MemcacheService.

### [MemcacheServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb)

### [MemcacheServicePb.AppOverride](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.AppOverride)

### [MemcacheServicePb.AppOverride.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.AppOverride.Builder)

### [MemcacheServicePb.ItemTimestamps](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.ItemTimestamps)

### [MemcacheServicePb.ItemTimestamps.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.ItemTimestamps.Builder)

### [MemcacheServicePb.MemcacheBatchIncrementRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheBatchIncrementRequest)

### [MemcacheServicePb.MemcacheBatchIncrementRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheBatchIncrementRequest.Builder)

### [MemcacheServicePb.MemcacheBatchIncrementResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheBatchIncrementResponse)

### [MemcacheServicePb.MemcacheBatchIncrementResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheBatchIncrementResponse.Builder)

### [MemcacheServicePb.MemcacheDeleteRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteRequest)

### [MemcacheServicePb.MemcacheDeleteRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteRequest.Builder)

### [MemcacheServicePb.MemcacheDeleteRequest.Item](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteRequest.Item)

### [MemcacheServicePb.MemcacheDeleteRequest.Item.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteRequest.Item.Builder)

### [MemcacheServicePb.MemcacheDeleteResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteResponse)

### [MemcacheServicePb.MemcacheDeleteResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteResponse.Builder)

### [MemcacheServicePb.MemcacheFlushRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheFlushRequest)

### [MemcacheServicePb.MemcacheFlushRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheFlushRequest.Builder)

### [MemcacheServicePb.MemcacheFlushResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheFlushResponse)

### [MemcacheServicePb.MemcacheFlushResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheFlushResponse.Builder)

### [MemcacheServicePb.MemcacheGetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetRequest)

### [MemcacheServicePb.MemcacheGetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetRequest.Builder)

### [MemcacheServicePb.MemcacheGetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse)

### [MemcacheServicePb.MemcacheGetResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.Builder)

### [MemcacheServicePb.MemcacheGetResponse.Item](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.Item)

### [MemcacheServicePb.MemcacheGetResponse.Item.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.Item.Builder)

### [MemcacheServicePb.MemcacheHotKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheHotKey)

### [MemcacheServicePb.MemcacheHotKey.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheHotKey.Builder)

### [MemcacheServicePb.MemcacheIncrementRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementRequest)

### [MemcacheServicePb.MemcacheIncrementRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementRequest.Builder)

### [MemcacheServicePb.MemcacheIncrementResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementResponse)

### [MemcacheServicePb.MemcacheIncrementResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementResponse.Builder)

### [MemcacheServicePb.MemcacheServiceError](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheServiceError)

### [MemcacheServicePb.MemcacheServiceError.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheServiceError.Builder)

### [MemcacheServicePb.MemcacheSetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequest)

### [MemcacheServicePb.MemcacheSetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequest.Builder)

### [MemcacheServicePb.MemcacheSetRequest.Item](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequest.Item)

### [MemcacheServicePb.MemcacheSetRequest.Item.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequest.Item.Builder)

### [MemcacheServicePb.MemcacheSetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetResponse)

### [MemcacheServicePb.MemcacheSetResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetResponse.Builder)

### [MemcacheServicePb.MemcacheStatsRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheStatsRequest)

### [MemcacheServicePb.MemcacheStatsRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheStatsRequest.Builder)

### [MemcacheServicePb.MemcacheStatsResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheStatsResponse)

### [MemcacheServicePb.MemcacheStatsResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheStatsResponse.Builder)

### [MemcacheServicePb.MergedNamespaceStats](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MergedNamespaceStats)

### [MemcacheServicePb.MergedNamespaceStats.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MergedNamespaceStats.Builder)

### [StrictErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.StrictErrorHandler)

A strict error handler, which will throw [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) or [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException) for any service error condition.

## Interfaces 

### [AsyncMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.AsyncMemcacheService)

An asynchronous version of [MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService). All methods return immediately and provide [Futures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) as their return values.

### [BaseMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService)

Methods that are common between [MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService) and [AsyncMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.AsyncMemcacheService).

### [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler)

A marker interface to indicate that all [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) exceptions should be handled by [ErrorHandler#handleServiceError(MemcacheServiceException)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler#com_google_appengine_api_memcache_ErrorHandler_handleServiceError_com_google_appengine_api_memcache_MemcacheServiceException_). This interface was added to enable handling [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) thrown by the various [MemcacheService#put(Object, Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_) methods while preserving backward compatibility with [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler) which did not handle such cases.

### [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler)

Handles errors raised by the `MemcacheService`, registered with MemcacheService#setErrorHandler(ErrorHandler).

The default error handler is an instance of [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler). In most cases, this will log exceptions without throwing, which looks like a cache-miss behavior to the caller. A less permissive alternative is [StrictErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.StrictErrorHandler), which will throw a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) to surface errors to callers.

To guarantee that all instances of [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) are directed to the error handler, use a [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) such as [ErrorHandlers#getConsistentLogAndContinue(Level)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getConsistentLogAndContinue_java_util_logging_Level_) or [ErrorHandlers#getStrict()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getStrict__).

### [IMemcacheServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.IMemcacheServiceFactory)

The factory by which users acquire a handle to the MemcacheService.

### [MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService)

The Java API for the App Engine Memcache service. This offers a fast distributed cache for commonly-used data. The cache is limited both in duration and also in total space, so objects stored in it may be discarded at any time.

Note that `null` is a legal value to store in the cache, or to use as a cache key. Although the API is written for [Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)s, both keys and values should be [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html), although future versions may someday accept specific types of non-`Serializable` `Objects`.

The values returned from this API are mutable copies from the cache; altering them has no effect upon the cached value itself until assigned with one of the [put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_) methods. Likewise, the methods returning collections return mutable collections, but changes do not affect the cache.

Methods that operate on single entries, including [#increment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_), are atomic, while batch methods such as #getAll, #putAll, and #deleteAll do not provide atomicity. Arbitrary operations on single entries can be performed atomically by using [#putIfUntouched](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_putIfUntouched_) in combination with [#getIdentifiable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getIdentifiable_).

[Increment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_) has a number of caveats to its use; please consult the method documentation.

An [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler) configures how errors are treated. The default error handler is an instance of [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler). In most cases this will log the underlying error condition and emulate cache-miss behavior instead of throwing an error to the calling code. For example, it returns `null` from [#get(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_).

A less permissive alternative is [StrictErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.StrictErrorHandler), which will instead throw a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) to expose any errors for application code to resolve.

To guarantee that all [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) are directed to the error handler use a [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) such as [ErrorHandlers#getConsistentLogAndContinue(Level)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getConsistentLogAndContinue_java_util_logging_Level_) or [ErrorHandlers#getStrict()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getStrict__).

### [MemcacheService.IdentifiableValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.IdentifiableValue)

Encapsulates an Object that is returned by #getIdentifiable. An `IdentifiableValue` can later be used in a #putIfUntouched operation.

### [MemcacheService.ItemForPeek](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.ItemForPeek)

...

### [MemcacheServicePb.AppOverrideOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.AppOverrideOrBuilder)

### [MemcacheServicePb.ItemTimestampsOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.ItemTimestampsOrBuilder)

### [MemcacheServicePb.MemcacheBatchIncrementRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheBatchIncrementRequestOrBuilder)

### [MemcacheServicePb.MemcacheBatchIncrementResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheBatchIncrementResponseOrBuilder)

### [MemcacheServicePb.MemcacheDeleteRequest.ItemOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteRequest.ItemOrBuilder)

### [MemcacheServicePb.MemcacheDeleteRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteRequestOrBuilder)

### [MemcacheServicePb.MemcacheDeleteResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteResponseOrBuilder)

### [MemcacheServicePb.MemcacheFlushRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheFlushRequestOrBuilder)

### [MemcacheServicePb.MemcacheFlushResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheFlushResponseOrBuilder)

### [MemcacheServicePb.MemcacheGetRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetRequestOrBuilder)

### [MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.ItemOrBuilder)

### [MemcacheServicePb.MemcacheGetResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponseOrBuilder)

### [MemcacheServicePb.MemcacheHotKeyOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheHotKeyOrBuilder)

### [MemcacheServicePb.MemcacheIncrementRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementRequestOrBuilder)

### [MemcacheServicePb.MemcacheIncrementResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementResponseOrBuilder)

### [MemcacheServicePb.MemcacheServiceErrorOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheServiceErrorOrBuilder)

### [MemcacheServicePb.MemcacheSetRequest.ItemOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequest.ItemOrBuilder)

### [MemcacheServicePb.MemcacheSetRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequestOrBuilder)

### [MemcacheServicePb.MemcacheSetResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetResponseOrBuilder)

### [MemcacheServicePb.MemcacheStatsRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheStatsRequestOrBuilder)

### [MemcacheServicePb.MemcacheStatsResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheStatsResponseOrBuilder)

### [MemcacheServicePb.MergedNamespaceStatsOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MergedNamespaceStatsOrBuilder)

### [Stats](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.Stats)

Statistics from the cache, available via [MemcacheService#getStatistics()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_getStatistics__)

## Enums 

### [MemcacheSerialization.Flag](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheSerialization.Flag)

Values used as flags on the MemcacheService's values.

### [MemcacheService.SetPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService.SetPolicy)

Cache replacement strategies for [MemcacheService#put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_) operations, indicating how to handle putting a value that already exists.

### [MemcacheServicePb.MemcacheDeleteResponse.DeleteStatusCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheDeleteResponse.DeleteStatusCode)

### [MemcacheServicePb.MemcacheGetResponse.GetStatusCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheGetResponse.GetStatusCode)

### [MemcacheServicePb.MemcacheIncrementRequest.Direction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementRequest.Direction)

### [MemcacheServicePb.MemcacheIncrementResponse.IncrementStatusCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheIncrementResponse.IncrementStatusCode)

### [MemcacheServicePb.MemcacheServiceError.ErrorCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheServiceError.ErrorCode)

### [MemcacheServicePb.MemcacheSetRequest.SetPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetRequest.SetPolicy)

### [MemcacheServicePb.MemcacheSetResponse.SetStatusCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServicePb.MemcacheSetResponse.SetStatusCode)

## Exceptions 

### [InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException)

Thrown when a cache entry has content, but it cannot be read. For example: 

  * An attempt to [MemcacheService#increment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_increment_) a non-integral value 
  * Version skew between your application and the data in the cache, causing a serialization error. 



### [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException)

An exception for backend non-availability or similar error states which may occur, but are not necessarily indicative of a coding or usage error by the application. Also used for MemcacheService#put(Object, Object) when the combined key and value size is too large.

In most cases these will be given to the [ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler) to resolve. Use [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) if in all cases this exception should be directed to the `ErrorHandler`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
