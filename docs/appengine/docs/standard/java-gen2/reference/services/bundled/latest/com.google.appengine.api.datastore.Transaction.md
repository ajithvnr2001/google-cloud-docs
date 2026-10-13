---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction
title: Interface Transaction (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:49.025836+00:00
---

# Interface Transaction (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface Transaction (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface Transaction

Describes a logical unit of work to be performed against the datastore. Operations performed as part of a single [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) succeed or fail as a unit. Transactions can be committed and rolled back synchronously and asynchronously.

## Methods 

### commit()
    
    
    public abstract void commit()

Commits the transaction. Whether this call succeeds or fails, all subsequent method invocations on this object will throw IllegalStateException.

### commitAsync()
    
    
    public abstract Future<Void> commitAsync()

An asynchronous implementation of [#commit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_commit__). See Also: [#commit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_commit__)

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | A Future associated with the call.  
  
### getApp()
    
    
    public abstract String getApp()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The application id for the `Transaction`.  
  
### getId()
    
    
    public abstract String getId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The globally unique identifier for the `Transaction`.  
  
### isActive()
    
    
    public abstract boolean isActive()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the transaction is active, `false` otherwise.  
  
### rollback()
    
    
    public abstract void rollback()

Rolls back the transaction. Whether this call succeeds or fails, all subsequent method invocations on this object will throw IllegalStateException.

### rollbackAsync()
    
    
    public abstract Future<Void> rollbackAsync()

An asynchronous implementation of [#rollback()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_rollback__). See Also: [#rollback()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_rollback__)

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` | A Future associated with the call.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
