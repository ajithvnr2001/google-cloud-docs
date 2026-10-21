---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler
title: Interface ErrorHandler (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:56:54.310274+00:00
---

# Interface ErrorHandler (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface ErrorHandler (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface ErrorHandler

Handles errors raised by the `MemcacheService`, registered with MemcacheService#setErrorHandler(ErrorHandler).

The default error handler is an instance of [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler). In most cases, this will log exceptions without throwing, which looks like a cache-miss behavior to the caller. A less permissive alternative is [StrictErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.StrictErrorHandler), which will throw a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) to surface errors to callers.

To guarantee that all instances of [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) are directed to the error handler, use a [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) such as [ErrorHandlers#getConsistentLogAndContinue(Level)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getConsistentLogAndContinue_java_util_logging_Level_) or [ErrorHandlers#getStrict()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getStrict__).

## Methods 

### handleDeserializationError(InvalidValueException ivx)
    
    
    public abstract void handleDeserializationError(InvalidValueException ivx)

Handles deserialization errors. This method is called from either of the [get](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_get_java_lang_Object_) methods, if the retrieved value cannot be deserialized. This normally indicates an application upgrade since the cache entry was stored, and should thus be treated as a cache miss, which is the behavior of [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler) (the default).

**Parameter**  
---  
**Name** | **Description**  
`ivx` | `[InvalidValueException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.InvalidValueException)`  
  
  
### handleServiceError(MemcacheServiceException ex)
    
    
    public abstract void handleServiceError(MemcacheServiceException ex)

Handles back-end service errors. This method is called from most of the `MemcacheService` methods in the event of a service error. This is also called for [MemcacheService#put(Object, Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService#com_google_appengine_api_memcache_MemcacheService_put_java_lang_Object_java_lang_Object_) when the combined key and value size is too large.

The handler may throw any [RuntimeException](https://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html), or it may simply return for "permissive" error handling, which will generally emulate behavior of a cache miss due to a discarded entry.

**Parameter**  
---  
**Name** | **Description**  
`ex` | `[MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException)`  
the service error exception  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
