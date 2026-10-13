---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptGrpc.InterceptStub
title: Class InterceptGrpc.InterceptStub (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:24.354939+00:00
---

# Class InterceptGrpc.InterceptStub (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptGrpc.InterceptStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InterceptGrpc.InterceptStub (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public static final class InterceptGrpc.InterceptStub extends AbstractAsyncStub<InterceptGrpc.InterceptStub>

A stub to allow clients to do asynchronous rpc calls to service Intercept.

Service for Third-Party Packet Intercept (TPPI). TPPI is the "in-band" flavor of the Network Security Integrations product.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > InterceptGrpc.InterceptStub

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
    
    
    protected InterceptGrpc.InterceptStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[InterceptGrpc.InterceptStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptGrpc.InterceptStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createInterceptDeployment(CreateInterceptDeploymentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInterceptDeployment(CreateInterceptDeploymentRequest request, StreamObserver<Operation> responseObserver)

Creates a deployment in a given project and location. See <https://google.aip.dev/133>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInterceptDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateInterceptDeploymentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createInterceptDeploymentGroup(CreateInterceptDeploymentGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInterceptDeploymentGroup(CreateInterceptDeploymentGroupRequest request, StreamObserver<Operation> responseObserver)

Creates a deployment group in a given project and location. See <https://google.aip.dev/133>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInterceptDeploymentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateInterceptDeploymentGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createInterceptEndpointGroup(CreateInterceptEndpointGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInterceptEndpointGroup(CreateInterceptEndpointGroupRequest request, StreamObserver<Operation> responseObserver)

Creates an endpoint group in a given project and location. See <https://google.aip.dev/133>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInterceptEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateInterceptEndpointGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createInterceptEndpointGroupAssociation(CreateInterceptEndpointGroupAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInterceptEndpointGroupAssociation(CreateInterceptEndpointGroupAssociationRequest request, StreamObserver<Operation> responseObserver)

Creates an association in a given project and location. See <https://google.aip.dev/133>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInterceptEndpointGroupAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateInterceptEndpointGroupAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInterceptDeployment(DeleteInterceptDeploymentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInterceptDeployment(DeleteInterceptDeploymentRequest request, StreamObserver<Operation> responseObserver)

Deletes a deployment. See <https://google.aip.dev/135>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInterceptDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteInterceptDeploymentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInterceptDeploymentGroup(DeleteInterceptDeploymentGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInterceptDeploymentGroup(DeleteInterceptDeploymentGroupRequest request, StreamObserver<Operation> responseObserver)

Deletes a deployment group. See <https://google.aip.dev/135>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInterceptDeploymentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteInterceptDeploymentGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInterceptEndpointGroup(DeleteInterceptEndpointGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInterceptEndpointGroup(DeleteInterceptEndpointGroupRequest request, StreamObserver<Operation> responseObserver)

Deletes an endpoint group. See <https://google.aip.dev/135>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInterceptEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteInterceptEndpointGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInterceptEndpointGroupAssociation(DeleteInterceptEndpointGroupAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInterceptEndpointGroupAssociation(DeleteInterceptEndpointGroupAssociationRequest request, StreamObserver<Operation> responseObserver)

Deletes an association. See <https://google.aip.dev/135>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInterceptEndpointGroupAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteInterceptEndpointGroupAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getInterceptDeployment(GetInterceptDeploymentRequest request, StreamObserver<InterceptDeployment> responseObserver)
    
    
    public void getInterceptDeployment(GetInterceptDeploymentRequest request, StreamObserver<InterceptDeployment> responseObserver)

Gets a specific deployment. See <https://google.aip.dev/131>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterceptDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetInterceptDeploymentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InterceptDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptDeployment)>`  
  
  
### getInterceptDeploymentGroup(GetInterceptDeploymentGroupRequest request, StreamObserver<InterceptDeploymentGroup> responseObserver)
    
    
    public void getInterceptDeploymentGroup(GetInterceptDeploymentGroupRequest request, StreamObserver<InterceptDeploymentGroup> responseObserver)

Gets a specific deployment group. See <https://google.aip.dev/131>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterceptDeploymentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetInterceptDeploymentGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InterceptDeploymentGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptDeploymentGroup)>`  
  
  
### getInterceptEndpointGroup(GetInterceptEndpointGroupRequest request, StreamObserver<InterceptEndpointGroup> responseObserver)
    
    
    public void getInterceptEndpointGroup(GetInterceptEndpointGroupRequest request, StreamObserver<InterceptEndpointGroup> responseObserver)

Gets a specific endpoint group. See <https://google.aip.dev/131>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterceptEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetInterceptEndpointGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InterceptEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptEndpointGroup)>`  
  
  
### getInterceptEndpointGroupAssociation(GetInterceptEndpointGroupAssociationRequest request, StreamObserver<InterceptEndpointGroupAssociation> responseObserver)
    
    
    public void getInterceptEndpointGroupAssociation(GetInterceptEndpointGroupAssociationRequest request, StreamObserver<InterceptEndpointGroupAssociation> responseObserver)

Gets a specific association. See <https://google.aip.dev/131>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInterceptEndpointGroupAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetInterceptEndpointGroupAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[InterceptEndpointGroupAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.InterceptEndpointGroupAssociation)>`  
  
  
### listInterceptDeploymentGroups(ListInterceptDeploymentGroupsRequest request, StreamObserver<ListInterceptDeploymentGroupsResponse> responseObserver)
    
    
    public void listInterceptDeploymentGroups(ListInterceptDeploymentGroupsRequest request, StreamObserver<ListInterceptDeploymentGroupsResponse> responseObserver)

Lists deployment groups in a given project and location. See <https://google.aip.dev/132>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterceptDeploymentGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptDeploymentGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInterceptDeploymentGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptDeploymentGroupsResponse)>`  
  
  
### listInterceptDeployments(ListInterceptDeploymentsRequest request, StreamObserver<ListInterceptDeploymentsResponse> responseObserver)
    
    
    public void listInterceptDeployments(ListInterceptDeploymentsRequest request, StreamObserver<ListInterceptDeploymentsResponse> responseObserver)

Lists deployments in a given project and location. See <https://google.aip.dev/132>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterceptDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptDeploymentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInterceptDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptDeploymentsResponse)>`  
  
  
### listInterceptEndpointGroupAssociations(ListInterceptEndpointGroupAssociationsRequest request, StreamObserver<ListInterceptEndpointGroupAssociationsResponse> responseObserver)
    
    
    public void listInterceptEndpointGroupAssociations(ListInterceptEndpointGroupAssociationsRequest request, StreamObserver<ListInterceptEndpointGroupAssociationsResponse> responseObserver)

Lists associations in a given project and location. See <https://google.aip.dev/132>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterceptEndpointGroupAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptEndpointGroupAssociationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInterceptEndpointGroupAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptEndpointGroupAssociationsResponse)>`  
  
  
### listInterceptEndpointGroups(ListInterceptEndpointGroupsRequest request, StreamObserver<ListInterceptEndpointGroupsResponse> responseObserver)
    
    
    public void listInterceptEndpointGroups(ListInterceptEndpointGroupsRequest request, StreamObserver<ListInterceptEndpointGroupsResponse> responseObserver)

Lists endpoint groups in a given project and location. See <https://google.aip.dev/132>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInterceptEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptEndpointGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInterceptEndpointGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListInterceptEndpointGroupsResponse)>`  
  
  
### updateInterceptDeployment(UpdateInterceptDeploymentRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInterceptDeployment(UpdateInterceptDeploymentRequest request, StreamObserver<Operation> responseObserver)

Updates a deployment. See <https://google.aip.dev/134>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInterceptDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateInterceptDeploymentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInterceptDeploymentGroup(UpdateInterceptDeploymentGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInterceptDeploymentGroup(UpdateInterceptDeploymentGroupRequest request, StreamObserver<Operation> responseObserver)

Updates a deployment group. See <https://google.aip.dev/134>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInterceptDeploymentGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateInterceptDeploymentGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInterceptEndpointGroup(UpdateInterceptEndpointGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInterceptEndpointGroup(UpdateInterceptEndpointGroupRequest request, StreamObserver<Operation> responseObserver)

Updates an endpoint group. See <https://google.aip.dev/134>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInterceptEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateInterceptEndpointGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInterceptEndpointGroupAssociation(UpdateInterceptEndpointGroupAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInterceptEndpointGroupAssociation(UpdateInterceptEndpointGroupAssociationRequest request, StreamObserver<Operation> responseObserver)

Updates an association. See <https://google.aip.dev/134>.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInterceptEndpointGroupAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateInterceptEndpointGroupAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
