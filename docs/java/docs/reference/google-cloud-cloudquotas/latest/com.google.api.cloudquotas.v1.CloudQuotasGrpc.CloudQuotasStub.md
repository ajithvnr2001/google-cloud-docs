---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasGrpc.CloudQuotasStub
title: Class CloudQuotasGrpc.CloudQuotasStub (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:19.273893+00:00
---

# Class CloudQuotasGrpc.CloudQuotasStub (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasGrpc.CloudQuotasStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudQuotasGrpc.CloudQuotasStub (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class CloudQuotasGrpc.CloudQuotasStub extends AbstractAsyncStub<CloudQuotasGrpc.CloudQuotasStub>

A stub to allow clients to do asynchronous rpc calls to service CloudQuotas.

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.

  * List/Get the metadata and current status of the quotas for a service.
  * Create/Update quota preferencess that declare the preferred quota values.
  * Check the status of a quota preference request.
  * List/Get pending and historical quota preference.



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > CloudQuotasGrpc.CloudQuotasStub

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
    
    
    protected CloudQuotasGrpc.CloudQuotasStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudQuotasGrpc.CloudQuotasStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasGrpc.CloudQuotasStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createQuotaPreference(CreateQuotaPreferenceRequest request, StreamObserver<QuotaPreference> responseObserver)
    
    
    public void createQuotaPreference(CreateQuotaPreferenceRequest request, StreamObserver<QuotaPreference> responseObserver)

Creates a new QuotaPreference that declares the desired value for a quota.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CreateQuotaPreferenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaPreference)>`  
  
  
### getQuotaInfo(GetQuotaInfoRequest request, StreamObserver<QuotaInfo> responseObserver)
    
    
    public void getQuotaInfo(GetQuotaInfoRequest request, StreamObserver<QuotaInfo> responseObserver)

Retrieve the QuotaInfo of a quota for a project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfo)>`  
  
  
### getQuotaPreference(GetQuotaPreferenceRequest request, StreamObserver<QuotaPreference> responseObserver)
    
    
    public void getQuotaPreference(GetQuotaPreferenceRequest request, StreamObserver<QuotaPreference> responseObserver)

Gets details of a single QuotaPreference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaPreferenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaPreference)>`  
  
  
### listQuotaInfos(ListQuotaInfosRequest request, StreamObserver<ListQuotaInfosResponse> responseObserver)
    
    
    public void listQuotaInfos(ListQuotaInfosRequest request, StreamObserver<ListQuotaInfosResponse> responseObserver)

Lists QuotaInfos of all quotas for a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.ListQuotaInfosRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListQuotaInfosResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.ListQuotaInfosResponse)>`  
  
  
### listQuotaPreferences(ListQuotaPreferencesRequest request, StreamObserver<ListQuotaPreferencesResponse> responseObserver)
    
    
    public void listQuotaPreferences(ListQuotaPreferencesRequest request, StreamObserver<ListQuotaPreferencesResponse> responseObserver)

Lists QuotaPreferences in a given project, folder or organization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaPreferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.ListQuotaPreferencesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListQuotaPreferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.ListQuotaPreferencesResponse)>`  
  
  
### updateQuotaPreference(UpdateQuotaPreferenceRequest request, StreamObserver<QuotaPreference> responseObserver)
    
    
    public void updateQuotaPreference(UpdateQuotaPreferenceRequest request, StreamObserver<QuotaPreference> responseObserver)

Updates the parameters of a single QuotaPreference. It can updates the config in any states, not just the ones pending approval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.UpdateQuotaPreferenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaPreference)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
