---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.JobServiceGrpc.JobServiceFutureStub
title: Class JobServiceGrpc.JobServiceFutureStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:18.166403+00:00
---

# Class JobServiceGrpc.JobServiceFutureStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.JobServiceGrpc.JobServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class JobServiceGrpc.JobServiceFutureStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class JobServiceGrpc.JobServiceFutureStub extends AbstractFutureStub<JobServiceGrpc.JobServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service JobService.

A service for creating and managing Vertex AI's jobs.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > JobServiceGrpc.JobServiceFutureStub

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
    
    
    protected JobServiceGrpc.JobServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceGrpc.JobServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.JobServiceGrpc.JobServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelBatchPredictionJob(CancelBatchPredictionJobRequest request)
    
    
    public ListenableFuture<Empty> cancelBatchPredictionJob(CancelBatchPredictionJobRequest request)

Cancels a BatchPredictionJob. Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelBatchPredictionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelCustomJob(CancelCustomJobRequest request)
    
    
    public ListenableFuture<Empty> cancelCustomJob(CancelCustomJobRequest request)

Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelCustomJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelDataLabelingJob(CancelDataLabelingJobRequest request)
    
    
    public ListenableFuture<Empty> cancelDataLabelingJob(CancelDataLabelingJobRequest request)

Cancels a DataLabelingJob. Success of cancellation is not guaranteed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelDataLabelingJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request)
    
    
    public ListenableFuture<Empty> cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request)

Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelHyperparameterTuningJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelNasJob(CancelNasJobRequest request)
    
    
    public ListenableFuture<Empty> cancelNasJob(CancelNasJobRequest request)

Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CancelNasJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### createBatchPredictionJob(CreateBatchPredictionJobRequest request)
    
    
    public ListenableFuture<BatchPredictionJob> createBatchPredictionJob(CreateBatchPredictionJobRequest request)

Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateBatchPredictionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchPredictionJob)>` |   
  
### createCustomJob(CreateCustomJobRequest request)
    
    
    public ListenableFuture<CustomJob> createCustomJob(CreateCustomJobRequest request)

Creates a CustomJob. A created CustomJob right away will be attempted to be run.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateCustomJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CustomJob)>` |   
  
### createDataLabelingJob(CreateDataLabelingJobRequest request)
    
    
    public ListenableFuture<DataLabelingJob> createDataLabelingJob(CreateDataLabelingJobRequest request)

Creates a DataLabelingJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateDataLabelingJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DataLabelingJob)>` |   
  
### createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request)
    
    
    public ListenableFuture<HyperparameterTuningJob> createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request)

Creates a HyperparameterTuningJob

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateHyperparameterTuningJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.HyperparameterTuningJob)>` |   
  
### createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request)
    
    
    public ListenableFuture<ModelDeploymentMonitoringJob> createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request)

Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateModelDeploymentMonitoringJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob)>` |   
  
### createNasJob(CreateNasJobRequest request)
    
    
    public ListenableFuture<NasJob> createNasJob(CreateNasJobRequest request)

Creates a NasJob

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateNasJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NasJob)>` |   
  
### deleteBatchPredictionJob(DeleteBatchPredictionJobRequest request)
    
    
    public ListenableFuture<Operation> deleteBatchPredictionJob(DeleteBatchPredictionJobRequest request)

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteBatchPredictionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCustomJob(DeleteCustomJobRequest request)
    
    
    public ListenableFuture<Operation> deleteCustomJob(DeleteCustomJobRequest request)

Deletes a CustomJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteCustomJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataLabelingJob(DeleteDataLabelingJobRequest request)
    
    
    public ListenableFuture<Operation> deleteDataLabelingJob(DeleteDataLabelingJobRequest request)

Deletes a DataLabelingJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteDataLabelingJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHyperparameterTuningJob(DeleteHyperparameterTuningJobRequest request)
    
    
    public ListenableFuture<Operation> deleteHyperparameterTuningJob(DeleteHyperparameterTuningJobRequest request)

Deletes a HyperparameterTuningJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteHyperparameterTuningJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteModelDeploymentMonitoringJob(DeleteModelDeploymentMonitoringJobRequest request)
    
    
    public ListenableFuture<Operation> deleteModelDeploymentMonitoringJob(DeleteModelDeploymentMonitoringJobRequest request)

Deletes a ModelDeploymentMonitoringJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteModelDeploymentMonitoringJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNasJob(DeleteNasJobRequest request)
    
    
    public ListenableFuture<Operation> deleteNasJob(DeleteNasJobRequest request)

Deletes a NasJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteNasJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBatchPredictionJob(GetBatchPredictionJobRequest request)
    
    
    public ListenableFuture<BatchPredictionJob> getBatchPredictionJob(GetBatchPredictionJobRequest request)

Gets a BatchPredictionJob

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetBatchPredictionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.BatchPredictionJob)>` |   
  
### getCustomJob(GetCustomJobRequest request)
    
    
    public ListenableFuture<CustomJob> getCustomJob(GetCustomJobRequest request)

Gets a CustomJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetCustomJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CustomJob)>` |   
  
### getDataLabelingJob(GetDataLabelingJobRequest request)
    
    
    public ListenableFuture<DataLabelingJob> getDataLabelingJob(GetDataLabelingJobRequest request)

Gets a DataLabelingJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetDataLabelingJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DataLabelingJob)>` |   
  
### getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request)
    
    
    public ListenableFuture<HyperparameterTuningJob> getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request)

Gets a HyperparameterTuningJob

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetHyperparameterTuningJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.HyperparameterTuningJob)>` |   
  
### getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request)
    
    
    public ListenableFuture<ModelDeploymentMonitoringJob> getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request)

Gets a ModelDeploymentMonitoringJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetModelDeploymentMonitoringJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModelDeploymentMonitoringJob)>` |   
  
### getNasJob(GetNasJobRequest request)
    
    
    public ListenableFuture<NasJob> getNasJob(GetNasJobRequest request)

Gets a NasJob

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetNasJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NasJob)>` |   
  
### getNasTrialDetail(GetNasTrialDetailRequest request)
    
    
    public ListenableFuture<NasTrialDetail> getNasTrialDetail(GetNasTrialDetailRequest request)

Gets a NasTrialDetail.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNasTrialDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetNasTrialDetailRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NasTrialDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.NasTrialDetail)>` |   
  
### listBatchPredictionJobs(ListBatchPredictionJobsRequest request)
    
    
    public ListenableFuture<ListBatchPredictionJobsResponse> listBatchPredictionJobs(ListBatchPredictionJobsRequest request)

Lists BatchPredictionJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListBatchPredictionJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListBatchPredictionJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListBatchPredictionJobsResponse)>` |   
  
### listCustomJobs(ListCustomJobsRequest request)
    
    
    public ListenableFuture<ListCustomJobsResponse> listCustomJobs(ListCustomJobsRequest request)

Lists CustomJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListCustomJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListCustomJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListCustomJobsResponse)>` |   
  
### listDataLabelingJobs(ListDataLabelingJobsRequest request)
    
    
    public ListenableFuture<ListDataLabelingJobsResponse> listDataLabelingJobs(ListDataLabelingJobsRequest request)

Lists DataLabelingJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataLabelingJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListDataLabelingJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListDataLabelingJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListDataLabelingJobsResponse)>` |   
  
### listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request)
    
    
    public ListenableFuture<ListHyperparameterTuningJobsResponse> listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request)

Lists HyperparameterTuningJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHyperparameterTuningJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListHyperparameterTuningJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListHyperparameterTuningJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListHyperparameterTuningJobsResponse)>` |   
  
### listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request)
    
    
    public ListenableFuture<ListModelDeploymentMonitoringJobsResponse> listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request)

Lists ModelDeploymentMonitoringJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelDeploymentMonitoringJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListModelDeploymentMonitoringJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListModelDeploymentMonitoringJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListModelDeploymentMonitoringJobsResponse)>` |   
  
### listNasJobs(ListNasJobsRequest request)
    
    
    public ListenableFuture<ListNasJobsResponse> listNasJobs(ListNasJobsRequest request)

Lists NasJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNasJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListNasJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasJobsResponse)>` |   
  
### listNasTrialDetails(ListNasTrialDetailsRequest request)
    
    
    public ListenableFuture<ListNasTrialDetailsResponse> listNasTrialDetails(ListNasTrialDetailsRequest request)

List top NasTrialDetails of a NasJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNasTrialDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasTrialDetailsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListNasTrialDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListNasTrialDetailsResponse)>` |   
  
### pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request)
    
    
    public ListenableFuture<Empty> pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request)

Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PauseModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.PauseModelDeploymentMonitoringJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request)
    
    
    public ListenableFuture<Empty> resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request)

Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ResumeModelDeploymentMonitoringJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request)
    
    
    public ListenableFuture<SearchModelDeploymentMonitoringStatsAnomaliesResponse> searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request)

Searches Model Monitoring Statistics generated within a given time window.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchModelDeploymentMonitoringStatsAnomaliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchModelDeploymentMonitoringStatsAnomaliesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SearchModelDeploymentMonitoringStatsAnomaliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SearchModelDeploymentMonitoringStatsAnomaliesResponse)>` |   
  
### updateModelDeploymentMonitoringJob(UpdateModelDeploymentMonitoringJobRequest request)
    
    
    public ListenableFuture<Operation> updateModelDeploymentMonitoringJob(UpdateModelDeploymentMonitoringJobRequest request)

Updates a ModelDeploymentMonitoringJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateModelDeploymentMonitoringJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
