---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceGrpc.DepServiceBlockingV2Stub
title: Class DepServiceGrpc.DepServiceBlockingV2Stub (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:51.872802+00:00
---

# Class DepServiceGrpc.DepServiceBlockingV2Stub (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceGrpc.DepServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DepServiceGrpc.DepServiceBlockingV2Stub (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class DepServiceGrpc.DepServiceBlockingV2Stub extends AbstractBlockingStub<DepServiceGrpc.DepServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service DepService.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > DepServiceGrpc.DepServiceBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected DepServiceGrpc.DepServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceGrpc.DepServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceGrpc.DepServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createExtensionBinding(CreateExtensionBindingRequest request)
    
    
    public Operation createExtensionBinding(CreateExtensionBindingRequest request)

Creates a new `ExtensionBinding` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateExtensionBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createLbRouteExtension(CreateLbRouteExtensionRequest request)
    
    
    public Operation createLbRouteExtension(CreateLbRouteExtensionRequest request)

Creates a new `LbRouteExtension` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbRouteExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createLbTrafficExtension(CreateLbTrafficExtensionRequest request)
    
    
    public Operation createLbTrafficExtension(CreateLbTrafficExtensionRequest request)

Creates a new `LbTrafficExtension` resource in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbTrafficExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteExtensionBinding(DeleteExtensionBindingRequest request)
    
    
    public Operation deleteExtensionBinding(DeleteExtensionBindingRequest request)

Deletes the specified `ExtensionBinding` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteExtensionBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteLbRouteExtension(DeleteLbRouteExtensionRequest request)
    
    
    public Operation deleteLbRouteExtension(DeleteLbRouteExtensionRequest request)

Deletes the specified `LbRouteExtension` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbRouteExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteLbTrafficExtension(DeleteLbTrafficExtensionRequest request)
    
    
    public Operation deleteLbTrafficExtension(DeleteLbTrafficExtensionRequest request)

Deletes the specified `LbTrafficExtension` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbTrafficExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getExtensionBinding(GetExtensionBindingRequest request)
    
    
    public ExtensionBinding getExtensionBinding(GetExtensionBindingRequest request)

Gets details of the specified `ExtensionBinding` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetExtensionBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getLbRouteExtension(GetLbRouteExtensionRequest request)
    
    
    public LbRouteExtension getLbRouteExtension(GetLbRouteExtensionRequest request)

Gets details of the specified `LbRouteExtension` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbRouteExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getLbTrafficExtension(GetLbTrafficExtensionRequest request)
    
    
    public LbTrafficExtension getLbTrafficExtension(GetLbTrafficExtensionRequest request)

Gets details of the specified `LbTrafficExtension` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbTrafficExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listExtensionBindings(ListExtensionBindingsRequest request)
    
    
    public ListExtensionBindingsResponse listExtensionBindings(ListExtensionBindingsRequest request)

Lists `ExtensionBinding` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExtensionBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListExtensionBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listLbRouteExtensions(ListLbRouteExtensionsRequest request)
    
    
    public ListLbRouteExtensionsResponse listLbRouteExtensions(ListLbRouteExtensionsRequest request)

Lists `LbRouteExtension` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListLbRouteExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listLbTrafficExtensions(ListLbTrafficExtensionsRequest request)
    
    
    public ListLbTrafficExtensionsResponse listLbTrafficExtensions(ListLbTrafficExtensionsRequest request)

Lists `LbTrafficExtension` resources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateExtensionBinding(UpdateExtensionBindingRequest request)
    
    
    public Operation updateExtensionBinding(UpdateExtensionBindingRequest request)

Updates the parameters of the specified `ExtensionBinding` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateExtensionBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateLbRouteExtension(UpdateLbRouteExtensionRequest request)
    
    
    public Operation updateLbRouteExtension(UpdateLbRouteExtensionRequest request)

Updates the parameters of the specified `LbRouteExtension` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbRouteExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateLbTrafficExtension(UpdateLbTrafficExtensionRequest request)
    
    
    public Operation updateLbTrafficExtension(UpdateLbTrafficExtensionRequest request)

Updates the parameters of the specified `LbTrafficExtension` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbTrafficExtensionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
