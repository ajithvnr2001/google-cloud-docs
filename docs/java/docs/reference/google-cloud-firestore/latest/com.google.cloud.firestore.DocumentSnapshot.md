---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.DocumentSnapshot
title: Class DocumentSnapshot (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:55.694652+00:00
---

# Class DocumentSnapshot (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.DocumentSnapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DocumentSnapshot (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public class DocumentSnapshot

A DocumentSnapshot contains data read from a document in a Firestore database. The data can be extracted with the [#getData()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.DocumentSnapshot#com_google_cloud_firestore_DocumentSnapshot_getData__) or [#get(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.DocumentSnapshot#com_google_cloud_firestore_DocumentSnapshot_get_java_lang_String_) methods.

If the DocumentSnapshot points to a non-existing document, getData() and its corresponding methods will return null. You can always explicitly check for a document's existence by calling [#exists()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.DocumentSnapshot#com_google_cloud_firestore_DocumentSnapshot_exists__).

**Subclassing Note** : Firestore classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DocumentSnapshot

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

## Methods 

### <T>get(FieldPath fieldPath, Class<T> valueType)
    
    
    public T <T>get(FieldPath fieldPath, Class<T> valueType)

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

**Parameters**  
---  
**Name** | **Description**  
`fieldPath` | `[FieldPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FieldPath)`  
The path to the field  
`valueType` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<T>`  
The Java class to convert the field value to.  
**Returns**  
---  
**Type** | **Description**  
`T` | The value at the given field or null.  
  
### <T>get(String field, Class<T> valueType)
    
    
    public T <T>get(String field, Class<T> valueType)

Returns the value at the field, converted to a POJO, or null if the field or document doesn't exist.

**Parameters**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field  
`valueType` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<T>`  
The Java class to convert the field value to.  
**Returns**  
---  
**Type** | **Description**  
`T` | The value at the given field or null.  
  
### <T>toObject(Class<T> valueType)
    
    
    public T <T>toObject(Class<T> valueType)

Returns the contents of the document converted to a POJO or null if the document doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`valueType` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<T>`  
The Java class to create  
**Returns**  
---  
**Type** | **Description**  
`T` | The contents of the document in an object of type T or null if the document doesn't exist.  
  
### contains(FieldPath fieldPath)
    
    
    public boolean contains(FieldPath fieldPath)

Returns whether or not the field exists in the document. Returns false if the document does not exist.

**Parameter**  
---  
**Name** | **Description**  
`fieldPath` | `[FieldPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FieldPath)`  
the path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true iff the field exists.  
  
### contains(String field)
    
    
    public boolean contains(String field)

Returns whether or not the field exists in the document. Returns false if the document does not exist.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true iff the field exists.  
  
### equals(Object obj)
    
    
    public boolean equals(Object obj)

Returns true if the document's data and path in this DocumentSnapshot equals the provided snapshot.

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
The object to compare against.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether this DocumentSnapshot is equal to the provided object.  
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### exists()
    
    
    public boolean exists()

Returns whether or not the field exists in the document. Returns false if the document does not exist.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | whether the document existed in this snapshot.  
  
### get(FieldPath fieldPath)
    
    
    public Object get(FieldPath fieldPath)

Returns the value at the field or null if the field doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`fieldPath` | `[FieldPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.FieldPath)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)` | The value at the given field or null.  
  
### get(String field)
    
    
    public Object get(String field)

Returns the value at the field or null if the field doesn't exist.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)` | The value at the given field or null.  
  
### getBlob(String field)
    
    
    public Blob getBlob(String field)

Returns the value of the field as a Blob.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Blob)` | The value of the field.  
  
### getBoolean(String field)
    
    
    public Boolean getBoolean(String field)

Returns the value of the field as a boolean.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` | The value of the field.  
  
### getBsonObjectId(String field)
    
    
    public BsonObjectId getBsonObjectId(String field)

Returns the value of the field as a BsonObjectId.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[BsonObjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.BsonObjectId)` | The value of the field.  
  
### getBsonTimestamp(String field)
    
    
    public BsonTimestamp getBsonTimestamp(String field)

Returns the value of the field as a BsonTimestamp.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[BsonTimestamp](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.BsonTimestamp)` | The value of the field.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Returns the time at which this document was created. Returns null for non-existing documents.

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Timestamp` | The last time the document in the snapshot was created. Null if the document doesn't exist.  
  
### getData()
    
    
    public Map<String,Object> getData()

Returns the fields of the document as a Map or null if the document doesn't exist. Field values will be converted to their native Java representation.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)>` | The fields of the document as a Map or null if the document doesn't exist.  
  
### getDate(String field)
    
    
    public Date getDate(String field)

Returns the value of the field as a Date.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` | The value of the field.  
  
### getDecimal128Value(String field)
    
    
    public Decimal128Value getDecimal128Value(String field)

Returns the value of the field as a 128-bit decimal.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Decimal128Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Decimal128Value)` | The value of the field.  
  
### getDouble(String field)
    
    
    public Double getDouble(String field)

Returns the value of the field as a double.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)` | The value of the field.  
  
### getGeoPoint(String field)
    
    
    public GeoPoint getGeoPoint(String field)

Returns the value of the field as a GeoPoint.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[GeoPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.GeoPoint)` | The value of the field.  
  
### getId()
    
    
    public String getId()

Returns the ID of the document contained in this snapshot.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id of the document.  
  
### getInt32Value(String field)
    
    
    public Int32Value getInt32Value(String field)

Returns the value of the field as a 32-bit integer.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Int32Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Int32Value)` | The value of the field.  
  
### getLong(String field)
    
    
    public Long getLong(String field)

Returns the value of the field as a long.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` | The value of the field.  
  
### getMaxKey(String field)
    
    
    public MaxKey getMaxKey(String field)

Returns the value of the field as a MaxKey.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[MaxKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.MaxKey)` | The value of the field.  
  
### getMinKey(String field)
    
    
    public MinKey getMinKey(String field)

Returns the value of the field as a MinKey.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[MinKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.MinKey)` | The value of the field.  
  
### getReadTime()
    
    
    public Timestamp getReadTime()

Returns the time at which this snapshot was read.

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Timestamp` | The read time of this snapshot.  
  
### getReference()
    
    
    public DocumentReference getReference()

Gets the reference to the document.

**Returns**  
---  
**Type** | **Description**  
`[DocumentReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.DocumentReference)` | The reference to the document.  
  
### getRegexValue(String field)
    
    
    public RegexValue getRegexValue(String field)

Returns the value of the field as a RegexValue.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[RegexValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.RegexValue)` | The value of the field.  
  
### getString(String field)
    
    
    public String getString(String field)

Returns the value of the field as a String.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The value of the field.  
  
### getTimestamp(String field)
    
    
    public Timestamp getTimestamp(String field)

Returns the value of the field as a Timestamp.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Timestamp` | The value of the field.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Returns the time at which this document was last updated. Returns null for non-existing documents.

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Timestamp` | The last time the document in the snapshot was updated. Null if the document doesn't exist.  
  
### getVectorValue(String field)
    
    
    public VectorValue getVectorValue(String field)

Returns the value of the field as a VectorValue.

**Parameter**  
---  
**Name** | **Description**  
`field` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The path to the field.  
**Returns**  
---  
**Type** | **Description**  
`[VectorValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.VectorValue)` | The value of the field.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

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

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
