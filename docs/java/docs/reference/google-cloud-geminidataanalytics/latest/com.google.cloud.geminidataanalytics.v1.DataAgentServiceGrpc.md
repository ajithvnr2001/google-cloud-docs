---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc
title: Class DataAgentServiceGrpc (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:30.293890+00:00
---

# Class DataAgentServiceGrpc (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataAgentServiceGrpc (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class DataAgentServiceGrpc

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataAgentServiceGrpc

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

### bindService(DataAgentServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(DataAgentServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[DataAgentServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateDataAgentMethod()
    
    
    public static MethodDescriptor<CreateDataAgentRequest,Operation> getCreateDataAgentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.CreateDataAgentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateDataAgentSyncMethod()
    
    
    public static MethodDescriptor<CreateDataAgentRequest,DataAgent> getCreateDataAgentSyncMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.CreateDataAgentRequest),[DataAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent)>` |   
  
### getDeleteDataAgentMethod()
    
    
    public static MethodDescriptor<DeleteDataAgentRequest,Operation> getDeleteDataAgentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DeleteDataAgentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteDataAgentSyncMethod()
    
    
    public static MethodDescriptor<DeleteDataAgentRequest,Empty> getDeleteDataAgentSyncMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DeleteDataAgentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetDataAgentMethod()
    
    
    public static MethodDescriptor<GetDataAgentRequest,DataAgent> getGetDataAgentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.GetDataAgentRequest),[DataAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent)>` |   
  
### getGetIamPolicyMethod()
    
    
    public static MethodDescriptor<GetIamPolicyRequest,Policy> getGetIamPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getListAccessibleDataAgentsMethod()
    
    
    public static MethodDescriptor<ListAccessibleDataAgentsRequest,ListAccessibleDataAgentsResponse> getListAccessibleDataAgentsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAccessibleDataAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListAccessibleDataAgentsRequest),[ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListAccessibleDataAgentsResponse)>` |   
  
### getListDataAgentsMethod()
    
    
    public static MethodDescriptor<ListDataAgentsRequest,ListDataAgentsResponse> getListDataAgentsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListDataAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListDataAgentsRequest),[ListDataAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListDataAgentsResponse)>` |   
  
### getRetrieveAgentOpsObservabilityMethod()
    
    
    public static MethodDescriptor<RetrieveAgentOpsObservabilityRequest,RetrieveAgentOpsObservabilityResponse> getRetrieveAgentOpsObservabilityMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.RetrieveAgentOpsObservabilityRequest),[RetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.RetrieveAgentOpsObservabilityResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getSetAgentOpsObservabilityMethod()
    
    
    public static MethodDescriptor<SetAgentOpsObservabilityRequest,Operation> getSetAgentOpsObservabilityMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SetAgentOpsObservabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.SetAgentOpsObservabilityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getSetIamPolicyMethod()
    
    
    public static MethodDescriptor<SetIamPolicyRequest,Policy> getSetIamPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getUpdateDataAgentMethod()
    
    
    public static MethodDescriptor<UpdateDataAgentRequest,Operation> getUpdateDataAgentMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.UpdateDataAgentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateDataAgentSyncMethod()
    
    
    public static MethodDescriptor<UpdateDataAgentRequest,DataAgent> getUpdateDataAgentSyncMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.UpdateDataAgentRequest),[DataAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static DataAgentServiceGrpc.DataAgentServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAgentServiceGrpc.DataAgentServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static DataAgentServiceGrpc.DataAgentServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAgentServiceGrpc.DataAgentServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static DataAgentServiceGrpc.DataAgentServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAgentServiceGrpc.DataAgentServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static DataAgentServiceGrpc.DataAgentServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAgentServiceGrpc.DataAgentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
