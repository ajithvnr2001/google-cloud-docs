---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager
title: Class NamespaceManager (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:54.503934+00:00
---

# Class NamespaceManager (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.NamespaceManager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class NamespaceManager (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class NamespaceManager

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

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NamespaceManager

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

### get()
    
    
    public static String get()

Returns the current namespace setting or either `null` or "" (empty) if not set.

If the current namespace is unset, callers should assume the use of the "" (empty) namespace in all namespace-aware services.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getGoogleAppsNamespace()
    
    
    public static String getGoogleAppsNamespace()

Returns the Google Apps domain referring this request or otherwise the empty string ("").

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### set(String newNamespace)
    
    
    public static void set(String newNamespace)

Set the value used to initialize the namespace of namespace-aware services.

**Parameter**  
---  
**Name** | **Description**  
`newNamespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the new namespace.  
  
### validateNamespace(String namespace)
    
    
    public static void validateNamespace(String namespace)

Validate the format of a namespace string.

**Parameter**  
---  
**Name** | **Description**  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
