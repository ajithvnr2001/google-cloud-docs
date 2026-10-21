---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceFactory
title: Class DatastoreServiceFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:55.359072+00:00
---

# Class DatastoreServiceFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DatastoreServiceFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class DatastoreServiceFactory

Creates DatastoreService implementations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastoreServiceFactory

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

### getAsyncDatastoreService()
    
    
    public static AsyncDatastoreService getAsyncDatastoreService()

Creates an `AsyncDatastoreService` using the default config ( [DatastoreServiceConfig.Builder#withDefaults()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig.Builder#com_google_appengine_api_datastore_DatastoreServiceConfig_Builder_withDefaults__)).

**Returns**  
---  
**Type** | **Description**  
`[AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService)` |   
  
### getAsyncDatastoreService(DatastoreServiceConfig config)
    
    
    public static AsyncDatastoreService getAsyncDatastoreService(DatastoreServiceConfig config)

Creates an `AsyncDatastoreService` using the provided config. The async datastore service does not support implicit transaction management policy [ImplicitTransactionManagementPolicy#AUTO](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy#com_google_appengine_api_datastore_ImplicitTransactionManagementPolicy_AUTO).

**Parameter**  
---  
**Name** | **Description**  
`config` | `[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService)` |   
  
### getDatastoreService()
    
    
    public static DatastoreService getDatastoreService()

Creates a `DatastoreService` using the default config ( [DatastoreServiceConfig.Builder#withDefaults()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig.Builder#com_google_appengine_api_datastore_DatastoreServiceConfig_Builder_withDefaults__)).

**Returns**  
---  
**Type** | **Description**  
`[DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService)` |   
  
### getDatastoreService(DatastoreConfig oldConfig) (deprecated)
    
    
    public static DatastoreService getDatastoreService(DatastoreConfig oldConfig)

**Deprecated.** _Use[#getDatastoreService(DatastoreServiceConfig)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceFactory#com_google_appengine_api_datastore_DatastoreServiceFactory_getDatastoreService_com_google_appengine_api_datastore_DatastoreServiceConfig_) instead._

Creates a `DatastoreService` using the provided config.

**Parameter**  
---  
**Name** | **Description**  
`oldConfig` | `[DatastoreConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService)` |   
  
### getDatastoreService(DatastoreServiceConfig config)
    
    
    public static DatastoreService getDatastoreService(DatastoreServiceConfig config)

Creates a `DatastoreService` using the provided config.

**Parameter**  
---  
**Name** | **Description**  
`config` | `[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService)` |   
  
### getDefaultDatastoreConfig() (deprecated)
    
    
    public static DatastoreConfig getDefaultDatastoreConfig()

**Deprecated.** _Use[DatastoreServiceConfig.Builder#withDefaults()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig.Builder#com_google_appengine_api_datastore_DatastoreServiceConfig_Builder_withDefaults__) instead._

**Returns**  
---  
**Type** | **Description**  
`[DatastoreConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreConfig)` |   
  
## Constructors 

### DatastoreServiceFactory() (deprecated)
    
    
    public DatastoreServiceFactory()

**Deprecated.** _Exposed by accident, do not instantiate._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
