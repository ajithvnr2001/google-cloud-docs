---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService
title: Interface DatastoreService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:45.780991+00:00
---

# Interface DatastoreService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface DatastoreService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface DatastoreService extends BaseDatastoreService

The `DatastoreService` provides synchronous access to a schema-less data storage system. The fundamental unit of data in this system is the `Entity`, which has an immutable identity (represented by a `Key`) and zero or more mutable properties. `Entity` objects can be created, updated, deleted, retrieved by identifier, and queried via a combination of properties.

The `DatastoreService` can be used transactionally and supports the notion of a "current" transaction. A current transaction is established by calling [#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__). The transaction returned by this method ceases to be current when an attempt is made to commit or rollback or when another call is made to [#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__). A transaction can only be current within the Thread that created it.

The various overloads of put, get, and delete all support transactions. Users of this class have the choice of explicitly passing a (potentially `null`) [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) to these methods or relying on the behavior governed by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy). If a user explicitly provides a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) it is up to the user to call [Transaction#commit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_commit__) or [Transaction#rollback()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_rollback__) at the proper time. If a user relies on implicit transaction management and the installed policy creates a transaction, that transaction will be committed (in the case of a success) or rolled back (in the case of a failure) before the operation returns to the user. The methods that manage transactions according to [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) are: [#delete(Key...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_), [#delete(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_java_lang_Iterable_com_google_appengine_api_datastore_Key__), [#get(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_com_google_appengine_api_datastore_Key_), [#get(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_java_lang_Iterable_com_google_appengine_api_datastore_Key__), [#put(Entity)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Entity_), and [#put(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_java_lang_Iterable_com_google_appengine_api_datastore_Entity__).

The overload of prepare that takes a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) parameter behaves the same as the overloads of put, get, and delete that take a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) parameter. However, the overload of prepare that does not take a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) parameter, unlike put, get, and delete, does not use an existing [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) if one is already running and does not consult the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) if one is not already running.

## Implements

[BaseDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService)

## Methods 

### allocateIdRange(KeyRange range)
    
    
    public abstract DatastoreService.KeyRangeState allocateIdRange(KeyRange range)

This method allocates a user-specified contiguous range of unique IDs.

Once these IDs have been allocated they may be provided manually to newly created entities.

Since the datastore's automatic ID allocator will never assign a key to a new entity that will cause an existing entity to be overwritten, entities written to the given [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange) will never be overwritten. However, writing entities with manually assigned keys in this range may overwrite existing entities (or new entities written by a separate request) depending on the KeyRangeState returned.

This method should only be used if you have an existing numeric id range that you want to reserve, e.g. bulk loading entities that already have IDs. If you don't care about which IDs you receive, use [#allocateIds](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_allocateIds_) instead.

**Parameter**  
---  
**Name** | **Description**  
`range` | `[KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)`  
The key range to allocate.  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreService.KeyRangeState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService.KeyRangeState)` | The state of the id range allocated.  
  
### allocateIds(Key parent, String kind, long num)
    
    
    public abstract KeyRange allocateIds(Key parent, String kind, long num)

IDs are allocated within a namespace defined by a parent key and a kind. This method allocates a contiguous range of unique IDs of size `num` within the namespace defined by the given parent key and the given kind.

IDs allocated in this manner may be provided manually to newly created entities. They will not be used by the datastore's automatic ID allocator for entities with the same kind and parent.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
The key for which the child entity IDs should be allocated. Can be null.  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kind for which the child entity IDs should be allocated.  
`num` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of IDs to allocate.  
**Returns**  
---  
**Type** | **Description**  
`[KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)` | A range of IDs of size `num` that are guaranteed to be unique.  
  
### allocateIds(String kind, long num)
    
    
    public abstract KeyRange allocateIds(String kind, long num)

IDs are allocated within a namespace defined by a parent key and a kind. This method allocates a contiguous range of unique IDs of size `num` within the namespace defined by a null parent key (root entities) and the given kind.

IDs allocated in this manner may be provided manually to newly created entities. They will not be used by the datastore's automatic ID allocator for root entities of the same kind.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kind for which the root entity IDs should be allocated.  
`num` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of IDs to allocate.  
**Returns**  
---  
**Type** | **Description**  
`[KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)` | A `KeyRange` of size `num`.  
  
### beginTransaction()
    
    
    public abstract Transaction beginTransaction()

Equivalent to `beginTransaction(TransactionOptions.Builder.withDefaults())`. See Also: [#beginTransaction(TransactionOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction_com_google_appengine_api_datastore_TransactionOptions_)

**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` | the `Transaction` that was started.  
  
### beginTransaction(TransactionOptions options)
    
    
    public abstract Transaction beginTransaction(TransactionOptions options)

Begins a transaction against the datastore. Callers are responsible for explicitly calling [Transaction#commit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_commit__) or [Transaction#rollback()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_rollback__) when they no longer need the `Transaction`.

The `Transaction` returned by this call will be considered the current transaction and will be returned by subsequent, same-thread calls to #getCurrentTransaction() and #getCurrentTransaction(Transaction) until one of the following happens: 1) [#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__) is invoked from the same thread. In this case #getCurrentTransaction() and #getCurrentTransaction(Transaction) will return the result of the more recent call to [#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__). 2) [Transaction#commit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_commit__) is invoked on the [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) returned by this method. Whether or not the commit returns successfully, the `Transaction` will no longer be the current transaction. 3) [Transaction#rollback()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_rollback__) ()} is invoked on the [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) returned by this method. Whether or not the rollback returns successfully, the `Transaction` will no longer be the current transaction. See Also: [TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions), #getCurrentTransaction()

**Parameter**  
---  
**Name** | **Description**  
`options` | `[TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)`  
The options for the new transaction.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)` | the `Transaction` that was started.  
  
### delete(Key[] keys)
    
    
    public abstract void delete(Key[] keys)

Deletes the `Entity entities` specified by `keys`.

If there is a current transaction, this operation will execute within that transaction. In this case it is up to the caller to commit or rollback. If there is no current transaction, the behavior of this method with respect to transactions will be determined by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) available on the [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)[]`  
  
  
### delete(Transaction txn, Key[] keys)
    
    
    public abstract void delete(Transaction txn, Key[] keys)

Exhibits the same behavior as [#delete(Key...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`keys` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)[]`  
  
  
### delete(Transaction txn, Iterable<Key> keys)
    
    
    public abstract void delete(Transaction txn, Iterable<Key> keys)

Exhibits the same behavior as [#delete(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_java_lang_Iterable_com_google_appengine_api_datastore_Key__), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
  
### delete(Iterable<Key> keys)
    
    
    public abstract void delete(Iterable<Key> keys)

Equivalent to [#delete(Key...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
  
### get(Key key)
    
    
    public abstract Entity get(Key key)

Retrieves the `Entity` with the specified `Key`.

If there is a current transaction, this operation will execute within that transaction. In this case it is up to the caller to commit or rollback. If there is no current transaction, the behavior of this method with respect to transactions will be determined by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) available on the [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[EntityNotFoundException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityNotFoundException)` | If the specified entity could not be found.  
  
### get(Transaction txn, Key key)
    
    
    public abstract Entity get(Transaction txn, Key key)

Exhibits the same behavior as [#get(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_com_google_appengine_api_datastore_Key_), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[EntityNotFoundException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityNotFoundException)` | If `txn` is not null and not active.  
  
### get(Transaction txn, Iterable<Key> keys)
    
    
    public abstract Map<Key,Entity> get(Transaction txn, Iterable<Key> keys)

Exhibits the same behavior as [#get(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_java_lang_Iterable_com_google_appengine_api_datastore_Key__), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key),[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### get(Iterable<Key> keys)
    
    
    public abstract Map<Key,Entity> get(Iterable<Key> keys)

Retrieves the set of [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) matching `keys`. The result `Map` will only contain `Keys` for which `Entities` could be found.

If there is a current transaction, this operation will execute within that transaction. In this case it is up to the caller to commit or rollback. If there is no current transaction, the behavior of this method with respect to transactions will be determined by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) available on the [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

**Parameter**  
---  
**Name** | **Description**  
`keys` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key),[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### getDatastoreAttributes()
    
    
    public abstract DatastoreAttributes getDatastoreAttributes()

Retrieves the current datastore's attributes.

**Returns**  
---  
**Type** | **Description**  
`[DatastoreAttributes](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreAttributes)` | The attributes of the datastore used to fulfill requests.  
  
### getIndexes()
    
    
    public abstract Map<Index,Index.IndexState> getIndexes()

Returns the application indexes and their states.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index),[IndexState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index.IndexState)>` |   
  
### put(Entity entity)
    
    
    public abstract Key put(Entity entity)

If the specified `Entity` does not yet exist in the data store, create it and assign its `Key`. If the specified `Entity` already exists in the data store, save the new version.

The `Key` is returned, and is also returned by future calls to ` entity.getKey()`.

If there is a current transaction, this operation will execute within that transaction. In this case it is up to the caller to commit or rollback. If there is no current transaction, the behavior of this method with respect to transactions will be determined by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) available on the [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

**Parameter**  
---  
**Name** | **Description**  
`entity` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### put(Transaction txn, Entity entity)
    
    
    public abstract Key put(Transaction txn, Entity entity)

Exhibits the same behavior as [#put(Entity)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Entity_), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`entity` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### put(Transaction txn, Iterable<Entity> entities)
    
    
    public abstract List<Key> put(Transaction txn, Iterable<Entity> entities)

Exhibits the same behavior as [#put(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_java_lang_Iterable_com_google_appengine_api_datastore_Entity__), but executes within the provided transaction. It is up to the caller to commit or rollback. Transaction can be null.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
  
`entities` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>` | The `Key`s that were assigned to the entities that were put. If the ` Iterable` that was provided as an argument has a stable iteration order the `Key`s in the `List` we return are in that same order. If the `Iterable` that was provided as an argument does not have a stable iteration order the order of the ` Key`s in the `List` we return is undefined.  
  
### put(Iterable<Entity> entities)
    
    
    public abstract List<Key> put(Iterable<Entity> entities)

Performs a batch [put](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Entity_) of all `entities`.

If there is a current transaction, this operation will execute within that transaction. In this case it is up to the caller to commit or rollback. If there is no current transaction, the behavior of this method with respect to transactions will be determined by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) available on the [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

**Parameter**  
---  
**Name** | **Description**  
`entities` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)>` | The `Key`s that were assigned to the entities that were put. If the ` Iterable` that was provided as an argument has a stable iteration order the `Key`s in the `List` we return are in that same order. If the `Iterable` that was provided as an argument does not have a stable iteration order the order of the ` Key`s in the `List` we return is undefined.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
