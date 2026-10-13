---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeUtils
title: Class DataTypeUtils (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:53.425661+00:00
---

# Class DataTypeUtils (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DataTypeUtils

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DataTypeUtils (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class DataTypeUtils

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



## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataTypeUtils

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

## Static Fields 

### MAX_LINK_PROPERTY_LENGTH
    
    
    public static final int MAX_LINK_PROPERTY_LENGTH

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAX_SHORT_BLOB_PROPERTY_LENGTH
    
    
    public static final int MAX_SHORT_BLOB_PROPERTY_LENGTH

This is the maximum number of bytes that a `ShortBlob` property can contain. If your data is larger, you need to use a `Blob`.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAX_STRING_PROPERTY_LENGTH
    
    
    public static final int MAX_STRING_PROPERTY_LENGTH

This is the maximum number of bytes that a string property can contain. If your string has more bytes, you need to wrap it in a [Text](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Text).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### checkSupportedValue(@Nullable String name, @Nullable Object value)
    
    
    public static void checkSupportedValue(@Nullable String name, @Nullable Object value)

If the specified object cannot be used as the value for a `Entity` property, throw an exception with the appropriate explanation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)`  
  
`value` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
  
### checkSupportedValue(Object value)
    
    
    public static void checkSupportedValue(Object value)

If the specified object cannot be used as the value for a `Entity` property, throw an exception with the appropriate explanation.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
  
### getSupportedTypes()
    
    
    public static Set<Class<?>> getSupportedTypes()

Returns an unmodifiable `Set` of supported `Class` objects.

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>>` |   
  
### isSupportedType(Class<?> clazz)
    
    
    public static boolean isSupportedType(Class<?> clazz)

Returns true if and only if the supplied `Class` can be stored in the data store.

**Parameter**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isUnindexableType(Class<?> clazz)
    
    
    public static boolean isUnindexableType(Class<?> clazz)

Returns true if the supplied `Class` cannot be indexed.

**Parameter**  
---  
**Name** | **Description**  
`clazz` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
