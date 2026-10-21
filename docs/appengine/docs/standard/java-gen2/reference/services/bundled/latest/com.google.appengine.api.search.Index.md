---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index
title: Interface Index (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:20:49.384007+00:00
---

# Interface Index (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface Index (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface Index

An Index allows synchronous and asynchronous adding and deleting of [Documents](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document) as well as synchronous and asynchronous searching for Documents for a given [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)). The following code fragment shows how to add documents, then search the index for documents matching a query.
    
    
      // Get the SearchService for the default namespace
      SearchService searchService = SearchServiceFactory.getSearchService();
      // Get the index. If not yet created, create it.
      Index index = searchService.getIndex(
          IndexSpec.newBuilder().setIndexName("indexName"));
    
      // Create a document.
      Document document = Document.newBuilder()
          .setId("documentId")
          .addField(Field.newBuilder().setName("subject").setText("my first email"))
          .addField(Field.newBuilder().setName("body")
               .setHTML(some content here")
          .build();
    
      // Put the document.
      try {
        index.put(document);
      } catch (PutException e) {
        if (StatusCode.TRANSIENT_ERROR.equals(e.getOperationResult().getCode())) {
          // retry putting document
        }
      }
    
      // Query the index.
      try {
        Results<ScoredDocument> results =
            index.search(Query.newBuilder().build("subject:first body:here"));
    
        // Iterate through the search results.
        for (ScoredDocument document : results) {
          // display results
        }
      } catch (SearchException e) {
        if (StatusCode.TRANSIENT_ERROR.equals(e.getOperationResult().getCode())) {
          // retry
        }
      }
     
     

## Methods 

### delete(Iterable<String> documentIds)
    
    
    public abstract void delete(Iterable<String> documentIds)

See Also: [#delete(String...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_delete_)

**Parameter**  
---  
**Name** | **Description**  
`documentIds` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
  
### delete(String[] documentIds)
    
    
    public abstract void delete(String[] documentIds)

Delete documents for the given document ids from the index if they are in the index.

**Parameter**  
---  
**Name** | **Description**  
`documentIds` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
the ids of documents to delete  
  
### deleteAsync(Iterable<String> documentIds)
    
    
    public abstract Future<Void> deleteAsync(Iterable<String> documentIds)

See Also: [#delete(String...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_delete_)

**Parameter**  
---  
**Name** | **Description**  
`documentIds` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### deleteAsync(String[] documentId)
    
    
    public abstract Future<Void> deleteAsync(String[] documentId)

See Also: [#delete(String...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_delete_)

**Parameter**  
---  
**Name** | **Description**  
`documentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### deleteSchema()
    
    
    public abstract void deleteSchema()

Delete the schema from the index. To fully delete an index, you must delete both the index's documents and schema. This method deletes the index's schema, which contains field names and field types of previously indexed documents.

### deleteSchemaAsync()
    
    
    public abstract Future<Void> deleteSchemaAsync()

See Also: [#deleteSchema()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_deleteSchema__)

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Void](https://docs.oracle.com/javase/8/docs/api/java/lang/Void.html)>` |   
  
### get(String documentId)
    
    
    public abstract Document get(String documentId)

Gets a [Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document) for the given document Id.

**Parameter**  
---  
**Name** | **Description**  
`documentId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the identifier for the document to retrieve  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)` | the associated [Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document). can be null  
  
### getName()
    
    
    public abstract String getName()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the name of the index  
  
### getNamespace()
    
    
    public abstract String getNamespace()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | the namespace of the index name  
  
### getRange(GetRequest request)
    
    
    public abstract GetResponse<Document> getRange(GetRequest request)

Get an index's documents, in document Id order.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest)`  
contains various options restricting which documents are returned.  
**Returns**  
---  
**Type** | **Description**  
`[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)>` | a [GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse) containing a list of documents from the index  
  
### getRange(GetRequest.Builder builder)
    
    
    public abstract GetResponse<Document> getRange(GetRequest.Builder builder)

See Also: [#getRange(GetRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_getRange_com_google_appengine_api_search_GetRequest_)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)>` |   
  
### getRangeAsync(GetRequest request)
    
    
    public abstract Future<GetResponse<Document>> getRangeAsync(GetRequest request)

See Also: [#getRange(GetRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_getRange_com_google_appengine_api_search_GetRequest_)

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)>>` |   
  
### getRangeAsync(GetRequest.Builder builder)
    
    
    public abstract Future<GetResponse<Document>> getRangeAsync(GetRequest.Builder builder)

See Also: [#getRange(GetRequest)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_getRange_com_google_appengine_api_search_GetRequest_)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[GetRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetRequest.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetResponse)<[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)>>` |   
  
### getSchema()
    
    
    public abstract Schema getSchema()

**Returns**  
---  
**Type** | **Description**  
`[Schema](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Schema)` | the [Schema](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Schema) describing supported document field names and [Field.FieldType](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Field.FieldType)s supported for those field names. This schema will only be populated if the [GetIndexesRequest#isSchemaFetched](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.GetIndexesRequest#com_google_appengine_api_search_GetIndexesRequest_isSchemaFetched_) is set to `true` on a [SearchService#getIndexes](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.SearchService#com_google_appengine_api_search_SearchService_getIndexes_) request  
  
### getStorageLimit()
    
    
    public abstract long getStorageLimit()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the maximum amount of storage space that the application may use in this index, expressed in bytes  
  
### getStorageUsage()
    
    
    public abstract long getStorageUsage()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | a rough approximation of the amount of storage space currently used by this index, expressed in bytes  
  
### put(Document[] documents)
    
    
    public abstract PutResponse put(Document[] documents)

Put the documents into the index, updating any document that is already present.

**Parameter**  
---  
**Name** | **Description**  
`documents` | `[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)[]`  
the documents to put into the index  
**Returns**  
---  
**Type** | **Description**  
`[PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)` | an [PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse) containing the result of the put operations indicating success or failure as well as the document ids. The search service will allocate document ids for documents which have none provided  
  
### put(Document.Builder[] builders)
    
    
    public abstract PutResponse put(Document.Builder[] builders)

See Also: [#put(Document...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_put_)

**Parameter**  
---  
**Name** | **Description**  
`builders` | `[Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)` |   
  
### put(Iterable<Document> documents)
    
    
    public abstract PutResponse put(Iterable<Document> documents)

See Also: [#put(Document...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_put_)

**Parameter**  
---  
**Name** | **Description**  
`documents` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)` |   
  
### putAsync(Document[] document)
    
    
    public abstract Future<PutResponse> putAsync(Document[] document)

See Also: [#put(Document...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_put_)

**Parameter**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)>` |   
  
### putAsync(Document.Builder[] document)
    
    
    public abstract Future<PutResponse> putAsync(Document.Builder[] document)

See Also: [#put(Document...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_put_)

**Parameter**  
---  
**Name** | **Description**  
`document` | `[Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document.Builder)[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)>` |   
  
### putAsync(Iterable<Document> documents)
    
    
    public abstract Future<PutResponse> putAsync(Iterable<Document> documents)

See Also: [#put(Document...)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_put_)

**Parameter**  
---  
**Name** | **Description**  
`documents` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Document](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Document)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[PutResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.PutResponse)>` |   
  
### search(Query query)
    
    
    public abstract Results<ScoredDocument> search(Query query)

Search the index for documents matching the query. The query must specify a query string, and optionally, how many documents are requested, how the results are to be sorted, scored and which fields are to be returned.

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))`  
the fully specified [Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\)) object  
**Returns**  
---  
**Type** | **Description**  
`[Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)<[ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)>` | a [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) containing [ScoredDocuments](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)  
  
### search(String query)
    
    
    public abstract Results<ScoredDocument> search(String query)

Search the index for documents matching the query string. See Also: [#search(Query)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_search_com_google_appengine_api_search_Query_)

**Parameter**  
---  
**Name** | **Description**  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the query string  
**Returns**  
---  
**Type** | **Description**  
`[Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)<[ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)>` | a [Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results) containing [ScoredDocuments](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)  
  
### searchAsync(Query query)
    
    
    public abstract Future<Results<ScoredDocument>> searchAsync(Query query)

See Also: [#search(Query)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_search_com_google_appengine_api_search_Query_)

**Parameter**  
---  
**Name** | **Description**  
`query` | `[Query](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Query\(class\))`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)<[ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)>>` |   
  
### searchAsync(String query)
    
    
    public abstract Future<Results<ScoredDocument>> searchAsync(String query)

See Also: [#search(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Index#com_google_appengine_api_search_Index_search_java_lang_String_)

**Parameter**  
---  
**Name** | **Description**  
`query` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Results](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.Results)<[ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.ScoredDocument)>>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
