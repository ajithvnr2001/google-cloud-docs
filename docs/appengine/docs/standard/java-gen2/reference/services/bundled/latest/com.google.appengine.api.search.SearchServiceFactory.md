---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceFactory
title: Class SearchServiceFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:32:13.299539+00:00
---

# Class SearchServiceFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class SearchServiceFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class SearchServiceFactory

An factory that creates default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).
    
    
       SearchService search = SearchServiceFactory.getSearchService();
     

Optionally, you may pass a [SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig) instance to customize the search service. e.g, setting deadline and namespace:
    
    
       SearchServiceFactory.getSearchService(
           SearchServiceConfig.newBuilder().setDeadline(10.0).setNamespace("acme").build())
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SearchServiceFactory

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### getSearchService()
    
    
    public static SearchService getSearchService()

Equivalent to [getSearchService(SearchServiceConfig.newBuilder().build())](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceFactory#com_google_appengine_api_search_SearchServiceFactory_getSearchService_com_google_appengine_api_search_SearchServiceConfig_).

**Returns**  
---  
**Type** | **Description**  
`[SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService)` |   
  
### getSearchService(SearchServiceConfig config)
    
    
    public static SearchService getSearchService(SearchServiceConfig config)

Returns an instance of the [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService) with the given config.

**Parameter**  
---  
**Name** | **Description**  
`config` | `[SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig)`  
a [SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig) instance that describes the requested search service. If no namespace provided in config, NamespaceManager.get() will be used.  
**Returns**  
---  
**Type** | **Description**  
`[SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService)` | the default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).  
  
### getSearchService(String namespace) (deprecated)
    
    
    public static SearchService getSearchService(String namespace)

**Deprecated.** _Use[SearchServiceFactory#getSearchService(SearchServiceConfig)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceFactory#com_google_appengine_api_search_SearchServiceFactory_getSearchService_com_google_appengine_api_search_SearchServiceConfig_)_

Returns an instance of the [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService). The instance will exist in the user provided namespace. The namespace must be valid, as per [NamespaceManager#validateNamespace(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_validateNamespace_java_lang_String_) method.

**Parameter**  
---  
**Name** | **Description**  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
a namespace to be assigned to the returned search service.  
**Returns**  
---  
**Type** | **Description**  
`[SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService)` | the default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
