---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AsyncLazyDatastoreQuery
title: Google Cloud Datastore v1 API - Class AsyncLazyDatastoreQuery (5.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:53.093605+00:00
---

# Google Cloud Datastore v1 API - Class AsyncLazyDatastoreQuery (5.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AsyncLazyDatastoreQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Datastore v1 API - Class AsyncLazyDatastoreQuery (5.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  5.0.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class AsyncLazyDatastoreQuery : IAsyncEnumerable<Entity>

Reference documentation and code samples for the Google Cloud Datastore v1 API class AsyncLazyDatastoreQuery.

A Datastore query which is executed lazily. Iterating over this object will provide a sequence of entities; alternatively, all the results can be fetched using [GetAllResultsAsync()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AsyncLazyDatastoreQuery#Google_Cloud_Datastore_V1_AsyncLazyDatastoreQuery_GetAllResultsAsync), or for diagnostic use cases the RPC responses can be viewed using [AsResponses()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AsyncLazyDatastoreQuery#Google_Cloud_Datastore_V1_AsyncLazyDatastoreQuery_AsResponses). The lazy evaluation is important: if you iterate over the query multiple times, it will execute multiple times, potentially returning different results each time.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AsyncLazyDatastoreQuery

## Implements

[IAsyncEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerable-1)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1)

## Assembly

Google.Cloud.Datastore.V1.dll

## Constructors 

### AsyncLazyDatastoreQuery(IAsyncEnumerable<RunQueryResponse>)
    
    
    public AsyncLazyDatastoreQuery(IAsyncEnumerable<RunQueryResponse> responses)

Constructs a new instance from the given sequence of responses. This constructor is only present to facilitate testing; application code will normally obtain instances of this class by calling [RunQueryLazilyAsync(Query, ReadConsistency?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreDb#Google_Cloud_Datastore_V1_DatastoreDb_RunQueryLazilyAsync_Google_Cloud_Datastore_V1_Query_System_Nullable_Google_Cloud_Datastore_V1_ReadOptions_Types_ReadConsistency__Google_Api_Gax_Grpc_CallSettings_).

**Parameter**  
---  
**Name** | **Description**  
`responses` | `[IAsyncEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerable-1)[RunQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunQueryResponse)`  
The responses to return.  
**Remarks**

The sequence of responses will be returned directly from [AsResponses()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AsyncLazyDatastoreQuery#Google_Cloud_Datastore_V1_AsyncLazyDatastoreQuery_AsResponses), and used to lazily construct the other sequences returned by this class. It should not contain any null references.

## Methods 

### AsResponses()
    
    
    public IAsyncEnumerable<RunQueryResponse> AsResponses()

This method is for advanced use cases only, where more diagnostic information is required; most application code should merely iterate over the query results as [Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity) values, or call [GetAllResultsAsync()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.AsyncLazyDatastoreQuery#Google_Cloud_Datastore_V1_AsyncLazyDatastoreQuery_GetAllResultsAsync). The results of this query are returned as a sequence of [RunQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunQueryResponse) values exactly as returned by the Datastore API.

**Returns**  
---  
**Type** | **Description**  
`[IAsyncEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerable-1)[RunQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunQueryResponse)` | A sequence of [RunQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.RunQueryResponse) values.  
  
### GetAllResultsAsync()
    
    
    public Task<DatastoreQueryResults> GetAllResultsAsync()

Reads all the results from this query, until either the query-specified limit or end cursor is reached, or there is no more data to read. Note that all the entities are read into memory, so this method is not appropriate for use cases where a query could return a very large number of results. However, it is the simplest approach to use cases where the query is bounded, such as displaying a page of results at a time in a web application.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DatastoreQueryResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.DatastoreQueryResults)` | A task representing the asynchronous operation. When completed, the result of the task is the complete set of query results.  
  
### GetAsyncEnumerator(CancellationToken)
    
    
    public IAsyncEnumerator<Entity> GetAsyncEnumerator(CancellationToken cancellationToken)

Returns an enumerator that iterates asynchronously through the collection.

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) that may be used to cancel the asynchronous iteration.  
**Returns**  
---  
**Type** | **Description**  
`[IAsyncEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerator-1)[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity)` | An enumerator that can be used to iterate asynchronously through the collection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
