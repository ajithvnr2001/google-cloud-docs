---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions
title: Class QueryOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:10:51.979667+00:00
---

# Class QueryOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class QueryOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class QueryOptions

Represents options which control where and what in the search results to return, from restricting the document fields returned to those given, and scoring and sorting the results, whilst supporting pagination.

For example, the following options will return documents from search results for some given query, returning up to 20 results including the fields 'author' and 'date-sent' as well as snippeted fields 'subject' and 'body'. The results are sorted by 'author' in descending order, getting the next 20 results from the responseCursor in the previously returned results, giving back a single cursor in the [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) to get the next batch of results after this.
    
    
     QueryOptions request = QueryOptions.newBuilder()
          .setLimit(20)
          .setFieldsToReturn("author", "date-sent")
          .setFieldsToSnippet("subject", "body")
          .setSortOptions(SortOptions.newBuilder().
              .addSortExpression(SortExpression.newBuilder()
                  .setExpression("author")
                  .setDirection(SortExpression.SortDirection.DESCENDING)
                  .setDefaultValue("")))
    
          .setCursor(Cursor.newBuilder().build())
          .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QueryOptions

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
    
    
    public static QueryOptions.Builder newBuilder()

Creates and returns a [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions) builder. Set the search request parameters and use the Builder#build() method to create a concrete instance of QueryOptions.

**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | a Builder which can construct a search request  
  
### newBuilder(QueryOptions request)
    
    
    public static QueryOptions.Builder newBuilder(QueryOptions request)

Creates a builder from the given request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions)`  
the search request for the builder to use to build another request  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | a new builder with values set from the given request  
  
## Methods 

### getCursor()
    
    
    public Cursor getCursor()

**Returns**  
---  
**Type** | **Description**  
`[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)` | a cursor returned from a previous set of search results to use as a starting point to retrieve the next set of results. Can be null  
  
### getExpressionsToReturn()
    
    
    public List<FieldExpression> getExpressionsToReturn()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FieldExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression)>` | an unmodifiable list of expressions which will be evaluated and returned in results  
  
### getFieldsToReturn()
    
    
    public List<String> getFieldsToReturn()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | an unmodifiable list of names of fields to return in search results  
  
### getFieldsToSnippet()
    
    
    public List<String> getFieldsToSnippet()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | an unmodifiable list of names of fields to snippet in search results  
  
### getLimit()
    
    
    public int getLimit()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the limit on the number of documents to return in search results  
  
### getNumberFoundAccuracy()
    
    
    public int getNumberFoundAccuracy()

Any [Results#getNumberFound()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results#com_google_appengine_api_search_Results_getNumberFound__) less than or equal to this setting will be accurate.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the found count accuracy  
  
### getOffset()
    
    
    public int getOffset()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the offset of the first result to return; returns 0 if was not set  
  
### getSortOptions()
    
    
    public SortOptions getSortOptions()

**Returns**  
---  
**Type** | **Description**  
`[SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions)` | a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions) specifying how to sort Documents in [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)  
  
### hasNumberFoundAccuracy()
    
    
    public boolean hasNumberFoundAccuracy()

Returns true iff there is an accuracy requirement set.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the found count accuracy  
  
### isReturningIdsOnly()
    
    
    public boolean isReturningIdsOnly()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | if this search request returns results document IDs only  
  
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
