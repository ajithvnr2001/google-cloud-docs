---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeTranslator
title: Class DataTypeTranslator (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:53.783417+00:00
---

# Class DataTypeTranslator (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeTranslator

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DataTypeTranslator (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class DataTypeTranslator

`DataTypeTranslator` is a utility class for converting between the data store's ` Property` protocol buffers and the user-facing classes (`String`, `User`, etc.).

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataTypeTranslator

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

### addPropertiesToPb(Map<String,?> map, OnestoreEntity.EntityProto.Builder proto)
    
    
    public static void addPropertiesToPb(Map<String,?> map, OnestoreEntity.EntityProto.Builder proto)

Add all of the properties in the specified map to an `EntityProto`. This involves determining the type of each property and creating the proper type-specific protocol buffer.

If the property value is an UnindexedValue, or if it's a type that is never indexed, e.g. `Text` and `Blob`, it's added to `EntityProto.raw_property`. Otherwise it's added to `EntityProto.property`.

**Parameters**  
---  
**Name** | **Description**  
`map` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),?>`  
A not `null` map of all the properties which will be set on `proto`  
`proto` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.EntityProto.Builder`  
A not `null` protocol buffer  
  
### extractImplicitPropertiesFromPb(OnestoreEntity.EntityProto proto, Map<String,@Nullable Object> map)
    
    
    public static void extractImplicitPropertiesFromPb(OnestoreEntity.EntityProto proto, Map<String,@Nullable Object> map)

Copy all of the implicit properties present on `proto` into `map`.

**Parameters**  
---  
**Name** | **Description**  
`proto` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.EntityProto`  
  
`map` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)>`  
  
  
### extractIndexedPropertiesFromPb(OnestoreEntity.EntityProto proto, Map<String,@Nullable Object> map)
    
    
    public static void extractIndexedPropertiesFromPb(OnestoreEntity.EntityProto proto, Map<String,@Nullable Object> map)

Copy all of the indexed properties present on `proto` into `map`.

**Parameters**  
---  
**Name** | **Description**  
`proto` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.EntityProto`  
  
`map` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)>`  
  
  
### extractPropertiesFromPb(OnestoreEntity.EntityProto proto, Map<String,@Nullable Object> map)
    
    
    public static void extractPropertiesFromPb(OnestoreEntity.EntityProto proto, Map<String,@Nullable Object> map)

Copy all of the properties present on `proto` into `map`.

**Parameters**  
---  
**Name** | **Description**  
`proto` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.EntityProto`  
  
`map` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)>`  
  
  
### findIndexedPropertiesOnPb(OnestoreEntity.EntityProto proto, String propertyName)
    
    
    public static Collection<OnestoreEntity.Property> findIndexedPropertiesOnPb(OnestoreEntity.EntityProto proto, String propertyName)

Locates and returns all indexed properties with the given name on the given proto. If there are a mix of matching multiple and non-multiple properties, the collection will contain the first non-multiple property.

**Parameters**  
---  
**Name** | **Description**  
`proto` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.EntityProto`  
  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Property>` | A list, potentially empty, containing matching properties.  
  
### getComparablePropertyValue(OnestoreEntity.Property property)
    
    
    public static @Nullable Comparable<Object> getComparablePropertyValue(OnestoreEntity.Property property)

Returns the value for the property as its comparable representation type.

**Parameter**  
---  
**Name** | **Description**  
`property` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Property`  
a not `null` property  
**Returns**  
---  
**Type** | **Description**  
`[Nullable Comparable](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Comparable.html)<[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>` | `null` if no value was set for `property`  
  
### getPropertyValue(OnestoreEntity.Property property)
    
    
    public static @Nullable Object getPropertyValue(OnestoreEntity.Property property)

Returns the value for the property as its canonical type.

**Parameter**  
---  
**Name** | **Description**  
`property` | `com.google.storage.onestore.v3_bytes.proto2api.OnestoreEntity.Property`  
a not `null` property  
**Returns**  
---  
**Type** | **Description**  
`[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)` | `null` if no value was set for `property`  
  
### getTypeRank(Class<? extends Comparable> datastoreType)
    
    
    public static int getTypeRank(Class<? extends Comparable> datastoreType)

Get the rank of the given datastore type relative to other datastore types. Note that datastore types do not necessarily have unique ranks.

**Parameter**  
---  
**Name** | **Description**  
`datastoreType` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<? extends java.lang.Comparable>`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### toEntityFromSerializedV1Proto(byte[] serializedV1Entity)
    
    
    public static Entity toEntityFromSerializedV1Proto(byte[] serializedV1Entity)

Deserializes a Cloud Datastore V1 `Entity` protobuf and converts it to an App Engine Datastore `Entity`. `serializedV1Entity` should be an output of [#toSerializedV1Proto](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeTranslator#com_google_appengine_api_datastore_DataTypeTranslator_toSerializedV1Proto_); no guarantees for other inputs.

**Parameter**  
---  
**Name** | **Description**  
`serializedV1Entity` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)` |   
  
### toSerializedV1Proto(Entity entity)
    
    
    public static byte[] toSerializedV1Proto(Entity entity)

Converts an App Engine Datastore `Entity` to a Cloud Datastore `Entity` V1 protobuf and serializes it.

Note that the conversion may be lossy or fail; for example, the Cloud Datastore V1 API supports only UTF-8 strings, so App Engine Datastore entities with string properties that are not UTF-8 encoded may behave in unexpected ways if supplied to Cloud Datastore. You can verify that the conversion was successful for entity `x` by checking ` x.equals(toEntityFromSerializedV1Proto(toSerializedV1Proto(x))`.

**Parameter**  
---  
**Name** | **Description**  
`entity` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
