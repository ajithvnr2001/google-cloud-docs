---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub
title: Class RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub (0.82.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:10.237176+00:00
---

# Class RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub (0.82.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub (0.82.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.82.0 (latest)  0.78.0  0.77.0  0.76.0  0.74.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.63.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub extends AbstractFutureStub<RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service RapidMigrationAssessment.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub

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
    
    
    protected RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.RapidMigrationAssessmentGrpc.RapidMigrationAssessmentFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAnnotation(CreateAnnotationRequest request)
    
    
    public ListenableFuture<Operation> createAnnotation(CreateAnnotationRequest request)

Creates an Annotation

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAnnotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.CreateAnnotationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCollector(CreateCollectorRequest request)
    
    
    public ListenableFuture<Operation> createCollector(CreateCollectorRequest request)

Create a Collector to manage the on-prem appliance which collects information about Customer assets.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.CreateCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCollector(DeleteCollectorRequest request)
    
    
    public ListenableFuture<Operation> deleteCollector(DeleteCollectorRequest request)

Deletes a single Collector - changes state of collector to "Deleting". Background jobs does final deletion through producer API.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.DeleteCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAnnotation(GetAnnotationRequest request)
    
    
    public ListenableFuture<Annotation> getAnnotation(GetAnnotationRequest request)

Gets details of a single Annotation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.GetAnnotationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.Annotation)>` |   
  
### getCollector(GetCollectorRequest request)
    
    
    public ListenableFuture<Collector> getCollector(GetCollectorRequest request)

Gets details of a single Collector.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.GetCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Collector](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.Collector)>` |   
  
### listCollectors(ListCollectorsRequest request)
    
    
    public ListenableFuture<ListCollectorsResponse> listCollectors(ListCollectorsRequest request)

Lists Collectors in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCollectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.ListCollectorsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListCollectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.ListCollectorsResponse)>` |   
  
### pauseCollector(PauseCollectorRequest request)
    
    
    public ListenableFuture<Operation> pauseCollector(PauseCollectorRequest request)

Pauses the given collector.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PauseCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.PauseCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### registerCollector(RegisterCollectorRequest request)
    
    
    public ListenableFuture<Operation> registerCollector(RegisterCollectorRequest request)

Registers the given collector.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RegisterCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.RegisterCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resumeCollector(ResumeCollectorRequest request)
    
    
    public ListenableFuture<Operation> resumeCollector(ResumeCollectorRequest request)

Resumes the given collector.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.ResumeCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCollector(UpdateCollectorRequest request)
    
    
    public ListenableFuture<Operation> updateCollector(UpdateCollectorRequest request)

Updates the parameters of a single Collector.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCollectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-rapidmigrationassessment/latest/com.google.cloud.rapidmigrationassessment.v1.UpdateCollectorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
