---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub
title: Class ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:00.986490+00:00
---

# Class ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub extends AbstractBlockingStub<ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service ExampleStoreService.

A service for managing and retrieving few-shot examples.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExampleStoreServiceGrpc.ExampleStoreServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createExampleStore(CreateExampleStoreRequest request)
    
    
    public Operation createExampleStore(CreateExampleStoreRequest request)

Create an ExampleStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExampleStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateExampleStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteExampleStore(DeleteExampleStoreRequest request)
    
    
    public Operation deleteExampleStore(DeleteExampleStoreRequest request)

Delete an ExampleStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExampleStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteExampleStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### fetchExamples(FetchExamplesRequest request)
    
    
    public FetchExamplesResponse fetchExamples(FetchExamplesRequest request)

Get Examples from the Example Store.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FetchExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FetchExamplesResponse)` |   
  
### getExampleStore(GetExampleStoreRequest request)
    
    
    public ExampleStore getExampleStore(GetExampleStoreRequest request)

Get an ExampleStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExampleStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetExampleStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExampleStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ExampleStore)` |   
  
### listExampleStores(ListExampleStoresRequest request)
    
    
    public ListExampleStoresResponse listExampleStores(ListExampleStoresRequest request)

List ExampleStores in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExampleStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListExampleStoresRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListExampleStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListExampleStoresResponse)` |   
  
### removeExamples(RemoveExamplesRequest request)
    
    
    public RemoveExamplesResponse removeExamples(RemoveExamplesRequest request)

Remove Examples from the Example Store.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RemoveExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RemoveExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.RemoveExamplesResponse)` |   
  
### searchExamples(SearchExamplesRequest request)
    
    
    public SearchExamplesResponse searchExamples(SearchExamplesRequest request)

Search for similar Examples for given selection criteria.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchExamplesResponse)` |   
  
### updateExampleStore(UpdateExampleStoreRequest request)
    
    
    public Operation updateExampleStore(UpdateExampleStoreRequest request)

Update an ExampleStore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExampleStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateExampleStoreRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### upsertExamples(UpsertExamplesRequest request)
    
    
    public UpsertExamplesResponse upsertExamples(UpsertExamplesRequest request)

Create or update Examples in the Example Store.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpsertExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpsertExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpsertExamplesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpsertExamplesResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
