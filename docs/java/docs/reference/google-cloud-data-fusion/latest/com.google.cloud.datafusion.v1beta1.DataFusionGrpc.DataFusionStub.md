---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionGrpc.DataFusionStub
title: Class DataFusionGrpc.DataFusionStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:27.584900+00:00
---

# Class DataFusionGrpc.DataFusionStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionGrpc.DataFusionStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataFusionGrpc.DataFusionStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.1.1 
    
    
    public static final class DataFusionGrpc.DataFusionStub extends AbstractAsyncStub<DataFusionGrpc.DataFusionStub>

A stub to allow clients to do asynchronous rpc calls to service DataFusion.

Service for creating and managing Data Fusion instances. Data Fusion enables ETL developers to build code-free, data integration pipelines via a point-and-click UI.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > DataFusionGrpc.DataFusionStub

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

### addDnsPeering(AddDnsPeeringRequest request, StreamObserver<AddDnsPeeringResponse> responseObserver)
    
    
    public void addDnsPeering(AddDnsPeeringRequest request, StreamObserver<AddDnsPeeringResponse> responseObserver)

Add DNS peering on the given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddDnsPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AddDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.AddDnsPeeringResponse)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected DataFusionGrpc.DataFusionStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataFusionGrpc.DataFusionStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DataFusionGrpc.DataFusionStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)

Creates a new Data Fusion instance in the specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.CreateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Data Fusion instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.DeleteInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)
    
    
    public void getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)

Gets details of a single Data Fusion instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.GetInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.Instance)>`  
  
  
### listAvailableVersions(ListAvailableVersionsRequest request, StreamObserver<ListAvailableVersionsResponse> responseObserver)
    
    
    public void listAvailableVersions(ListAvailableVersionsRequest request, StreamObserver<ListAvailableVersionsResponse> responseObserver)

Lists possible versions for Data Fusion instances in the specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAvailableVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListAvailableVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAvailableVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListAvailableVersionsResponse)>`  
  
  
### listDnsPeerings(ListDnsPeeringsRequest request, StreamObserver<ListDnsPeeringsResponse> responseObserver)
    
    
    public void listDnsPeerings(ListDnsPeeringsRequest request, StreamObserver<ListDnsPeeringsResponse> responseObserver)

List DNS peering for a given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDnsPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListDnsPeeringsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDnsPeeringsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListDnsPeeringsResponse)>`  
  
  
### listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)
    
    
    public void listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)

Lists Data Fusion instances in the specified project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListInstancesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListInstancesResponse)>`  
  
  
### listNamespaces(ListNamespacesRequest request, StreamObserver<ListNamespacesResponse> responseObserver)
    
    
    public void listNamespaces(ListNamespacesRequest request, StreamObserver<ListNamespacesResponse> responseObserver)

List namespaces in a given instance

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListNamespacesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNamespacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.ListNamespacesResponse)>`  
  
  
### removeDnsPeering(RemoveDnsPeeringRequest request, StreamObserver<RemoveDnsPeeringResponse> responseObserver)
    
    
    public void removeDnsPeering(RemoveDnsPeeringRequest request, StreamObserver<RemoveDnsPeeringResponse> responseObserver)

Remove DNS peering on the given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveDnsPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RemoveDnsPeeringResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveDnsPeeringResponse)>`  
  
  
### removeIamPolicy(RemoveIamPolicyRequest request, StreamObserver<RemoveIamPolicyResponse> responseObserver)
    
    
    public void removeIamPolicy(RemoveIamPolicyRequest request, StreamObserver<RemoveIamPolicyResponse> responseObserver)

Remove IAM policy that is currently set on the given resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveIamPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RemoveIamPolicyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RemoveIamPolicyResponse)>`  
  
  
### restartInstance(RestartInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void restartInstance(RestartInstanceRequest request, StreamObserver<Operation> responseObserver)

Restart a single Data Fusion instance. At the end of an operation instance is fully restarted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.RestartInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)

Updates a single Data Fusion instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpdateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### upgradeInstance(UpgradeInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void upgradeInstance(UpgradeInstanceRequest request, StreamObserver<Operation> responseObserver)

Upgrade a single Data Fusion instance. At the end of an operation instance is fully upgraded.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-data-fusion/latest/com.google.cloud.datafusion.v1beta1.UpgradeInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
