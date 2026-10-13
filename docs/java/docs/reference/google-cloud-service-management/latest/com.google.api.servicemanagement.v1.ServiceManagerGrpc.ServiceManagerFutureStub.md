---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ServiceManagerGrpc.ServiceManagerFutureStub
title: Class ServiceManagerGrpc.ServiceManagerFutureStub (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:02.891155+00:00
---

# Class ServiceManagerGrpc.ServiceManagerFutureStub (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ServiceManagerGrpc.ServiceManagerFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ServiceManagerGrpc.ServiceManagerFutureStub (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.7  3.0.1  2.1.7 
    
    
    public static final class ServiceManagerGrpc.ServiceManagerFutureStub extends AbstractFutureStub<ServiceManagerGrpc.ServiceManagerFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service ServiceManager.

[Google Service Management API](https://cloud.google.com/service-infrastructure/docs/overview)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > ServiceManagerGrpc.ServiceManagerFutureStub

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
    
    
    protected ServiceManagerGrpc.ServiceManagerFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ServiceManagerGrpc.ServiceManagerFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ServiceManagerGrpc.ServiceManagerFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createService(CreateServiceRequest request)
    
    
    public ListenableFuture<Operation> createService(CreateServiceRequest request)

Creates a new managed service. A managed service is immutable, and is subject to mandatory 30-day data retention. You cannot move a service or recreate it within 30 days after deletion. One producer project can own no more than 500 services. For security and reliability purposes, a production service should be hosted in a dedicated producer project. Operation<response: ManagedService>

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.CreateServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceConfig(CreateServiceConfigRequest request)
    
    
    public ListenableFuture<Service> createServiceConfig(CreateServiceConfigRequest request)

Creates a new service configuration (version) for a managed service. This method only stores the service configuration. To roll out the service configuration to backend systems please call CreateServiceRollout. Only the 100 most recent service configurations and ones referenced by existing rollouts are kept for each service. The rest will be deleted eventually.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.CreateServiceConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.api.Service>` |   
  
### createServiceRollout(CreateServiceRolloutRequest request)
    
    
    public ListenableFuture<Operation> createServiceRollout(CreateServiceRolloutRequest request)

Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging. Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts. Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually. Operation<response: Rollout>

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.CreateServiceRolloutRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteService(DeleteServiceRequest request)
    
    
    public ListenableFuture<Operation> deleteService(DeleteServiceRequest request)

Deletes a managed service. This method will change the service to the `Soft-Delete` state for 30 days. Within this period, service producers may call UndeleteService to restore the service. After 30 days, the service will be permanently deleted. Operation<response: google.protobuf.Empty>

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.DeleteServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateConfigReport(GenerateConfigReportRequest request)
    
    
    public ListenableFuture<GenerateConfigReportResponse> generateConfigReport(GenerateConfigReportRequest request)

Generates and returns a report (errors, warnings and changes from existing configurations) associated with GenerateConfigReportRequest.new_value If GenerateConfigReportRequest.old_value is specified, GenerateConfigReportRequest will contain a single ChangeReport based on the comparison between GenerateConfigReportRequest.new_value and GenerateConfigReportRequest.old_value. If GenerateConfigReportRequest.old_value is not specified, this method will compare GenerateConfigReportRequest.new_value with the last pushed service configuration.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateConfigReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GenerateConfigReportRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GenerateConfigReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GenerateConfigReportResponse)>` |   
  
### getService(GetServiceRequest request)
    
    
    public ListenableFuture<ManagedService> getService(GetServiceRequest request)

Gets a managed service. Authentication is required unless the service is public.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GetServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ManagedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ManagedService)>` |   
  
### getServiceConfig(GetServiceConfigRequest request)
    
    
    public ListenableFuture<Service> getServiceConfig(GetServiceConfigRequest request)

Gets a service configuration (version) for a managed service.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GetServiceConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.api.Service>` |   
  
### getServiceRollout(GetServiceRolloutRequest request)
    
    
    public ListenableFuture<Rollout> getServiceRollout(GetServiceRolloutRequest request)

Gets a service configuration rollout.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.GetServiceRolloutRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.Rollout)>` |   
  
### listServiceConfigs(ListServiceConfigsRequest request)
    
    
    public ListenableFuture<ListServiceConfigsResponse> listServiceConfigs(ListServiceConfigsRequest request)

Lists the history of the service configuration for a managed service, from the newest to the oldest.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ListServiceConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListServiceConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ListServiceConfigsResponse)>` |   
  
### listServiceRollouts(ListServiceRolloutsRequest request)
    
    
    public ListenableFuture<ListServiceRolloutsResponse> listServiceRollouts(ListServiceRolloutsRequest request)

Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ListServiceRolloutsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListServiceRolloutsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ListServiceRolloutsResponse)>` |   
  
### listServices(ListServicesRequest request)
    
    
    public ListenableFuture<ListServicesResponse> listServices(ListServicesRequest request)

Lists managed services. Returns all public services. For authenticated users, also returns all services the calling user has "servicemanagement.services.get" permission for.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ListServicesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.ListServicesResponse)>` |   
  
### submitConfigSource(SubmitConfigSourceRequest request)
    
    
    public ListenableFuture<Operation> submitConfigSource(SubmitConfigSourceRequest request)

Creates a new service configuration (version) for a managed service based on user-supplied configuration source files (for example: OpenAPI Specification). This method stores the source configurations as well as the generated service configuration. To rollout the service configuration to other services, please call CreateServiceRollout. Only the 100 most recent configuration sources and ones referenced by existing service configurtions are kept for each service. The rest will be deleted eventually. Operation<response: SubmitConfigSourceResponse>

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SubmitConfigSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.SubmitConfigSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeleteService(UndeleteServiceRequest request)
    
    
    public ListenableFuture<Operation> undeleteService(UndeleteServiceRequest request)

Revives a previously deleted managed service. The method restores the service using the configuration at the time the service was deleted. The target service must exist and must have been deleted within the last 30 days. Operation<response: UndeleteServiceResponse>

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-management/latest/com.google.api.servicemanagement.v1.UndeleteServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
