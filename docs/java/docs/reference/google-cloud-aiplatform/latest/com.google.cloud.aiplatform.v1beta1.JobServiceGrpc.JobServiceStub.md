---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.JobServiceGrpc.JobServiceStub
title: Class JobServiceGrpc.JobServiceStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:51.774096+00:00
---

# Class JobServiceGrpc.JobServiceStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.JobServiceGrpc.JobServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class JobServiceGrpc.JobServiceStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class JobServiceGrpc.JobServiceStub extends AbstractAsyncStub<JobServiceGrpc.JobServiceStub>

A stub to allow clients to do asynchronous rpc calls to service JobService.

A service for creating and managing Vertex AI's jobs.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > JobServiceGrpc.JobServiceStub

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
    
    
    protected JobServiceGrpc.JobServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceGrpc.JobServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.JobServiceGrpc.JobServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelBatchPredictionJob(CancelBatchPredictionJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelBatchPredictionJob(CancelBatchPredictionJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a BatchPredictionJob. Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelBatchPredictionJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### cancelCustomJob(CancelCustomJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelCustomJob(CancelCustomJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelCustomJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### cancelDataLabelingJob(CancelDataLabelingJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelDataLabelingJob(CancelDataLabelingJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a DataLabelingJob. Success of cancellation is not guaranteed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelDataLabelingJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelHyperparameterTuningJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### cancelNasJob(CancelNasJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void cancelNasJob(CancelNasJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelNasJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### createBatchPredictionJob(CreateBatchPredictionJobRequest request, StreamObserver<BatchPredictionJob> responseObserver)
    
    
    public void createBatchPredictionJob(CreateBatchPredictionJobRequest request, StreamObserver<BatchPredictionJob> responseObserver)

Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateBatchPredictionJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchPredictionJob)>`  
  
  
### createCustomJob(CreateCustomJobRequest request, StreamObserver<CustomJob> responseObserver)
    
    
    public void createCustomJob(CreateCustomJobRequest request, StreamObserver<CustomJob> responseObserver)

Creates a CustomJob. A created CustomJob right away will be attempted to be run.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateCustomJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CustomJob)>`  
  
  
### createDataLabelingJob(CreateDataLabelingJobRequest request, StreamObserver<DataLabelingJob> responseObserver)
    
    
    public void createDataLabelingJob(CreateDataLabelingJobRequest request, StreamObserver<DataLabelingJob> responseObserver)

Creates a DataLabelingJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateDataLabelingJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DataLabelingJob)>`  
  
  
### createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request, StreamObserver<HyperparameterTuningJob> responseObserver)
    
    
    public void createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request, StreamObserver<HyperparameterTuningJob> responseObserver)

Creates a HyperparameterTuningJob

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateHyperparameterTuningJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.HyperparameterTuningJob)>`  
  
  
### createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request, StreamObserver<ModelDeploymentMonitoringJob> responseObserver)
    
    
    public void createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request, StreamObserver<ModelDeploymentMonitoringJob> responseObserver)

Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateModelDeploymentMonitoringJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob)>`  
  
  
### createNasJob(CreateNasJobRequest request, StreamObserver<NasJob> responseObserver)
    
    
    public void createNasJob(CreateNasJobRequest request, StreamObserver<NasJob> responseObserver)

Creates a NasJob

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateNasJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NasJob)>`  
  
  
### deleteBatchPredictionJob(DeleteBatchPredictionJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBatchPredictionJob(DeleteBatchPredictionJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteBatchPredictionJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteCustomJob(DeleteCustomJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteCustomJob(DeleteCustomJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a CustomJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteCustomJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteDataLabelingJob(DeleteDataLabelingJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteDataLabelingJob(DeleteDataLabelingJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a DataLabelingJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteDataLabelingJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteHyperparameterTuningJob(DeleteHyperparameterTuningJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteHyperparameterTuningJob(DeleteHyperparameterTuningJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a HyperparameterTuningJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteHyperparameterTuningJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteModelDeploymentMonitoringJob(DeleteModelDeploymentMonitoringJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteModelDeploymentMonitoringJob(DeleteModelDeploymentMonitoringJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a ModelDeploymentMonitoringJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteModelDeploymentMonitoringJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteNasJob(DeleteNasJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteNasJob(DeleteNasJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a NasJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteNasJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getBatchPredictionJob(GetBatchPredictionJobRequest request, StreamObserver<BatchPredictionJob> responseObserver)
    
    
    public void getBatchPredictionJob(GetBatchPredictionJobRequest request, StreamObserver<BatchPredictionJob> responseObserver)

Gets a BatchPredictionJob

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetBatchPredictionJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchPredictionJob)>`  
  
  
### getCustomJob(GetCustomJobRequest request, StreamObserver<CustomJob> responseObserver)
    
    
    public void getCustomJob(GetCustomJobRequest request, StreamObserver<CustomJob> responseObserver)

Gets a CustomJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetCustomJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CustomJob)>`  
  
  
### getDataLabelingJob(GetDataLabelingJobRequest request, StreamObserver<DataLabelingJob> responseObserver)
    
    
    public void getDataLabelingJob(GetDataLabelingJobRequest request, StreamObserver<DataLabelingJob> responseObserver)

Gets a DataLabelingJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetDataLabelingJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DataLabelingJob)>`  
  
  
### getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request, StreamObserver<HyperparameterTuningJob> responseObserver)
    
    
    public void getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request, StreamObserver<HyperparameterTuningJob> responseObserver)

Gets a HyperparameterTuningJob

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetHyperparameterTuningJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.HyperparameterTuningJob)>`  
  
  
### getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request, StreamObserver<ModelDeploymentMonitoringJob> responseObserver)
    
    
    public void getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request, StreamObserver<ModelDeploymentMonitoringJob> responseObserver)

Gets a ModelDeploymentMonitoringJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetModelDeploymentMonitoringJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob)>`  
  
  
### getNasJob(GetNasJobRequest request, StreamObserver<NasJob> responseObserver)
    
    
    public void getNasJob(GetNasJobRequest request, StreamObserver<NasJob> responseObserver)

Gets a NasJob

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetNasJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NasJob)>`  
  
  
### getNasTrialDetail(GetNasTrialDetailRequest request, StreamObserver<NasTrialDetail> responseObserver)
    
    
    public void getNasTrialDetail(GetNasTrialDetailRequest request, StreamObserver<NasTrialDetail> responseObserver)

Gets a NasTrialDetail.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetNasTrialDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetNasTrialDetailRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[NasTrialDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NasTrialDetail)>`  
  
  
### listBatchPredictionJobs(ListBatchPredictionJobsRequest request, StreamObserver<ListBatchPredictionJobsResponse> responseObserver)
    
    
    public void listBatchPredictionJobs(ListBatchPredictionJobsRequest request, StreamObserver<ListBatchPredictionJobsResponse> responseObserver)

Lists BatchPredictionJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListBatchPredictionJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBatchPredictionJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListBatchPredictionJobsResponse)>`  
  
  
### listCustomJobs(ListCustomJobsRequest request, StreamObserver<ListCustomJobsResponse> responseObserver)
    
    
    public void listCustomJobs(ListCustomJobsRequest request, StreamObserver<ListCustomJobsResponse> responseObserver)

Lists CustomJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListCustomJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCustomJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListCustomJobsResponse)>`  
  
  
### listDataLabelingJobs(ListDataLabelingJobsRequest request, StreamObserver<ListDataLabelingJobsResponse> responseObserver)
    
    
    public void listDataLabelingJobs(ListDataLabelingJobsRequest request, StreamObserver<ListDataLabelingJobsResponse> responseObserver)

Lists DataLabelingJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataLabelingJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListDataLabelingJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDataLabelingJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListDataLabelingJobsResponse)>`  
  
  
### listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request, StreamObserver<ListHyperparameterTuningJobsResponse> responseObserver)
    
    
    public void listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request, StreamObserver<ListHyperparameterTuningJobsResponse> responseObserver)

Lists HyperparameterTuningJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHyperparameterTuningJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListHyperparameterTuningJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHyperparameterTuningJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListHyperparameterTuningJobsResponse)>`  
  
  
### listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request, StreamObserver<ListModelDeploymentMonitoringJobsResponse> responseObserver)
    
    
    public void listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request, StreamObserver<ListModelDeploymentMonitoringJobsResponse> responseObserver)

Lists ModelDeploymentMonitoringJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelDeploymentMonitoringJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListModelDeploymentMonitoringJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListModelDeploymentMonitoringJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListModelDeploymentMonitoringJobsResponse)>`  
  
  
### listNasJobs(ListNasJobsRequest request, StreamObserver<ListNasJobsResponse> responseObserver)
    
    
    public void listNasJobs(ListNasJobsRequest request, StreamObserver<ListNasJobsResponse> responseObserver)

Lists NasJobs in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNasJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNasJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasJobsResponse)>`  
  
  
### listNasTrialDetails(ListNasTrialDetailsRequest request, StreamObserver<ListNasTrialDetailsResponse> responseObserver)
    
    
    public void listNasTrialDetails(ListNasTrialDetailsRequest request, StreamObserver<ListNasTrialDetailsResponse> responseObserver)

List top NasTrialDetails of a NasJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListNasTrialDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasTrialDetailsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListNasTrialDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasTrialDetailsResponse)>`  
  
  
### pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request, StreamObserver<Empty> responseObserver)

Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.PauseModelDeploymentMonitoringJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request, StreamObserver<Empty> responseObserver)

Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ResumeModelDeploymentMonitoringJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request, StreamObserver<SearchModelDeploymentMonitoringStatsAnomaliesResponse> responseObserver)
    
    
    public void searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request, StreamObserver<SearchModelDeploymentMonitoringStatsAnomaliesResponse> responseObserver)

Searches Model Monitoring Statistics generated within a given time window.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchModelDeploymentMonitoringStatsAnomaliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchModelDeploymentMonitoringStatsAnomaliesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchModelDeploymentMonitoringStatsAnomaliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchModelDeploymentMonitoringStatsAnomaliesResponse)>`  
  
  
### updateModelDeploymentMonitoringJob(UpdateModelDeploymentMonitoringJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateModelDeploymentMonitoringJob(UpdateModelDeploymentMonitoringJobRequest request, StreamObserver<Operation> responseObserver)

Updates a ModelDeploymentMonitoringJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateModelDeploymentMonitoringJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
