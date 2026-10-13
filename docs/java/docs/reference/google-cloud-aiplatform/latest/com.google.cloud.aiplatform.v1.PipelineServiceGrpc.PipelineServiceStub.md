---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceGrpc.PipelineServiceStub
title: Class PipelineServiceGrpc.PipelineServiceStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:51.867310+00:00
---

# Class PipelineServiceGrpc.PipelineServiceStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceGrpc.PipelineServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PipelineServiceGrpc.PipelineServiceStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class PipelineServiceGrpc.PipelineServiceStub extends AbstractAsyncStub<PipelineServiceGrpc.PipelineServiceStub>

A stub to allow clients to do asynchronous rpc calls to service PipelineService.

A service for creating and managing Vertex AI's pipelines. This includes both `TrainingPipeline` resources (used for AutoML and custom training) and `PipelineJob` resources (used for Vertex AI Pipelines).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > PipelineServiceGrpc.PipelineServiceStub

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

### batchCancelPipelineJobs(BatchCancelPipelineJobsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void batchCancelPipelineJobs(BatchCancelPipelineJobsRequest request, StreamObserver<Operation> responseObserver)

Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCancelPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### batchDeletePipelineJobs(BatchDeletePipelineJobsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void batchDeletePipelineJobs(BatchDeletePipelineJobsRequest request, StreamObserver<Operation> responseObserver)

Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchDeletePipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected PipelineServiceGrpc.PipelineServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceGrpc.PipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceGrpc.PipelineServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelPipelineJob(CancelPipelineJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelPipelineJob(CancelPipelineJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelPipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelPipelineJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### cancelTrainingPipeline(CancelTrainingPipelineRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelTrainingPipeline(CancelTrainingPipelineRequest request, StreamObserver<Empty> responseObserver)

Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelTrainingPipelineRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### createPipelineJob(CreatePipelineJobRequest request, StreamObserver<PipelineJob> responseObserver)
    
    
    public void createPipelineJob(CreatePipelineJobRequest request, StreamObserver<PipelineJob> responseObserver)

Creates a PipelineJob. A PipelineJob will run immediately when created.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePipelineJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)>`  
  
  
### createTrainingPipeline(CreateTrainingPipelineRequest request, StreamObserver<TrainingPipeline> responseObserver)
    
    
    public void createTrainingPipeline(CreateTrainingPipelineRequest request, StreamObserver<TrainingPipeline> responseObserver)

Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTrainingPipelineRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)>`  
  
  
### deletePipelineJob(DeletePipelineJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deletePipelineJob(DeletePipelineJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a PipelineJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePipelineJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteTrainingPipeline(DeleteTrainingPipelineRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteTrainingPipeline(DeleteTrainingPipelineRequest request, StreamObserver<Operation> responseObserver)

Deletes a TrainingPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTrainingPipelineRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getPipelineJob(GetPipelineJobRequest request, StreamObserver<PipelineJob> responseObserver)
    
    
    public void getPipelineJob(GetPipelineJobRequest request, StreamObserver<PipelineJob> responseObserver)

Gets a PipelineJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetPipelineJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)>`  
  
  
### getTrainingPipeline(GetTrainingPipelineRequest request, StreamObserver<TrainingPipeline> responseObserver)
    
    
    public void getTrainingPipeline(GetTrainingPipelineRequest request, StreamObserver<TrainingPipeline> responseObserver)

Gets a TrainingPipeline.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTrainingPipelineRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)>`  
  
  
### listPipelineJobs(ListPipelineJobsRequest request, StreamObserver<ListPipelineJobsResponse> responseObserver)
    
    
    public void listPipelineJobs(ListPipelineJobsRequest request, StreamObserver<ListPipelineJobsResponse> responseObserver)

Lists PipelineJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPipelineJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPipelineJobsResponse)>`  
  
  
### listTrainingPipelines(ListTrainingPipelinesRequest request, StreamObserver<ListTrainingPipelinesResponse> responseObserver)
    
    
    public void listTrainingPipelines(ListTrainingPipelinesRequest request, StreamObserver<ListTrainingPipelinesResponse> responseObserver)

Lists TrainingPipelines in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTrainingPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrainingPipelinesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTrainingPipelinesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrainingPipelinesResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
