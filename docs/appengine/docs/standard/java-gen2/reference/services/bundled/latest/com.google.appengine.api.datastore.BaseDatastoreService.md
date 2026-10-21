---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService
title: Interface BaseDatastoreService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:44.306488+00:00
---

# Interface BaseDatastoreService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface BaseDatastoreService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface BaseDatastoreService

Methods that are common between [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) and [AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService).

## Methods 

### getActiveTransactions()
    
    
    public abstract Collection<Transaction> getActiveTransactions()

Returns all [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)s started by this thread upon which no attempt to commit or rollback has been made.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)>` |   
  
### getCurrentTransaction()
    
    
    public abstract Transaction getCurrentTransaction()

Returns the current transaction for this thread, or throws an exception if there is no current transaction. The current transaction is defined as the result of the most recent, same-thread invocation of beginTransaction() that has not been committed or rolled back.

Use this method for when you expect there to be a current transaction and consider it an error if there isn't.

**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` | The current transaction.  
  
### getCurrentTransaction(Transaction returnedIfNoTxn)
    
    
    public abstract Transaction getCurrentTransaction(Transaction returnedIfNoTxn)

Returns the current transaction for this thread, or returns the parameter if there is no current transaction. You can use `null` or provide your own object to represent null. See [#getCurrentTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService#com_google_appengine_api_datastore_BaseDatastoreService_getCurrentTransaction__) for a definition of "current transaction."

Use this method when you're not sure if there is a current transaction.

**Parameter**  
---  
**Name** | **Description**  
`returnedIfNoTxn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
The return value of this method if there is no current transaction. Can be null.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` | The current transaction, or the parameter that was passed in if there is no current transaction.  
  
### prepare(Query query)
    
    
    public abstract PreparedQuery prepare(Query query)

Prepares a query for execution.

This method returns a [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) which can be used to execute and retrieve results from the datastore for `query`.

This operation will not execute in a transaction even if there is a current transaction and the provided query is an ancestor query. This operation also ignores the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy). If you are preparing an ancestory query and you want it to execute in a transaction, use [#prepare(Transaction, Query)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService#com_google_appengine_api_datastore_BaseDatastoreService_prepare_com_google_appengine_api_datastore_Transaction_com_google_appengine_api_datastore_Query_).

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
a not `null Query`.  
**Returns**  
---  
**Type** | **Description**  
`[PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery)` | a not `null PreparedQuery`.  
  
### prepare(Transaction txn, Query query)
    
    
    public abstract PreparedQuery prepare(Transaction txn, Query query)

Exhibits the same behavior as [#prepare(Query)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService#com_google_appengine_api_datastore_BaseDatastoreService_prepare_com_google_appengine_api_datastore_Query_), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
