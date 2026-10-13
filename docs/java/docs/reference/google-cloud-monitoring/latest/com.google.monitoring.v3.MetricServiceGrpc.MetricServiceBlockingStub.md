---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.MetricServiceGrpc.MetricServiceBlockingStub
title: Class MetricServiceGrpc.MetricServiceBlockingStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:48.457239+00:00
---

# Class MetricServiceGrpc.MetricServiceBlockingStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.MetricServiceGrpc.MetricServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetricServiceGrpc.MetricServiceBlockingStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.6  3.3.6  3.2.10 
    
    
    public static final class MetricServiceGrpc.MetricServiceBlockingStub extends AbstractBlockingStub<MetricServiceGrpc.MetricServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service MetricService.

Manages metric descriptors, monitored resource descriptors, and time series data.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > MetricServiceGrpc.MetricServiceBlockingStub

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
    
    
    protected MetricServiceGrpc.MetricServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricServiceGrpc.MetricServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.MetricServiceGrpc.MetricServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createMetricDescriptor(CreateMetricDescriptorRequest request)
    
    
    public MetricDescriptor createMetricDescriptor(CreateMetricDescriptorRequest request)

Creates a new metric descriptor. The creation is executed asynchronously. User-created metric descriptors define [custom metrics](https://cloud.google.com/monitoring/custom-metrics). The metric descriptor is updated if it already exists, except that metric labels are never removed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMetricDescriptorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateMetricDescriptorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.MetricDescriptor` |   
  
### createServiceTimeSeries(CreateTimeSeriesRequest request)
    
    
    public Empty createServiceTimeSeries(CreateTimeSeriesRequest request)

Creates or adds data to one or more service time series. A service time series is a time series for a metric from a Google Cloud service. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This endpoint rejects writes to user-defined metrics. This method is only for use by Google Cloud services. Use projects.timeSeries.create instead.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### createTimeSeries(CreateTimeSeriesRequest request)
    
    
    public Empty createTimeSeries(CreateTimeSeriesRequest request)

Creates or adds data to one or more time series. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This method does not support [resource locations constraint of an organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deleteMetricDescriptor(DeleteMetricDescriptorRequest request)
    
    
    public Empty deleteMetricDescriptor(DeleteMetricDescriptorRequest request)

Deletes a metric descriptor. Only user-created [custom metrics](https://cloud.google.com/monitoring/custom-metrics) can be deleted.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMetricDescriptorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.DeleteMetricDescriptorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### getMetricDescriptor(GetMetricDescriptorRequest request)
    
    
    public MetricDescriptor getMetricDescriptor(GetMetricDescriptorRequest request)

Gets a single metric descriptor.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMetricDescriptorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.GetMetricDescriptorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.MetricDescriptor` |   
  
### getMonitoredResourceDescriptor(GetMonitoredResourceDescriptorRequest request)
    
    
    public MonitoredResourceDescriptor getMonitoredResourceDescriptor(GetMonitoredResourceDescriptorRequest request)

Gets a single monitored resource descriptor.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMonitoredResourceDescriptorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.GetMonitoredResourceDescriptorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.MonitoredResourceDescriptor` |   
  
### listMetricDescriptors(ListMetricDescriptorsRequest request)
    
    
    public ListMetricDescriptorsResponse listMetricDescriptors(ListMetricDescriptorsRequest request)

Lists metric descriptors that match a filter.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMetricDescriptorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListMetricDescriptorsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMetricDescriptorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListMetricDescriptorsResponse)` |   
  
### listMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest request)
    
    
    public ListMonitoredResourceDescriptorsResponse listMonitoredResourceDescriptors(ListMonitoredResourceDescriptorsRequest request)

Lists monitored resource descriptors that match a filter.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListMonitoredResourceDescriptorsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMonitoredResourceDescriptorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListMonitoredResourceDescriptorsResponse)` |   
  
### listTimeSeries(ListTimeSeriesRequest request)
    
    
    public ListTimeSeriesResponse listTimeSeries(ListTimeSeriesRequest request)

Lists time series that match a filter.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListTimeSeriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTimeSeriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListTimeSeriesResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
