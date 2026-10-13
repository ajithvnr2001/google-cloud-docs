---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity.Builder
title: Class BaseEntity.Builder<K,B> (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:01.499590+00:00
---

# Class BaseEntity.Builder<K,B> (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BaseEntity.Builder<K,B> (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public abstract static class BaseEntity.Builder<K,B>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BaseEntity.Builder<K,B>

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

## Type Parameters  
  
---  
**Name** | **Description**  
`K` |   
`B` |   
  
## Methods 

### build()
    
    
    public abstract BaseEntity<K> build()

**Returns**  
---  
**Type** | **Description**  
`[BaseEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity)<K>` |   
  
### clear()
    
    
    public B clear()

Clears all the properties.

**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### key()
    
    
    protected K key()

**Returns**  
---  
**Type** | **Description**  
`K` |   
  
### remove(String name)
    
    
    public B remove(String name)

Removes a property with the given `name`.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, boolean value)
    
    
    public B set(String name, boolean value)

Sets a property of type [BooleanValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BooleanValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, boolean first, boolean second, boolean[] others)
    
    
    public B set(String name, boolean first, boolean second, boolean[] others)

Sets a list property containing elements of type [BooleanValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BooleanValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the first boolean in the list  
`second` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the second boolean in the list  
`others` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
other booleans in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Timestamp value)
    
    
    public B set(String name, Timestamp value)

Sets a property of type [TimestampValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.TimestampValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `com.google.cloud.Timestamp`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Timestamp first, Timestamp second, Timestamp[] others)
    
    
    public B set(String name, Timestamp first, Timestamp second, Timestamp[] others)

Sets a list property containing elements of type [TimestampValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.TimestampValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `com.google.cloud.Timestamp`  
the first Timestamp in the list  
`second` | `com.google.cloud.Timestamp`  
the second Timestamp in the list  
`others` | `com.google.cloud.Timestamp[]`  
other Timestamps in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Blob value)
    
    
    public B set(String name, Blob value)

Sets a property of type [BlobValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BlobValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Blob first, Blob second, Blob[] others)
    
    
    public B set(String name, Blob first, Blob second, Blob[] others)

Sets a list property containing elements of type [BlobValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BlobValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob)`  
the first [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob) in the list  
`second` | `[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob)`  
the second [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob) in the list  
`others` | `[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob)[]`  
other [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Blob)s in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, FullEntity<?> value)
    
    
    public B set(String name, FullEntity<?> value)

Sets a property of type [EntityValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.EntityValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity)<?>`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, FullEntity<?> first, FullEntity<?> second, FullEntity<?>[] others)
    
    
    public B set(String name, FullEntity<?> first, FullEntity<?> second, FullEntity<?>[] others)

Sets a list property containing elements of type [EntityValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.EntityValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity)<?>`  
the first [FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity) in the list  
`second` | `[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity)<?>`  
the second [FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity) in the list  
`others` | `[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity)<?>[]`  
other entities in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Key value)
    
    
    public B set(String name, Key value)

Sets a property of type [KeyValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.KeyValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Key first, Key second, Key[] others)
    
    
    public B set(String name, Key first, Key second, Key[] others)

Sets a list property containing elements of type [KeyValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.KeyValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key)`  
the first [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key) in the list  
`second` | `[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key)`  
the second [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key) in the list  
`others` | `[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key)[]`  
other [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Key)s in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, LatLng value)
    
    
    public B set(String name, LatLng value)

Sets a property of type [LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, LatLng first, LatLng second, LatLng[] others)
    
    
    public B set(String name, LatLng first, LatLng second, LatLng[] others)

Sets a list property containing elements of type [LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng)`  
the first [LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng) in the list  
`second` | `[LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng)`  
the second [LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng) in the list  
`others` | `[LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng)[]`  
other [LatLng](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LatLng)s in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Value<?> value)
    
    
    public B set(String name, Value<?> value)

Sets a property.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Value)<?>`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, Value<?> first, Value<?> second, Value<?>[] others)
    
    
    public B set(String name, Value<?> first, Value<?> second, Value<?>[] others)

Sets a property of type [ListValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.ListValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Value)<?>`  
the first value in the list  
`second` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Value)<?>`  
the second value in the list  
`others` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Value)<?>[]`  
other values in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, double value)
    
    
    public B set(String name, double value)

Sets a property of type [DoubleValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DoubleValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, double first, double second, double[] others)
    
    
    public B set(String name, double first, double second, double[] others)

Sets a list property containing elements of type [DoubleValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.DoubleValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the first double in the list  
`second` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the second double in the list  
`others` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
other doubles in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, String value)
    
    
    public B set(String name, String value)

Sets a property of type [StringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StringValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, String first, String second, String[] others)
    
    
    public B set(String name, String first, String second, String[] others)

Sets a list property containing elements of type [StringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.StringValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the first string in the list  
`second` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the second string in the list  
`others` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
other strings in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, List<? extends Value<?>> values)
    
    
    public B set(String name, List<? extends Value<?>> values)

Sets a property of type [ListValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.ListValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`values` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.datastore.Value<?>>`  
list of values associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, long value)
    
    
    public B set(String name, long value)

Sets a property of type [LongValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LongValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
value associated with the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### set(String name, long first, long second, long[] others)
    
    
    public B set(String name, long first, long second, long[] others)

Sets a list property containing elements of type [LongValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.LongValue).

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
`first` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the first long in the list  
`second` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the second long in the list  
`others` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[]`  
other longs in the list  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### setKey(K key)
    
    
    public B setKey(K key)

Sets the key for the entity.

**Parameter**  
---  
**Name** | **Description**  
`key` | `K`  
  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### setNull(String name)
    
    
    public B setNull(String name)

Sets a property of type `NullValue`.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the property  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
### setProperties()
    
    
    protected Map<String,Value<?>> setProperties()

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Value)<?>>` |   
  
### setProperties(Map<String,Value<?>> properties)
    
    
    protected B setProperties(Map<String,Value<?>> properties)

**Parameter**  
---  
**Name** | **Description**  
`properties` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.Value)<?>>`  
  
**Returns**  
---  
**Type** | **Description**  
`B` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
