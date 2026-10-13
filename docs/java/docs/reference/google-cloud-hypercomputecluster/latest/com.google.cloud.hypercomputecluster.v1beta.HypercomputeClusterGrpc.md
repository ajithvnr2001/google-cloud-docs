---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc
title: Class HypercomputeClusterGrpc (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:17.003847+00:00
---

# Class HypercomputeClusterGrpc (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HypercomputeClusterGrpc (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class HypercomputeClusterGrpc

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > HypercomputeClusterGrpc

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

### bindService(HypercomputeClusterGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(HypercomputeClusterGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[HypercomputeClusterGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateClusterMethod()
    
    
    public static MethodDescriptor<CreateClusterRequest,Operation> getCreateClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteClusterMethod()
    
    
    public static MethodDescriptor<DeleteClusterRequest,Operation> getDeleteClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetClusterMethod()
    
    
    public static MethodDescriptor<GetClusterRequest,Cluster> getGetClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.Cluster)>` |   
  
### getListClustersMethod()
    
    
    public static MethodDescriptor<ListClustersRequest,ListClustersResponse> getListClustersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ListClustersResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateClusterMethod()
    
    
    public static MethodDescriptor<UpdateClusterRequest,Operation> getUpdateClusterMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static HypercomputeClusterGrpc.HypercomputeClusterBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HypercomputeClusterGrpc.HypercomputeClusterBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc.HypercomputeClusterBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static HypercomputeClusterGrpc.HypercomputeClusterBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HypercomputeClusterGrpc.HypercomputeClusterBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc.HypercomputeClusterBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static HypercomputeClusterGrpc.HypercomputeClusterFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HypercomputeClusterGrpc.HypercomputeClusterFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc.HypercomputeClusterFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static HypercomputeClusterGrpc.HypercomputeClusterStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[HypercomputeClusterGrpc.HypercomputeClusterStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.HypercomputeClusterGrpc.HypercomputeClusterStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
