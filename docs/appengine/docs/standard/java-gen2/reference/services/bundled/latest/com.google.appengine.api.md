---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api
title: Package com.google.appengine.api (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:52.952578+00:00
---

# Package com.google.appengine.api (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides facilities for server lifecycle management, threading and namespaces/multitenancy. These facilities, along with the services defined in subpackages, make up the Google App Engine API. See Also: [Multitenancy and the Namespaces Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/multitenancy/).

## Classes 

### [LifecycleManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.LifecycleManager)

### [NamespaceManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager)

Provides functions for manipulating the current namespace used for App Engine APIs.

The "current namespace" is the string that is returned by [#get()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_get__) and used by a number of APIs including Datatore, Memcache and Task Queue.

When a namespace aware class (e.g., [com.google.appengine.api.datastore.Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key), [com.google.appengine.api.datastore.Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) and [com.google.appengine.api.memcache.MemcacheService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.memcache.MemcacheService)) is constructed, it determines which namespace will be used by calling [NamespaceManager#get()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_get__) if it is otherwise unspecified. If [NamespaceManager#get()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_get__) returns null, the current namespace is unset and these APIs will use the empty ("") namespace in its place.

Example: 
    
    
     [NamespaceManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager).[#set](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_set_)("a-namespace");
     MemcacheService memcache = MemcacheServiceFactory.getMemcacheService();
     // Store record in namespace "a-namespace"
     memcache.put("key1", "value1");
    
    
    
    
     [NamespaceManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager).[#set](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_set_)("other-namespace");
     // Store record in namespace "other-namespace"
     memcache.put("key2", "value2");
    
    
    
    
     MemcacheService boundMemcache =
         MemcacheServiceFactory.getMemcacheService("specific-namespace");
     [NamespaceManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager).[#set](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_set_)("whatever-namespace");
     // The record is still stored in namespace "specific-namespace".
     boundMemcache.put("key3", "value3");
     

MemcacheService `memcache` (in the above example) uses the current namespace and `key1` will be stored in namespace `"a-namespace"`, while `key2` is stored in namespace `"other-namespace"`. It is possible to override the current namespace and store data in specific namespace. In the above example `key3` is stored in namespace `"specific-namespace"`.

The Task Queue com.google.appengine.api.taskqueue.Queue#add methods will forward the [NamespaceManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager) settings into the task being added causing the added task to be executed with the same current namespace as the task creator. The exception is that an unset current namespace (i.e. [NamespaceManager#get()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager#com_google_appengine_api_NamespaceManager_get__) returns null) will be forwarded as an empty ("") namespace to the created task's requests. See Also: [ Multitenancy and the Namespaces Java API. In _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/multitenancy/).

### [ThreadManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager)

`ThreadManager` exposes a [ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html) that allows App Engine applications to spawn new threads.

Refer to [ this discussion of threads](https://cloud.google.com/appengine/docs/java/runtime#threads) for drawbacks of thread usage and possible alternatives.

## Interfaces 

### [EnvironmentProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.EnvironmentProvider)

An interface for providing environment variables.

### [LifecycleManager.ShutdownHook](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.LifecycleManager.ShutdownHook)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
