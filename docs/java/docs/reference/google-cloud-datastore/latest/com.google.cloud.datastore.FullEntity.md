---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity
title: Class FullEntity<K> (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:13.167380+00:00
---

# Class FullEntity<K> (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FullEntity<K> (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public class FullEntity<K> extends BaseEntity<K>

A full entity is a [BaseEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity) that holds all the properties associated with a Datastore entity (as opposed to [ProjectionEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.ProjectionEntity)).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [BaseEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity) > FullEntity<K>

## Inherited Members

[BaseEntity.<K>getEntity(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity__K_getEntity_java_lang_String_)

[BaseEntity.<T>getList(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity__T_getList_java_lang_String_)

[BaseEntity.<V>getValue(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity__V_getValue_java_lang_String_)

[BaseEntity.contains(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_contains_java_lang_String_)

[BaseEntity.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_equals_java_lang_Object_)

[BaseEntity.getBlob(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getBlob_java_lang_String_)

[BaseEntity.getBoolean(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getBoolean_java_lang_String_)

[BaseEntity.getDouble(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getDouble_java_lang_String_)

[BaseEntity.getKey()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getKey__)

[BaseEntity.getKey(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getKey_java_lang_String_)

[BaseEntity.getLatLng(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getLatLng_java_lang_String_)

[BaseEntity.getLong(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getLong_java_lang_String_)

[BaseEntity.getNames()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getNames__)

[BaseEntity.getProperties()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getProperties__)

[BaseEntity.getString(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getString_java_lang_String_)

[BaseEntity.getTimestamp(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_getTimestamp_java_lang_String_)

[BaseEntity.hasKey()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_hasKey__)

[BaseEntity.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_hashCode__)

[BaseEntity.isNull(String)](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_isNull_java_lang_String_)

[BaseEntity.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.BaseEntity#com_google_cloud_datastore_BaseEntity_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Type Parameter  
  
---  
**Name** | **Description**  
`K` |   
  
## Static Methods 

### <K>newBuilder(K key)
    
    
    public static FullEntity.Builder<K> <K>newBuilder(K key)

**Parameter**  
---  
**Name** | **Description**  
`key` | `K`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity.Builder)<K>` |   
  
### <K>newBuilder(FullEntity<K> copyFrom)
    
    
    public static FullEntity.Builder<K> <K>newBuilder(FullEntity<K> copyFrom)

**Parameter**  
---  
**Name** | **Description**  
`copyFrom` | `[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity)<K>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity.Builder)<K>` |   
  
### fromPb(Entity entityPb)
    
    
    public static FullEntity<?> fromPb(Entity entityPb)

**Parameter**  
---  
**Name** | **Description**  
`entityPb` | `[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.Entity)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FullEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity)<?>` |   
  
### newBuilder()
    
    
    public static FullEntity.Builder<IncompleteKey> newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.FullEntity.Builder)<[IncompleteKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.cloud.datastore.IncompleteKey)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
