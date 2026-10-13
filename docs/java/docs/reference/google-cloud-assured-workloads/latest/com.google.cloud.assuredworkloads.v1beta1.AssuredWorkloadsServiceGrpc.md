---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc
title: Class AssuredWorkloadsServiceGrpc (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:47.767805+00:00
---

# Class AssuredWorkloadsServiceGrpc (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AssuredWorkloadsServiceGrpc (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.1.0  2.0.0  1.1.0  1.0.4  0.9.0  0.8.2 
    
    
    public final class AssuredWorkloadsServiceGrpc

Service to manage AssuredWorkloads.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AssuredWorkloadsServiceGrpc

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

### bindService(AssuredWorkloadsServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(AssuredWorkloadsServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[AssuredWorkloadsServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAnalyzeWorkloadMoveMethod()
    
    
    public static MethodDescriptor<AnalyzeWorkloadMoveRequest,AnalyzeWorkloadMoveResponse> getAnalyzeWorkloadMoveMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AnalyzeWorkloadMoveRequest),[AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AnalyzeWorkloadMoveResponse)>` |   
  
### getCreateWorkloadMethod()
    
    
    public static MethodDescriptor<CreateWorkloadRequest,Operation> getCreateWorkloadMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.CreateWorkloadRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteWorkloadMethod()
    
    
    public static MethodDescriptor<DeleteWorkloadRequest,Empty> getDeleteWorkloadMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.DeleteWorkloadRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetWorkloadMethod()
    
    
    public static MethodDescriptor<GetWorkloadRequest,Workload> getGetWorkloadMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.GetWorkloadRequest),[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload)>` |   
  
### getListWorkloadsMethod()
    
    
    public static MethodDescriptor<ListWorkloadsRequest,ListWorkloadsResponse> getListWorkloadsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.ListWorkloadsRequest),[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.ListWorkloadsResponse)>` |   
  
### getRestrictAllowedResourcesMethod()
    
    
    public static MethodDescriptor<RestrictAllowedResourcesRequest,RestrictAllowedResourcesResponse> getRestrictAllowedResourcesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesRequest),[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateWorkloadMethod()
    
    
    public static MethodDescriptor<UpdateWorkloadRequest,Workload> getUpdateWorkloadMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.UpdateWorkloadRequest),[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
