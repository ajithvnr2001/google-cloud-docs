---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService
title: Interface SearchService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:12:26.822639+00:00
---

# Interface SearchService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface SearchService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface SearchService

The SearchService is used to get available indexes, which can be queried about their metadata or have index/delete/search operations performed on them. For example:
    
    
     SearchService searchService = SearchServiceFactory.getSearchService();
     GetResponse<Index> response = searchService.getIndexes(
         GetIndexesRequest.newBuilder());
     for (Index index : response) {
       index.getName();
       index.getNamespace();
       index.search("query");
     }
     

SearchService is also responsible for creating new indexes. For example:
    
    
     SearchService searchService = SearchServiceFactory.getSearchService();
     Index index = searchService.getIndex(IndexSpec.newBuilder().setName("myindex"));
     

## Methods 

### getIndex(IndexSpec spec)
    
    
    public abstract Index getIndex(IndexSpec spec)

Returns an instance of [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index) corresponding to the provided specification.

**Parameter**  
---  
**Name** | **Description**  
`spec` | `[IndexSpec](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.IndexSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)` | an instance of [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index) corresponding to the given `spec`  
  
### getIndex(IndexSpec.Builder builder)
    
    
    public abstract Index getIndex(IndexSpec.Builder builder)

Returns an instance of [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index) corresponding to the specification built from the given `builder`.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[IndexSpec.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.IndexSpec.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)` | an instance of [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index) corresponding to the given `spec`  
  
### getIndexes(GetIndexesRequest request)
    
    
    public abstract GetResponse<Index> getIndexes(GetIndexesRequest request)

Gets the indexes specified. The following code fragment shows how to get the schemas of each available [Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index).
    
    
       // Get the SearchService for the default namespace
       SearchService searchService = SearchServiceFactory.newSearchService();
    
       // Get the first page of indexes available and retrieve schemas
       GetResponse<Index> response = searchService.getIndexes(
           GetIndexesRequest.newBuilder().setSchemaFetched(true).build());
    
       // List out elements of Schema
       for (Index index : response) {
         String name = index.getName();
         Schema schema = index.getSchema();
         for (String fieldName : schema.getFieldNames()) {
            List<FieldType> typesForField = schema.getFieldTypes(fieldName);
         }
       }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest)`  
a request specifying which indexes to get  
**Returns**  
---  
**Type** | **Description**  
`[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)>` | a [GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)`<Index>` containing a list of existing indexes  
  
### getIndexes(GetIndexesRequest.Builder builder)
    
    
    public abstract GetResponse<Index> getIndexes(GetIndexesRequest.Builder builder)

Gets the indexes specified in the request built from the `builder`.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)`  
a builder to be used to construct a [GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest) specifying which indexes to get  
**Returns**  
---  
**Type** | **Description**  
`[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)>` | a [GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)`<Index>` containing a list of existing indexes  
  
### getIndexesAsync(GetIndexesRequest request)
    
    
    public abstract Future<GetResponse<Index>> getIndexesAsync(GetIndexesRequest request)

Gets the indexes requested asynchronously.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest)`  
a request specifying which indexes to get  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)>>` | a [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) that will allow getting a [GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)`<Index>` containing a list of existing indexes  
  
### getIndexesAsync(GetIndexesRequest.Builder builder)
    
    
    public abstract Future<GetResponse<Index>> getIndexesAsync(GetIndexesRequest.Builder builder)

Gets the indexes asynchronously for those specified in the request built from the `builder`.

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[GetIndexesRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest.Builder)`  
a builder to be used to construct a [GetIndexesRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest) specifying which indexes to get  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Index](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index)>>` | a [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) that will allow getting a [GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)`<Index>` containing a list of existing indexes  
  
### getNamespace()
    
    
    public abstract String getNamespace()

Returns the namespace associated with this search service. Each service instance is assigned one namespace and all operations, such as listing documents, indexes inherit it. Also, when you get an index, the namespace of this service is passed to the returned index.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the namespace associated with this search service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
