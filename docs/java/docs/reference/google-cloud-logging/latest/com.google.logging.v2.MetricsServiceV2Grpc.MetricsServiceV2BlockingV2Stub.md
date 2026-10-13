---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub
title: Class MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:40.105460+00:00
---

# Class MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static final class MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub extends AbstractBlockingStub<MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service MetricsServiceV2.

Service for configuring logs-based metrics.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub

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
    
    
    protected MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.MetricsServiceV2Grpc.MetricsServiceV2BlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createLogMetric(CreateLogMetricRequest request)
    
    
    public LogMetric createLogMetric(CreateLogMetricRequest request)

Creates a logs-based metric.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLogMetricRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteLogMetric(DeleteLogMetricRequest request)
    
    
    public Empty deleteLogMetric(DeleteLogMetricRequest request)

Deletes a logs-based metric.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLogMetricRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getLogMetric(GetLogMetricRequest request)
    
    
    public LogMetric getLogMetric(GetLogMetricRequest request)

Gets a logs-based metric.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLogMetricRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listLogMetrics(ListLogMetricsRequest request)
    
    
    public ListLogMetricsResponse listLogMetrics(ListLogMetricsRequest request)

Lists logs-based metrics.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLogMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListLogMetricsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLogMetricsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateLogMetric(UpdateLogMetricRequest request)
    
    
    public LogMetric updateLogMetric(UpdateLogMetricRequest request)

Creates or updates a logs-based metric.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLogMetricRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateLogMetricRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogMetric](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogMetric)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
