---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery
title: Interface PreparedQuery (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:46.477743+00:00
---

# Interface PreparedQuery (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface PreparedQuery (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface PreparedQuery

Contains methods for fetching and returning entities from a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)). If the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) specified a sort order, [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) are returned in that order. Otherwise, the order is undefined.

A [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) does not cache results. Each use of [PreparedQuery](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery) results in a new trip to the datastore.

## Methods 

### asIterable()
    
    
    public abstract Iterable<Entity> asIterable()

Equivalent to [#asIterable(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterable_com_google_appengine_api_datastore_FetchOptions_) but uses default [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions).

**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asIterable(FetchOptions fetchOptions)
    
    
    public abstract Iterable<Entity> asIterable(FetchOptions fetchOptions)

Retrieves the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) as an [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html) using the provided [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions).

Each use of Iterable#iterator results in an entirely new and independent [Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html). See Also: [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
The fetch options to apply.  
**Returns**  
---  
**Type** | **Description**  
`[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` | The result of the PreparedQuery, represented as an [Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html).  
  
### asIterator()
    
    
    public abstract Iterator<Entity> asIterator()

Equivalent to [#asIterator(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterator_com_google_appengine_api_datastore_FetchOptions_) but uses default [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions).

**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asIterator(FetchOptions fetchOptions)
    
    
    public abstract Iterator<Entity> asIterator(FetchOptions fetchOptions)

Retrieves the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) as an [Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html) using the provided [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions). See Also: [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
The fetch strategy to apply.  
**Returns**  
---  
**Type** | **Description**  
`[Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` | The result of the PreparedQuery, represented as an [Iterator](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html).  
  
### asList(FetchOptions fetchOptions)
    
    
    public abstract List<Entity> asList(FetchOptions fetchOptions)

Retrieves the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) as a [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html) using the provided [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions).

Note that if [FetchOptions#getLimit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions#com_google_appengine_api_datastore_FetchOptions_getLimit__) is greater than the number of [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity), the length of the returned [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html) will be smaller than[FetchOptions#getLimit()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions#com_google_appengine_api_datastore_FetchOptions_getLimit__).

To operate on large result sets, you should prefer [#asIterable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterable_) and [#asIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterator_), which stream the results from the datastore. See Also: [FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
The fetch options to apply.  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` | The result of the PreparedQuery, represented as a [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html).  
  
### asQueryResultIterable()
    
    
    public abstract QueryResultIterable<Entity> asQueryResultIterable()

Similar to [#asIterable()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterable__) except a [QueryResultIterable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterable) is returned. Call this method to have (indirect) access to [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)s for your result set.

**Returns**  
---  
**Type** | **Description**  
`[QueryResultIterable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterable)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asQueryResultIterable(FetchOptions fetchOptions)
    
    
    public abstract QueryResultIterable<Entity> asQueryResultIterable(FetchOptions fetchOptions)

Similar to [#asIterable(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterable_com_google_appengine_api_datastore_FetchOptions_) except a [QueryResultIterable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterable) is returned. Call this method to have (indirect) access to [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)s for your result set.

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueryResultIterable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterable)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asQueryResultIterator()
    
    
    public abstract QueryResultIterator<Entity> asQueryResultIterator()

Similar to [#asIterator()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterator__) except a [QueryResultIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator) is returned. Call this method to have access to [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)s for your result set.

**Returns**  
---  
**Type** | **Description**  
`[QueryResultIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asQueryResultIterator(FetchOptions fetchOptions)
    
    
    public abstract QueryResultIterator<Entity> asQueryResultIterator(FetchOptions fetchOptions)

Similar to [#asIterator(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asIterator_com_google_appengine_api_datastore_FetchOptions_) except a [QueryResultIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator) is returned. Call this method to have access to [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Cursor)s for your result set.

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueryResultIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asQueryResultList(FetchOptions fetchOptions)
    
    
    public abstract QueryResultList<Entity> asQueryResultList(FetchOptions fetchOptions)

Similar to [#asList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_asList_) except a [QueryResultIterator](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultIterator) is returned.

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueryResultList](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultList)<[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)>` |   
  
### asSingleEntity()
    
    
    public abstract Entity asSingleEntity()

Retrieves the one and only result for the [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)).

**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity)` | the single, matching result, or `null` if no entities match  
**Exceptions**  
---  
**Type** | **Description**  
`[PreparedQuery.TooManyResultsException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery.TooManyResultsException)` | if more than one result is returned from the Query.  
  
### countEntities() (deprecated)
    
    
    public abstract int countEntities()

**Deprecated.** _Use[#countEntities(FetchOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.PreparedQuery#com_google_appengine_api_datastore_PreparedQuery_countEntities_com_google_appengine_api_datastore_FetchOptions_) instead. Calling this function imposes a maximum result limit of 1000._

Retrieves the number of [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) that currently match this [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)).

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | a count >= 0  
  
### countEntities(FetchOptions fetchOptions)
    
    
    public abstract int countEntities(FetchOptions fetchOptions)

Retrieves the number of [Entities](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Entity) that currently match this [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)).

**Parameter**  
---  
**Name** | **Description**  
`fetchOptions` | `[FetchOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FetchOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | a count >= 0  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
