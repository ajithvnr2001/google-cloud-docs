---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IDatastoreServiceFactory
title: Interface IDatastoreServiceFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:46.115494+00:00
---

# Interface IDatastoreServiceFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IDatastoreServiceFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface IDatastoreServiceFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface IDatastoreServiceFactory

This interface should be implemented by providers of the [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) and registered with [com.google.appengine.spi.ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory).

## Methods 

### getAsyncDatastoreService(DatastoreServiceConfig config)
    
    
    public abstract AsyncDatastoreService getAsyncDatastoreService(DatastoreServiceConfig config)

Creates an `AsyncDatastoreService` using the provided config.

**Parameter**  
---  
**Name** | **Description**  
`config` | `[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService)` |   
  
### getDatastoreService(DatastoreServiceConfig config)
    
    
    public abstract DatastoreService getDatastoreService(DatastoreServiceConfig config)

Creates a `DatastoreService` using the provided config.

**Parameter**  
---  
**Name** | **Description**  
`config` | `[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
