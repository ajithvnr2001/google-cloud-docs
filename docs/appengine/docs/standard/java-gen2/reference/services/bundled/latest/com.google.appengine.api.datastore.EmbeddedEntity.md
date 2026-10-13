---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity
title: Class EmbeddedEntity (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:56.339290+00:00
---

# Class EmbeddedEntity (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class EmbeddedEntity (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class EmbeddedEntity extends PropertyContainer

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
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [PropertyContainer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer) > EmbeddedEntity

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

## Constructors 

### EmbeddedEntity()
    
    
    public EmbeddedEntity()

## Methods 

### clone()
    
    
    public EmbeddedEntity clone()

**Returns**  
---  
**Type** | **Description**  
`[EmbeddedEntity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity)` |   
**Overrides**

[PropertyContainer.clone()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_clone__)

### equals(@Nullable Object obj)
    
    
    public boolean equals(@Nullable Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getKey()
    
    
    public @Nullable Key getKey()

Returns the key or `null`.

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

### setKey(@Nullable Key key)
    
    
    public void setKey(@Nullable Key key)

**Parameter**  
---  
**Name** | **Description**  
`key` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
the key to set  
  
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
