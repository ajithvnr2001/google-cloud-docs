---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory
title: Class KeyFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:02.514988+00:00
---

# Class KeyFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class KeyFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class KeyFactory

This class enables direct creation of `Key` objects, both in the root entity group (no parent) and as the child of a given parent. Keys can also be created indirectly by putting named Entities into the datastore, which will allocate a new key. See Entity#Entity(String, String) for details.

This class also has methods for encoding and decoding `Key` objects to and from strings. Clients should not make any assumptions about the encoding format, except that it is a websafe string that does not need to be quoted when used in HTML or in URLs. See Also: [Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > KeyFactory

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

### createKey(@Nullable Key parent, String kind, String name)
    
    
    public static Key createKey(@Nullable Key parent, String kind, String name)

Creates a new `Key` with the provided parent from its kind and name.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
the parent of the key to create, can be `null`  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the key in `kind`, as an arbitrary string unique across all entities of this `kind` with the same parent  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### createKey(@Nullable Key parent, String kind, long id)
    
    
    public static Key createKey(@Nullable Key parent, String kind, long id)

Creates a new `Key` with the provided parent from its kind and ID.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
the parent of the key to create, can be `null`  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the numeric identifier of the key in `kind`, unique across all entities of this kind with the same parent, must not be zero  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### createKey(String kind, String name)
    
    
    public static Key createKey(String kind, String name)

Creates a new `Key` having no parent from its kind and name.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the key in `kind`, as an arbitrary string unique across all root entities of this `kind`  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### createKey(String kind, long id)
    
    
    public static Key createKey(String kind, long id)

Creates a new `Key` having no parent from its kind and ID.

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the numeric identifier of the key in `kind`, unique across all root entities of this kind, must not be zero  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
### createKeyString(@Nullable Key parent, String kind, String name)
    
    
    public static String createKeyString(@Nullable Key parent, String kind, String name)

Shorthand for invoking [#keyToString(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_keyToString_com_google_appengine_api_datastore_Key_) on the result of #createKey(Key, String, String)

**Parameters**  
---  
**Name** | **Description**  
`parent` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
the parent of the key to create, can be `null`.  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the key in `kind`, as an arbitrary string unique across entities of this `kind` with the same parent  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A websafe `String` representation of the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that was created  
  
### createKeyString(@Nullable Key parent, String kind, long id)
    
    
    public static String createKeyString(@Nullable Key parent, String kind, long id)

Shorthand for invoking [#keyToString(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_keyToString_com_google_appengine_api_datastore_Key_) on the result of #createKey(Key, String, long)

**Parameters**  
---  
**Name** | **Description**  
`parent` | `com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Key`  
the parent of the key to create, can be `null`.  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the numeric identifier of the key in `kind`, unique across entities of this kind with the same parent, must not be zero  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A websafe `String` representation of the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that was created  
  
### createKeyString(String kind, String name)
    
    
    public static String createKeyString(String kind, String name)

Shorthand for invoking [#keyToString(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_keyToString_com_google_appengine_api_datastore_Key_) on the result of #createKey(String, String)

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the key in `kind`, as an arbitrary string unique across root entities of this `kind`  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A websafe `String` representation of the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that was created  
  
### createKeyString(String kind, long id)
    
    
    public static String createKeyString(String kind, long id)

Shorthand for invoking [#keyToString(Key)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_keyToString_com_google_appengine_api_datastore_Key_) on the result of #createKey(String, long)

**Parameters**  
---  
**Name** | **Description**  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
`id` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the numeric identifier of the key in `kind`, unique across all root entities of this kind, must not be zero  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A websafe `String` representation of the [Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key) that was created  
  
### keyToString(Key key)
    
    
    public static String keyToString(Key key)

Converts a `Key` into a websafe string. For example, this string can safely be used as an URL parameter embedded in a HTML document. Note that ` key.equals(KeyFactory.stringToKey(KeyFactory.keyToString(key)) ` should evaluate to `true`.

**Parameter**  
---  
**Name** | **Description**  
`key` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
The `Key` to convert to a `String`.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | A websafe `String` representation of the provided `String`.  
  
### stringToKey(String encoded)
    
    
    public static Key stringToKey(String encoded)

Converts a `String`-representation of a `Key` into the `Key` instance it represents. Note that ` str.equals(KeyFactory.keyToString(KeyFactory.stringToKey(str)) ` should evaluate to `true` for all strings returned by [KeyFactory#keyToString](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.KeyFactory#com_google_appengine_api_datastore_KeyFactory_keyToString_).

**Parameter**  
---  
**Name** | **Description**  
`encoded` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The `String` representation of a `Key`.  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` | The `Key` that the given `String` represents.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
