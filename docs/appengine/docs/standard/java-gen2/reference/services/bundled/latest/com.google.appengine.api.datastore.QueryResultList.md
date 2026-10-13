---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultList
title: Interface QueryResultList<T> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:47.546852+00:00
---

# Interface QueryResultList<T> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.QueryResultList

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface QueryResultList<T> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface QueryResultList<T> extends List<T>

A list of results returned by executing a [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)).

## Implements

[List<T>](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)

## Type Parameter  
  
---  
**Name** | **Description**  
`T` |   
  
## Methods 

### getCursor()
    
    
    public abstract Cursor getCursor()

Gets a [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor) that points to the result immediately after the last one in this list.

**Returns**  
---  
**Type** | **Description**  
`[Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor)` | a [Cursor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Cursor) or `null` if this query result cannot be resumed. (Note that a Cursor is returned even if the end of the result list has been reached).  
  
### getIndexList()
    
    
    public abstract List<Index> getIndexList()

Get the indexes used to perform the query.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Index)>` | A list of index references, with no duplicates, or `null` if the indexes are not known.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
