---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringGrpc.MonitoringStub
title: Class MonitoringGrpc.MonitoringStub (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:55.842799+00:00
---

# Class MonitoringGrpc.MonitoringStub (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringGrpc.MonitoringStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MonitoringGrpc.MonitoringStub (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MonitoringGrpc.MonitoringStub extends AbstractAsyncStub<MonitoringGrpc.MonitoringStub>

A stub to allow clients to do asynchronous rpc calls to service Monitoring.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > MonitoringGrpc.MonitoringStub

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

### aggregateFrameworkComplianceReport(AggregateFrameworkComplianceReportRequest request, StreamObserver<AggregateFrameworkComplianceReportResponse> responseObserver)
    
    
    public void aggregateFrameworkComplianceReport(AggregateFrameworkComplianceReportRequest request, StreamObserver<AggregateFrameworkComplianceReportResponse> responseObserver)

Gets the aggregated compliance report over time for a given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AggregateFrameworkComplianceReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AggregateFrameworkComplianceReportResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AggregateFrameworkComplianceReportResponse)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected MonitoringGrpc.MonitoringStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MonitoringGrpc.MonitoringStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.MonitoringGrpc.MonitoringStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### fetchFrameworkComplianceReport(FetchFrameworkComplianceReportRequest request, StreamObserver<FrameworkComplianceReport> responseObserver)
    
    
    public void fetchFrameworkComplianceReport(FetchFrameworkComplianceReportRequest request, StreamObserver<FrameworkComplianceReport> responseObserver)

Fetches the framework compliance report for a given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchFrameworkComplianceReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FetchFrameworkComplianceReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FrameworkComplianceReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FrameworkComplianceReport)>`  
  
  
### listControlComplianceSummaries(ListControlComplianceSummariesRequest request, StreamObserver<ListControlComplianceSummariesResponse> responseObserver)
    
    
    public void listControlComplianceSummaries(ListControlComplianceSummariesRequest request, StreamObserver<ListControlComplianceSummariesResponse> responseObserver)

Lists the control compliance summary for a given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListControlComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListControlComplianceSummariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListControlComplianceSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListControlComplianceSummariesResponse)>`  
  
  
### listFindingSummaries(ListFindingSummariesRequest request, StreamObserver<ListFindingSummariesResponse> responseObserver)
    
    
    public void listFindingSummaries(ListFindingSummariesRequest request, StreamObserver<ListFindingSummariesResponse> responseObserver)

Lists the finding summary by category for a given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFindingSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFindingSummariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFindingSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFindingSummariesResponse)>`  
  
  
### listFrameworkComplianceSummaries(ListFrameworkComplianceSummariesRequest request, StreamObserver<ListFrameworkComplianceSummariesResponse> responseObserver)
    
    
    public void listFrameworkComplianceSummaries(ListFrameworkComplianceSummariesRequest request, StreamObserver<ListFrameworkComplianceSummariesResponse> responseObserver)

Lists the framework compliance summary for a given scope.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFrameworkComplianceSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFrameworkComplianceSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworkComplianceSummariesResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
