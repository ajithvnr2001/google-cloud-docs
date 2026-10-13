---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc
title: Class LiveVideoAnalyticsGrpc (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:20.127723+00:00
---

# Class LiveVideoAnalyticsGrpc (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LiveVideoAnalyticsGrpc (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class LiveVideoAnalyticsGrpc

Service describing handlers for resources. The service enables clients to run Live Video Analytics (LVA) on the streaming inputs.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LiveVideoAnalyticsGrpc

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

### bindService(LiveVideoAnalyticsGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(LiveVideoAnalyticsGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[LiveVideoAnalyticsGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getBatchRunProcessMethod()
    
    
    public static MethodDescriptor<BatchRunProcessRequest,Operation> getBatchRunProcessMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchRunProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.BatchRunProcessRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateAnalysisMethod()
    
    
    public static MethodDescriptor<CreateAnalysisRequest,Operation> getCreateAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateAnalysisRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateOperatorMethod()
    
    
    public static MethodDescriptor<CreateOperatorRequest,Operation> getCreateOperatorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateOperatorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateOperatorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateProcessMethod()
    
    
    public static MethodDescriptor<CreateProcessRequest,Operation> getCreateProcessMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.CreateProcessRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteAnalysisMethod()
    
    
    public static MethodDescriptor<DeleteAnalysisRequest,Operation> getDeleteAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteAnalysisRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteOperatorMethod()
    
    
    public static MethodDescriptor<DeleteOperatorRequest,Operation> getDeleteOperatorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteOperatorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteOperatorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteProcessMethod()
    
    
    public static MethodDescriptor<DeleteProcessRequest,Operation> getDeleteProcessMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DeleteProcessRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetAnalysisMethod()
    
    
    public static MethodDescriptor<GetAnalysisRequest,Analysis> getGetAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetAnalysisRequest),[Analysis](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Analysis)>` |   
  
### getGetOperatorMethod()
    
    
    public static MethodDescriptor<GetOperatorRequest,Operator> getGetOperatorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetOperatorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetOperatorRequest),[Operator](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Operator)>` |   
  
### getGetProcessMethod()
    
    
    public static MethodDescriptor<GetProcessRequest,Process> getGetProcessMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.GetProcessRequest),[Process](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Process)>` |   
  
### getListAnalysesMethod()
    
    
    public static MethodDescriptor<ListAnalysesRequest,ListAnalysesResponse> getListAnalysesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAnalysesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListAnalysesRequest),[ListAnalysesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListAnalysesResponse)>` |   
  
### getListOperatorsMethod()
    
    
    public static MethodDescriptor<ListOperatorsRequest,ListOperatorsResponse> getListOperatorsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListOperatorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListOperatorsRequest),[ListOperatorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListOperatorsResponse)>` |   
  
### getListProcessesMethod()
    
    
    public static MethodDescriptor<ListProcessesRequest,ListProcessesResponse> getListProcessesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListProcessesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListProcessesRequest),[ListProcessesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListProcessesResponse)>` |   
  
### getListPublicOperatorsMethod()
    
    
    public static MethodDescriptor<ListPublicOperatorsRequest,ListPublicOperatorsResponse> getListPublicOperatorsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPublicOperatorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListPublicOperatorsRequest),[ListPublicOperatorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ListPublicOperatorsResponse)>` |   
  
### getResolveOperatorInfoMethod()
    
    
    public static MethodDescriptor<ResolveOperatorInfoRequest,ResolveOperatorInfoResponse> getResolveOperatorInfoMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ResolveOperatorInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ResolveOperatorInfoRequest),[ResolveOperatorInfoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ResolveOperatorInfoResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateAnalysisMethod()
    
    
    public static MethodDescriptor<UpdateAnalysisRequest,Operation> getUpdateAnalysisMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAnalysisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateAnalysisRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateOperatorMethod()
    
    
    public static MethodDescriptor<UpdateOperatorRequest,Operation> getUpdateOperatorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateOperatorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateOperatorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateProcessMethod()
    
    
    public static MethodDescriptor<UpdateProcessRequest,Operation> getUpdateProcessMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.UpdateProcessRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static LiveVideoAnalyticsGrpc.LiveVideoAnalyticsBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveVideoAnalyticsGrpc.LiveVideoAnalyticsBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc.LiveVideoAnalyticsBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static LiveVideoAnalyticsGrpc.LiveVideoAnalyticsBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveVideoAnalyticsGrpc.LiveVideoAnalyticsBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc.LiveVideoAnalyticsBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static LiveVideoAnalyticsGrpc.LiveVideoAnalyticsFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveVideoAnalyticsGrpc.LiveVideoAnalyticsFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc.LiveVideoAnalyticsFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static LiveVideoAnalyticsGrpc.LiveVideoAnalyticsStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveVideoAnalyticsGrpc.LiveVideoAnalyticsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.LiveVideoAnalyticsGrpc.LiveVideoAnalyticsStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
