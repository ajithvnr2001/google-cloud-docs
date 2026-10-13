---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ExtendableEntityUtil
title: Class ExtendableEntityUtil (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:58.216381+00:00
---

# Class ExtendableEntityUtil (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.ExtendableEntityUtil

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ExtendableEntityUtil (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class ExtendableEntityUtil

Internal class that provides utility methods for extendable entity objects.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ExtendableEntityUtil

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

### areKeysEqual(Key key1, Key key2)
    
    
    public static boolean areKeysEqual(Key key1, Key key2)

Check if the input `Key` objects are equal (including keys that are incomplete).

**Parameters**  
---  
**Name** | **Description**  
`key1` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
the first input key  
`key2` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
the second input key  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | `true` if the keys are equal. `false` otherwise.  
  
### checkSupportedValue(String propertyName, Object value, boolean valuePreChecked, Set<Class<?>> supportedTypes)
    
    
    public static void checkSupportedValue(String propertyName, Object value, boolean valuePreChecked, Set<Class<?>> supportedTypes)

If the specified object cannot be used as the value for a `Entity` property, throw an exception with the appropriate explanation.

**Parameters**  
---  
**Name** | **Description**  
`propertyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the name of the property.  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
value in question  
`valuePreChecked` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
`true` if the value without the name has already been checked. `false` otherwise.  
`supportedTypes` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>>`  
the types considered to be valid types for the value.  
  
### createKey(Key parent, String kind)
    
    
    public static Key createKey(Key parent, String kind)

Creates a new `Key` with the provided parent and kind. The instantiated `Key` will be incomplete.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)`  
the parent of the key to create, can be `null`  
`kind` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the kind of the key to create  
**Returns**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Key)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
