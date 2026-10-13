---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceGrpc.DepServiceStub
title: Class DepServiceGrpc.DepServiceStub (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:47.047533+00:00
---

# Class DepServiceGrpc.DepServiceStub (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceGrpc.DepServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DepServiceGrpc.DepServiceStub (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class DepServiceGrpc.DepServiceStub extends AbstractAsyncStub<DepServiceGrpc.DepServiceStub>

A stub to allow clients to do asynchronous rpc calls to service DepService.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > DepServiceGrpc.DepServiceStub

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
    
    
    protected DepServiceGrpc.DepServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceGrpc.DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceGrpc.DepServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createExtensionBinding(CreateExtensionBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createExtensionBinding(CreateExtensionBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a new `ExtensionBinding` resource in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateExtensionBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createLbRouteExtension(CreateLbRouteExtensionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createLbRouteExtension(CreateLbRouteExtensionRequest request, StreamObserver<Operation> responseObserver)

Creates a new `LbRouteExtension` resource in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbRouteExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createLbTrafficExtension(CreateLbTrafficExtensionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createLbTrafficExtension(CreateLbTrafficExtensionRequest request, StreamObserver<Operation> responseObserver)

Creates a new `LbTrafficExtension` resource in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbTrafficExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteExtensionBinding(DeleteExtensionBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteExtensionBinding(DeleteExtensionBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified `ExtensionBinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteExtensionBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteLbRouteExtension(DeleteLbRouteExtensionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteLbRouteExtension(DeleteLbRouteExtensionRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified `LbRouteExtension` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbRouteExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteLbTrafficExtension(DeleteLbTrafficExtensionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteLbTrafficExtension(DeleteLbTrafficExtensionRequest request, StreamObserver<Operation> responseObserver)

Deletes the specified `LbTrafficExtension` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbTrafficExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getExtensionBinding(GetExtensionBindingRequest request, StreamObserver<ExtensionBinding> responseObserver)
    
    
    public void getExtensionBinding(GetExtensionBindingRequest request, StreamObserver<ExtensionBinding> responseObserver)

Gets details of the specified `ExtensionBinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetExtensionBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)>`  
  
  
### getLbRouteExtension(GetLbRouteExtensionRequest request, StreamObserver<LbRouteExtension> responseObserver)
    
    
    public void getLbRouteExtension(GetLbRouteExtensionRequest request, StreamObserver<LbRouteExtension> responseObserver)

Gets details of the specified `LbRouteExtension` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbRouteExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)>`  
  
  
### getLbTrafficExtension(GetLbTrafficExtensionRequest request, StreamObserver<LbTrafficExtension> responseObserver)
    
    
    public void getLbTrafficExtension(GetLbTrafficExtensionRequest request, StreamObserver<LbTrafficExtension> responseObserver)

Gets details of the specified `LbTrafficExtension` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbTrafficExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)>`  
  
  
### listExtensionBindings(ListExtensionBindingsRequest request, StreamObserver<ListExtensionBindingsResponse> responseObserver)
    
    
    public void listExtensionBindings(ListExtensionBindingsRequest request, StreamObserver<ListExtensionBindingsResponse> responseObserver)

Lists `ExtensionBinding` resources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExtensionBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListExtensionBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsResponse)>`  
  
  
### listLbRouteExtensions(ListLbRouteExtensionsRequest request, StreamObserver<ListLbRouteExtensionsResponse> responseObserver)
    
    
    public void listLbRouteExtensions(ListLbRouteExtensionsRequest request, StreamObserver<ListLbRouteExtensionsResponse> responseObserver)

Lists `LbRouteExtension` resources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListLbRouteExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsResponse)>`  
  
  
### listLbTrafficExtensions(ListLbTrafficExtensionsRequest request, StreamObserver<ListLbTrafficExtensionsResponse> responseObserver)
    
    
    public void listLbTrafficExtensions(ListLbTrafficExtensionsRequest request, StreamObserver<ListLbTrafficExtensionsResponse> responseObserver)

Lists `LbTrafficExtension` resources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsResponse)>`  
  
  
### updateExtensionBinding(UpdateExtensionBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateExtensionBinding(UpdateExtensionBindingRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of the specified `ExtensionBinding` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateExtensionBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateLbRouteExtension(UpdateLbRouteExtensionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateLbRouteExtension(UpdateLbRouteExtensionRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of the specified `LbRouteExtension` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbRouteExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateLbTrafficExtension(UpdateLbTrafficExtensionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateLbTrafficExtension(UpdateLbTrafficExtensionRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of the specified `LbTrafficExtension` resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbTrafficExtensionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
