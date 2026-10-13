---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer
title: Class PropertyContainer (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:05.177497+00:00
---

# Class PropertyContainer (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class PropertyContainer (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class PropertyContainer implements Serializable, Cloneable

A mutable property container.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PropertyContainer

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html), [Cloneable](https://docs.oracle.com/javase/8/docs/api/java/lang/Cloneable.html)

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

### appendPropertiesTo(StringBuilder builder)
    
    
    protected void appendPropertiesTo(StringBuilder builder)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[StringBuilder](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html)`  
  
  
### clone()
    
    
    protected Object clone()

**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)` |   
**Overrides**

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

### getProperties()
    
    
    public Map<String,@Nullable Object> getProperties()

Gets all of the properties belonging to this container.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)>` | an unmodifiable `Map` of properties.  
  
### getProperty(String propertyName)
    
    
    public @Nullable Object getProperty(String propertyName)

Gets the property with the specified name. The value returned may not be the same type as originally set via [#setProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setProperty_).

**Parameter**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)` | the property corresponding to `propertyName`.  
  
### hasProperty(String propertyName)
    
    
    public boolean hasProperty(String propertyName)

Returns true if a property has been set. If a property has been explicitly set to `null`, this function will return true.

**Parameter**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true iff the property named `propertyName` exists.  
  
### isUnindexedProperty(String propertyName)
    
    
    public boolean isUnindexedProperty(String propertyName)

Returns true if `propertyName` has a value that will not be indexed. This includes [Text](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Text), [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob), and any property added using [#setUnindexedProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setUnindexedProperty_).

Note: The behavior of this method is not well defined in case of an indexed property whose value is a list that contains unindexable values.

**Parameter**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### removeProperty(String propertyName)
    
    
    public void removeProperty(String propertyName)

Removes any property with the specified name. If there is no property with this name set, simply does nothing.

**Parameter**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### setIndexedProperty(String propertyName, Object value)
    
    
    public void setIndexedProperty(String propertyName, Object value)

Like {link #setProperty}, but requires that the value is indexable or a collection of indexable values.

**Parameters**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
  
### setPropertiesFrom(PropertyContainer src)
    
    
    public void setPropertiesFrom(PropertyContainer src)

A convenience method that populates properties from those in the given container.

This method transfers information about unindexed properties and clones any mutable values.

**Parameter**  
---  
**Name** | **Description**  
`src` | `[PropertyContainer](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer)`  
The container from which we will populate ourself.  
  
### setProperty(String propertyName, @Nullable Object value)
    
    
    public void setProperty(String propertyName, @Nullable Object value)

Sets the property named, `propertyName`, to `value`.

As the value is stored in the datastore, it is converted to the datastore's native type. This may include widening, such as converting a `Short` to a `Long`.

If value is a `Collection`, the values will be stored in the datastore with the collection's iteration order with one caveat: all indexed values will come before all unindexed values (this can occur if the `Collection` contains both values that are normally indexed like strings, and values that are never indexed like [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob), [Text](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Text) and [EmbeddedEntity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity)).

Overrides any existing value for this property, whether indexed or unindexed.

Note that [Blob](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Blob), [Text](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Text) and [EmbeddedEntity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.EmbeddedEntity) property values are never indexed. To store other types without being indexed, use [#setUnindexedProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setUnindexedProperty_). See Also: [#setUnindexedProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setUnindexedProperty_)

**Parameters**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
may be one of the supported datatypes or a heterogeneous `Collection` of one of the supported datatypes.  
  
### setUnindexedProperty(String propertyName, Object value)
    
    
    public void setUnindexedProperty(String propertyName, Object value)

Like `#setProperty`, but doesn't index the property in the built-in single property indexes or the user-defined composite indexes. See Also: [#setProperty](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PropertyContainer#com_google_appengine_api_datastore_PropertyContainer_setProperty_)

**Parameters**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
may be one of the supported datatypes, or a heterogeneous `Collection` of one of the supported datatypes. Overrides any existing value for this property, whether indexed or unindexed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
