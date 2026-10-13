---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub
title: Class CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:00.974738+00:00
---

# Class CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub extends AbstractAsyncStub<CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub>

A stub to allow clients to do asynchronous rpc calls to service CloudControlsPartnerCore.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub

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
    
    
    protected CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCoreGrpc.CloudControlsPartnerCoreStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createCustomer(CreateCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public void createCustomer(CreateCustomerRequest request, StreamObserver<Customer> responseObserver)

Creates a new customer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.CreateCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.Customer)>`  
  
  
### deleteCustomer(DeleteCustomerRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteCustomer(DeleteCustomerRequest request, StreamObserver<Empty> responseObserver)

Delete details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.DeleteCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getCustomer(GetCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public void getCustomer(GetCustomerRequest request, StreamObserver<Customer> responseObserver)

Gets details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.GetCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.Customer)>`  
  
  
### getEkmConnections(GetEkmConnectionsRequest request, StreamObserver<EkmConnections> responseObserver)
    
    
    public void getEkmConnections(GetEkmConnectionsRequest request, StreamObserver<EkmConnections> responseObserver)

Gets the EKM connections associated with a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEkmConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.GetEkmConnectionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[EkmConnections](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.EkmConnections)>`  
  
  
### getPartner(GetPartnerRequest request, StreamObserver<Partner> responseObserver)
    
    
    public void getPartner(GetPartnerRequest request, StreamObserver<Partner> responseObserver)

Get details of a Partner.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.GetPartnerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Partner](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.Partner)>`  
  
  
### getPartnerPermissions(GetPartnerPermissionsRequest request, StreamObserver<PartnerPermissions> responseObserver)
    
    
    public void getPartnerPermissions(GetPartnerPermissionsRequest request, StreamObserver<PartnerPermissions> responseObserver)

Gets the partner permissions granted for a workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPartnerPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.GetPartnerPermissionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PartnerPermissions](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.PartnerPermissions)>`  
  
  
### getWorkload(GetWorkloadRequest request, StreamObserver<Workload> responseObserver)
    
    
    public void getWorkload(GetWorkloadRequest request, StreamObserver<Workload> responseObserver)

Gets details of a single workload

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.GetWorkloadRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.Workload)>`  
  
  
### listAccessApprovalRequests(ListAccessApprovalRequestsRequest request, StreamObserver<ListAccessApprovalRequestsResponse> responseObserver) (deprecated)
    
    
    public void listAccessApprovalRequests(ListAccessApprovalRequestsRequest request, StreamObserver<ListAccessApprovalRequestsResponse> responseObserver)

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessApprovalRequestsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.ListAccessApprovalRequestsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAccessApprovalRequestsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.ListAccessApprovalRequestsResponse)>`  
  
  
### listCustomers(ListCustomersRequest request, StreamObserver<ListCustomersResponse> responseObserver)
    
    
    public void listCustomers(ListCustomersRequest request, StreamObserver<ListCustomersResponse> responseObserver)

Lists customers of a partner identified by its Google Cloud organization ID

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.ListCustomersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCustomersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.ListCustomersResponse)>`  
  
  
### listWorkloads(ListWorkloadsRequest request, StreamObserver<ListWorkloadsResponse> responseObserver)
    
    
    public void listWorkloads(ListWorkloadsRequest request, StreamObserver<ListWorkloadsResponse> responseObserver)

Lists customer workloads for a given customer org id

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.ListWorkloadsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.ListWorkloadsResponse)>`  
  
  
### updateCustomer(UpdateCustomerRequest request, StreamObserver<Customer> responseObserver)
    
    
    public void updateCustomer(UpdateCustomerRequest request, StreamObserver<Customer> responseObserver)

Update details of a single customer

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.UpdateCustomerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcontrolspartner/latest/com.google.cloud.cloudcontrolspartner.v1beta.Customer)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
