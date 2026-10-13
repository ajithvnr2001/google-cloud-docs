---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreStub
title: Class LustreGrpc.LustreStub (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:31.321047+00:00
---

# Class LustreGrpc.LustreStub (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LustreGrpc.LustreStub (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static final class LustreGrpc.LustreStub extends AbstractAsyncStub<LustreGrpc.LustreStub>

A stub to allow clients to do asynchronous rpc calls to service Lustre.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > LustreGrpc.LustreStub

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected LustreGrpc.LustreStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[LustreGrpc.LustreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.LustreGrpc.LustreStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createDirectoryPolicy(CreateDirectoryPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createDirectoryPolicy(CreateDirectoryPolicyRequest request, StreamObserver<Operation> responseObserver)

Creates a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDirectoryPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.CreateDirectoryPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)

Creates a new instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.CreateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createMirror(CreateMirrorRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createMirror(CreateMirrorRequest request, StreamObserver<Operation> responseObserver)

Creates a new mirror in a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.CreateMirrorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteDirectoryPolicy(DeleteDirectoryPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteDirectoryPolicy(DeleteDirectoryPolicyRequest request, StreamObserver<Operation> responseObserver)

Deletes a directory policy resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DeleteDirectoryPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)

Deletes a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DeleteInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMirror(DeleteMirrorRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteMirror(DeleteMirrorRequest request, StreamObserver<Operation> responseObserver)

Deletes a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DeleteMirrorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### exportData(ExportDataRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void exportData(ExportDataRequest request, StreamObserver<Operation> responseObserver)

Exports data from a Managed Lustre instance to Cloud Storage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ExportDataRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getDirectoryPolicy(GetDirectoryPolicyRequest request, StreamObserver<DirectoryPolicy> responseObserver)
    
    
    public void getDirectoryPolicy(GetDirectoryPolicyRequest request, StreamObserver<DirectoryPolicy> responseObserver)

Gets details of a single directory policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDirectoryPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GetDirectoryPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DirectoryPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.DirectoryPolicy)>`  
  
  
### getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)
    
    
    public void getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)

Gets details of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GetInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.Instance)>`  
  
  
### getMirror(GetMirrorRequest request, StreamObserver<Mirror> responseObserver)
    
    
    public void getMirror(GetMirrorRequest request, StreamObserver<Mirror> responseObserver)

Gets details of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.GetMirrorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Mirror](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.Mirror)>`  
  
  
### importData(ImportDataRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void importData(ImportDataRequest request, StreamObserver<Operation> responseObserver)

Imports data from Cloud Storage to a Managed Lustre instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ImportDataRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### listDirectoryPolicies(ListDirectoryPoliciesRequest request, StreamObserver<ListDirectoryPoliciesResponse> responseObserver)
    
    
    public void listDirectoryPolicies(ListDirectoryPoliciesRequest request, StreamObserver<ListDirectoryPoliciesResponse> responseObserver)

Gets details of multiple directory policies under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDirectoryPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListDirectoryPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDirectoryPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListDirectoryPoliciesResponse)>`  
  
  
### listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)
    
    
    public void listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)

Lists instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListInstancesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListInstancesResponse)>`  
  
  
### listMirrors(ListMirrorsRequest request, StreamObserver<ListMirrorsResponse> responseObserver)
    
    
    public void listMirrors(ListMirrorsRequest request, StreamObserver<ListMirrorsResponse> responseObserver)

Gets details of multiple mirrors under a given instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMirrorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListMirrorsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMirrorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.ListMirrorsResponse)>`  
  
  
### rescheduleMaintenance(RescheduleMaintenanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void rescheduleMaintenance(RescheduleMaintenanceRequest request, StreamObserver<Operation> responseObserver)

Reschedules a planned maintenance event for a specific instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.RescheduleMaintenanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.UpdateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateMirror(UpdateMirrorRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateMirror(UpdateMirrorRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single mirror.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMirrorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.UpdateMirrorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
