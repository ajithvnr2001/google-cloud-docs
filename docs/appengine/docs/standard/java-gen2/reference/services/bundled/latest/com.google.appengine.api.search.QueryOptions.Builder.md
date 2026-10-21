---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder
title: Class QueryOptions.Builder (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:13.627001+00:00
---

# Class QueryOptions.Builder (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class QueryOptions.Builder (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class QueryOptions.Builder

A builder which constructs QueryOptions objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QueryOptions.Builder

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

### addExpressionToReturn(FieldExpression expression)
    
    
    public QueryOptions.Builder addExpressionToReturn(FieldExpression expression)

Adds a [FieldExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression) to return in search results.

**Parameter**  
---  
**Name** | **Description**  
`expression` | `[FieldExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression)`  
a named expression to compute and return in results  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### addExpressionToReturn(FieldExpression.Builder expressionBuilder)
    
    
    public QueryOptions.Builder addExpressionToReturn(FieldExpression.Builder expressionBuilder)

Adds a [FieldExpression](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression) build from the given `expressionBuilder` to return in search results. Snippets will be returned as fields with the same names in [ScoredDocument#getExpressions()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument#com_google_appengine_api_search_ScoredDocument_getExpressions__).

**Parameter**  
---  
**Name** | **Description**  
`expressionBuilder` | `[FieldExpression.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.FieldExpression.Builder)`  
a builder of named expressions to evaluate and return in results  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### build()
    
    
    public QueryOptions build()

Construct the final message.

**Returns**  
---  
**Type** | **Description**  
`[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions)` | the QueryOptions built from the parameters entered on this Builder  
  
### clearNumberFoundAccuracy()
    
    
    public QueryOptions.Builder clearNumberFoundAccuracy()

Clears any accuracy requirement for [Results#getNumberFound()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results#com_google_appengine_api_search_Results_getNumberFound__).

**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` |   
  
### setCursor(Cursor cursor)
    
    
    public QueryOptions.Builder setCursor(Cursor cursor)

Sets the cursor. The cursor is obtained from either a [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) or one of the individual [ScoredDocuments](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument).

This is illustrated from the following code fragment: 
    
    
     Cursor cursor = Cursor.newBuilder().build();
    
     SearchResults results = index.search(
         Query.newBuilder()
             .setOptions(QueryOptions.newBuilder()
                 .setLimit(20)
                 .setCursor(cursor)
                 .build())
             .build("some query"));
    
     // If the Cursor is built without setPerResult(true), then
     // by default[ a sin](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)gle Cursor is returned wit[h the](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)
     // Results.
     cursor = results.getCursor();
    
     for (ScoredDocument result : results) {
         // If you set Cursor.newBuilder().setPerResult(true)
         // then a cursor is returned with each result.
         result.getCursor();
     }

**Parameter**  
---  
**Name** | **Description**  
`cursor` | `[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)`  
use a cursor returned from a previous set of search results as a starting point to retrieve the next set of results. This can get you better performance, and also improves the consistency of pagination through index updates  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setCursor(Cursor.Builder cursorBuilder)
    
    
    public QueryOptions.Builder setCursor(Cursor.Builder cursorBuilder)

Sets a cursor built from the builder. See Also: [#setCursor(Cursor)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder#com_google_appengine_api_search_QueryOptions_Builder_setCursor_com_google_appengine_api_search_Cursor_)

**Parameter**  
---  
**Name** | **Description**  
`cursorBuilder` | `[Cursor.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor.Builder)`  
a [Cursor.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor.Builder) that is used to build a [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor).  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setFieldsToReturn(String[] fields)
    
    
    public QueryOptions.Builder setFieldsToReturn(String[] fields)

Specifies one or more fields to return in results.

**Parameter**  
---  
**Name** | **Description**  
`fields` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
the names of fields to return in results  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setFieldsToSnippet(String[] fieldsToSnippet)
    
    
    public QueryOptions.Builder setFieldsToSnippet(String[] fieldsToSnippet)

Specifies one or more fields to snippet in results. Snippets will be returned as fields with the same names in [ScoredDocument#getExpressions()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument#com_google_appengine_api_search_ScoredDocument_getExpressions__).

**Parameter**  
---  
**Name** | **Description**  
`fieldsToSnippet` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
the names of fields to snippet in results  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setLimit(int limit)
    
    
    public QueryOptions.Builder setLimit(int limit)

Sets the limit on the number of documents to return in [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results).

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of documents to return  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setNumberFoundAccuracy(int numberFoundAccuracy)
    
    
    public QueryOptions.Builder setNumberFoundAccuracy(int numberFoundAccuracy)

Sets the accuracy requirement for [Results#getNumberFound()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results#com_google_appengine_api_search_Results_getNumberFound__). If set, `getNumberFound()` will be accurate up to at least that number. For example, when set to 100, any `getNumberFound() <= 100` is accurate. This option may add considerable latency / expense, especially when used with Builder#setFieldsToReturn(String...).

**Parameter**  
---  
**Name** | **Description**  
`numberFoundAccuracy` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the minimum accuracy requirement  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setOffset(int offset)
    
    
    public QueryOptions.Builder setOffset(int offset)

Sets the offset of the first result to return.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the offset into all search results to return the limit amount of results  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setReturningIdsOnly(boolean idsOnly)
    
    
    public QueryOptions.Builder setReturningIdsOnly(boolean idsOnly)

Sets whether or not the search should return documents or document IDs only. This setting is incompatible with [#addExpressionToReturn(FieldExpression)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder#com_google_appengine_api_search_QueryOptions_Builder_addExpressionToReturn_com_google_appengine_api_search_FieldExpression_) and with #setFieldsToReturn(String...) methods.

**Parameter**  
---  
**Name** | **Description**  
`idsOnly` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
whether or not only IDs of documents are returned by search request  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setSortOptions(SortOptions sortOptions)
    
    
    public QueryOptions.Builder setSortOptions(SortOptions sortOptions)

Sets a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions) to sort documents with.

**Parameter**  
---  
**Name** | **Description**  
`sortOptions` | `[SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions)`  
specifies how to sort the documents in [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
### setSortOptions(SortOptions.Builder builder)
    
    
    public QueryOptions.Builder setSortOptions(SortOptions.Builder builder)

Sets a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions) using a builder.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[SortOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions.Builder)`  
a builder of a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SortOptions)  
**Returns**  
---  
**Type** | **Description**  
`[QueryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.QueryOptions.Builder)` | this Builder  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
