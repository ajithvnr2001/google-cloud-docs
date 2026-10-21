---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results
title: Class Results<T> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:42:52.964313+00:00
---

# Class Results<T> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Results<T> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class Results<T> implements Iterable<T>, Serializable

Represents a result of executing a search. The Results include an [OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult), a collection of results, and a number of found and returned results.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Results<T>

## Implements

[Iterable<T>](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html), [Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Constructors 

### Results(OperationResult operationResult, Collection<T> results, long numberFound, int numberReturned, Cursor cursor)
    
    
    protected Results(OperationResult operationResult, Collection<T> results, long numberFound, int numberReturned, Cursor cursor)

Creates a [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) by specifying a collection of search results, the number of results found, and the number of results returned.

**Parameters**  
---  
**Name** | **Description**  
`operationResult` | `[OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult)`  
the result of the search operation  
`results` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of results that resulted from the search  
`numberFound` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of results found by the search  
`numberReturned` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of results returned  
`cursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)`  
the [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor) if there are more results and user requested it  
  
### Results(OperationResult operationResult, Collection<T> results, long numberFound, int numberReturned, Cursor cursor, Collection<FacetResult> facets)
    
    
    protected Results(OperationResult operationResult, Collection<T> results, long numberFound, int numberReturned, Cursor cursor, Collection<FacetResult> facets)

Creates a [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) by specifying a collection of search results, the number of results found, and the number of results returned.

**Parameters**  
---  
**Name** | **Description**  
`operationResult` | `[OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult)`  
the result of the search operation  
`results` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>`  
a collection of results that resulted from the search  
`numberFound` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of results found by the search  
`numberReturned` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of results returned  
`cursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)`  
the [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor) if there are more results and user requested it  
`facets` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[FacetResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResult)>`  
aggregated facets of this search results as a collection of [FacetResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResult) from the search  
  
## Methods 

### getCursor()
    
    
    public Cursor getCursor()

A cursor to be used to continue the search after all the results in this search response. For this field to be populated, use [QueryOptions.Builder#setCursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder#com_google_appengine_api_search_QueryOptions_Builder_setCursor_) with a value of `Cursor.newBuilder().build()`, otherwise #getCursor will return null.

**Returns**  
---  
**Type** | **Description**  
`[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)` | cursor to be used to get the next set of results after the end of these results, or `null` if there are no more results to be expected or if no cursor was configured in the `QueryOptions`.  
  
### getFacets()
    
    
    public Collection<FacetResult> getFacets()

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[FacetResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FacetResult)>` | an unmodifiable collection of aggregated facets for this search results  
  
### getNumberFound()
    
    
    public long getNumberFound()

The number of results found by the search. If the value is less than or equal to the corresponding [QueryOptions#getNumberFoundAccuracy()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions#com_google_appengine_api_search_QueryOptions_getNumberFoundAccuracy__), then it is accurate, otherwise it is an approximation

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of results found  
  
### getNumberReturned()
    
    
    public int getNumberReturned()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of results returned  
  
### getOperationResult()
    
    
    public OperationResult getOperationResult()

**Returns**  
---  
**Type** | **Description**  
`[OperationResult](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.OperationResult)` | the result of the search operation  
  
### getResults()
    
    
    public Collection<T> getResults()

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<T>` | an unmodifiable collection of search results  
  
### iterator()
    
    
    public Iterator<T> iterator()

**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<T>` |   
  
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
