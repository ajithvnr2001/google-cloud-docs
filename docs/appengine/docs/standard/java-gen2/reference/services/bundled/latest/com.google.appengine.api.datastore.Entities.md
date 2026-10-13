---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entities
title: Class Entities (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:56.683532+00:00
---

# Class Entities (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entities

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Entities (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Entities

Utility functions and constants for entities.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Entities

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

### ENTITY_GROUP_METADATA_ID
    
    
    public static final long ENTITY_GROUP_METADATA_ID

ID for **entity_group** entities. See Also: [#ENTITY_GROUP_METADATA_KIND](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entities#com_google_appengine_api_datastore_Entities_ENTITY_GROUP_METADATA_KIND)

**Field Value**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ENTITY_GROUP_METADATA_KIND
    
    
    public static final String ENTITY_GROUP_METADATA_KIND

A metadata kind that can be used to get information about entity groups. The metadata for the entity group with root entity key R is fetched using a [DatastoreService#get](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreService#com_google_appengine_api_datastore_DatastoreService_get_) call on key `KeyFactory.createKey(R, ENTITY_GROUP_METADATA_KIND, ENTITY_GROUP_METADATA_ID)`.

The resulting entity has a [Entity#VERSION_RESERVED_PROPERTY](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity#com_google_appengine_api_datastore_Entity_VERSION_RESERVED_PROPERTY) numeric property whose value is guaranteed to increase on every change to the entity group. This value may also occasionally increase without any user-visible change to the entity group.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### KIND_METADATA_KIND
    
    
    public static final String KIND_METADATA_KIND

A metadata kind that can be used to query for kinds that exist in the datastore.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### NAMESPACE_METADATA_EMPTY_ID
    
    
    public static final long NAMESPACE_METADATA_EMPTY_ID

The numeric ID for **namespace** keys representing the empty namespace.

**Field Value**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NAMESPACE_METADATA_KIND
    
    
    public static final String NAMESPACE_METADATA_KIND

A metadata kind that can be used to query for namespaces that exist in the datastore.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### PROPERTY_METADATA_KIND
    
    
    public static final String PROPERTY_METADATA_KIND

A metadata kind that can be used to query for properties that exist in the datastore.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### createEntityGroupKey(Key key)
    
    
    public static Key createEntityGroupKey(Key key)

Create an **entity_group** key for the entity group containing `key`.

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
Key of any entity in the entity group.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` | **entity_group** key.  
  
### createKindKey(String kind)
    
    
    public static Key createKindKey(String kind)

Create a **kind** key for `kind`.

**Parameter**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Kind to create key for.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` | **kind** key.  
  
### createNamespaceKey(String namespace)
    
    
    public static Key createNamespaceKey(String namespace)

Create a **namespace** key for `namespace`.

**Parameter**  
---  
**Name** | **Description**  
`namespace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Namespace to create key for.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` | **namespace** key.  
  
### createPropertyKey(String kind, String property)
    
    
    public static Key createPropertyKey(String kind, String property)

Create a **property** key for `property` of `kind`.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Kind to create key for.  
`property` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Property to create key for.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` | **property** key.  
  
### getNamespaceFromNamespaceKey(Key namespaceKey)
    
    
    public static @Nullable String getNamespaceFromNamespaceKey(Key namespaceKey)

Extract the namespace name from a **namespace** key.

**Parameter**  
---  
**Name** | **Description**  
`namespaceKey` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
Key to extract namespace from.  
**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` | The namespace name.  
  
### getVersionProperty(Entity entity)
    
    
    public static long getVersionProperty(Entity entity)

Get the value of the **version** property from `entity`.

**Parameter**  
---  
**Name** | **Description**  
`entity` | `[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)`  
Entity to fetch **version** from (must have a numeric **version** property).  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | **version** property value.  
  
## Constructors 

### Entities()
    
    
    public Entities()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
