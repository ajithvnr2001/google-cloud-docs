---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor
title: Class Cursor (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:12:20.214500+00:00
---

# Class Cursor (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class Cursor (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class Cursor implements Serializable

Represents a cursor on the set of results found for executing a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) during a search on the [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index). 

For example, the following code shows how to use a cursor to get the next page of results 
    
    
     Index index = ...
     Cursor cursor = Cursor.newBuilder().build();
     Query query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(cursor).build("some query"));
    
     // Get the first page of results
     Results<ScoredDocument> results = index.search(query);
    
     // process results
     ...
    
     // Get the next set of results from the returned cursor
     query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(
             results.getCursor()).build("some query"));
    
     results = index.search(query);
     

Alternatively, you can get a cursor to continue from each of the returned results.
    
    
     Cursor cursor =
         Cursor.newBuilder().setPerResult(true).build();
     Query query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(cursor).build("some query"));
    
     // Get the first page of results
     Results<ScoredDocument> results = index.search(query);
    
     // process results
     for (ScoredDocument result : results) {
       // choose a cursor from one of the results
       cursor = result.getCursor();
     }
    
     // Get the next set of results from the result's cursor
     query = Query.newBuilder().setOptions(
         QueryOptions.newBuilder().setCursor(cursor).build("some query"));
    
     results = index.search(query);
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Cursor

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### newBuilder()
    
    
    public static Cursor.Builder newBuilder()

Creates and returns a [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor) builder. Set the search request parameters and use the Builder#build() method to create a concrete instance of Cursor.

**Returns**  
---  
**Type** | **Description**  
`[Cursor.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor.Builder)` | a Builder which can construct a search request  
  
### newBuilder(Cursor request)
    
    
    public static Cursor.Builder newBuilder(Cursor request)

Creates a builder from the given request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)`  
the search request for the builder to use to build another request  
**Returns**  
---  
**Type** | **Description**  
`[Cursor.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor.Builder)` | this builder  
  
## Methods 

### isPerResult()
    
    
    public boolean isPerResult()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | whether the cursor is for all Results or one cursor per result  
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### toWebSafeString()
    
    
    public String toWebSafeString()

A web safe string representing a cursor returned from a previous set of search results to use as a starting point to retrieve the next set of results. Can be null.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a web safe string representation of the cursor  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
