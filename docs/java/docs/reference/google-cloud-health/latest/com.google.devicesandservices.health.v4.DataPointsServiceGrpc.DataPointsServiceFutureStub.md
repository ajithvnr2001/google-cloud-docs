---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceGrpc.DataPointsServiceFutureStub
title: Class DataPointsServiceGrpc.DataPointsServiceFutureStub (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:30.174879+00:00
---

# Class DataPointsServiceGrpc.DataPointsServiceFutureStub (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceGrpc.DataPointsServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataPointsServiceGrpc.DataPointsServiceFutureStub (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public static final class DataPointsServiceGrpc.DataPointsServiceFutureStub extends AbstractFutureStub<DataPointsServiceGrpc.DataPointsServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service DataPointsService.

Data Points Service exposing the user's health and fitness measured and derived data.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > DataPointsServiceGrpc.DataPointsServiceFutureStub

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

### batchDeleteDataPoints(BatchDeleteDataPointsRequest request)
    
    
    public ListenableFuture<Operation> batchDeleteDataPoints(BatchDeleteDataPointsRequest request)

Delete a batch of identifyable data points.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected DataPointsServiceGrpc.DataPointsServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceGrpc.DataPointsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceGrpc.DataPointsServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createDataPoint(CreateDataPointRequest request)
    
    
    public ListenableFuture<Operation> createDataPoint(CreateDataPointRequest request)

Creates a single identifiable data point.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### dailyRollUpDataPoints(DailyRollUpDataPointsRequest request)
    
    
    public ListenableFuture<DailyRollUpDataPointsResponse> dailyRollUpDataPoints(DailyRollUpDataPointsRequest request)

Roll up data points over civil time intervals for supported data types.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DailyRollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollUpDataPointsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DailyRollUpDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollUpDataPointsResponse)>` |   
  
### exportExerciseTcx(ExportExerciseTcxRequest request)
    
    
    public ListenableFuture<ExportExerciseTcxResponse> exportExerciseTcx(ExportExerciseTcxRequest request)

Exports exercise data in TCX format. **IMPORTANT:** HTTP clients must append `?alt=media` to the request URL to download the raw TCX file. Example: `<https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media>` Without `alt=media`, the server returns a JSON response (`ExportExerciseTcxResponse`) which is intended primarily for gRPC clients. **Note:** While the Authorization section below states that any one of the listed scopes is accepted, this specific method requires the user to provide both one of the `activity_and_fitness` scopes (`normal` or `readonly`) AND one of the `location` scopes (`normal` or `readonly`) in their access token to succeed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportExerciseTcxRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ExportExerciseTcxResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxResponse)>` |   
  
### getDataPoint(GetDataPointRequest request)
    
    
    public ListenableFuture<DataPoint> getDataPoint(GetDataPointRequest request)

Get a single identifyable data point.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetDataPointRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)>` |   
  
### listDataPoints(ListDataPointsRequest request)
    
    
    public ListenableFuture<ListDataPointsResponse> listDataPoints(ListDataPointsRequest request)

Query user health and fitness data points.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListDataPointsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListDataPointsResponse)>` |   
  
### reconcileDataPoints(ReconcileDataPointsRequest request)
    
    
    public ListenableFuture<ReconcileDataPointsResponse> reconcileDataPoints(ReconcileDataPointsRequest request)

Reconcile data points from multiple data sources into a single data stream.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReconcileDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ReconcileDataPointsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ReconcileDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ReconcileDataPointsResponse)>` |   
  
### rollUpDataPoints(RollUpDataPointsRequest request)
    
    
    public ListenableFuture<RollUpDataPointsResponse> rollUpDataPoints(RollUpDataPointsRequest request)

Roll up data points over physical time intervals for supported data types.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RollUpDataPointsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RollUpDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RollUpDataPointsResponse)>` |   
  
### updateDataPoint(UpdateDataPointRequest request)
    
    
    public ListenableFuture<Operation> updateDataPoint(UpdateDataPointRequest request)

Updates a single identifiable data point. If a data point with the specified `name` is not found, the request will fail.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
