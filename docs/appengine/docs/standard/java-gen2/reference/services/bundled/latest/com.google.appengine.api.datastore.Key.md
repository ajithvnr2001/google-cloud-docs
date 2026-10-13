---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key
title: Class Key (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:02.138560+00:00
---

# Class Key (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Key (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Key implements Serializable, Comparable<Key>

The primary key for a datastore entity.

A datastore GUID. A Key instance uniquely identifies an entity across all apps, and includes all information necessary to fetch the entity from the datastore with ` DatastoreService.get(Key)`.

You can create `Key` objects directly by using [KeyFactory#createKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_createKey_) or [#getChild](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key#com_google_appengine_api_datastore_Key_getChild_).

You can also retrieve the `Key` automatically created when you create a new [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity), or serialize `Key` objects, or use [KeyFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory) to convert them to and from websafe String values. See Also: [KeyFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Key

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html), [Comparable<Key>](https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable<com/google/appengine/api/datastore/Key>.html)

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

### compareTo(Key other)
    
    
    public int compareTo(Key other)

Compares two `Key` objects. The algorithm proceeds as follows: Turn each `Key` into an iterator where the first element returned is the top-most ancestor, the next element is the child of the previous element, and so on. The last element will be the `Key` we started with. Once we have assembled these two iterators (one for 'this' and one for the `Key` we're comparing to), consume them in parallel, comparing the next element from each iterator. If at any point the comparison of these two elements yields a non-zero result, return that as the result of the overall comparison. If we exhaust the iterator built from 'this' before we exhaust the iterator built from the other `Key`, we return less than. An example:

`app1.type1.4.app1.type2.9 < app1.type1.4.app1.type2.9.app1.type3.2`

If we exhaust the iterator built from the other `Key` before we exhaust the iterator built from 'this', we return greater than. An example:

`app1.type1.4.app1.type2.9.app1.type3.2 > app1.type1.4.app1.type2.9`

The relationship between individual `Key Keys` is performed by comparing app followed by kind followed by id. If both keys are assigned names rather than ids, compares names instead of ids. If neither key has an id or a name we return an arbitrary but consistent result. Assuming all other components are equal, all ids are less than all names.

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### equals(@Nullable Object object)
    
    
    public boolean equals(@Nullable Object object)

Compares two `Key` objects by comparing ids, kinds, parent and appIdNamespace. If both keys are assigned names rather than ids, compares names instead of ids. If neither key has an id or a name, the keys are only equal if they reference the same object.

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

Returns the appId for this [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getChild(String kind, String name)
    
    
    public Key getChild(String kind, String name)

Creates a new key having `this` as parent and the given name. The parent key must be complete.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the child key to create  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the key in `kind`, as an arbitrary string unique for this parent  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### getChild(String kind, long id)
    
    
    public Key getChild(String kind, long id)

Creates a new key having `this` as parent and the given numeric identifier. The parent key must be complete.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the child key to create  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the numeric identifier of the key in `kind`, unique for this parent  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### getId()
    
    
    public long getId()

Returns the numeric identifier of this `Key`.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getKind()
    
    
    public String getKind()

Returns the kind of the `Entity` represented by this `Key`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public @Nullable String getName()

Returns the name of this `Key`.

**Returns**  
---  
**Type** | **Description**  
`[Nullable String](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20String.html)` |   
  
### getNamespace()
    
    
    public String getNamespace()

Returns the namespace for this [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key).

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getParent()
    
    
    public @Nullable Key getParent()

If this `Key` has a parent, return a `Key` that represents it. If not, simply return null.

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

### isComplete()
    
    
    public boolean isComplete()

Returns true if this Key has a name specified or has been assigned an identifier.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
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
