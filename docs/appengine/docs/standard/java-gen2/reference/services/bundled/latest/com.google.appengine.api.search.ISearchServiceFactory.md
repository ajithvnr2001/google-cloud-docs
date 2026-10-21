---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ISearchServiceFactory
title: Interface ISearchServiceFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:35:55.110661+00:00
---

# Interface ISearchServiceFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ISearchServiceFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface ISearchServiceFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface ISearchServiceFactory

A factory that creates default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).

## Methods 

### getSearchService(SearchServiceConfig config)
    
    
    public abstract SearchService getSearchService(SearchServiceConfig config)

Returns an instance of the [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService) with the given config.

**Parameter**  
---  
**Name** | **Description**  
`config` | `[SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig)`  
a [SearchServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchServiceConfig) instance that describes the requested search service. If no namespace provided in config, NamespaceManager.get() will be used. will be used.  
**Returns**  
---  
**Type** | **Description**  
`[SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService)` | the default implementation of [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService).  
  
### getSearchService(String namespace) (deprecated)
    
    
    public abstract SearchService getSearchService(String namespace)

**Deprecated.** _Use[ISearchServiceFactory#getSearchService(SearchServiceConfig)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ISearchServiceFactory#com_google_appengine_api_search_ISearchServiceFactory_getSearchService_com_google_appengine_api_search_SearchServiceConfig_)_

Returns an instance of the [SearchService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService). The instance will exist in the user provided namespace. The namespace must be valid, as per [com.google.appengine.api.NamespaceManager#validateNamespace(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_validateNamespace_java_lang_String_) method. Equivalent to ` getSearchService(SearchServiceConfig.newBuilder().setNamespace(namespace).build()) `

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
