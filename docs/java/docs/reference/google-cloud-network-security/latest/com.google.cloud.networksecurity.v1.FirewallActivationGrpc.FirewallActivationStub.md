---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.FirewallActivationGrpc.FirewallActivationStub
title: Class FirewallActivationGrpc.FirewallActivationStub (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:39.439452+00:00
---

# Class FirewallActivationGrpc.FirewallActivationStub (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.FirewallActivationGrpc.FirewallActivationStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FirewallActivationGrpc.FirewallActivationStub (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public static final class FirewallActivationGrpc.FirewallActivationStub extends AbstractAsyncStub<FirewallActivationGrpc.FirewallActivationStub>

A stub to allow clients to do asynchronous rpc calls to service FirewallActivation.

Service for managing Firewall Endpoints and Associations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > FirewallActivationGrpc.FirewallActivationStub

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
    
    
    protected FirewallActivationGrpc.FirewallActivationStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirewallActivationGrpc.FirewallActivationStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.FirewallActivationGrpc.FirewallActivationStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createFirewallEndpoint(CreateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createFirewallEndpoint(CreateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)

Creates a new FirewallEndpoint in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createFirewallEndpointAssociation(CreateFirewallEndpointAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createFirewallEndpointAssociation(CreateFirewallEndpointAssociationRequest request, StreamObserver<Operation> responseObserver)

Creates a new FirewallEndpointAssociation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateFirewallEndpointAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createProjectFirewallEndpoint(CreateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createProjectFirewallEndpoint(CreateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)

Creates a new FirewallEndpoint in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteFirewallEndpoint(DeleteFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteFirewallEndpoint(DeleteFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)

Deletes a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteFirewallEndpointAssociation(DeleteFirewallEndpointAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteFirewallEndpointAssociation(DeleteFirewallEndpointAssociationRequest request, StreamObserver<Operation> responseObserver)

Deletes a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteFirewallEndpointAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteProjectFirewallEndpoint(DeleteFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteProjectFirewallEndpoint(DeleteFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)

Deletes a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getFirewallEndpoint(GetFirewallEndpointRequest request, StreamObserver<FirewallEndpoint> responseObserver)
    
    
    public void getFirewallEndpoint(GetFirewallEndpointRequest request, StreamObserver<FirewallEndpoint> responseObserver)

Gets details of a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FirewallEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.FirewallEndpoint)>`  
  
  
### getFirewallEndpointAssociation(GetFirewallEndpointAssociationRequest request, StreamObserver<FirewallEndpointAssociation> responseObserver)
    
    
    public void getFirewallEndpointAssociation(GetFirewallEndpointAssociationRequest request, StreamObserver<FirewallEndpointAssociation> responseObserver)

Gets details of a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetFirewallEndpointAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FirewallEndpointAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.FirewallEndpointAssociation)>`  
  
  
### getProjectFirewallEndpoint(GetFirewallEndpointRequest request, StreamObserver<FirewallEndpoint> responseObserver)
    
    
    public void getProjectFirewallEndpoint(GetFirewallEndpointRequest request, StreamObserver<FirewallEndpoint> responseObserver)

Gets details of a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FirewallEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.FirewallEndpoint)>`  
  
  
### listFirewallEndpointAssociations(ListFirewallEndpointAssociationsRequest request, StreamObserver<ListFirewallEndpointAssociationsResponse> responseObserver)
    
    
    public void listFirewallEndpointAssociations(ListFirewallEndpointAssociationsRequest request, StreamObserver<ListFirewallEndpointAssociationsResponse> responseObserver)

Lists Associations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListFirewallEndpointAssociationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFirewallEndpointAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListFirewallEndpointAssociationsResponse)>`  
  
  
### listFirewallEndpoints(ListFirewallEndpointsRequest request, StreamObserver<ListFirewallEndpointsResponse> responseObserver)
    
    
    public void listFirewallEndpoints(ListFirewallEndpointsRequest request, StreamObserver<ListFirewallEndpointsResponse> responseObserver)

Lists FirewallEndpoints in a given organization and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListFirewallEndpointsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFirewallEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListFirewallEndpointsResponse)>`  
  
  
### listProjectFirewallEndpoints(ListFirewallEndpointsRequest request, StreamObserver<ListFirewallEndpointsResponse> responseObserver)
    
    
    public void listProjectFirewallEndpoints(ListFirewallEndpointsRequest request, StreamObserver<ListFirewallEndpointsResponse> responseObserver)

Lists FirewallEndpoints in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFirewallEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListFirewallEndpointsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFirewallEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListFirewallEndpointsResponse)>`  
  
  
### updateFirewallEndpoint(UpdateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateFirewallEndpoint(UpdateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)

Update a single org Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateFirewallEndpointAssociation(UpdateFirewallEndpointAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateFirewallEndpointAssociation(UpdateFirewallEndpointAssociationRequest request, StreamObserver<Operation> responseObserver)

Update a single FirewallEndpointAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateFirewallEndpointAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateProjectFirewallEndpoint(UpdateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateProjectFirewallEndpoint(UpdateFirewallEndpointRequest request, StreamObserver<Operation> responseObserver)

Update a single project Endpoint.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFirewallEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateFirewallEndpointRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
