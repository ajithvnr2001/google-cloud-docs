---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.IMemcacheServiceFactory
title: Interface IMemcacheServiceFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:44:54.386743+00:00
---

# Interface IMemcacheServiceFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.IMemcacheServiceFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface IMemcacheServiceFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface IMemcacheServiceFactory

The factory by which users acquire a handle to the MemcacheService.

## Methods 

### getAsyncMemcacheService(String namespace)
    
    
    public abstract AsyncMemcacheService getAsyncMemcacheService(String namespace)

Similar to [#getMemcacheService(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.IMemcacheServiceFactory#com_google_appengine_api_memcache_IMemcacheServiceFactory_getMemcacheService_java_lang_String_) but returns a handle to an asynchronous version of the cache service.

**Parameter**  
---  
**Name** | **Description**  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AsyncMemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.AsyncMemcacheService)` |   
  
### getMemcacheService(String namespace)
    
    
    public abstract MemcacheService getMemcacheService(String namespace)

Gets a handle to the cache service, forcing use of specific namespace.

Although there is only one actual cache, an application may make as many `MemcacheService` instances as it finds convenient. If using multiple instances, note that the error handler established with MemcacheService#setErrorHandler(ErrorHandler) is specific to each instance.

**Parameter**  
---  
**Name** | **Description**  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
if not `null` forces the use of `namespace` for all operations in `MemcacheService` . If `namespace` is `null` \- created `MemcacheService` will use current namespace provided by [com.google.appengine.api.NamespaceManager#get()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_get__).  
**Returns**  
---  
**Type** | **Description**  
`[MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService)` | a new `MemcacheService` instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
