---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService
title: Interface AsyncDatastoreService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:45.497608+00:00
---

# Interface AsyncDatastoreService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface AsyncDatastoreService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface AsyncDatastoreService extends BaseDatastoreService

An asynchronous version of [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService). All methods return immediately and provide [Futures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) as their return values.

The key difference between implementations of [AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService) and implementations of [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) is that async implementations do not perform implicit transaction management. The reason is that implicit transaction management requires automatic commits of some transactions, and without some sort of callback mechanism there is no way to determine that a put/get/delete that has been implicitly enrolled in a transaction is complete and therefore ready to be committed. See [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) for more information.

## Implements

[BaseDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService)

## Methods 

### allocateIds(@Nullable Key parent, String kind, long num)
    
    
    public abstract Future<KeyRange> allocateIds(@Nullable Key parent, String kind, long num)

See [DatastoreService#allocateIds(Key, String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_allocateIds_com_google_appengine_api_datastore_Key_java_lang_String_long_).

**Parameters**  
---  
**Name** | **Description**  
`parent` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`num` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)>` |   
  
### allocateIds(String kind, long num)
    
    
    public abstract Future<KeyRange> allocateIds(String kind, long num)

See [DatastoreService#allocateIds(String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_allocateIds_java_lang_String_long_).

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`num` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)>` |   
  
### beginTransaction()
    
    
    public abstract Future<Transaction> beginTransaction()

See [DatastoreService#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)>` |   
  
### beginTransaction(TransactionOptions options)
    
    
    public abstract Future<Transaction> beginTransaction(TransactionOptions options)

See [DatastoreService#beginTransaction(TransactionOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction_com_google_appengine_api_datastore_TransactionOptions_).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)>` |   
  
### delete(@Nullable Transaction txn, Key[] keys)
    
    
    public abstract Future<Void> delete(@Nullable Transaction txn, Key[] keys)

See [DatastoreService#delete(Transaction, Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_com_google_appengine_api_datastore_Transaction_java_lang_Iterable_com_google_appengine_api_datastore_Key__).

**Parameters**  
---  
**Name** | **Description**  
`txn` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction`  
  
`keys` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### delete(@Nullable Transaction txn, Iterable<Key> keys)
    
    
    public abstract Future<Void> delete(@Nullable Transaction txn, Iterable<Key> keys)

See [DatastoreService#delete(Transaction, Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_com_google_appengine_api_datastore_Transaction_java_lang_Iterable_com_google_appengine_api_datastore_Key__).

**Parameters**  
---  
**Name** | **Description**  
`txn` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction`  
  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### delete(Key[] keys)
    
    
    public abstract Future<Void> delete(Key[] keys)

See [DatastoreService#delete(Key...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### delete(Iterable<Key> keys)
    
    
    public abstract Future<Void> delete(Iterable<Key> keys)

See [DatastoreService#delete(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_java_lang_Iterable_com_google_appengine_api_datastore_Key__).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### get(@Nullable Transaction txn, Key key)
    
    
    public abstract Future<Entity> get(@Nullable Transaction txn, Key key)

See [DatastoreService#get(Transaction, Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_com_google_appengine_api_datastore_Transaction_com_google_appengine_api_datastore_Key_).

**Parameters**  
---  
**Name** | **Description**  
`txn` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction`  
  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### get(@Nullable Transaction txn, Iterable<Key> keys)
    
    
    public abstract Future<Map<Key,Entity>> get(@Nullable Transaction txn, Iterable<Key> keys)

See [DatastoreService#get(Transaction, Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_com_google_appengine_api_datastore_Transaction_java_lang_Iterable_com_google_appengine_api_datastore_Key__).

**Parameters**  
---  
**Name** | **Description**  
`txn` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction`  
  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key),[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>>` |   
  
### get(Key key)
    
    
    public abstract Future<Entity> get(Key key)

See [DatastoreService#get(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_com_google_appengine_api_datastore_Key_).

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### get(Iterable<Key> keys)
    
    
    public abstract Future<Map<Key,Entity>> get(Iterable<Key> keys)

See [DatastoreService#get(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_java_lang_Iterable_com_google_appengine_api_datastore_Key__).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key),[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>>` |   
  
### getDatastoreAttributes()
    
    
    public abstract Future<DatastoreAttributes> getDatastoreAttributes()

See [DatastoreService#getDatastoreAttributes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_getDatastoreAttributes__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[DatastoreAttributes](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreAttributes)>` |   
  
### getIndexes()
    
    
    public abstract Future<Map<Index,Index.IndexState>> getIndexes()

See [DatastoreService#getIndexes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_getIndexes__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index),[IndexState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index.IndexState)>>` |   
  
### put(@Nullable Transaction txn, Entity entity)
    
    
    public abstract Future<Key> put(@Nullable Transaction txn, Entity entity)

See [DatastoreService#put(Transaction, Entity)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Transaction_com_google_appengine_api_datastore_Entity_).

**Parameters**  
---  
**Name** | **Description**  
`txn` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction`  
  
`entity` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>` |   
  
### put(@Nullable Transaction txn, Iterable<Entity> entities)
    
    
    public abstract Future<List<Key>> put(@Nullable Transaction txn, Iterable<Entity> entities)

See [DatastoreService#put(Transaction, Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Transaction_java_lang_Iterable_com_google_appengine_api_datastore_Entity__).

**Parameters**  
---  
**Name** | **Description**  
`txn` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Transaction`  
  
`entities` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>>` |   
  
### put(Entity entity)
    
    
    public abstract Future<Key> put(Entity entity)

See [DatastoreService#put(Entity)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Entity_).

**Parameter**  
---  
**Name** | **Description**  
`entity` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>` |   
  
### put(Iterable<Entity> entities)
    
    
    public abstract Future<List<Key>> put(Iterable<Entity> entities)

See [DatastoreService#put(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_java_lang_Iterable_com_google_appengine_api_datastore_Entity__).

**Parameter**  
---  
**Name** | **Description**  
`entities` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
