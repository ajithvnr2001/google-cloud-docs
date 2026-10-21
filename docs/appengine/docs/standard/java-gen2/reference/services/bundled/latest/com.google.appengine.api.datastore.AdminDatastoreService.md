---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService
title: Class AdminDatastoreService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:48.084795+00:00
---

# Class AdminDatastoreService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class AdminDatastoreService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class AdminDatastoreService implements AsyncDatastoreService

An AsyncDatastoreService implementation that is pinned to a specific appId and namesapce. This implementation ignores the "current" appId provided by ` ApiProxy.getCurrentEnvironment().getAppId()` and the "current" namespace provided by ` NamespaceManager.get()`. Note, this is particularly important in the following methods:

  * [AsyncDatastoreService#getIndexes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_getIndexes__)
  * [AsyncDatastoreService#getDatastoreAttributes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_getDatastoreAttributes__)
  * [AsyncDatastoreService#allocateIds(String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_allocateIds_java_lang_String_long_)



In addition this class provides ways to create [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query), [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) and [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that are pinned to the same appId/namespace.

Note: users should not access this class directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdminDatastoreService

## Implements

[AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService)

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

### getInstance(DatastoreServiceConfig config, String appId)
    
    
    public static AdminDatastoreService getInstance(DatastoreServiceConfig config, String appId)

Returns an AdminUtils instance for the given `appId` and the "" (empty) namespace.

**Parameters**  
---  
**Name** | **Description**  
`config` | `[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)`  
  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService)` |   
  
### getInstance(DatastoreServiceConfig config, String appId, String namespace)
    
    
    public static AdminDatastoreService getInstance(DatastoreServiceConfig config, String appId, String namespace)

Returns an AdminUtils instance for the given `appId` and `namespace`.

**Parameters**  
---  
**Name** | **Description**  
`config` | `[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)`  
  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService)` |   
  
### getInstance(String appId)
    
    
    public static AdminDatastoreService getInstance(String appId)

Returns an AdminUtils instance for the given `appId` and the "" (empty) namespace.

**Parameter**  
---  
**Name** | **Description**  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService)` |   
  
### getInstance(String appId, String namespace)
    
    
    public static AdminDatastoreService getInstance(String appId, String namespace)

Returns an AdminUtils instance for the given `appId` and `namespace`.

**Parameters**  
---  
**Name** | **Description**  
`appId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService)` |   
  
## Methods 

### allocateIds(@Nullable Key parent, String kind, long num)
    
    
    public Future<KeyRange> allocateIds(@Nullable Key parent, String kind, long num)

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
    
    
    public Future<KeyRange> allocateIds(String kind, long num)

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
    
    
    public Future<Transaction> beginTransaction()

See [DatastoreService#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)>` |   
  
### beginTransaction(TransactionOptions options)
    
    
    public Future<Transaction> beginTransaction(TransactionOptions options)

See [DatastoreService#beginTransaction(TransactionOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction_com_google_appengine_api_datastore_TransactionOptions_).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)>` |   
  
### compositeIndexForQuery(Query query)
    
    
    public Index compositeIndexForQuery(Query query)

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)` |   
  
### compositeIndexesForQuery(Query query)
    
    
    public Set<Index> compositeIndexesForQuery(Query query)

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)>` |   
  
### delete(@Nullable Transaction txn, Key[] keys)
    
    
    public Future<Void> delete(@Nullable Transaction txn, Key[] keys)

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
    
    
    public Future<Void> delete(@Nullable Transaction txn, Iterable<Key> keys)

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
    
    
    public Future<Void> delete(Key[] keys)

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
    
    
    public Future<Void> delete(Iterable<Key> keys)

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
    
    
    public Future<Entity> get(@Nullable Transaction txn, Key key)

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
    
    
    public Future<Map<Key,Entity>> get(@Nullable Transaction txn, Iterable<Key> keys)

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
    
    
    public Future<Entity> get(Key key)

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
    
    
    public Future<Map<Key,Entity>> get(Iterable<Key> keys)

See [DatastoreService#get(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_java_lang_Iterable_com_google_appengine_api_datastore_Key__).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key),[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>>` |   
  
### getActiveTransactions()
    
    
    public Collection<Transaction> getActiveTransactions()

Returns all [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)s started by this thread upon which no attempt to commit or rollback has been made.

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)>` |   
  
### getAppId()
    
    
    public String getAppId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCurrentTransaction()
    
    
    public Transaction getCurrentTransaction()

Returns the current transaction for this thread, or throws an exception if there is no current transaction. The current transaction is defined as the result of the most recent, same-thread invocation of beginTransaction() that has not been committed or rolled back.

Use this method for when you expect there to be a current transaction and consider it an error if there isn't.

**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` |   
  
### getCurrentTransaction(Transaction returnedIfNoTxn)
    
    
    public Transaction getCurrentTransaction(Transaction returnedIfNoTxn)

Returns the current transaction for this thread, or returns the parameter if there is no current transaction. You can use `null` or provide your own object to represent null. See [#getCurrentTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService#com_google_appengine_api_datastore_AdminDatastoreService_getCurrentTransaction__) for a definition of "current transaction."

Use this method when you're not sure if there is a current transaction.

**Parameter**  
---  
**Name** | **Description**  
`returnedIfNoTxn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` |   
  
### getDatastoreAttributes()
    
    
    public Future<DatastoreAttributes> getDatastoreAttributes()

See [DatastoreService#getDatastoreAttributes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_getDatastoreAttributes__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[DatastoreAttributes](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreAttributes)>` |   
  
### getIndexes()
    
    
    public Future<Map<Index,Index.IndexState>> getIndexes()

See [DatastoreService#getIndexes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_getIndexes__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index),[IndexState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index.IndexState)>>` |   
  
### getNamespace()
    
    
    public String getNamespace()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### minimumCompositeIndexForQuery(Query query, Collection<Index> indexes)
    
    
    public Index minimumCompositeIndexForQuery(Query query, Collection<Index> indexes)

**Parameters**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
`indexes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)` |   
  
### minimumCompositeIndexesForQuery(Query query, Collection<Index> indexes)
    
    
    public Set<Index> minimumCompositeIndexesForQuery(Query query, Collection<Index> indexes)

**Parameters**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
`indexes` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)>` |   
  
### newEntityBuilder(String kind)
    
    
    public AdminDatastoreService.EntityBuilder newEntityBuilder(String kind)

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService.EntityBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.EntityBuilder)` |   
  
### newKeyBuilder(String kind)
    
    
    public AdminDatastoreService.KeyBuilder newKeyBuilder(String kind)

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService.KeyBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.KeyBuilder)` |   
  
### newQueryBuilder()
    
    
    public AdminDatastoreService.QueryBuilder newQueryBuilder()

**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService.QueryBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.QueryBuilder)` |   
  
### newQueryBuilder(String kind)
    
    
    public AdminDatastoreService.QueryBuilder newQueryBuilder(String kind)

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdminDatastoreService.QueryBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.QueryBuilder)` |   
  
### prepare(Query query)
    
    
    public PreparedQuery prepare(Query query)

Prepares a query for execution.

This method returns a [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) which can be used to execute and retrieve results from the datastore for `query`.

This operation will not execute in a transaction even if there is a current transaction and the provided query is an ancestor query. This operation also ignores the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy). If you are preparing an ancestory query and you want it to execute in a transaction, use [#prepare(Transaction, Query)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService#com_google_appengine_api_datastore_AdminDatastoreService_prepare_com_google_appengine_api_datastore_Transaction_com_google_appengine_api_datastore_Query_).

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery)` |   
  
### prepare(Transaction txn, Query query)
    
    
    public PreparedQuery prepare(Transaction txn, Query query)

Exhibits the same behavior as [#prepare(Query)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService#com_google_appengine_api_datastore_AdminDatastoreService_prepare_com_google_appengine_api_datastore_Query_), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery)` |   
  
### put(@Nullable Transaction txn, Entity entity)
    
    
    public Future<Key> put(@Nullable Transaction txn, Entity entity)

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
    
    
    public Future<List<Key>> put(@Nullable Transaction txn, Iterable<Entity> entities)

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
    
    
    public Future<Key> put(Entity entity)

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
    
    
    public Future<List<Key>> put(Iterable<Entity> entities)

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
