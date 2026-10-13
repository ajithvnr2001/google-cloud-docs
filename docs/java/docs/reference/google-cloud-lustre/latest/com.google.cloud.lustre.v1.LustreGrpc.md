---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc
title: Class LustreGrpc (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:44.198014+00:00
---

# Class LustreGrpc (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LustreGrpc (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public final class LustreGrpc

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LustreGrpc

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

### bindService(LustreGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(LustreGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[LustreGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateDirectoryPolicyMethod()
    
    
    public static MethodDescriptor<CreateDirectoryPolicyRequest,Operation> getCreateDirectoryPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateDirectoryPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.CreateDirectoryPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateInstanceMethod()
    
    
    public static MethodDescriptor<CreateInstanceRequest,Operation> getCreateInstanceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateMirrorMethod()
    
    
    public static MethodDescriptor<CreateMirrorRequest,Operation> getCreateMirrorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.CreateMirrorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteDirectoryPolicyMethod()
    
    
    public static MethodDescriptor<DeleteDirectoryPolicyRequest,Operation> getDeleteDirectoryPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DeleteDirectoryPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteInstanceMethod()
    
    
    public static MethodDescriptor<DeleteInstanceRequest,Operation> getDeleteInstanceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteMirrorMethod()
    
    
    public static MethodDescriptor<DeleteMirrorRequest,Operation> getDeleteMirrorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DeleteMirrorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getExportDataMethod()
    
    
    public static MethodDescriptor<ExportDataRequest,Operation> getExportDataMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ExportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetDirectoryPolicyMethod()
    
    
    public static MethodDescriptor<GetDirectoryPolicyRequest,DirectoryPolicy> getGetDirectoryPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetDirectoryPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GetDirectoryPolicyRequest),[DirectoryPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DirectoryPolicy)>` |   
  
### getGetInstanceMethod()
    
    
    public static MethodDescriptor<GetInstanceRequest,Instance> getGetInstanceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.Instance)>` |   
  
### getGetMirrorMethod()
    
    
    public static MethodDescriptor<GetMirrorRequest,Mirror> getGetMirrorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GetMirrorRequest),[Mirror](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.Mirror)>` |   
  
### getImportDataMethod()
    
    
    public static MethodDescriptor<ImportDataRequest,Operation> getImportDataMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ImportDataRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getListDirectoryPoliciesMethod()
    
    
    public static MethodDescriptor<ListDirectoryPoliciesRequest,ListDirectoryPoliciesResponse> getListDirectoryPoliciesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListDirectoryPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListDirectoryPoliciesRequest),[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListDirectoryPoliciesResponse)>` |   
  
### getListInstancesMethod()
    
    
    public static MethodDescriptor<ListInstancesRequest,ListInstancesResponse> getListInstancesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListInstancesResponse)>` |   
  
### getListMirrorsMethod()
    
    
    public static MethodDescriptor<ListMirrorsRequest,ListMirrorsResponse> getListMirrorsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListMirrorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListMirrorsRequest),[ListMirrorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListMirrorsResponse)>` |   
  
### getRescheduleMaintenanceMethod()
    
    
    public static MethodDescriptor<RescheduleMaintenanceRequest,Operation> getRescheduleMaintenanceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.RescheduleMaintenanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateInstanceMethod()
    
    
    public static MethodDescriptor<UpdateInstanceRequest,Operation> getUpdateInstanceMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateMirrorMethod()
    
    
    public static MethodDescriptor<UpdateMirrorRequest,Operation> getUpdateMirrorMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.UpdateMirrorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static LustreGrpc.LustreBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LustreGrpc.LustreBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static LustreGrpc.LustreBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LustreGrpc.LustreBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static LustreGrpc.LustreFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LustreGrpc.LustreFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static LustreGrpc.LustreStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LustreGrpc.LustreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
