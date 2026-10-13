---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions
title: Class FetchOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:58.797917+00:00
---

# Class FetchOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FetchOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class FetchOptions

Describes the limit, offset, and chunk size to be applied when executing a [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery).

`limit` is the maximum number of results the query will return.

`offset` is the number of results to skip before returning any results. Results that are skipped due to offset do not count against `limit`.  
**Note:** Using `offset` still retrieves skipped entities internally. This affects the latency of the query, and **your application is billed for the operations** required to retrieve them. Using cursors lets you avoid these costs.

`startCursor` and `endCursor` are previously generated cursors that point to locations in a result set. If specified queries will start and end at these locations.

`prefetchSize` is the number of results retrieved on the first call to the datastore.

`chunkSize` determines the internal chunking strategy of the [Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html) returned by [PreparedQuery#asIterator(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterator_com_google_appengine_api_datastore_FetchOptions_) and the [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html) returned by [PreparedQuery#asIterable(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterable_com_google_appengine_api_datastore_FetchOptions_).

Note that unlike `limit`, `offset` and `cursor`, `prefetchSize` and `chunkSize` have no impact on the result of the [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery), but rather only the performance of the [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery).

Notes on usage:  
The recommended way to instantiate a `FetchOptions` object is to import [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions) and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import com.google.appengine.api.datastore.[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html);
    
     [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor.html) cursor = ...
    
     ...
    
     // limit 10
     datastoreService.prepare(query).[asList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery.html#com_google_appengine_api_datastore_PreparedQuery_asList_com_google_appengine_api_datastore_FetchOptions_)([FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html).Builder.[withLimit](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder.html#com_google_appengine_api_datastore_FetchOptions_Builder_withLimit_int_)(10));
    
     // limit 10, start cursor
     datastoreService.prepare(query).[asList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery.html#com_google_appengine_api_datastore_PreparedQuery_asList_com_google_appengine_api_datastore_FetchOptions_)([FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html).Builder.[withLimit](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.Builder.html#com_google_appengine_api_datastore_FetchOptions_Builder_withLimit_int_)(10).[startCursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions.html#com_google_appengine_api_datastore_FetchOptions_startCursor_com_google_appengine_api_datastore_Cursor_)(cursor));
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FetchOptions

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

### DEFAULT_CHUNK_SIZE (deprecated)
    
    
    public static final int DEFAULT_CHUNK_SIZE

**Deprecated.** _Instead of using DEFAULT_CHUNK_SIZE, do not specify a chunk size._

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Methods 

### chunkSize(int chunkSize)
    
    
    public FetchOptions chunkSize(int chunkSize)

Sets the chunk size. Please read the class javadoc for an explanation of how chunk size is used.

**Parameter**  
---  
**Name** | **Description**  
`chunkSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The chunk size to set. Must be greater than 0.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
### cursor(Cursor cursor) (deprecated)
    
    
    public FetchOptions cursor(Cursor cursor)

**Deprecated.** _use[#startCursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions#com_google_appengine_api_datastore_FetchOptions_startCursor_) instead._

Sets the cursor to start the query from.

**Parameter**  
---  
**Name** | **Description**  
`cursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)`  
the cursor to set  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
### endCursor(Cursor endCursor)
    
    
    public FetchOptions endCursor(Cursor endCursor)

Sets the cursor at which to end the query.

**Parameter**  
---  
**Name** | **Description**  
`endCursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)`  
the cursor to set  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
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

### getChunkSize()
    
    
    public @Nullable Integer getChunkSize()

Returns the chunk size, or `null` if no chunk size was provided.

**Returns**  
---  
**Type** | **Description**  
`[Nullable Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Integer.html)` |   
  
### getCursor() (deprecated)
    
    
    public @Nullable Cursor getCursor()

**Deprecated.** _use[#getStartCursor()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions#com_google_appengine_api_datastore_FetchOptions_getStartCursor__) instead_

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Cursor` | The start cursor, or `null` if no cursor was provided.  
  
### getEndCursor()
    
    
    public @Nullable Cursor getEndCursor()

Returns the end cursor, or `null` if no end cursor was provided.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Cursor` |   
  
### getLimit()
    
    
    public @Nullable Integer getLimit()

Returns the limit, or `null` if no limit was provided.

**Returns**  
---  
**Type** | **Description**  
`[Nullable Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Integer.html)` |   
  
### getOffset()
    
    
    public @Nullable Integer getOffset()

Returns the offset, or `null` if no offset was provided.

**Returns**  
---  
**Type** | **Description**  
`[Nullable Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Integer.html)` |   
  
### getPrefetchSize()
    
    
    public @Nullable Integer getPrefetchSize()

Returns the prefetch size, or `null` if no prefetch size was provided.

**Returns**  
---  
**Type** | **Description**  
`[Nullable Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Integer.html)` |   
  
### getStartCursor()
    
    
    public @Nullable Cursor getStartCursor()

Returns the start cursor, or `null` if no start cursor was provided.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.datastore.@org.jspecify.annotations.Nullable Cursor` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### limit(int limit)
    
    
    public FetchOptions limit(int limit)

Sets the limit. Please read the class javadoc for an explanation of how limit is used.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The limit to set. Must be non-negative.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
### offset(int offset)
    
    
    public FetchOptions offset(int offset)

Sets the offset. Please read the class javadoc for an explanation of how offset is used.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The offset to set. Must be 0 or greater.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
### prefetchSize(int prefetchSize)
    
    
    public FetchOptions prefetchSize(int prefetchSize)

Sets the number of entities to prefetch.

**Parameter**  
---  
**Name** | **Description**  
`prefetchSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The prefetch size to set. Must be >= 0.  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
### startCursor(Cursor startCursor)
    
    
    public FetchOptions startCursor(Cursor startCursor)

Sets the cursor at which to start the query.

**Parameter**  
---  
**Name** | **Description**  
`startCursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)`  
the cursor to set  
**Returns**  
---  
**Type** | **Description**  
`[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)` | `this` (for chaining)  
  
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
