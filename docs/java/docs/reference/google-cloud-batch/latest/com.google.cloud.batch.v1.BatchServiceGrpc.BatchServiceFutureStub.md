---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.BatchServiceFutureStub
title: Class BatchServiceGrpc.BatchServiceFutureStub (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:40.614956+00:00
---

# Class BatchServiceGrpc.BatchServiceFutureStub (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.BatchServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BatchServiceGrpc.BatchServiceFutureStub (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static final class BatchServiceGrpc.BatchServiceFutureStub extends AbstractFutureStub<BatchServiceGrpc.BatchServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service BatchService.

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > BatchServiceGrpc.BatchServiceFutureStub

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
    
    
    protected BatchServiceGrpc.BatchServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceGrpc.BatchServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.BatchServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelJob(CancelJobRequest request)
    
    
    public ListenableFuture<Operation> cancelJob(CancelJobRequest request)

Cancel a Job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createJob(CreateJobRequest request)
    
    
    public ListenableFuture<Job> createJob(CreateJobRequest request)

Create a Job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job)>` |   
  
### deleteJob(DeleteJobRequest request)
    
    
    public ListenableFuture<Operation> deleteJob(DeleteJobRequest request)

Delete a Job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.DeleteJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getJob(GetJobRequest request)
    
    
    public ListenableFuture<Job> getJob(GetJobRequest request)

Get a Job specified by its resource name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job)>` |   
  
### getTask(GetTaskRequest request)
    
    
    public ListenableFuture<Task> getTask(GetTaskRequest request)

Return a single Task.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetTaskRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task)>` |   
  
### listJobs(ListJobsRequest request)
    
    
    public ListenableFuture<ListJobsResponse> listJobs(ListJobsRequest request)

List all Jobs for a project within a region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsResponse)>` |   
  
### listTasks(ListTasksRequest request)
    
    
    public ListenableFuture<ListTasksResponse> listTasks(ListTasksRequest request)

List Tasks associated with a job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
