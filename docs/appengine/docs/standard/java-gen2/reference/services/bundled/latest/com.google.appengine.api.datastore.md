---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore
title: Package com.google.appengine.api.datastore (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:44.095319+00:00
---

# Package com.google.appengine.api.datastore (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.datastore (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides persistent storage, also accessible via [JDO](http://www.oracle.com/technetwork/java/index-jsp-135919.html) or [JPA](http://www.oracle.com/technetwork/articles/javaee/jpa-137156.html) interfaces. It provides redundant storage for fault-tolerance.

A common pattern of usage is:
    
    
     // Get a handle on the datastore itself
     DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
    
     // Lookup data by known key name
     Entity userEntity = datastore.get(KeyFactory.createKey("UserInfo", email));
    
     // Or perform a query
     Query query = new Query("Task");
     query.addFilter("dueDate", Query.FilterOperator.LESS_THAN, today);
     for (Entity taskEntity : datastore.prepare(query).asIterable()) {
       if ("done".equals(taskEntity.getProperty("status"))) {
         datastore.delete(taskEntity);
       } else {
         taskEntity.setProperty("status", "overdue");
         datastore.put(taskEntity);
       }
     }
     

This illustrates several basic points:

  * The actual datastore itself is accessed through a [com.google.appengine.api.datastore.DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) object, produced from a [com.google.appengine.api.datastore.DatastoreServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceFactory). 
  * The unit of storage is the [com.google.appengine.api.datastore.Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) object, which are of named kinds ("UserInfo" and "Task" above). 
  * Entities have a [com.google.appengine.api.datastore.Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) value, which can be created by a [com.google.appengine.api.datastore.KeyFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory) to retrieve a specific known entity. If the key is not readily determined, then [com.google.appengine.api.datastore.Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) objects can be used to retrieve one Entity, multiple as a list, [java.lang.Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html), or [java.util.Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html), or to retrieve the count of matching entities. 
  * Entities have named properties, the values of which may be basic types or collections of basic types. Richer objects, of course, may be stored if serialized as byte arrays, although that may prevent effective querying by those properties. 
  * Entities may be associated in a tree structure; the [com.google.appengine.api.datastore.Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) in the snippet above searches only for Task entities associated with a specific UserInfo entity, and then filters those for Tasks due before today. 



In production, non-trivial queries cannot be performed until one or more indexes have been built to ensure that the individual queries can be processed efficiently. You can specify the set of indexes your application requires in a `WEB-INF/datastore-indexes.xml` file, or they can be generated automatically as you test your application in the Development Server. If a query requires an index that cannot be found, a [com.google.appengine.api.datastore.DatastoreNeedIndexException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreNeedIndexException) will be thrown at runtime.

Although Google App Engine allows many versions of your application to be accessible, there is only one datastore for your application, shared by all versions. Similarly, the set of indexes is shared by all application versions.

Application authors may also consider using either of the provided JDO or JPA interfaces to the datastore. See Also: [com.google.appengine.api.datastore.DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService), [JPA API](http://www.oracle.com/technetwork/articles/javaee/jpa-137156.html), [JDO API](http://www.oracle.com/technetwork/java/index-jsp-135919.html), [The Datastore Java API in the Google App Engine Developers Guide](http://cloud.google.com/appengine/docs/java/datastore/)

## Classes 

### [AdminDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService)

An AsyncDatastoreService implementation that is pinned to a specific appId and namesapce. This implementation ignores the "current" appId provided by ` ApiProxy.getCurrentEnvironment().getAppId()` and the "current" namespace provided by ` NamespaceManager.get()`. Note, this is particularly important in the following methods:

  * [AsyncDatastoreService#getIndexes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_getIndexes__)
  * [AsyncDatastoreService#getDatastoreAttributes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_getDatastoreAttributes__)
  * [AsyncDatastoreService#allocateIds(String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_allocateIds_java_lang_String_long_)



In addition this class provides ways to create [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query), [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) and [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that are pinned to the same appId/namespace.

Note: users should not access this class directly.

### [AdminDatastoreService.EntityBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.EntityBuilder)

An [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) builder that pins it to the AdminUtils `appId` and `namespace`.

### [AdminDatastoreService.KeyBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.KeyBuilder)

A [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) builder that pins it to the AdminUtils `appId` and `namespace`.

### [AdminDatastoreService.QueryBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AdminDatastoreService.QueryBuilder)

A [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) builder that pins it to the AdminUtils `appId` and `namespace`.

### [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob)

`Blob` contains an array of bytes. This byte array can be no bigger than 1MB. To store files, particularly files larger than this 1MB limit, look at the Blobstore API.

### [Category](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Category)

A tag, ie a descriptive word or phrase. Entities may be tagged by users, and later returned by a queries for that tag. Tags can also be used for ranking results (frequency), photo captions, clustering, activity, etc. See Also: [Jeffrey Zeldmans blog post](http://www.zeldman.com/daily/0405d.shtml) on tag clouds for a more in-depth description.

### [CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig)

User-configurable global properties of Cloud Datastore.

Code not running in App Engine Standard can use the Cloud Datastore API by making a single call to [#setConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_setConfig_) before accessing any other classes from [com.google.appengine.api](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api). For example:
    
    
     public static void main(Strings[] args) {
       CloudDatastoreRemoteServiceConfig config = CloudDatastoreRemoteServiceConfig.builder()
           .appId(AppId.create(Location.US_CENTRAL, "my-project-id"))
           .build();
       CloudDatastoreRemoteServiceConfig.setConfig(config);
       DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
       ...
     }
     

Outside of tests, the config should not be cleared once it has been set. In tests, the config can be cleared by calling [#clear](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig#com_google_appengine_api_datastore_CloudDatastoreRemoteServiceConfig_clear_):
    
    
     {@literal @}Before
     public void before() {
       CloudDatastoreRemoteServiceConfig config = CloudDatastoreRemoteServiceConfig.builder()
           .appId(AppId.create(Location.US_CENTRAL, "my-project-id"))
           .emulatorHost(...)
           .build();
       CloudDatastoreRemoteServiceConfig.setConfig(config);
     }
    
     {@literal @}After
     public void after() {
       CloudDatastoreRemoteServiceConfig.clear();
     }
     

By default, this configuration uses [application-default credentials](https://developers.google.com/identity/protocols/application-default-credentials).

### [CloudDatastoreRemoteServiceConfig.AppId](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.AppId)

An App Engine application ID.

### [CloudDatastoreRemoteServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.Builder)

Builder for [CloudDatastoreRemoteServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig).

### [CompositeIndexManager](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager)

Composite index management operations needed by the datastore api.

### [CompositeIndexManager.IndexComponentsOnlyQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.IndexComponentsOnlyQuery)

Protected alias that allows us to make this class available to the local datastore without publicly exposing it in the api.

### [CompositeIndexManager.KeyTranslator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.KeyTranslator)

Protected alias that allows us to make this class available to the local datastore without publicly exposing it in the api.

### [CompositeIndexManager.ValidatedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.ValidatedQuery)

Protected alias that allows us to make this class available to the local datastore without publicly exposing it in the api.

### [CompositeIndexUtils](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexUtils)

Static utilities for working with composite indexes.

### [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)

A cursor that represents a position in a query.

To resume a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) at the position defined by a [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor), the [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor) must be present in the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.urlfetch.FetchOptions) passed to a [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) identical to the one it was created from.

Cursors can be retrieved from `PreparedQuery.asQueryResult*` functions. A typical use case would be:

> 
>      Cursor originalCursor = preparedQuery.asQueryResultList(withLimit(20)).getCursor();
>      String encodedCursor = original.toWebSafeString();
>      

The encoded cursor can then be passed safely in a get or post arg of a web request and on another request the next batch of results can be retrieved with:

> 
>      Cursor decodedCursor = Cursor.fromWebSafeString(encodedCursor);
>      List<Entity> nextBatch = preparedQuery.asQueryResultList(withLimit(20).cursor(decoded));
>      

### [DataTypeTranslator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeTranslator)

`DataTypeTranslator` is a utility class for converting between the data store's ` Property` protocol buffers and the user-facing classes (`String`, `User`, etc.).

### [DataTypeTranslator.ComparableByteArray](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeTranslator.ComparableByteArray)

A wrapper for a `byte[]` that implements [Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html). Comparison algorithm is the same as the prod datastore.

### [DataTypeUtils](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeUtils)

`DataTypeUtils` presents a simpler interface that allows user-code to determine what Classes can safely be stored as properties in the data store.

Currently this list includes:

  * [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html) (but not StringBuffer), 
  * All numeric primitive wrappers (Byte through Long, Float and [Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html), but not java.math.BigInteger or java.math.BigDecimal. 
  * [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key), for storing references to other [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects. 
  * [User](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.users.User), for storing references to users. 
  * [ShortBlob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ShortBlob), for storing binary data small enough to be indexed. This means properties of this type, unlike [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob) properties, can be filtered and sorted on in queries. 
  * [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob), for storing unindexed binary data less than 1MB. 
  * [Text](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Text), for storing unindexed String data less than 1MB. 
  * [BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey), for storing references to user uploaded blobs (which may exceed 1MB). 
  * Date. 
  * [Link](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Link). 



### [DatastoreApiHelper](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreApiHelper)

Helper methods and constants shared by classes that implement the Java api on top of the datastore.

Note: users should not access this class directly.

### [DatastoreAttributes](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreAttributes)

Attributes of a datastore.

### [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig)

User-configurable properties of the datastore.

Notes on usage:  
The recommended way to instantiate a `DatastoreServiceConfig` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.datastore.DatastoreServiceConfig.Builder.*;
     import com.google.appengine.api.datastore.ReadPolicy.Consistency;
    
     ...
    
     // eventually consistent reads
     DatastoreServiceConfig config = withReadPolicy(new ReadPolicy(Consistency.EVENTUAL));
    
     // eventually consistent reads with a 5 second deadline
     DatastoreServiceConfig config =
       withReadPolicy(new ReadPolicy(Consistency.EVENTUAL)).deadline(5.0);
     

### [DatastoreServiceConfig.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig.Builder)

Contains static creation methods for [DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig).

### [DatastoreServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceFactory)

Creates DatastoreService implementations.

### [DeleteContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DeleteContext)

Concrete [CallbackContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext) implementation that is specific to delete() callbacks.

### [Email](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Email)

An e-mail address datatype. Makes no attempt at validation. See Also: [RFC 2822](http://tools.ietf.org/html/rfc2822) for the e-mail address specification.

### [EmbeddedEntity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity)

A property value containing embedded entity properties (and optionally a [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)).

This class is similar to [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity), but differs in the following ways:

  * [#equals(Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity#com_google_appengine_api_datastore_EmbeddedEntity_equals_) and [#hashCode()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity#com_google_appengine_api_datastore_EmbeddedEntity_hashCode__) compare the embedded properties in addition to the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key). 
  * It is not queryable when stored in the datastore. 
  * A [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) is optional. 
  * [Keys](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) without a name or id are considered equal if all other aspects of the keys are equal (as they will not be assigned IDs by the datastore when embedded). 



To convert from an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) use:
    
    
     EmbeddedEntity sv = new EmbeddedEntity();
     sv.setKey(entity.getKey())
     sv.setPropertiesFrom(entity)
     

To convert to an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) use:
    
    
     Entity entity = new Entity(sv.getKey())
     entity.setPropertiesFrom(sv);
     

### [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entities)

Utility functions and constants for entities.

### [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)

`Entity` is the fundamental unit of data storage. It has an immutable identifier (contained in the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)) object, a reference to an optional parent `Entity`, a kind (represented as an arbitrary string), and a set of zero or more typed properties.

### [EntityProtoComparators](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityProtoComparators)

Utilities for comparing EntityProto. This class is only public because the dev appserver needs access to it. It should not be accessed by user code.

### [EntityProtoComparators.EntityProtoComparator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityProtoComparators.EntityProtoComparator)

A comparator for EntityProto objects with the same ordering as EntityComparator.

### [EntityTranslator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityTranslator)

`EntityTranslator` contains the logic to translate an `Entity` into the protocol buffers that are used to pass it to the implementation of the API.

### [ExtendableEntityUtil](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ExtendableEntityUtil)

Internal class that provides utility methods for extendable entity objects.

### [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)

Describes the limit, offset, and chunk size to be applied when executing a [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery).

`limit` is the maximum number of results the query will return.

`offset` is the number of results to skip before returning any results. Results that are skipped due to offset do not count against `limit`.  
**Note:** Using `offset` still retrieves skipped entities internally. This affects the latency of the query, and **your application is billed for the operations** required to retrieve them. Using cursors lets you avoid these costs.

`startCursor` and `endCursor` are previously generated cursors that point to locations in a result set. If specified queries will start and end at these locations.

`prefetchSize` is the number of results retrieved on the first call to the datastore.

`chunkSize` determines the internal chunking strategy of the [Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html) returned by [PreparedQuery#asIterator(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterator_com_google_appengine_api_datastore_FetchOptions_) and the [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html) returned by [PreparedQuery#asIterable(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterable_com_google_appengine_api_datastore_FetchOptions_).

Note that unlike `limit`, `offset` and `cursor`, `prefetchSize` and `chunkSize` have no impact on the result of the [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery), but rather only the performance of the [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery).

Notes on usage:  
The recommended way to instantiate a `FetchOptions` object is to import [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import com.google.appengine.api.datastore.[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html);
    
     [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor.html) cursor = ...
    
     ...
    
     // limit 10
     datastoreService.prepare(query).[asList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery.html#com_google_appengine_api_datastore_PreparedQuery_asList_com_google_appengine_api_datastore_FetchOptions_)([FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html).Builder.[withLimit](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder.html#com_google_appengine_api_datastore_FetchOptions_Builder_withLimit_int_)(10));
    
     // limit 10, start cursor
     datastoreService.prepare(query).[asList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery.html#com_google_appengine_api_datastore_PreparedQuery_asList_com_google_appengine_api_datastore_FetchOptions_)([FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html).Builder.[withLimit](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder.html#com_google_appengine_api_datastore_FetchOptions_Builder_withLimit_int_)(10).[startCursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html#com_google_appengine_api_datastore_FetchOptions_startCursor_com_google_appengine_api_datastore_Cursor_)(cursor));
     

### [FetchOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder)

Contains static creation methods for [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions).

### [FriendHacks](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FriendHacks)

Provides limited access to unlaunched (package-private) methods and classes from outside this package. This class is not bundled with the API jar. As features launch, code should be updated to use the public interfaces instead of the contents of this class.

### [FutureHelper](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FutureHelper)

Utilities for working with [Futures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) in the synchronous datastore api.

### [GeoPt](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.GeoPt)

A geographical point, specified by float latitude and longitude coordinates. Often used to integrate with mapping sites like Google Maps.

### [IDatastoreServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IDatastoreServiceFactoryProvider)

Creates `IDatastoreServiceFactory` implementations.

**Note:** This class is not intended for end users.

### [IMHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IMHandle)

An instant messaging handle. Includes both an address and its protocol. The protocol value is either a standard IM scheme (legal scheme values are defined by Scheme or a URL identifying the IM network for the protocol (e.g. <http://aim.com/>).

### [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)

A Datastore `Index` definition.

### [Index.Property](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index.Property)

An indexed property.

### [IndexTranslator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IndexTranslator)

Helper class to translate between Index to com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Index.

### [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)

The primary key for a datastore entity.

A datastore GUID. A Key instance uniquely identifies an entity across all apps, and includes all information necessary to fetch the entity from the datastore with ` DatastoreService.get(Key)`.

You can create `Key` objects directly by using [KeyFactory#createKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_createKey_) or [#getChild](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key#com_google_appengine_api_datastore_Key_getChild_).

You can also retrieve the `Key` automatically created when you create a new [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity), or serialize `Key` objects, or use [KeyFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory) to convert them to and from websafe String values. See Also: [KeyFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory)

### [KeyFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory)

This class enables direct creation of `Key` objects, both in the root entity group (no parent) and as the child of a given parent. Keys can also be created indirectly by putting named Entities into the datastore, which will allocate a new key. See Entity#Entity(String, String) for details.

This class also has methods for encoding and decoding `Key` objects to and from strings. Clients should not make any assumptions about the encoding format, except that it is a websafe string that does not need to be quoted when used in HTML or in URLs. See Also: [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)

### [KeyFactory.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory.Builder)

Helper class that aids in the construction of [Keys](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) with ancestors. Initialize the `Builder` with the topmost ancestor in your key path and then add children using the [#addChild](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory.Builder#com_google_appengine_api_datastore_KeyFactory_Builder_addChild_) overload that best suits your needs. When finished adding children, call [#getKey()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory.Builder#com_google_appengine_api_datastore_KeyFactory_Builder_getKey__) to retrieve your [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) or [#getString()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory.Builder#com_google_appengine_api_datastore_KeyFactory_Builder_getString__) to retrieve your [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) encoded as a websafe [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html).

Examples:  

    
    
     import com.google.appengine.api.datastore.KeyFactory.Builder;
    
     ...
    
     Key key = new Builder("Person", 88).addChild("Address", 24).getKey();
     String keyStr = new Builder("Photo Album", "Vacation").addChild("Photo", 1424).getString();
     

### [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)

Represents a range of unique datastore identifiers from `getStart().getId()` to ` getEnd().getId()` inclusive. If an instance of this class is the result of a call to ` DatastoreService.allocateIds()`, the [Keys](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) returned by this instance have been consumed in the datastore's id-space and are guaranteed never to be reused.   
This class can be used to construct [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) with [Keys](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that have specific id values without fear of the datastore creating new records with those same ids at a later date. This can be helpful as part of a data migration or large bulk upload where you may need to preserve existing ids and relationships between entities.   
This class is threadsafe but the [Iterators](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html) returned by [#iterator()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange#com_google_appengine_api_datastore_KeyRange_iterator__) are not.

### [Link](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Link)

A `Link` is a URL of limited length.

In addition to adding the meaning of `URL` onto a String, a `Link` can also be longer than a Text value, with a limit of 2083 characters.

### [PhoneNumber](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PhoneNumber)

A human-readable phone number. No validation is performed because phone numbers have many different formats - local, long distance, domestic, international, internal extension, TTY, VOIP, SMS, and alternative networks like Skype, XFire and Roger Wilco. They all have their own numbering and addressing formats.

### [PostLoadContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostLoadContext)

Concrete [CallbackContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext) implementation that is specific to intercepted operations that load [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity), currently get and "query". It is important to note that when a PostLoadContext is provided to a callback following a get operation, #getElements() returns all retrieved Entities. However, when a PostLoadContext is provided to a callback following a query, a separate PostLoadContext will be constructed for each Entity in the result set so #getElements() will only return a [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html) containing a single Entity. This is due to the streaming nature of query responses.

### [PostalAddress](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostalAddress)

A human-readable mailing address. Mailing address formats vary widely so no validation is performed.

### [PreGetContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGetContext)

Concrete [CallbackContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext) implementation that is specific to intercepted get() operations. Methods annotated with [PreGet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGet) that receive instances of this class may modify the result of the get() operation by calling [#setResultForCurrentElement(Entity)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGetContext#com_google_appengine_api_datastore_PreGetContext_setResultForCurrentElement_com_google_appengine_api_datastore_Entity_). Keys that receive results via this method will not be fetched from the datastore. This is an effective way to inject cached results.

### [PreQueryContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQueryContext)

Concrete [CallbackContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext) implementation that is specific to intercepted queries. Methods annotated with [PreQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQuery) that receive instances of this class may modify the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) returned by calling #getCurrentElement(). This is an effective way to modify queries prior to execution.

### [Projection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Projection)

A query projection. See Also: [Query#getProjections()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_getProjections__)

### [PropertyContainer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer)

A mutable property container.

### [PropertyProjection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyProjection)

A property projection.

If specified on a query, this will cause the query return the specified property. See Also: [Query#getProjections()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_getProjections__)

### [PutContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PutContext)

Concrete [CallbackContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext) implementation that is specific to put() callbacks.

### [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query)

[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query) encapsulates a request for zero or more [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects out of the datastore. It supports querying on zero or more properties, querying by ancestor, and sorting. [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) objects which match the query can be retrieved in a single list, or with an unbounded iterator.

### [Query.CompositeFilter](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.CompositeFilter)

A [Filter](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.Filter) that combines several sub filters using a CompositeFilterOperator.

For example, to construct a filter of the form `a = 1 AND (b = 2 OR c = 3)` use:
    
    
     new CompositeFilter(CompositeFilterOperator.AND, Arrays.asList(
         new FilterPredicate("a", FilterOperator.EQUAL, 1),
         new CompositeFilter(CompositeFilterOperator.OR, Arrays.<Filter>asList(
             new FilterPredicate("b", FilterOperator.EQUAL, 2),
             new FilterPredicate("c", FilterOperator.EQUAL, 3)))));
     

or
    
    
     CompositeFilterOperator.and(
         FilterOperator.EQUAL.of("a", 1),
         CompositeFilterOperator.or(
             FilterOperator.EQUAL.of("b", 2),
             FilterOperator.EQUAL.of("c", 3)));
     

### [Query.Filter](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.Filter)

The base class for a query filter.

All sub classes should be immutable.

### [Query.FilterPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterPredicate)

A Filter on a single property.

### [Query.GeoRegion](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.GeoRegion)

A geographic region intended for use in a StContainsFilter. Note that this is the only purpose for which it should be used: in particular, it is not suitable as a Property value to be stored in Datastore.

### [Query.GeoRegion.Circle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.GeoRegion.Circle)

A geographical region representing all points within a fixed distance from a central point, i.e., a circle. Intended for use in a geo-containment predicate filter.

### [Query.GeoRegion.Rectangle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.GeoRegion.Rectangle)

A simple geographical region bounded by two latitude lines, and two longitude lines, i.e., a "rectangle". It's not really a rectangle, of course, because longitude lines are not really parallel.

Intended for use in a geo-containment predicate filter.

### [Query.SortPredicate](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.SortPredicate)

SortPredicate is a data container that holds a single sort predicate.

### [Query.StContainsFilter](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.StContainsFilter)

A Filter representing a geo-region containment predicate.

### [Rating](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Rating)

A user-provided integer rating for a piece of content. Normalized to a 0-100 scale.

### [RawValue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.RawValue)

A raw datastore value.

These are returned by projection queries when a [PropertyProjection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyProjection) does not specify a type. See Also: [Query#getProjections()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query#com_google_appengine_api_datastore_Query_getProjections__)

### [ReadPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ReadPolicy)

Policy for reads.

### [ShortBlob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ShortBlob)

`ShortBlob` contains an array of bytes no longer than [DataTypeUtils#MAX_SHORT_BLOB_PROPERTY_LENGTH](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeUtils#com_google_appengine_api_datastore_DataTypeUtils_MAX_SHORT_BLOB_PROPERTY_LENGTH). Unlike [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob), `ShortBlobs` are indexed by the datastore and can therefore be filtered and sorted on in queries. If your data is too large to fit in a `ShortBlob` use [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob) instead.

### [Text](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Text)

`Text` wraps around a string of unlimited size.

Ordinary Java strings stored as properties in `Entity` objects are limited to 1500 bytes. However, `Text` objects can also be stored in properties, and are unlimited in size. However, they will not be indexed for query purposes.

Consider using a standard Java string and storing it with the Entity#setUnindexedProperty method instead.

### [TransactionHelper](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionHelper)

[TransactionHelper](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionHelper) enables the task queue API to serialize a datastore transaction without knowing the details of how it is implemented.

### [TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions)

Describes options for transactions, passed at transaction creation time.

Notes on usage:  
The recommended way to instantiate a `TransactionsOptions` object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.datastore.TransactionOptions.Builder.*;
    
     ...
    
     datastoreService.beginTransaction(withXG(true));
     

### [TransactionOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions.Builder)

Contains static creation methods for [TransactionOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions).

## Interfaces 

### [AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService)

An asynchronous version of [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService). All methods return immediately and provide [Futures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) as their return values.

The key difference between implementations of [AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService) and implementations of [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) is that async implementations do not perform implicit transaction management. The reason is that implicit transaction management requires automatic commits of some transactions, and without some sort of callback mechanism there is no way to determine that a put/get/delete that has been implicitly enrolled in a transaction is complete and therefore ready to be committed. See [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) for more information.

### [BaseDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.BaseDatastoreService)

Methods that are common between [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) and [AsyncDatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService).

### [CallbackContext<T>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CallbackContext)

Describes the context in which a callback runs. The context has access to the current transaction (if any), the element that the callback is operating on (eg the Entity being put or the Key being deleted), as well as all elements being operated on in the operation that triggered the callback..

### [DatastoreConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreConfig) (deprecated)

**Deprecated.** _Use[DatastoreServiceConfig](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreServiceConfig) instead._

User-configurable properties of the datastore.

### [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService)

The `DatastoreService` provides synchronous access to a schema-less data storage system. The fundamental unit of data in this system is the `Entity`, which has an immutable identity (represented by a `Key`) and zero or more mutable properties. `Entity` objects can be created, updated, deleted, retrieved by identifier, and queried via a combination of properties.

The `DatastoreService` can be used transactionally and supports the notion of a "current" transaction. A current transaction is established by calling [#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__). The transaction returned by this method ceases to be current when an attempt is made to commit or rollback or when another call is made to [#beginTransaction()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_beginTransaction__). A transaction can only be current within the Thread that created it.

The various overloads of put, get, and delete all support transactions. Users of this class have the choice of explicitly passing a (potentially `null`) [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) to these methods or relying on the behavior governed by the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy). If a user explicitly provides a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) it is up to the user to call [Transaction#commit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_commit__) or [Transaction#rollback()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction#com_google_appengine_api_datastore_Transaction_rollback__) at the proper time. If a user relies on implicit transaction management and the installed policy creates a transaction, that transaction will be committed (in the case of a success) or rolled back (in the case of a failure) before the operation returns to the user. The methods that manage transactions according to [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) are: [#delete(Key...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_), [#delete(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_delete_java_lang_Iterable_com_google_appengine_api_datastore_Key__), [#get(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_com_google_appengine_api_datastore_Key_), [#get(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_java_lang_Iterable_com_google_appengine_api_datastore_Key__), [#put(Entity)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_com_google_appengine_api_datastore_Entity_), and [#put(Iterable)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_put_java_lang_Iterable_com_google_appengine_api_datastore_Entity__).

The overload of prepare that takes a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) parameter behaves the same as the overloads of put, get, and delete that take a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) parameter. However, the overload of prepare that does not take a [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) parameter, unlike put, get, and delete, does not use an existing [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) if one is already running and does not consult the [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy) if one is not already running.

### [IDatastoreServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IDatastoreServiceFactory)

This interface should be implemented by providers of the [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) and registered with [com.google.appengine.spi.ServiceFactoryFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.spi.ServiceFactoryFactory).

### [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery)

Contains methods for fetching and returning entities from a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)). If the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) specified a sort order, [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) are returned in that order. Otherwise, the order is undefined.

A [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) does not cache results. Each use of [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) results in a new trip to the datastore.

### [QueryResultIterable<T>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterable)

A class that produces [QueryResultIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator)s.

### [QueryResultIterator<T>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator)

A class that iterates through the results of a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))

### [QueryResultList<T>](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultList)

A list of results returned by executing a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)).

### [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)

Describes a logical unit of work to be performed against the datastore. Operations performed as part of a single [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) succeed or fail as a unit. Transactions can be committed and rolled back synchronously and asynchronously.

## Enums 

### [CloudDatastoreRemoteServiceConfig.AppId.Location](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CloudDatastoreRemoteServiceConfig.AppId.Location)

Locations for App Engine applications.

### [CompositeIndexManager.IndexSource](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CompositeIndexManager.IndexSource)

The source of an index in the index file. These are used as literals in an xml document that we read and write.

### [DatastoreAttributes.DatastoreType](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreAttributes.DatastoreType)

Indicates the type of datastore being used. Currently always returns HIGH_REPLICATION.

### [DatastoreService.KeyRangeState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService.KeyRangeState)

Indicates the state of a [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange). See Also: [DatastoreService#allocateIdRange(KeyRange)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_allocateIdRange_com_google_appengine_api_datastore_KeyRange_)

### [IMHandle.Scheme](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.IMHandle.Scheme)

Supported IM schemes.

### [ImplicitTransactionManagementPolicy](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy)

Describes the various policies the datastore can follow for implicit transaction management. When deciding which policy to use, keep the following in mind: The datastore will automatically retry operations that fail due to concurrent updates to the same entity group if the operation is not part of a transaction. The datastore will not retry operations that fail due to concurrent updates to the same entity group if the operation is part of a transaction, and will instead immediately throw a ConcurrentModificationException. If your application needs to perform any sort of intelligent merging when concurrent attempts are made to update the same entity group you probably want [#AUTO](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy#com_google_appengine_api_datastore_ImplicitTransactionManagementPolicy_AUTO), otherwise [#NONE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ImplicitTransactionManagementPolicy#com_google_appengine_api_datastore_ImplicitTransactionManagementPolicy_NONE) is probably acceptable.

See [DatastoreService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService) for a list of operations that perform implicit transaction management.

### [Index.IndexState](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index.IndexState)

Indicates the state of the [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index).

### [Query.CompositeFilterOperator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.CompositeFilterOperator)

Operators supported by CompositeFilter.

### [Query.FilterOperator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.FilterOperator)

Operators supported by FilterPredicate.

### [Query.SortDirection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Query.SortDirection)

SortDirection controls the order of a sort.

### [ReadPolicy.Consistency](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ReadPolicy.Consistency)

Setting the `Consistency` for reads allows you to decide whether freshness or availability is more important.

### [TransactionOptions.Mode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.TransactionOptions.Mode)

The mode of the transaction.

## Exceptions 

### [CommittedButStillApplyingException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.CommittedButStillApplyingException)

`CommittedButStillApplyingException` is thrown when the write or transaction was committed, but some entities or index rows may not have been fully updated. Those updates should automatically be applied soon. You can roll them forward immediately by reading one of the entities inside a transaction.

### [DatastoreFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreFailureException)

`DatastoreFailureException` is thrown when any unknown error occurs while communicating with the data store.

Clients should not attempt to retry after receiving this exception.

### [DatastoreNeedIndexException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreNeedIndexException)

`DatastoreNeedIndexException` is thrown when no matching index was found for a query requiring an index. Check the Indexes page in the Admin Console and your datastore-indexes.xml file.

### [DatastoreTimeoutException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreTimeoutException)

`DatastoreTimeoutException` is thrown when a datastore operation times out. This can happen when you attempt to put, get, or delete too many entities or an entity with too many properties, or if the datastore is overloaded or having trouble.

### [EntityNotFoundException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EntityNotFoundException)

`EntityNotFoundException` is thrown when no `Entity` with the specified `Key` could be found.

### [PreparedQuery.TooManyResultsException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery.TooManyResultsException)

Indicates that too many results were found for [PreparedQuery#asSingleEntity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asSingleEntity_).

## Annotation Types 

### [PostDelete](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostDelete)

Identifies a callback method to be invoked after an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is deleted from the datastore. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostDelete#com_google_appengine_api_datastore_PostDelete_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [DeleteContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DeleteContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will **not** have any impact on the result of the datastore operation. Methods with this annotation will not be invoked if the datastore operation fails.

### [PostLoad](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostLoad)

Identifies a callback method to be invoked after an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is loaded from the datastore. This can happen as the result of a get() operation or a query. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostLoad#com_google_appengine_api_datastore_PostLoad_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [PostLoadContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostLoadContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will **not** have any impact on the result of the datastore operation. Methods with this annotation will not be invoked if the datastore operation fails.

### [PostPut](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostPut)

Identifies a callback method to be invoked after an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is written to the datastore. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PostPut#com_google_appengine_api_datastore_PostPut_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [PutContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PutContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will **not** have any impact on the result of the datastore operation. Methods with this annotation will not be invoked if the datastore operation fails.

### [PreDelete](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete)

Identifies a callback method to be invoked before an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is deleted from the datastore. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreDelete#com_google_appengine_api_datastore_PreDelete_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [DeleteContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DeleteContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will prevent the datastore operation from executing.

### [PreGet](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGet)

Identifies a callback method to be invoked before an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is fetched from the datastore via a get() rpc. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGet#com_google_appengine_api_datastore_PreGet_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [PreGetContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreGetContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will prevent the datastore operation from executing.

### [PrePut](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PrePut)

Identifies a callback method to be invoked before an [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) of any of the specified kinds is written to the datastore. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PrePut#com_google_appengine_api_datastore_PrePut_kinds__) is not provided the callback will execute for all kinds. Methods with this annotation must return `void`, must accept a single argument of type [PutContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PutContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will prevent the datastore operation from executing.

### [PreQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQuery)

Identifies a callback method to be invoked before a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) for any of the specified kinds is executed against the datastore. If [#kinds()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQuery#com_google_appengine_api_datastore_PreQuery_kinds__) is not provided the callback will execute for queries against all kinds, including kind-less queries. Methods with this annotation must return `void`, must accept a single argument of type [PreQueryContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreQueryContext), must not throw any checked exceptions, must not be static, and must belong to a class with a no-arg constructor. Neither the method nor the no-arg constructor of the class to which it belongs are required to be public. Methods with this annotation are free to throw any unchecked exception they like. Throwing an unchecked exception will prevent callbacks that have not yet been executed from running, and the exception will propagate to the code that invoked the datastore operation that resulted in the invocation of the callback. Throwing an unchecked exception from a callback will prevent the datastore operation from executing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
