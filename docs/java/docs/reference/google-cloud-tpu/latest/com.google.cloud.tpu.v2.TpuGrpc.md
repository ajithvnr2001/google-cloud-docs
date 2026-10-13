---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc
title: Class TpuGrpc (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:58.416866+00:00
---

# Class TpuGrpc (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TpuGrpc (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.2.6 
    
    
    public final class TpuGrpc

Manages TPU nodes and other resources TPU API v2

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TpuGrpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(TpuGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(TpuGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[TpuGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateNodeMethod()
    
    
    public static MethodDescriptor<CreateNodeRequest,Operation> getCreateNodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateQueuedResourceMethod()
    
    
    public static MethodDescriptor<CreateQueuedResourceRequest,Operation> getCreateQueuedResourceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateQueuedResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateQueuedResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteNodeMethod()
    
    
    public static MethodDescriptor<DeleteNodeRequest,Operation> getDeleteNodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.DeleteNodeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteQueuedResourceMethod()
    
    
    public static MethodDescriptor<DeleteQueuedResourceRequest,Operation> getDeleteQueuedResourceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteQueuedResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.DeleteQueuedResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGenerateServiceIdentityMethod()
    
    
    public static MethodDescriptor<GenerateServiceIdentityRequest,GenerateServiceIdentityResponse> getGenerateServiceIdentityMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GenerateServiceIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GenerateServiceIdentityRequest),[GenerateServiceIdentityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GenerateServiceIdentityResponse)>` |   
  
### getGetAcceleratorTypeMethod()
    
    
    public static MethodDescriptor<GetAcceleratorTypeRequest,AcceleratorType> getGetAcceleratorTypeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAcceleratorTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetAcceleratorTypeRequest),[AcceleratorType](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.AcceleratorType)>` |   
  
### getGetGuestAttributesMethod()
    
    
    public static MethodDescriptor<GetGuestAttributesRequest,GetGuestAttributesResponse> getGetGuestAttributesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetGuestAttributesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetGuestAttributesRequest),[GetGuestAttributesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetGuestAttributesResponse)>` |   
  
### getGetNodeMethod()
    
    
    public static MethodDescriptor<GetNodeRequest,Node> getGetNodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetNodeRequest),[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node)>` |   
  
### getGetQueuedResourceMethod()
    
    
    public static MethodDescriptor<GetQueuedResourceRequest,QueuedResource> getGetQueuedResourceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetQueuedResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetQueuedResourceRequest),[QueuedResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.QueuedResource)>` |   
  
### getGetRuntimeVersionMethod()
    
    
    public static MethodDescriptor<GetRuntimeVersionRequest,RuntimeVersion> getGetRuntimeVersionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetRuntimeVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetRuntimeVersionRequest),[RuntimeVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.RuntimeVersion)>` |   
  
### getListAcceleratorTypesMethod()
    
    
    public static MethodDescriptor<ListAcceleratorTypesRequest,ListAcceleratorTypesResponse> getListAcceleratorTypesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAcceleratorTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListAcceleratorTypesRequest),[ListAcceleratorTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListAcceleratorTypesResponse)>` |   
  
### getListNodesMethod()
    
    
    public static MethodDescriptor<ListNodesRequest,ListNodesResponse> getListNodesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListNodesRequest),[ListNodesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListNodesResponse)>` |   
  
### getListQueuedResourcesMethod()
    
    
    public static MethodDescriptor<ListQueuedResourcesRequest,ListQueuedResourcesResponse> getListQueuedResourcesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListQueuedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListQueuedResourcesRequest),[ListQueuedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListQueuedResourcesResponse)>` |   
  
### getListRuntimeVersionsMethod()
    
    
    public static MethodDescriptor<ListRuntimeVersionsRequest,ListRuntimeVersionsResponse> getListRuntimeVersionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListRuntimeVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListRuntimeVersionsRequest),[ListRuntimeVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListRuntimeVersionsResponse)>` |   
  
### getResetQueuedResourceMethod()
    
    
    public static MethodDescriptor<ResetQueuedResourceRequest,Operation> getResetQueuedResourceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ResetQueuedResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ResetQueuedResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getStartNodeMethod()
    
    
    public static MethodDescriptor<StartNodeRequest,Operation> getStartNodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StartNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StartNodeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getStopNodeMethod()
    
    
    public static MethodDescriptor<StopNodeRequest,Operation> getStopNodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StopNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StopNodeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateNodeMethod()
    
    
    public static MethodDescriptor<UpdateNodeRequest,Operation> getUpdateNodeMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.UpdateNodeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static TpuGrpc.TpuBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[TpuGrpc.TpuBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc.TpuBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static TpuGrpc.TpuBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[TpuGrpc.TpuBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc.TpuBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static TpuGrpc.TpuFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[TpuGrpc.TpuFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc.TpuFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static TpuGrpc.TpuStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[TpuGrpc.TpuStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuGrpc.TpuStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
