---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.DataObjectSearchServiceGrpc.DataObjectSearchServiceStub
title: Class DataObjectSearchServiceGrpc.DataObjectSearchServiceStub (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:57.136290+00:00
---

# Class DataObjectSearchServiceGrpc.DataObjectSearchServiceStub (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.DataObjectSearchServiceGrpc.DataObjectSearchServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataObjectSearchServiceGrpc.DataObjectSearchServiceStub (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class DataObjectSearchServiceGrpc.DataObjectSearchServiceStub extends AbstractAsyncStub<DataObjectSearchServiceGrpc.DataObjectSearchServiceStub>

A stub to allow clients to do asynchronous rpc calls to service DataObjectSearchService.

Service for searching data objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > DataObjectSearchServiceGrpc.DataObjectSearchServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

### aggregateDataObjects(AggregateDataObjectsRequest request, StreamObserver<AggregateDataObjectsResponse> responseObserver)
    
    
    public void aggregateDataObjects(AggregateDataObjectsRequest request, StreamObserver<AggregateDataObjectsResponse> responseObserver)

Aggregates data objects.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.AggregateDataObjectsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AggregateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.AggregateDataObjectsResponse)>`  
  
  
### batchSearchDataObjects(BatchSearchDataObjectsRequest request, StreamObserver<BatchSearchDataObjectsResponse> responseObserver)
    
    
    public void batchSearchDataObjects(BatchSearchDataObjectsRequest request, StreamObserver<BatchSearchDataObjectsResponse> responseObserver)

Batch searches data objects.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchSearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.BatchSearchDataObjectsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchSearchDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.BatchSearchDataObjectsResponse)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected DataObjectSearchServiceGrpc.DataObjectSearchServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceGrpc.DataObjectSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.DataObjectSearchServiceGrpc.DataObjectSearchServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### queryDataObjects(QueryDataObjectsRequest request, StreamObserver<QueryDataObjectsResponse> responseObserver)
    
    
    public void queryDataObjects(QueryDataObjectsRequest request, StreamObserver<QueryDataObjectsResponse> responseObserver)

Queries data objects.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.QueryDataObjectsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.QueryDataObjectsResponse)>`  
  
  
### searchDataObjects(SearchDataObjectsRequest request, StreamObserver<SearchDataObjectsResponse> responseObserver)
    
    
    public void searchDataObjects(SearchDataObjectsRequest request, StreamObserver<SearchDataObjectsResponse> responseObserver)

Searches data objects.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchDataObjectsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchDataObjectsResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
