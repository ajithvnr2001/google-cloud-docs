---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder
title: Class FetchOptions.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:59.184105+00:00
---

# Class FetchOptions.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FetchOptions.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class FetchOptions.Builder

Contains static creation methods for [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FetchOptions.Builder

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

### withChunkSize(int chunkSize)
    
    
    public static FetchOptions withChunkSize(int chunkSize)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given chunk size. Shorthand for ` FetchOptions.withDefaults().chunkSize(...);` Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how chunk size is used.

**Parameter**  
---  
**Name** | **Description**  
`chunkSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the chunkSize to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
### withCursor(Cursor cursor) (deprecated)
    
    
    public static FetchOptions withCursor(Cursor cursor)

**Deprecated.** _use[#withStartCursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder#com_google_appengine_api_datastore_FetchOptions_Builder_withStartCursor_) instead._

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given cursor. Shorthand for ` FetchOptions.withDefaults().cursor(cursor);`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how cursors are used.

**Parameter**  
---  
**Name** | **Description**  
`cursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)`  
the cursor to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
### withDefaults()
    
    
    public static FetchOptions withDefaults()

Helper method for creating a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) instance with default values. The defaults are `null` for all values.

**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` |   
  
### withEndCursor(Cursor endCursor)
    
    
    public static FetchOptions withEndCursor(Cursor endCursor)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given end cursor. Shorthand for ` FetchOptions.withDefaults().endCursor(cursor);`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how cursors are used.

**Parameter**  
---  
**Name** | **Description**  
`endCursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)`  
the cursor to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
### withLimit(int limit)
    
    
    public static FetchOptions withLimit(int limit)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given limit. Shorthand for ` FetchOptions.withDefaults().limit(...);` Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how limit is used.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the limit to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
### withOffset(int offset)
    
    
    public static FetchOptions withOffset(int offset)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given offset. Shorthand for ` FetchOptions.withDefaults().offset(...);` Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how offset is used.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the offset to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
### withPrefetchSize(int prefetchSize)
    
    
    public static FetchOptions withPrefetchSize(int prefetchSize)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given prefetch size. Shorthand for ` FetchOptions.withDefaults().prefetchSize(...);`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how prefetch size is used.

**Parameter**  
---  
**Name** | **Description**  
`prefetchSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the prefetchSize to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
### withStartCursor(Cursor startCursor)
    
    
    public static FetchOptions withStartCursor(Cursor startCursor)

Create a [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) with the given start cursor. Shorthand for ` FetchOptions.withDefaults().startCursor(cursor);`. Please read the [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) class javadoc for an explanation of how cursors are used.

**Parameter**  
---  
**Name** | **Description**  
`startCursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)`  
the cursor to set.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | The newly created FetchOptions instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
