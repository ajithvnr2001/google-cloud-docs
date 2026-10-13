---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DataTransferServiceGrpc.DataTransferServiceFutureStub
title: Class DataTransferServiceGrpc.DataTransferServiceFutureStub (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:35.854324+00:00
---

# Class DataTransferServiceGrpc.DataTransferServiceFutureStub (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DataTransferServiceGrpc.DataTransferServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataTransferServiceGrpc.DataTransferServiceFutureStub (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 
    
    
    public static final class DataTransferServiceGrpc.DataTransferServiceFutureStub extends AbstractFutureStub<DataTransferServiceGrpc.DataTransferServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service DataTransferService.

DataTransferService is the service for the Data Transfer API.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > DataTransferServiceGrpc.DataTransferServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected DataTransferServiceGrpc.DataTransferServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataTransferServiceGrpc.DataTransferServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DataTransferServiceGrpc.DataTransferServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createDestination(CreateDestinationRequest request)
    
    
    public ListenableFuture<Operation> createDestination(CreateDestinationRequest request)

Creates a `Destination` resource in a specified project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateDestinationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMulticloudDataTransferConfig(CreateMulticloudDataTransferConfigRequest request)
    
    
    public ListenableFuture<Operation> createMulticloudDataTransferConfig(CreateMulticloudDataTransferConfigRequest request)

Creates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateMulticloudDataTransferConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDestination(DeleteDestinationRequest request)
    
    
    public ListenableFuture<Operation> deleteDestination(DeleteDestinationRequest request)

Deletes a `Destination` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteDestinationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMulticloudDataTransferConfig(DeleteMulticloudDataTransferConfigRequest request)
    
    
    public ListenableFuture<Operation> deleteMulticloudDataTransferConfig(DeleteMulticloudDataTransferConfigRequest request)

Deletes a `MulticloudDataTransferConfig` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteMulticloudDataTransferConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDestination(GetDestinationRequest request)
    
    
    public ListenableFuture<Destination> getDestination(GetDestinationRequest request)

Gets the details of a `Destination` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetDestinationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Destination](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Destination)>` |   
  
### getMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest request)
    
    
    public ListenableFuture<MulticloudDataTransferConfig> getMulticloudDataTransferConfig(GetMulticloudDataTransferConfigRequest request)

Gets the details of a `MulticloudDataTransferConfig` resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetMulticloudDataTransferConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[MulticloudDataTransferConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.MulticloudDataTransferConfig)>` |   
  
### getMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest request)
    
    
    public ListenableFuture<MulticloudDataTransferSupportedService> getMulticloudDataTransferSupportedService(GetMulticloudDataTransferSupportedServiceRequest request)

Gets the details of a service that is supported for Data Transfer Essentials.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMulticloudDataTransferSupportedServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetMulticloudDataTransferSupportedServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[MulticloudDataTransferSupportedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.MulticloudDataTransferSupportedService)>` |   
  
### listDestinations(ListDestinationsRequest request)
    
    
    public ListenableFuture<ListDestinationsResponse> listDestinations(ListDestinationsRequest request)

Lists the `Destination` resources in a specified project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDestinationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListDestinationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListDestinationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListDestinationsResponse)>` |   
  
### listMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest request)
    
    
    public ListenableFuture<ListMulticloudDataTransferConfigsResponse> listMulticloudDataTransferConfigs(ListMulticloudDataTransferConfigsRequest request)

Lists the `MulticloudDataTransferConfig` resources in a specified project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListMulticloudDataTransferConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListMulticloudDataTransferConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListMulticloudDataTransferConfigsResponse)>` |   
  
### listMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest request)
    
    
    public ListenableFuture<ListMulticloudDataTransferSupportedServicesResponse> listMulticloudDataTransferSupportedServices(ListMulticloudDataTransferSupportedServicesRequest request)

Lists the services in the project for a region that are supported for Data Transfer Essentials.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMulticloudDataTransferSupportedServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListMulticloudDataTransferSupportedServicesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListMulticloudDataTransferSupportedServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListMulticloudDataTransferSupportedServicesResponse)>` |   
  
### updateDestination(UpdateDestinationRequest request)
    
    
    public ListenableFuture<Operation> updateDestination(UpdateDestinationRequest request)

Updates a `Destination` resource in a specified project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDestinationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateDestinationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMulticloudDataTransferConfig(UpdateMulticloudDataTransferConfigRequest request)
    
    
    public ListenableFuture<Operation> updateMulticloudDataTransferConfig(UpdateMulticloudDataTransferConfigRequest request)

Updates a `MulticloudDataTransferConfig` resource in a specified project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMulticloudDataTransferConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateMulticloudDataTransferConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
