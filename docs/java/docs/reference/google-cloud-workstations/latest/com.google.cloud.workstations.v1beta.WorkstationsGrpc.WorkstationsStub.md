---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.WorkstationsGrpc.WorkstationsStub
title: Class WorkstationsGrpc.WorkstationsStub (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:40.104307+00:00
---

# Class WorkstationsGrpc.WorkstationsStub (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.WorkstationsGrpc.WorkstationsStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WorkstationsGrpc.WorkstationsStub (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.0  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class WorkstationsGrpc.WorkstationsStub extends AbstractAsyncStub<WorkstationsGrpc.WorkstationsStub>

A stub to allow clients to do asynchronous rpc calls to service Workstations.

Service for interacting with Cloud Workstations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > WorkstationsGrpc.WorkstationsStub

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
    
    
    protected WorkstationsGrpc.WorkstationsStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationsGrpc.WorkstationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.WorkstationsGrpc.WorkstationsStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createWorkstation(CreateWorkstationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createWorkstation(CreateWorkstationRequest request, StreamObserver<Operation> responseObserver)

Creates a new workstation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.CreateWorkstationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createWorkstationCluster(CreateWorkstationClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createWorkstationCluster(CreateWorkstationClusterRequest request, StreamObserver<Operation> responseObserver)

Creates a new workstation cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.CreateWorkstationClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createWorkstationConfig(CreateWorkstationConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createWorkstationConfig(CreateWorkstationConfigRequest request, StreamObserver<Operation> responseObserver)

Creates a new workstation configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.CreateWorkstationConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWorkstation(DeleteWorkstationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteWorkstation(DeleteWorkstationRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified workstation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.DeleteWorkstationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWorkstationCluster(DeleteWorkstationClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteWorkstationCluster(DeleteWorkstationClusterRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified workstation cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.DeleteWorkstationClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteWorkstationConfig(DeleteWorkstationConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteWorkstationConfig(DeleteWorkstationConfigRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified workstation configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.DeleteWorkstationConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### generateAccessToken(GenerateAccessTokenRequest request, StreamObserver<GenerateAccessTokenResponse> responseObserver)
    
    
    public void generateAccessToken(GenerateAccessTokenRequest request, StreamObserver<GenerateAccessTokenResponse> responseObserver)

Returns a short-lived credential that can be used to send authenticated and authorized traffic to a workstation. Once generated this token cannot be revoked and is good for the lifetime of the token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateAccessTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.GenerateAccessTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.GenerateAccessTokenResponse)>`  
  
  
### getWorkstation(GetWorkstationRequest request, StreamObserver<Workstation> responseObserver)
    
    
    public void getWorkstation(GetWorkstationRequest request, StreamObserver<Workstation> responseObserver)

Returns the requested workstation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.GetWorkstationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.Workstation)>`  
  
  
### getWorkstationCluster(GetWorkstationClusterRequest request, StreamObserver<WorkstationCluster> responseObserver)
    
    
    public void getWorkstationCluster(GetWorkstationClusterRequest request, StreamObserver<WorkstationCluster> responseObserver)

Returns the requested workstation cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.GetWorkstationClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkstationCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.WorkstationCluster)>`  
  
  
### getWorkstationConfig(GetWorkstationConfigRequest request, StreamObserver<WorkstationConfig> responseObserver)
    
    
    public void getWorkstationConfig(GetWorkstationConfigRequest request, StreamObserver<WorkstationConfig> responseObserver)

Returns the requested workstation configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.GetWorkstationConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.WorkstationConfig)>`  
  
  
### listUsableWorkstationConfigs(ListUsableWorkstationConfigsRequest request, StreamObserver<ListUsableWorkstationConfigsResponse> responseObserver)
    
    
    public void listUsableWorkstationConfigs(ListUsableWorkstationConfigsRequest request, StreamObserver<ListUsableWorkstationConfigsResponse> responseObserver)

Returns all workstation configurations in the specified cluster on which the caller has the "workstations.workstation.create" permission.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableWorkstationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListUsableWorkstationConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUsableWorkstationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListUsableWorkstationConfigsResponse)>`  
  
  
### listUsableWorkstations(ListUsableWorkstationsRequest request, StreamObserver<ListUsableWorkstationsResponse> responseObserver)
    
    
    public void listUsableWorkstations(ListUsableWorkstationsRequest request, StreamObserver<ListUsableWorkstationsResponse> responseObserver)

Returns all workstations using the specified workstation configuration on which the caller has the "workstations.workstations.use" permission.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUsableWorkstationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListUsableWorkstationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUsableWorkstationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListUsableWorkstationsResponse)>`  
  
  
### listWorkstationClusters(ListWorkstationClustersRequest request, StreamObserver<ListWorkstationClustersResponse> responseObserver)
    
    
    public void listWorkstationClusters(ListWorkstationClustersRequest request, StreamObserver<ListWorkstationClustersResponse> responseObserver)

Returns all workstation clusters in the specified location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkstationClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListWorkstationClustersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkstationClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListWorkstationClustersResponse)>`  
  
  
### listWorkstationConfigs(ListWorkstationConfigsRequest request, StreamObserver<ListWorkstationConfigsResponse> responseObserver)
    
    
    public void listWorkstationConfigs(ListWorkstationConfigsRequest request, StreamObserver<ListWorkstationConfigsResponse> responseObserver)

Returns all workstation configurations in the specified cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkstationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListWorkstationConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkstationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListWorkstationConfigsResponse)>`  
  
  
### listWorkstations(ListWorkstationsRequest request, StreamObserver<ListWorkstationsResponse> responseObserver)
    
    
    public void listWorkstations(ListWorkstationsRequest request, StreamObserver<ListWorkstationsResponse> responseObserver)

Returns all Workstations using the specified workstation configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkstationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListWorkstationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkstationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.ListWorkstationsResponse)>`  
  
  
### pushCredentials(PushCredentialsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void pushCredentials(PushCredentialsRequest request, StreamObserver<Operation> responseObserver)

Pushes credentials to a running workstation on behalf of a user. Once complete, supported credential types (application_default_credentials) are made available to processes running in the user container.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PushCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.PushCredentialsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### startWorkstation(StartWorkstationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void startWorkstation(StartWorkstationRequest request, StreamObserver<Operation> responseObserver)

Starts running a workstation so that users can connect to it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.StartWorkstationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### stopWorkstation(StopWorkstationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void stopWorkstation(StopWorkstationRequest request, StreamObserver<Operation> responseObserver)

Stops running a workstation, reducing costs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.StopWorkstationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateWorkstation(UpdateWorkstationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateWorkstation(UpdateWorkstationRequest request, StreamObserver<Operation> responseObserver)

Updates an existing workstation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.UpdateWorkstationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateWorkstationCluster(UpdateWorkstationClusterRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateWorkstationCluster(UpdateWorkstationClusterRequest request, StreamObserver<Operation> responseObserver)

Updates an existing workstation cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.UpdateWorkstationClusterRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateWorkstationConfig(UpdateWorkstationConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateWorkstationConfig(UpdateWorkstationConfigRequest request, StreamObserver<Operation> responseObserver)

Updates an existing workstation configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.UpdateWorkstationConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
