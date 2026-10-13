---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity
title: Class Entity (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:57.093735+00:00
---

# Class Entity (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Entity (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Entity extends PropertyContainer implements Cloneable

`Entity` is the fundamental unit of data storage. It has an immutable identifier (contained in the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)) object, a reference to an optional parent `Entity`, a kind (represented as an arbitrary string), and a set of zero or more typed properties.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [PropertyContainer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer) > Entity

## Implements

[Cloneable](https://docs.oracle.com/javase/8/docs/api/java/lang/Cloneable.html)

## Inherited Members

[PropertyContainer.appendPropertiesTo(StringBuilder)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_appendPropertiesTo_java_lang_StringBuilder_)

[PropertyContainer.clone()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_clone__)

[PropertyContainer.getProperties()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_getProperties__)

[PropertyContainer.getProperty(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_getProperty_java_lang_String_)

[PropertyContainer.hasProperty(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_hasProperty_java_lang_String_)

[PropertyContainer.isUnindexedProperty(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_isUnindexedProperty_java_lang_String_)

[PropertyContainer.removeProperty(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_removeProperty_java_lang_String_)

[PropertyContainer.setIndexedProperty(String,Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setIndexedProperty_java_lang_String_java_lang_Object_)

[PropertyContainer.setPropertiesFrom(PropertyContainer)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setPropertiesFrom_com_google_appengine_api_datastore_PropertyContainer_)

[PropertyContainer.setProperty(String,@Nullable Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setProperty_java_lang_String_java_lang__org_jspecify_annotations_Nullable_Object_)

[PropertyContainer.setUnindexedProperty(String,Object)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setUnindexedProperty_java_lang_String_java_lang_Object_)

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

## Static Fields 

### KEY_RESERVED_PROPERTY
    
    
    public static final String KEY_RESERVED_PROPERTY

A reserved property name used to refer to the key of the entity. This string can be used for filtering and sorting by the entity key itself.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### SCATTER_RESERVED_PROPERTY
    
    
    public static final String SCATTER_RESERVED_PROPERTY

A reserved property name used to refer to the scatter property of the entity. Used for finding split points (e.g. for mapping over a kind).

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### VERSION_RESERVED_PROPERTY
    
    
    public static final String VERSION_RESERVED_PROPERTY

A reserved property name used to report an entity group's version.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Constructors 

### Entity(Key key)
    
    
    public Entity(Key key)

Create a new `Entity` uniquely identified by the provided [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key). Creating an entity for the purpose of insertion (as opposed to update) with a key that has its `id` field set is strongly discouraged unless the key was returned by a [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange). See Also: [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange)

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
  
### Entity(String kind)
    
    
    public Entity(String kind)

Create a new `Entity` with the specified kind and no parent `Entity`. The instantiated `Entity` will have an incomplete [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) when this constructor returns. The [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) will remain incomplete until you put the `Entity`, after which time the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) will have its `id` set.

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### Entity(String kind, @Nullable Key parent)
    
    
    public Entity(String kind, @Nullable Key parent)

Create a new `Entity` with the specified kind and parent `Entity`. The instantiated `Entity` will have an incomplete [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) when this constructor returns. The [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) will remain incomplete until you put the `Entity`, after which time the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) will have its `id` set.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`parent` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
  
  
### Entity(String kind, String keyName)
    
    
    public Entity(String kind, String keyName)

Create a new `Entity` with the specified kind and key name and no parent `Entity`. The instantiated `Entity` will have a complete [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) when this constructor returns. The [Key's](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) `name` field will be set to the value of `keyName`.

This constructor is syntactic sugar for `new Entity(KeyFactory.createKey(kind, keyName))`.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`keyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### Entity(String kind, String keyName, Key parent)
    
    
    public Entity(String kind, String keyName, Key parent)

Create a new `Entity` with the specified kind, key name, and parent `Entity`. The instantiated `Entity` will have a complete [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) when this constructor returns. The [Key's](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) `name` field will be set to the value of `keyName`.

This constructor is syntactic sugar for `new Entity(KeyFactory.createKey(parent, kind, keyName))`.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`keyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`parent` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
  
### Entity(String kind, long id)
    
    
    public Entity(String kind, long id)

Create a new `Entity` with the specified kind and ID and no parent `Entity`. The instantiated `Entity` will have a complete [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) when this constructor returns. The [Key's](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) `id` field will be set to the value of `id`.

Creating an entity for the purpose of insertion (as opposed to update) with this constructor is discouraged unless the id was obtained from a key returned by a [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange) obtained from [AsyncDatastoreService#allocateIds(String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_allocateIds_java_lang_String_long_) or [DatastoreService#allocateIds(String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_allocateIds_java_lang_String_long_) for the same kind.

This constructor is syntactic sugar for `new Entity(KeyFactory.createKey(kind, id))`.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### Entity(String kind, long id, Key parent)
    
    
    public Entity(String kind, long id, Key parent)

Create a new `Entity` with the specified kind and ID and parent `Entity`. The instantiated `Entity` will have a complete [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) when this constructor returns. The [Key's](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) `id` field will be set to the value of `id`.

Creating an entity for the purpose of insertion (as opposed to update) with this constructor is discouraged unless the id was obtained from a key returned by a [KeyRange](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyRange) obtained from [AsyncDatastoreService#allocateIds(Key, String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.AsyncDatastoreService#com_google_appengine_api_datastore_AsyncDatastoreService_allocateIds_) or [DatastoreService#allocateIds(Key, String, long)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_allocateIds_com_google_appengine_api_datastore_Key_java_lang_String_long_) for the same parent and kind.

This constructor is syntactic sugar for `new Entity(KeyFactory.createKey(parent, kind, id))`.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`parent` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
  
## Methods 

### clone()
    
    
    public Entity clone()

Returns a shallow copy of this `Entity` instance. `Collection` properties are cloned as an `ArrayList`, the type returned from the datastore. Instances of mutable datastore types are cloned as well. Instances of all other types are reused.

**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)` | a shallow copy of this `Entity`  
**Overrides**

[PropertyContainer.clone()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_clone__)

### equals(@Nullable Object object)
    
    
    public boolean equals(@Nullable Object object)

Two `Entity` objects are considered equal if they refer to the same entity (i.e. their `Key` objects match).

**Parameter**  
---  
**Name** | **Description**  
`object` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAppId()
    
    
    public String getAppId()

Returns the identifier of the application that owns this `Entity`. This is simply a convenience method that forwards to the `Key` for this `Entity`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getKey()
    
    
    public Key getKey()

Returns the `Key` that represents this `Entity`. If the entity has not yet been saved (e.g. via `DatastoreService.put`), this `Key` will not be fully specified and cannot be used for certain operations (like `DatastoreService.get`). Once the ` Entity` has been saved, its `Key` will be updated to be fully specified.

**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### getKind()
    
    
    public String getKind()

Returns a logical type that is associated with this `Entity`. This is simply a convenience method that forwards to the `Key` for this `Entity`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getNamespace()
    
    
    public String getNamespace()

Returns the namespace of the application/namespace that owns this `Entity`. This is simply a convenience method that forwards to the `Key` for this `Entity`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getParent()
    
    
    public @Nullable Key getParent()

Get a `Key` that corresponds to this the parent `Entity` of this `Entity`. This is simply a convenience method that forwards to the `Key` for this `Entity`.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### setPropertiesFrom(Entity src)
    
    
    public void setPropertiesFrom(Entity src)

**Parameter**  
---  
**Name** | **Description**  
`src` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
  
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
