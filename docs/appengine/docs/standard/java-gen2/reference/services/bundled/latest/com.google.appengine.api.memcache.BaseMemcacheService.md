---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService
title: Interface BaseMemcacheService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:21:57.218666+00:00
---

# Interface BaseMemcacheService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface BaseMemcacheService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface BaseMemcacheService

Methods that are common between [MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService) and [AsyncMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.AsyncMemcacheService).

## Methods 

### getErrorHandler()
    
    
    public abstract ErrorHandler getErrorHandler()

Fetches the current error handler.

See [#setErrorHandler(ErrorHandler)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.BaseMemcacheService#com_google_appengine_api_memcache_BaseMemcacheService_setErrorHandler_com_google_appengine_api_memcache_ErrorHandler_).

**Returns**  
---  
**Type** | **Description**  
`[ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler)` |   
  
### getNamespace()
    
    
    public abstract String getNamespace()

Method returns non-null value if the MemcacheService overrides the default namespace in API calls. Default namespace is the one returned by [com.google.appengine.api.NamespaceManager#get()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_get__).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | `null` if the MemcacheService uses default namespace in API calls. Otherwise it returns `namespace` which is overrides default namespace on the API calls.  
  
### setErrorHandler(ErrorHandler handler)
    
    
    public abstract void setErrorHandler(ErrorHandler handler)

Registers a new `ErrorHandler`. The `handler` is called for errors which are not the application's fault, like a network timeout. The handler can choose to propagate the error or suppress it. Errors which are caused by an incorrect use of the API will not be directed to the `handler` but rather will be thrown directly.

The default error handler is an instance of [LogAndContinueErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.LogAndContinueErrorHandler). In most cases, this will log exceptions without throwing, which looks like a cache-miss behavior to the caller. A less permissive alternative is [StrictErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.StrictErrorHandler), which will throw a [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) to surface errors to callers.

To guarantee that all instances of [MemcacheServiceException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheServiceException) are directed to the error handler, use a [ConsistentErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ConsistentErrorHandler) such as [ErrorHandlers#getConsistentLogAndContinue(Level)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getConsistentLogAndContinue_java_util_logging_Level_) or [ErrorHandlers#getStrict()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandlers#com_google_appengine_api_memcache_ErrorHandlers_getStrict__).

**Parameter**  
---  
**Name** | **Description**  
`handler` | `[ErrorHandler](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.ErrorHandler)`  
the new `ErrorHandler` to use  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
