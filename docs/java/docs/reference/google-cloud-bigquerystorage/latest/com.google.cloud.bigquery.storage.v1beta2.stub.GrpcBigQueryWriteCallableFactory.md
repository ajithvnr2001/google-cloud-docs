---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta2.stub.GrpcBigQueryWriteCallableFactory
title: Class GrpcBigQueryWriteCallableFactory (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:36.826624+00:00
---

# Class GrpcBigQueryWriteCallableFactory (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1beta2.stub.GrpcBigQueryWriteCallableFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrpcBigQueryWriteCallableFactory (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public class GrpcBigQueryWriteCallableFactory implements GrpcStubCallableFactory

**Deprecated.** _This class is deprecated and will be removed in the next major version update._

gRPC callable factory implementation for the BigQueryWrite service API.

This class is for advanced usage.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GrpcBigQueryWriteCallableFactory

## Implements

[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)

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

## Constructors 

### GrpcBigQueryWriteCallableFactory() (deprecated)
    
    
    public GrpcBigQueryWriteCallableFactory()

## Methods 

### <RequestT,ResponseT,MetadataT>createOperationCallable(GrpcCallSettings<RequestT,Operation> grpcCallSettings, OperationCallSettings<RequestT,ResponseT,MetadataT> callSettings, ClientContext clientContext, OperationsStub operationsStub) (deprecated)
    
    
    public OperationCallable<RequestT,ResponseT,MetadataT> <RequestT,ResponseT,MetadataT>createOperationCallable(GrpcCallSettings<RequestT,Operation> grpcCallSettings, OperationCallSettings<RequestT,ResponseT,MetadataT> callSettings, ClientContext clientContext, OperationsStub operationsStub)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
`callSettings` | `[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<RequestT,ResponseT,MetadataT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`operationsStub` | `[OperationsStub](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.stub.OperationsStub.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<RequestT,ResponseT,MetadataT>` |   
  
### <RequestT,ResponseT,PagedListResponseT>createPagedCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, PagedCallSettings<RequestT,ResponseT,PagedListResponseT> callSettings, ClientContext clientContext) (deprecated)
    
    
    public UnaryCallable<RequestT,PagedListResponseT> <RequestT,ResponseT,PagedListResponseT>createPagedCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, PagedCallSettings<RequestT,ResponseT,PagedListResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,ResponseT>`  
  
`callSettings` | `[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<RequestT,ResponseT,PagedListResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<RequestT,PagedListResponseT>` |   
  
### <RequestT,ResponseT>createBatchingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, BatchingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext) (deprecated)
    
    
    public UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>createBatchingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, BatchingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,ResponseT>`  
  
`callSettings` | `[BatchingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingCallSettings.html)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<RequestT,ResponseT>` |   
  
### <RequestT,ResponseT>createBidiStreamingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, StreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext) (deprecated)
    
    
    public BidiStreamingCallable<RequestT,ResponseT> <RequestT,ResponseT>createBidiStreamingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, StreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,ResponseT>`  
  
`callSettings` | `[StreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings.html)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BidiStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable.html)<RequestT,ResponseT>` |   
  
### <RequestT,ResponseT>createClientStreamingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, StreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext) (deprecated)
    
    
    public ClientStreamingCallable<RequestT,ResponseT> <RequestT,ResponseT>createClientStreamingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, StreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,ResponseT>`  
  
`callSettings` | `[StreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings.html)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientStreamingCallable.html)<RequestT,ResponseT>` |   
  
### <RequestT,ResponseT>createServerStreamingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, ServerStreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext) (deprecated)
    
    
    public ServerStreamingCallable<RequestT,ResponseT> <RequestT,ResponseT>createServerStreamingCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, ServerStreamingCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,ResponseT>`  
  
`callSettings` | `[ServerStreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings.html)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable.html)<RequestT,ResponseT>` |   
  
### <RequestT,ResponseT>createUnaryCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, UnaryCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext) (deprecated)
    
    
    public UnaryCallable<RequestT,ResponseT> <RequestT,ResponseT>createUnaryCallable(GrpcCallSettings<RequestT,ResponseT> grpcCallSettings, UnaryCallSettings<RequestT,ResponseT> callSettings, ClientContext clientContext)

**Parameters**  
---  
**Name** | **Description**  
`grpcCallSettings` | `[GrpcCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcCallSettings.html)<RequestT,ResponseT>`  
  
`callSettings` | `[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<RequestT,ResponseT>`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<RequestT,ResponseT>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
