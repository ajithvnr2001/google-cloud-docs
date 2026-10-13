---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient
title: Class JobServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:09.763243+00:00
---

# Class JobServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class JobServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/JobServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for creating and managing Vertex AI's jobs.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CustomJob customJob = CustomJob.newBuilder().build();
       CustomJob response = jobServiceClient.createCustomJob(parent, customJob);
     }
     

Note: close() needs to be called on the JobServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateCustomJob |  Creates a CustomJob. A created CustomJob right away will be attempted to be run. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomJob(CreateCustomJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCustomJob(LocationName parent, CustomJob customJob) 
  * createCustomJob(String parent, CustomJob customJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomJobCallable() 

  
GetCustomJob |  Gets a CustomJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomJob(GetCustomJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomJob(CustomJobName name) 
  * getCustomJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomJobCallable() 

  
ListCustomJobs |  Lists CustomJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomJobs(ListCustomJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomJobs(LocationName parent) 
  * listCustomJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomJobsPagedCallable() 
  * listCustomJobsCallable() 

  
DeleteCustomJob |  Deletes a CustomJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCustomJobAsync(DeleteCustomJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCustomJobAsync(CustomJobName name) 
  * deleteCustomJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCustomJobOperationCallable() 
  * deleteCustomJobCallable() 

  
CancelCustomJob |  Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelCustomJob(CancelCustomJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelCustomJob(CustomJobName name) 
  * cancelCustomJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelCustomJobCallable() 

  
CreateDataLabelingJob |  Creates a DataLabelingJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataLabelingJob(CreateDataLabelingJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDataLabelingJob(LocationName parent, DataLabelingJob dataLabelingJob) 
  * createDataLabelingJob(String parent, DataLabelingJob dataLabelingJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataLabelingJobCallable() 

  
GetDataLabelingJob |  Gets a DataLabelingJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataLabelingJob(GetDataLabelingJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataLabelingJob(DataLabelingJobName name) 
  * getDataLabelingJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataLabelingJobCallable() 

  
ListDataLabelingJobs |  Lists DataLabelingJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataLabelingJobs(ListDataLabelingJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataLabelingJobs(LocationName parent) 
  * listDataLabelingJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataLabelingJobsPagedCallable() 
  * listDataLabelingJobsCallable() 

  
DeleteDataLabelingJob |  Deletes a DataLabelingJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataLabelingJobAsync(DeleteDataLabelingJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataLabelingJobAsync(DataLabelingJobName name) 
  * deleteDataLabelingJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataLabelingJobOperationCallable() 
  * deleteDataLabelingJobCallable() 

  
CancelDataLabelingJob |  Cancels a DataLabelingJob. Success of cancellation is not guaranteed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelDataLabelingJob(CancelDataLabelingJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelDataLabelingJob(DataLabelingJobName name) 
  * cancelDataLabelingJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelDataLabelingJobCallable() 

  
CreateHyperparameterTuningJob |  Creates a HyperparameterTuningJob |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createHyperparameterTuningJob(LocationName parent, HyperparameterTuningJob hyperparameterTuningJob) 
  * createHyperparameterTuningJob(String parent, HyperparameterTuningJob hyperparameterTuningJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createHyperparameterTuningJobCallable() 

  
GetHyperparameterTuningJob |  Gets a HyperparameterTuningJob |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHyperparameterTuningJob(HyperparameterTuningJobName name) 
  * getHyperparameterTuningJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHyperparameterTuningJobCallable() 

  
ListHyperparameterTuningJobs |  Lists HyperparameterTuningJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listHyperparameterTuningJobs(LocationName parent) 
  * listHyperparameterTuningJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listHyperparameterTuningJobsPagedCallable() 
  * listHyperparameterTuningJobsCallable() 

  
DeleteHyperparameterTuningJob |  Deletes a HyperparameterTuningJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteHyperparameterTuningJobAsync(DeleteHyperparameterTuningJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteHyperparameterTuningJobAsync(HyperparameterTuningJobName name) 
  * deleteHyperparameterTuningJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteHyperparameterTuningJobOperationCallable() 
  * deleteHyperparameterTuningJobCallable() 

  
CancelHyperparameterTuningJob |  Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelHyperparameterTuningJob(HyperparameterTuningJobName name) 
  * cancelHyperparameterTuningJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelHyperparameterTuningJobCallable() 

  
CreateNasJob |  Creates a NasJob |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createNasJob(CreateNasJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createNasJob(LocationName parent, NasJob nasJob) 
  * createNasJob(String parent, NasJob nasJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createNasJobCallable() 

  
GetNasJob |  Gets a NasJob |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNasJob(GetNasJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNasJob(NasJobName name) 
  * getNasJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNasJobCallable() 

  
ListNasJobs |  Lists NasJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNasJobs(ListNasJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNasJobs(LocationName parent) 
  * listNasJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNasJobsPagedCallable() 
  * listNasJobsCallable() 

  
DeleteNasJob |  Deletes a NasJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNasJobAsync(DeleteNasJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNasJobAsync(NasJobName name) 
  * deleteNasJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNasJobOperationCallable() 
  * deleteNasJobCallable() 

  
CancelNasJob |  Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelNasJob(CancelNasJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelNasJob(NasJobName name) 
  * cancelNasJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelNasJobCallable() 

  
GetNasTrialDetail |  Gets a NasTrialDetail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNasTrialDetail(GetNasTrialDetailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNasTrialDetail(NasTrialDetailName name) 
  * getNasTrialDetail(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNasTrialDetailCallable() 

  
ListNasTrialDetails |  List top NasTrialDetails of a NasJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNasTrialDetails(ListNasTrialDetailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNasTrialDetails(NasJobName parent) 
  * listNasTrialDetails(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNasTrialDetailsPagedCallable() 
  * listNasTrialDetailsCallable() 

  
CreateBatchPredictionJob |  Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBatchPredictionJob(CreateBatchPredictionJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createBatchPredictionJob(LocationName parent, BatchPredictionJob batchPredictionJob) 
  * createBatchPredictionJob(String parent, BatchPredictionJob batchPredictionJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBatchPredictionJobCallable() 

  
GetBatchPredictionJob |  Gets a BatchPredictionJob |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBatchPredictionJob(GetBatchPredictionJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBatchPredictionJob(BatchPredictionJobName name) 
  * getBatchPredictionJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBatchPredictionJobCallable() 

  
ListBatchPredictionJobs |  Lists BatchPredictionJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBatchPredictionJobs(ListBatchPredictionJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBatchPredictionJobs(LocationName parent) 
  * listBatchPredictionJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBatchPredictionJobsPagedCallable() 
  * listBatchPredictionJobsCallable() 

  
DeleteBatchPredictionJob |  Deletes a BatchPredictionJob. Can only be called on jobs that already finished. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBatchPredictionJobAsync(DeleteBatchPredictionJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBatchPredictionJobAsync(BatchPredictionJobName name) 
  * deleteBatchPredictionJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBatchPredictionJobOperationCallable() 
  * deleteBatchPredictionJobCallable() 

  
CancelBatchPredictionJob |  Cancels a BatchPredictionJob.  Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelBatchPredictionJob(CancelBatchPredictionJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelBatchPredictionJob(BatchPredictionJobName name) 
  * cancelBatchPredictionJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelBatchPredictionJobCallable() 

  
CreateModelDeploymentMonitoringJob |  Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createModelDeploymentMonitoringJob(LocationName parent, ModelDeploymentMonitoringJob modelDeploymentMonitoringJob) 
  * createModelDeploymentMonitoringJob(String parent, ModelDeploymentMonitoringJob modelDeploymentMonitoringJob) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createModelDeploymentMonitoringJobCallable() 

  
SearchModelDeploymentMonitoringStatsAnomalies |  Searches Model Monitoring Statistics generated within a given time window. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchModelDeploymentMonitoringStatsAnomalies(ModelDeploymentMonitoringJobName modelDeploymentMonitoringJob, String deployedModelId) 
  * searchModelDeploymentMonitoringStatsAnomalies(String modelDeploymentMonitoringJob, String deployedModelId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchModelDeploymentMonitoringStatsAnomaliesPagedCallable() 
  * searchModelDeploymentMonitoringStatsAnomaliesCallable() 

  
GetModelDeploymentMonitoringJob |  Gets a ModelDeploymentMonitoringJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getModelDeploymentMonitoringJob(ModelDeploymentMonitoringJobName name) 
  * getModelDeploymentMonitoringJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getModelDeploymentMonitoringJobCallable() 

  
ListModelDeploymentMonitoringJobs |  Lists ModelDeploymentMonitoringJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listModelDeploymentMonitoringJobs(LocationName parent) 
  * listModelDeploymentMonitoringJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listModelDeploymentMonitoringJobsPagedCallable() 
  * listModelDeploymentMonitoringJobsCallable() 

  
UpdateModelDeploymentMonitoringJob |  Updates a ModelDeploymentMonitoringJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateModelDeploymentMonitoringJobAsync(UpdateModelDeploymentMonitoringJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateModelDeploymentMonitoringJobAsync(ModelDeploymentMonitoringJob modelDeploymentMonitoringJob, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateModelDeploymentMonitoringJobOperationCallable() 
  * updateModelDeploymentMonitoringJobCallable() 

  
DeleteModelDeploymentMonitoringJob |  Deletes a ModelDeploymentMonitoringJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteModelDeploymentMonitoringJobAsync(DeleteModelDeploymentMonitoringJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteModelDeploymentMonitoringJobAsync(ModelDeploymentMonitoringJobName name) 
  * deleteModelDeploymentMonitoringJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteModelDeploymentMonitoringJobOperationCallable() 
  * deleteModelDeploymentMonitoringJobCallable() 

  
PauseModelDeploymentMonitoringJob |  Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * pauseModelDeploymentMonitoringJob(ModelDeploymentMonitoringJobName name) 
  * pauseModelDeploymentMonitoringJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pauseModelDeploymentMonitoringJobCallable() 

  
ResumeModelDeploymentMonitoringJob |  Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * resumeModelDeploymentMonitoringJob(ModelDeploymentMonitoringJobName name) 
  * resumeModelDeploymentMonitoringJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeModelDeploymentMonitoringJobCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of JobServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     JobServiceSettings jobServiceSettings =
         JobServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     JobServiceClient jobServiceClient = JobServiceClient.create(jobServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     JobServiceSettings jobServiceSettings =
         JobServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     JobServiceClient jobServiceClient = JobServiceClient.create(jobServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > JobServiceClient

## Static Methods 

### create()
    
    
    public static final JobServiceClient create()

Constructs an instance of JobServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(JobServiceSettings settings)
    
    
    public static final JobServiceClient create(JobServiceSettings settings)

Constructs an instance of JobServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(JobServiceStub stub)
    
    
    public static final JobServiceClient create(JobServiceStub stub)

Constructs an instance of JobServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(JobServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[JobServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.JobServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient)` |   
  
## Constructors 

### JobServiceClient(JobServiceSettings settings)
    
    
    protected JobServiceClient(JobServiceSettings settings)

Constructs an instance of JobServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[JobServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceSettings)`  
  
  
### JobServiceClient(JobServiceStub stub)
    
    
    protected JobServiceClient(JobServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[JobServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.JobServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### cancelBatchPredictionJob(@Nullable BatchPredictionJobName name)
    
    
    public final void cancelBatchPredictionJob(@Nullable BatchPredictionJobName name)

Cancels a BatchPredictionJob.

Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       BatchPredictionJobName name =
           BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]");
       jobServiceClient.cancelBatchPredictionJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.BatchPredictionJobName`  
Required. The name of the BatchPredictionJob to cancel. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
  
### cancelBatchPredictionJob(CancelBatchPredictionJobRequest request)
    
    
    public final void cancelBatchPredictionJob(CancelBatchPredictionJobRequest request)

Cancels a BatchPredictionJob.

Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelBatchPredictionJobRequest request =
           CancelBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       jobServiceClient.cancelBatchPredictionJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelBatchPredictionJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelBatchPredictionJob(String name)
    
    
    public final void cancelBatchPredictionJob(String name)

Cancels a BatchPredictionJob.

Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]").toString();
       jobServiceClient.cancelBatchPredictionJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the BatchPredictionJob to cancel. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
  
### cancelBatchPredictionJobCallable()
    
    
    public final UnaryCallable<CancelBatchPredictionJobRequest,Empty> cancelBatchPredictionJobCallable()

Cancels a BatchPredictionJob.

Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelBatchPredictionJobRequest request =
           CancelBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           jobServiceClient.cancelBatchPredictionJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelBatchPredictionJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelCustomJob(@Nullable CustomJobName name)
    
    
    public final void cancelCustomJob(@Nullable CustomJobName name)

Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CustomJobName name = CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]");
       jobServiceClient.cancelCustomJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.CustomJobName`  
Required. The name of the CustomJob to cancel. Format: `projects/{project}/locations/{location}/customJobs/{custom_job}`  
  
### cancelCustomJob(CancelCustomJobRequest request)
    
    
    public final void cancelCustomJob(CancelCustomJobRequest request)

Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelCustomJobRequest request =
           CancelCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       jobServiceClient.cancelCustomJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelCustomJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelCustomJob(String name)
    
    
    public final void cancelCustomJob(String name)

Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name = CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString();
       jobServiceClient.cancelCustomJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CustomJob to cancel. Format: `projects/{project}/locations/{location}/customJobs/{custom_job}`  
  
### cancelCustomJobCallable()
    
    
    public final UnaryCallable<CancelCustomJobRequest,Empty> cancelCustomJobCallable()

Cancels a CustomJob. Starts asynchronous cancellation on the CustomJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetCustomJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the CustomJob is not deleted; instead it becomes a job with a CustomJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and CustomJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelCustomJobRequest request =
           CancelCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       ApiFuture<Empty> future = jobServiceClient.cancelCustomJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelCustomJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelDataLabelingJob(@Nullable DataLabelingJobName name)
    
    
    public final void cancelDataLabelingJob(@Nullable DataLabelingJobName name)

Cancels a DataLabelingJob. Success of cancellation is not guaranteed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DataLabelingJobName name =
           DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]");
       jobServiceClient.cancelDataLabelingJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DataLabelingJobName`  
Required. The name of the DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`  
  
### cancelDataLabelingJob(CancelDataLabelingJobRequest request)
    
    
    public final void cancelDataLabelingJob(CancelDataLabelingJobRequest request)

Cancels a DataLabelingJob. Success of cancellation is not guaranteed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelDataLabelingJobRequest request =
           CancelDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       jobServiceClient.cancelDataLabelingJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelDataLabelingJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelDataLabelingJob(String name)
    
    
    public final void cancelDataLabelingJob(String name)

Cancels a DataLabelingJob. Success of cancellation is not guaranteed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]").toString();
       jobServiceClient.cancelDataLabelingJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`  
  
### cancelDataLabelingJobCallable()
    
    
    public final UnaryCallable<CancelDataLabelingJobRequest,Empty> cancelDataLabelingJobCallable()

Cancels a DataLabelingJob. Success of cancellation is not guaranteed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelDataLabelingJobRequest request =
           CancelDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           jobServiceClient.cancelDataLabelingJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelDataLabelingJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelHyperparameterTuningJob(@Nullable HyperparameterTuningJobName name)
    
    
    public final void cancelHyperparameterTuningJob(@Nullable HyperparameterTuningJobName name)

Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       HyperparameterTuningJobName name =
           HyperparameterTuningJobName.of("[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]");
       jobServiceClient.cancelHyperparameterTuningJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.HyperparameterTuningJobName`  
Required. The name of the HyperparameterTuningJob to cancel. Format: `projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}`  
  
### cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request)
    
    
    public final void cancelHyperparameterTuningJob(CancelHyperparameterTuningJobRequest request)

Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelHyperparameterTuningJobRequest request =
           CancelHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       jobServiceClient.cancelHyperparameterTuningJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelHyperparameterTuningJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelHyperparameterTuningJob(String name)
    
    
    public final void cancelHyperparameterTuningJob(String name)

Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           HyperparameterTuningJobName.of("[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
               .toString();
       jobServiceClient.cancelHyperparameterTuningJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the HyperparameterTuningJob to cancel. Format: `projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}`  
  
### cancelHyperparameterTuningJobCallable()
    
    
    public final UnaryCallable<CancelHyperparameterTuningJobRequest,Empty> cancelHyperparameterTuningJobCallable()

Cancels a HyperparameterTuningJob. Starts asynchronous cancellation on the HyperparameterTuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetHyperparameterTuningJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the HyperparameterTuningJob is not deleted; instead it becomes a job with a HyperparameterTuningJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and HyperparameterTuningJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelHyperparameterTuningJobRequest request =
           CancelHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           jobServiceClient.cancelHyperparameterTuningJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelHyperparameterTuningJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelNasJob(@Nullable NasJobName name)
    
    
    public final void cancelNasJob(@Nullable NasJobName name)

Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       NasJobName name = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]");
       jobServiceClient.cancelNasJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NasJobName`  
Required. The name of the NasJob to cancel. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
  
### cancelNasJob(CancelNasJobRequest request)
    
    
    public final void cancelNasJob(CancelNasJobRequest request)

Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelNasJobRequest request =
           CancelNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       jobServiceClient.cancelNasJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelNasJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelNasJob(String name)
    
    
    public final void cancelNasJob(String name)

Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString();
       jobServiceClient.cancelNasJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NasJob to cancel. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
  
### cancelNasJobCallable()
    
    
    public final UnaryCallable<CancelNasJobRequest,Empty> cancelNasJobCallable()

Cancels a NasJob. Starts asynchronous cancellation on the NasJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetNasJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the NasJob is not deleted; instead it becomes a job with a NasJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and NasJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CancelNasJobRequest request =
           CancelNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       ApiFuture<Empty> future = jobServiceClient.cancelNasJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelNasJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### createBatchPredictionJob(@Nullable LocationName parent, BatchPredictionJob batchPredictionJob)
    
    
    public final BatchPredictionJob createBatchPredictionJob(@Nullable LocationName parent, BatchPredictionJob batchPredictionJob)

Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BatchPredictionJob batchPredictionJob = BatchPredictionJob.newBuilder().build();
       BatchPredictionJob response =
           jobServiceClient.createBatchPredictionJob(parent, batchPredictionJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the BatchPredictionJob in. Format: `projects/{project}/locations/{location}`  
`batchPredictionJob` | `[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)`  
Required. The BatchPredictionJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)` |   
  
### createBatchPredictionJob(CreateBatchPredictionJobRequest request)
    
    
    public final BatchPredictionJob createBatchPredictionJob(CreateBatchPredictionJobRequest request)

Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateBatchPredictionJobRequest request =
           CreateBatchPredictionJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBatchPredictionJob(BatchPredictionJob.newBuilder().build())
               .build();
       BatchPredictionJob response = jobServiceClient.createBatchPredictionJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateBatchPredictionJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)` |   
  
### createBatchPredictionJob(String parent, BatchPredictionJob batchPredictionJob)
    
    
    public final BatchPredictionJob createBatchPredictionJob(String parent, BatchPredictionJob batchPredictionJob)

Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       BatchPredictionJob batchPredictionJob = BatchPredictionJob.newBuilder().build();
       BatchPredictionJob response =
           jobServiceClient.createBatchPredictionJob(parent, batchPredictionJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the BatchPredictionJob in. Format: `projects/{project}/locations/{location}`  
`batchPredictionJob` | `[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)`  
Required. The BatchPredictionJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)` |   
  
### createBatchPredictionJobCallable()
    
    
    public final UnaryCallable<CreateBatchPredictionJobRequest,BatchPredictionJob> createBatchPredictionJobCallable()

Creates a BatchPredictionJob. A BatchPredictionJob once created will right away be attempted to start.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateBatchPredictionJobRequest request =
           CreateBatchPredictionJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setBatchPredictionJob(BatchPredictionJob.newBuilder().build())
               .build();
       ApiFuture<BatchPredictionJob> future =
           jobServiceClient.createBatchPredictionJobCallable().futureCall(request);
       // Do something.
       BatchPredictionJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateBatchPredictionJobRequest),[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)>` |   
  
### createCustomJob(@Nullable LocationName parent, CustomJob customJob)
    
    
    public final CustomJob createCustomJob(@Nullable LocationName parent, CustomJob customJob)

Creates a CustomJob. A created CustomJob right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CustomJob customJob = CustomJob.newBuilder().build();
       CustomJob response = jobServiceClient.createCustomJob(parent, customJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the CustomJob in. Format: `projects/{project}/locations/{location}`  
`customJob` | `[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)`  
Required. The CustomJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)` |   
  
### createCustomJob(CreateCustomJobRequest request)
    
    
    public final CustomJob createCustomJob(CreateCustomJobRequest request)

Creates a CustomJob. A created CustomJob right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateCustomJobRequest request =
           CreateCustomJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCustomJob(CustomJob.newBuilder().build())
               .build();
       CustomJob response = jobServiceClient.createCustomJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateCustomJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)` |   
  
### createCustomJob(String parent, CustomJob customJob)
    
    
    public final CustomJob createCustomJob(String parent, CustomJob customJob)

Creates a CustomJob. A created CustomJob right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       CustomJob customJob = CustomJob.newBuilder().build();
       CustomJob response = jobServiceClient.createCustomJob(parent, customJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the CustomJob in. Format: `projects/{project}/locations/{location}`  
`customJob` | `[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)`  
Required. The CustomJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)` |   
  
### createCustomJobCallable()
    
    
    public final UnaryCallable<CreateCustomJobRequest,CustomJob> createCustomJobCallable()

Creates a CustomJob. A created CustomJob right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateCustomJobRequest request =
           CreateCustomJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCustomJob(CustomJob.newBuilder().build())
               .build();
       ApiFuture<CustomJob> future = jobServiceClient.createCustomJobCallable().futureCall(request);
       // Do something.
       CustomJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateCustomJobRequest),[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)>` |   
  
### createDataLabelingJob(@Nullable LocationName parent, DataLabelingJob dataLabelingJob)
    
    
    public final DataLabelingJob createDataLabelingJob(@Nullable LocationName parent, DataLabelingJob dataLabelingJob)

Creates a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DataLabelingJob dataLabelingJob = DataLabelingJob.newBuilder().build();
       DataLabelingJob response = jobServiceClient.createDataLabelingJob(parent, dataLabelingJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The parent of the DataLabelingJob. Format: `projects/{project}/locations/{location}`  
`dataLabelingJob` | `[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)`  
Required. The DataLabelingJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)` |   
  
### createDataLabelingJob(CreateDataLabelingJobRequest request)
    
    
    public final DataLabelingJob createDataLabelingJob(CreateDataLabelingJobRequest request)

Creates a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateDataLabelingJobRequest request =
           CreateDataLabelingJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataLabelingJob(DataLabelingJob.newBuilder().build())
               .build();
       DataLabelingJob response = jobServiceClient.createDataLabelingJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDataLabelingJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)` |   
  
### createDataLabelingJob(String parent, DataLabelingJob dataLabelingJob)
    
    
    public final DataLabelingJob createDataLabelingJob(String parent, DataLabelingJob dataLabelingJob)

Creates a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DataLabelingJob dataLabelingJob = DataLabelingJob.newBuilder().build();
       DataLabelingJob response = jobServiceClient.createDataLabelingJob(parent, dataLabelingJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the DataLabelingJob. Format: `projects/{project}/locations/{location}`  
`dataLabelingJob` | `[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)`  
Required. The DataLabelingJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)` |   
  
### createDataLabelingJobCallable()
    
    
    public final UnaryCallable<CreateDataLabelingJobRequest,DataLabelingJob> createDataLabelingJobCallable()

Creates a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateDataLabelingJobRequest request =
           CreateDataLabelingJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDataLabelingJob(DataLabelingJob.newBuilder().build())
               .build();
       ApiFuture<DataLabelingJob> future =
           jobServiceClient.createDataLabelingJobCallable().futureCall(request);
       // Do something.
       DataLabelingJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDataLabelingJobRequest),[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)>` |   
  
### createHyperparameterTuningJob(@Nullable LocationName parent, HyperparameterTuningJob hyperparameterTuningJob)
    
    
    public final HyperparameterTuningJob createHyperparameterTuningJob(@Nullable LocationName parent, HyperparameterTuningJob hyperparameterTuningJob)

Creates a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       HyperparameterTuningJob hyperparameterTuningJob =
           HyperparameterTuningJob.newBuilder().build();
       HyperparameterTuningJob response =
           jobServiceClient.createHyperparameterTuningJob(parent, hyperparameterTuningJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the HyperparameterTuningJob in. Format: `projects/{project}/locations/{location}`  
`hyperparameterTuningJob` | `[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)`  
Required. The HyperparameterTuningJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)` |   
  
### createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request)
    
    
    public final HyperparameterTuningJob createHyperparameterTuningJob(CreateHyperparameterTuningJobRequest request)

Creates a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateHyperparameterTuningJobRequest request =
           CreateHyperparameterTuningJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHyperparameterTuningJob(HyperparameterTuningJob.newBuilder().build())
               .build();
       HyperparameterTuningJob response = jobServiceClient.createHyperparameterTuningJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateHyperparameterTuningJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)` |   
  
### createHyperparameterTuningJob(String parent, HyperparameterTuningJob hyperparameterTuningJob)
    
    
    public final HyperparameterTuningJob createHyperparameterTuningJob(String parent, HyperparameterTuningJob hyperparameterTuningJob)

Creates a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       HyperparameterTuningJob hyperparameterTuningJob =
           HyperparameterTuningJob.newBuilder().build();
       HyperparameterTuningJob response =
           jobServiceClient.createHyperparameterTuningJob(parent, hyperparameterTuningJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the HyperparameterTuningJob in. Format: `projects/{project}/locations/{location}`  
`hyperparameterTuningJob` | `[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)`  
Required. The HyperparameterTuningJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)` |   
  
### createHyperparameterTuningJobCallable()
    
    
    public final UnaryCallable<CreateHyperparameterTuningJobRequest,HyperparameterTuningJob> createHyperparameterTuningJobCallable()

Creates a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateHyperparameterTuningJobRequest request =
           CreateHyperparameterTuningJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setHyperparameterTuningJob(HyperparameterTuningJob.newBuilder().build())
               .build();
       ApiFuture<HyperparameterTuningJob> future =
           jobServiceClient.createHyperparameterTuningJobCallable().futureCall(request);
       // Do something.
       HyperparameterTuningJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateHyperparameterTuningJobRequest),[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)>` |   
  
### createModelDeploymentMonitoringJob(@Nullable LocationName parent, ModelDeploymentMonitoringJob modelDeploymentMonitoringJob)
    
    
    public final ModelDeploymentMonitoringJob createModelDeploymentMonitoringJob(@Nullable LocationName parent, ModelDeploymentMonitoringJob modelDeploymentMonitoringJob)

Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ModelDeploymentMonitoringJob modelDeploymentMonitoringJob =
           ModelDeploymentMonitoringJob.newBuilder().build();
       ModelDeploymentMonitoringJob response =
           jobServiceClient.createModelDeploymentMonitoringJob(parent, modelDeploymentMonitoringJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The parent of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}`  
`modelDeploymentMonitoringJob` | `[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)`  
Required. The ModelDeploymentMonitoringJob to create  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)` |   
  
### createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request)
    
    
    public final ModelDeploymentMonitoringJob createModelDeploymentMonitoringJob(CreateModelDeploymentMonitoringJobRequest request)

Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateModelDeploymentMonitoringJobRequest request =
           CreateModelDeploymentMonitoringJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setModelDeploymentMonitoringJob(ModelDeploymentMonitoringJob.newBuilder().build())
               .build();
       ModelDeploymentMonitoringJob response =
           jobServiceClient.createModelDeploymentMonitoringJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateModelDeploymentMonitoringJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)` |   
  
### createModelDeploymentMonitoringJob(String parent, ModelDeploymentMonitoringJob modelDeploymentMonitoringJob)
    
    
    public final ModelDeploymentMonitoringJob createModelDeploymentMonitoringJob(String parent, ModelDeploymentMonitoringJob modelDeploymentMonitoringJob)

Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ModelDeploymentMonitoringJob modelDeploymentMonitoringJob =
           ModelDeploymentMonitoringJob.newBuilder().build();
       ModelDeploymentMonitoringJob response =
           jobServiceClient.createModelDeploymentMonitoringJob(parent, modelDeploymentMonitoringJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}`  
`modelDeploymentMonitoringJob` | `[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)`  
Required. The ModelDeploymentMonitoringJob to create  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)` |   
  
### createModelDeploymentMonitoringJobCallable()
    
    
    public final UnaryCallable<CreateModelDeploymentMonitoringJobRequest,ModelDeploymentMonitoringJob> createModelDeploymentMonitoringJobCallable()

Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateModelDeploymentMonitoringJobRequest request =
           CreateModelDeploymentMonitoringJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setModelDeploymentMonitoringJob(ModelDeploymentMonitoringJob.newBuilder().build())
               .build();
       ApiFuture<ModelDeploymentMonitoringJob> future =
           jobServiceClient.createModelDeploymentMonitoringJobCallable().futureCall(request);
       // Do something.
       ModelDeploymentMonitoringJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateModelDeploymentMonitoringJobRequest),[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)>` |   
  
### createNasJob(@Nullable LocationName parent, NasJob nasJob)
    
    
    public final NasJob createNasJob(@Nullable LocationName parent, NasJob nasJob)

Creates a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       NasJob nasJob = NasJob.newBuilder().build();
       NasJob response = jobServiceClient.createNasJob(parent, nasJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the NasJob in. Format: `projects/{project}/locations/{location}`  
`nasJob` | `[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)`  
Required. The NasJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)` |   
  
### createNasJob(CreateNasJobRequest request)
    
    
    public final NasJob createNasJob(CreateNasJobRequest request)

Creates a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateNasJobRequest request =
           CreateNasJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNasJob(NasJob.newBuilder().build())
               .build();
       NasJob response = jobServiceClient.createNasJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNasJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)` |   
  
### createNasJob(String parent, NasJob nasJob)
    
    
    public final NasJob createNasJob(String parent, NasJob nasJob)

Creates a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       NasJob nasJob = NasJob.newBuilder().build();
       NasJob response = jobServiceClient.createNasJob(parent, nasJob);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the NasJob in. Format: `projects/{project}/locations/{location}`  
`nasJob` | `[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)`  
Required. The NasJob to create.  
**Returns**  
---  
**Type** | **Description**  
`[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)` |   
  
### createNasJobCallable()
    
    
    public final UnaryCallable<CreateNasJobRequest,NasJob> createNasJobCallable()

Creates a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CreateNasJobRequest request =
           CreateNasJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setNasJob(NasJob.newBuilder().build())
               .build();
       ApiFuture<NasJob> future = jobServiceClient.createNasJobCallable().futureCall(request);
       // Do something.
       NasJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNasJobRequest),[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)>` |   
  
### deleteBatchPredictionJobAsync(@Nullable BatchPredictionJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteBatchPredictionJobAsync(@Nullable BatchPredictionJobName name)

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       BatchPredictionJobName name =
           BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]");
       jobServiceClient.deleteBatchPredictionJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.BatchPredictionJobName`  
Required. The name of the BatchPredictionJob resource to be deleted. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteBatchPredictionJobAsync(DeleteBatchPredictionJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteBatchPredictionJobAsync(DeleteBatchPredictionJobRequest request)

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteBatchPredictionJobRequest request =
           DeleteBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       jobServiceClient.deleteBatchPredictionJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteBatchPredictionJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteBatchPredictionJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteBatchPredictionJobAsync(String name)

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]").toString();
       jobServiceClient.deleteBatchPredictionJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the BatchPredictionJob resource to be deleted. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteBatchPredictionJobCallable()
    
    
    public final UnaryCallable<DeleteBatchPredictionJobRequest,Operation> deleteBatchPredictionJobCallable()

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteBatchPredictionJobRequest request =
           DeleteBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           jobServiceClient.deleteBatchPredictionJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteBatchPredictionJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBatchPredictionJobOperationCallable()
    
    
    public final OperationCallable<DeleteBatchPredictionJobRequest,Empty,DeleteOperationMetadata> deleteBatchPredictionJobOperationCallable()

Deletes a BatchPredictionJob. Can only be called on jobs that already finished.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteBatchPredictionJobRequest request =
           DeleteBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           jobServiceClient.deleteBatchPredictionJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteBatchPredictionJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteCustomJobAsync(@Nullable CustomJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteCustomJobAsync(@Nullable CustomJobName name)

Deletes a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CustomJobName name = CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]");
       jobServiceClient.deleteCustomJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.CustomJobName`  
Required. The name of the CustomJob resource to be deleted. Format: `projects/{project}/locations/{location}/customJobs/{custom_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteCustomJobAsync(DeleteCustomJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteCustomJobAsync(DeleteCustomJobRequest request)

Deletes a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteCustomJobRequest request =
           DeleteCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       jobServiceClient.deleteCustomJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteCustomJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteCustomJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteCustomJobAsync(String name)

Deletes a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name = CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString();
       jobServiceClient.deleteCustomJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CustomJob resource to be deleted. Format: `projects/{project}/locations/{location}/customJobs/{custom_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteCustomJobCallable()
    
    
    public final UnaryCallable<DeleteCustomJobRequest,Operation> deleteCustomJobCallable()

Deletes a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteCustomJobRequest request =
           DeleteCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       ApiFuture<Operation> future = jobServiceClient.deleteCustomJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteCustomJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCustomJobOperationCallable()
    
    
    public final OperationCallable<DeleteCustomJobRequest,Empty,DeleteOperationMetadata> deleteCustomJobOperationCallable()

Deletes a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteCustomJobRequest request =
           DeleteCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           jobServiceClient.deleteCustomJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteCustomJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDataLabelingJobAsync(@Nullable DataLabelingJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDataLabelingJobAsync(@Nullable DataLabelingJobName name)

Deletes a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DataLabelingJobName name =
           DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]");
       jobServiceClient.deleteDataLabelingJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DataLabelingJobName`  
Required. The name of the DataLabelingJob to be deleted. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDataLabelingJobAsync(DeleteDataLabelingJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDataLabelingJobAsync(DeleteDataLabelingJobRequest request)

Deletes a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteDataLabelingJobRequest request =
           DeleteDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       jobServiceClient.deleteDataLabelingJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDataLabelingJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDataLabelingJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDataLabelingJobAsync(String name)

Deletes a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]").toString();
       jobServiceClient.deleteDataLabelingJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DataLabelingJob to be deleted. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDataLabelingJobCallable()
    
    
    public final UnaryCallable<DeleteDataLabelingJobRequest,Operation> deleteDataLabelingJobCallable()

Deletes a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteDataLabelingJobRequest request =
           DeleteDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           jobServiceClient.deleteDataLabelingJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDataLabelingJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataLabelingJobOperationCallable()
    
    
    public final OperationCallable<DeleteDataLabelingJobRequest,Empty,DeleteOperationMetadata> deleteDataLabelingJobOperationCallable()

Deletes a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteDataLabelingJobRequest request =
           DeleteDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           jobServiceClient.deleteDataLabelingJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDataLabelingJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteHyperparameterTuningJobAsync(@Nullable HyperparameterTuningJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteHyperparameterTuningJobAsync(@Nullable HyperparameterTuningJobName name)

Deletes a HyperparameterTuningJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       HyperparameterTuningJobName name =
           HyperparameterTuningJobName.of("[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]");
       jobServiceClient.deleteHyperparameterTuningJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.HyperparameterTuningJobName`  
Required. The name of the HyperparameterTuningJob resource to be deleted. Format: `projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteHyperparameterTuningJobAsync(DeleteHyperparameterTuningJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteHyperparameterTuningJobAsync(DeleteHyperparameterTuningJobRequest request)

Deletes a HyperparameterTuningJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteHyperparameterTuningJobRequest request =
           DeleteHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       jobServiceClient.deleteHyperparameterTuningJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteHyperparameterTuningJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteHyperparameterTuningJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteHyperparameterTuningJobAsync(String name)

Deletes a HyperparameterTuningJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           HyperparameterTuningJobName.of("[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
               .toString();
       jobServiceClient.deleteHyperparameterTuningJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the HyperparameterTuningJob resource to be deleted. Format: `projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteHyperparameterTuningJobCallable()
    
    
    public final UnaryCallable<DeleteHyperparameterTuningJobRequest,Operation> deleteHyperparameterTuningJobCallable()

Deletes a HyperparameterTuningJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteHyperparameterTuningJobRequest request =
           DeleteHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           jobServiceClient.deleteHyperparameterTuningJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteHyperparameterTuningJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHyperparameterTuningJobOperationCallable()
    
    
    public final OperationCallable<DeleteHyperparameterTuningJobRequest,Empty,DeleteOperationMetadata> deleteHyperparameterTuningJobOperationCallable()

Deletes a HyperparameterTuningJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteHyperparameterTuningJobRequest request =
           DeleteHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           jobServiceClient.deleteHyperparameterTuningJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteHyperparameterTuningJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelDeploymentMonitoringJobAsync(@Nullable ModelDeploymentMonitoringJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelDeploymentMonitoringJobAsync(@Nullable ModelDeploymentMonitoringJobName name)

Deletes a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ModelDeploymentMonitoringJobName name =
           ModelDeploymentMonitoringJobName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]");
       jobServiceClient.deleteModelDeploymentMonitoringJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobName`  
Required. The resource name of the model monitoring job to delete. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelDeploymentMonitoringJobAsync(DeleteModelDeploymentMonitoringJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelDeploymentMonitoringJobAsync(DeleteModelDeploymentMonitoringJobRequest request)

Deletes a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteModelDeploymentMonitoringJobRequest request =
           DeleteModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       jobServiceClient.deleteModelDeploymentMonitoringJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelDeploymentMonitoringJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelDeploymentMonitoringJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteModelDeploymentMonitoringJobAsync(String name)

Deletes a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           ModelDeploymentMonitoringJobName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
               .toString();
       jobServiceClient.deleteModelDeploymentMonitoringJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the model monitoring job to delete. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteModelDeploymentMonitoringJobCallable()
    
    
    public final UnaryCallable<DeleteModelDeploymentMonitoringJobRequest,Operation> deleteModelDeploymentMonitoringJobCallable()

Deletes a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteModelDeploymentMonitoringJobRequest request =
           DeleteModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           jobServiceClient.deleteModelDeploymentMonitoringJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelDeploymentMonitoringJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteModelDeploymentMonitoringJobOperationCallable()
    
    
    public final OperationCallable<DeleteModelDeploymentMonitoringJobRequest,Empty,DeleteOperationMetadata> deleteModelDeploymentMonitoringJobOperationCallable()

Deletes a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteModelDeploymentMonitoringJobRequest request =
           DeleteModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           jobServiceClient
               .deleteModelDeploymentMonitoringJobOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelDeploymentMonitoringJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNasJobAsync(@Nullable NasJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNasJobAsync(@Nullable NasJobName name)

Deletes a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       NasJobName name = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]");
       jobServiceClient.deleteNasJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NasJobName`  
Required. The name of the NasJob resource to be deleted. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNasJobAsync(DeleteNasJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNasJobAsync(DeleteNasJobRequest request)

Deletes a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteNasJobRequest request =
           DeleteNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       jobServiceClient.deleteNasJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNasJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNasJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteNasJobAsync(String name)

Deletes a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString();
       jobServiceClient.deleteNasJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NasJob resource to be deleted. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteNasJobCallable()
    
    
    public final UnaryCallable<DeleteNasJobRequest,Operation> deleteNasJobCallable()

Deletes a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteNasJobRequest request =
           DeleteNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       ApiFuture<Operation> future = jobServiceClient.deleteNasJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNasJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNasJobOperationCallable()
    
    
    public final OperationCallable<DeleteNasJobRequest,Empty,DeleteOperationMetadata> deleteNasJobOperationCallable()

Deletes a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DeleteNasJobRequest request =
           DeleteNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           jobServiceClient.deleteNasJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNasJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getBatchPredictionJob(@Nullable BatchPredictionJobName name)
    
    
    public final BatchPredictionJob getBatchPredictionJob(@Nullable BatchPredictionJobName name)

Gets a BatchPredictionJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       BatchPredictionJobName name =
           BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]");
       BatchPredictionJob response = jobServiceClient.getBatchPredictionJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.BatchPredictionJobName`  
Required. The name of the BatchPredictionJob resource. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)` |   
  
### getBatchPredictionJob(GetBatchPredictionJobRequest request)
    
    
    public final BatchPredictionJob getBatchPredictionJob(GetBatchPredictionJobRequest request)

Gets a BatchPredictionJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetBatchPredictionJobRequest request =
           GetBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       BatchPredictionJob response = jobServiceClient.getBatchPredictionJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetBatchPredictionJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)` |   
  
### getBatchPredictionJob(String name)
    
    
    public final BatchPredictionJob getBatchPredictionJob(String name)

Gets a BatchPredictionJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]").toString();
       BatchPredictionJob response = jobServiceClient.getBatchPredictionJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the BatchPredictionJob resource. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)` |   
  
### getBatchPredictionJobCallable()
    
    
    public final UnaryCallable<GetBatchPredictionJobRequest,BatchPredictionJob> getBatchPredictionJobCallable()

Gets a BatchPredictionJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetBatchPredictionJobRequest request =
           GetBatchPredictionJobRequest.newBuilder()
               .setName(
                   BatchPredictionJobName.of("[PROJECT]", "[LOCATION]", "[BATCH_PREDICTION_JOB]")
                       .toString())
               .build();
       ApiFuture<BatchPredictionJob> future =
           jobServiceClient.getBatchPredictionJobCallable().futureCall(request);
       // Do something.
       BatchPredictionJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBatchPredictionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetBatchPredictionJobRequest),[BatchPredictionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchPredictionJob)>` |   
  
### getCustomJob(@Nullable CustomJobName name)
    
    
    public final CustomJob getCustomJob(@Nullable CustomJobName name)

Gets a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       CustomJobName name = CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]");
       CustomJob response = jobServiceClient.getCustomJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.CustomJobName`  
Required. The name of the CustomJob resource. Format: `projects/{project}/locations/{location}/customJobs/{custom_job}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)` |   
  
### getCustomJob(GetCustomJobRequest request)
    
    
    public final CustomJob getCustomJob(GetCustomJobRequest request)

Gets a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetCustomJobRequest request =
           GetCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       CustomJob response = jobServiceClient.getCustomJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetCustomJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)` |   
  
### getCustomJob(String name)
    
    
    public final CustomJob getCustomJob(String name)

Gets a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name = CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString();
       CustomJob response = jobServiceClient.getCustomJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CustomJob resource. Format: `projects/{project}/locations/{location}/customJobs/{custom_job}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)` |   
  
### getCustomJobCallable()
    
    
    public final UnaryCallable<GetCustomJobRequest,CustomJob> getCustomJobCallable()

Gets a CustomJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetCustomJobRequest request =
           GetCustomJobRequest.newBuilder()
               .setName(CustomJobName.of("[PROJECT]", "[LOCATION]", "[CUSTOM_JOB]").toString())
               .build();
       ApiFuture<CustomJob> future = jobServiceClient.getCustomJobCallable().futureCall(request);
       // Do something.
       CustomJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetCustomJobRequest),[CustomJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJob)>` |   
  
### getDataLabelingJob(@Nullable DataLabelingJobName name)
    
    
    public final DataLabelingJob getDataLabelingJob(@Nullable DataLabelingJobName name)

Gets a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       DataLabelingJobName name =
           DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]");
       DataLabelingJob response = jobServiceClient.getDataLabelingJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DataLabelingJobName`  
Required. The name of the DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)` |   
  
### getDataLabelingJob(GetDataLabelingJobRequest request)
    
    
    public final DataLabelingJob getDataLabelingJob(GetDataLabelingJobRequest request)

Gets a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetDataLabelingJobRequest request =
           GetDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       DataLabelingJob response = jobServiceClient.getDataLabelingJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDataLabelingJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)` |   
  
### getDataLabelingJob(String name)
    
    
    public final DataLabelingJob getDataLabelingJob(String name)

Gets a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]").toString();
       DataLabelingJob response = jobServiceClient.getDataLabelingJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DataLabelingJob. Format: `projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}`  
**Returns**  
---  
**Type** | **Description**  
`[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)` |   
  
### getDataLabelingJobCallable()
    
    
    public final UnaryCallable<GetDataLabelingJobRequest,DataLabelingJob> getDataLabelingJobCallable()

Gets a DataLabelingJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetDataLabelingJobRequest request =
           GetDataLabelingJobRequest.newBuilder()
               .setName(
                   DataLabelingJobName.of("[PROJECT]", "[LOCATION]", "[DATA_LABELING_JOB]")
                       .toString())
               .build();
       ApiFuture<DataLabelingJob> future =
           jobServiceClient.getDataLabelingJobCallable().futureCall(request);
       // Do something.
       DataLabelingJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataLabelingJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDataLabelingJobRequest),[DataLabelingJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DataLabelingJob)>` |   
  
### getHyperparameterTuningJob(@Nullable HyperparameterTuningJobName name)
    
    
    public final HyperparameterTuningJob getHyperparameterTuningJob(@Nullable HyperparameterTuningJobName name)

Gets a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       HyperparameterTuningJobName name =
           HyperparameterTuningJobName.of("[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]");
       HyperparameterTuningJob response = jobServiceClient.getHyperparameterTuningJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.HyperparameterTuningJobName`  
Required. The name of the HyperparameterTuningJob resource. Format: `projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}`  
**Returns**  
---  
**Type** | **Description**  
`[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)` |   
  
### getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request)
    
    
    public final HyperparameterTuningJob getHyperparameterTuningJob(GetHyperparameterTuningJobRequest request)

Gets a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetHyperparameterTuningJobRequest request =
           GetHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       HyperparameterTuningJob response = jobServiceClient.getHyperparameterTuningJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetHyperparameterTuningJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)` |   
  
### getHyperparameterTuningJob(String name)
    
    
    public final HyperparameterTuningJob getHyperparameterTuningJob(String name)

Gets a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           HyperparameterTuningJobName.of("[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
               .toString();
       HyperparameterTuningJob response = jobServiceClient.getHyperparameterTuningJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the HyperparameterTuningJob resource. Format: `projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}`  
**Returns**  
---  
**Type** | **Description**  
`[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)` |   
  
### getHyperparameterTuningJobCallable()
    
    
    public final UnaryCallable<GetHyperparameterTuningJobRequest,HyperparameterTuningJob> getHyperparameterTuningJobCallable()

Gets a HyperparameterTuningJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetHyperparameterTuningJobRequest request =
           GetHyperparameterTuningJobRequest.newBuilder()
               .setName(
                   HyperparameterTuningJobName.of(
                           "[PROJECT]", "[LOCATION]", "[HYPERPARAMETER_TUNING_JOB]")
                       .toString())
               .build();
       ApiFuture<HyperparameterTuningJob> future =
           jobServiceClient.getHyperparameterTuningJobCallable().futureCall(request);
       // Do something.
       HyperparameterTuningJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHyperparameterTuningJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetHyperparameterTuningJobRequest),[HyperparameterTuningJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJob)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = jobServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = jobServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = jobServiceClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = jobServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getModelDeploymentMonitoringJob(@Nullable ModelDeploymentMonitoringJobName name)
    
    
    public final ModelDeploymentMonitoringJob getModelDeploymentMonitoringJob(@Nullable ModelDeploymentMonitoringJobName name)

Gets a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ModelDeploymentMonitoringJobName name =
           ModelDeploymentMonitoringJobName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]");
       ModelDeploymentMonitoringJob response =
           jobServiceClient.getModelDeploymentMonitoringJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobName`  
Required. The resource name of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)` |   
  
### getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request)
    
    
    public final ModelDeploymentMonitoringJob getModelDeploymentMonitoringJob(GetModelDeploymentMonitoringJobRequest request)

Gets a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetModelDeploymentMonitoringJobRequest request =
           GetModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       ModelDeploymentMonitoringJob response =
           jobServiceClient.getModelDeploymentMonitoringJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelDeploymentMonitoringJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)` |   
  
### getModelDeploymentMonitoringJob(String name)
    
    
    public final ModelDeploymentMonitoringJob getModelDeploymentMonitoringJob(String name)

Gets a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           ModelDeploymentMonitoringJobName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
               .toString();
       ModelDeploymentMonitoringJob response =
           jobServiceClient.getModelDeploymentMonitoringJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
**Returns**  
---  
**Type** | **Description**  
`[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)` |   
  
### getModelDeploymentMonitoringJobCallable()
    
    
    public final UnaryCallable<GetModelDeploymentMonitoringJobRequest,ModelDeploymentMonitoringJob> getModelDeploymentMonitoringJobCallable()

Gets a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetModelDeploymentMonitoringJobRequest request =
           GetModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       ApiFuture<ModelDeploymentMonitoringJob> future =
           jobServiceClient.getModelDeploymentMonitoringJobCallable().futureCall(request);
       // Do something.
       ModelDeploymentMonitoringJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelDeploymentMonitoringJobRequest),[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)>` |   
  
### getNasJob(@Nullable NasJobName name)
    
    
    public final NasJob getNasJob(@Nullable NasJobName name)

Gets a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       NasJobName name = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]");
       NasJob response = jobServiceClient.getNasJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NasJobName`  
Required. The name of the NasJob resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
**Returns**  
---  
**Type** | **Description**  
`[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)` |   
  
### getNasJob(GetNasJobRequest request)
    
    
    public final NasJob getNasJob(GetNasJobRequest request)

Gets a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetNasJobRequest request =
           GetNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       NasJob response = jobServiceClient.getNasJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNasJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)` |   
  
### getNasJob(String name)
    
    
    public final NasJob getNasJob(String name)

Gets a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString();
       NasJob response = jobServiceClient.getNasJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NasJob resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
**Returns**  
---  
**Type** | **Description**  
`[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)` |   
  
### getNasJobCallable()
    
    
    public final UnaryCallable<GetNasJobRequest,NasJob> getNasJobCallable()

Gets a NasJob

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetNasJobRequest request =
           GetNasJobRequest.newBuilder()
               .setName(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .build();
       ApiFuture<NasJob> future = jobServiceClient.getNasJobCallable().futureCall(request);
       // Do something.
       NasJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNasJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNasJobRequest),[NasJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasJob)>` |   
  
### getNasTrialDetail(@Nullable NasTrialDetailName name)
    
    
    public final NasTrialDetail getNasTrialDetail(@Nullable NasTrialDetailName name)

Gets a NasTrialDetail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       NasTrialDetailName name =
           NasTrialDetailName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]", "[NAS_TRIAL_DETAIL]");
       NasTrialDetail response = jobServiceClient.getNasTrialDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NasTrialDetailName`  
Required. The name of the NasTrialDetail resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}/nasTrialDetails/{nas_trial_detail}`  
**Returns**  
---  
**Type** | **Description**  
`[NasTrialDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasTrialDetail)` |   
  
### getNasTrialDetail(GetNasTrialDetailRequest request)
    
    
    public final NasTrialDetail getNasTrialDetail(GetNasTrialDetailRequest request)

Gets a NasTrialDetail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetNasTrialDetailRequest request =
           GetNasTrialDetailRequest.newBuilder()
               .setName(
                   NasTrialDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[NAS_JOB]", "[NAS_TRIAL_DETAIL]")
                       .toString())
               .build();
       NasTrialDetail response = jobServiceClient.getNasTrialDetail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNasTrialDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNasTrialDetailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NasTrialDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasTrialDetail)` |   
  
### getNasTrialDetail(String name)
    
    
    public final NasTrialDetail getNasTrialDetail(String name)

Gets a NasTrialDetail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           NasTrialDetailName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]", "[NAS_TRIAL_DETAIL]")
               .toString();
       NasTrialDetail response = jobServiceClient.getNasTrialDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NasTrialDetail resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}/nasTrialDetails/{nas_trial_detail}`  
**Returns**  
---  
**Type** | **Description**  
`[NasTrialDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasTrialDetail)` |   
  
### getNasTrialDetailCallable()
    
    
    public final UnaryCallable<GetNasTrialDetailRequest,NasTrialDetail> getNasTrialDetailCallable()

Gets a NasTrialDetail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       GetNasTrialDetailRequest request =
           GetNasTrialDetailRequest.newBuilder()
               .setName(
                   NasTrialDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[NAS_JOB]", "[NAS_TRIAL_DETAIL]")
                       .toString())
               .build();
       ApiFuture<NasTrialDetail> future =
           jobServiceClient.getNasTrialDetailCallable().futureCall(request);
       // Do something.
       NasTrialDetail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNasTrialDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNasTrialDetailRequest),[NasTrialDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NasTrialDetail)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable JobServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.JobServiceSettings` |   
  
### getStub()
    
    
    public JobServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[JobServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.JobServiceStub)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listBatchPredictionJobs(@Nullable LocationName parent)
    
    
    public final JobServiceClient.ListBatchPredictionJobsPagedResponse listBatchPredictionJobs(@Nullable LocationName parent)

Lists BatchPredictionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BatchPredictionJob element :
           jobServiceClient.listBatchPredictionJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the BatchPredictionJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListBatchPredictionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListBatchPredictionJobsPagedResponse)` |   
  
### listBatchPredictionJobs(ListBatchPredictionJobsRequest request)
    
    
    public final JobServiceClient.ListBatchPredictionJobsPagedResponse listBatchPredictionJobs(ListBatchPredictionJobsRequest request)

Lists BatchPredictionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListBatchPredictionJobsRequest request =
           ListBatchPredictionJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (BatchPredictionJob element :
           jobServiceClient.listBatchPredictionJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListBatchPredictionJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListBatchPredictionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListBatchPredictionJobsPagedResponse)` |   
  
### listBatchPredictionJobs(String parent)
    
    
    public final JobServiceClient.ListBatchPredictionJobsPagedResponse listBatchPredictionJobs(String parent)

Lists BatchPredictionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BatchPredictionJob element :
           jobServiceClient.listBatchPredictionJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the BatchPredictionJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListBatchPredictionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListBatchPredictionJobsPagedResponse)` |   
  
### listBatchPredictionJobsCallable()
    
    
    public final UnaryCallable<ListBatchPredictionJobsRequest,ListBatchPredictionJobsResponse> listBatchPredictionJobsCallable()

Lists BatchPredictionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListBatchPredictionJobsRequest request =
           ListBatchPredictionJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListBatchPredictionJobsResponse response =
             jobServiceClient.listBatchPredictionJobsCallable().call(request);
         for (BatchPredictionJob element : response.getBatchPredictionJobsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListBatchPredictionJobsRequest),[ListBatchPredictionJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListBatchPredictionJobsResponse)>` |   
  
### listBatchPredictionJobsPagedCallable()
    
    
    public final UnaryCallable<ListBatchPredictionJobsRequest,JobServiceClient.ListBatchPredictionJobsPagedResponse> listBatchPredictionJobsPagedCallable()

Lists BatchPredictionJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListBatchPredictionJobsRequest request =
           ListBatchPredictionJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<BatchPredictionJob> future =
           jobServiceClient.listBatchPredictionJobsPagedCallable().futureCall(request);
       // Do something.
       for (BatchPredictionJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBatchPredictionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListBatchPredictionJobsRequest),[ListBatchPredictionJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListBatchPredictionJobsPagedResponse)>` |   
  
### listCustomJobs(@Nullable LocationName parent)
    
    
    public final JobServiceClient.ListCustomJobsPagedResponse listCustomJobs(@Nullable LocationName parent)

Lists CustomJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CustomJob element : jobServiceClient.listCustomJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the CustomJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListCustomJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListCustomJobsPagedResponse)` |   
  
### listCustomJobs(ListCustomJobsRequest request)
    
    
    public final JobServiceClient.ListCustomJobsPagedResponse listCustomJobs(ListCustomJobsRequest request)

Lists CustomJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListCustomJobsRequest request =
           ListCustomJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (CustomJob element : jobServiceClient.listCustomJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListCustomJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListCustomJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListCustomJobsPagedResponse)` |   
  
### listCustomJobs(String parent)
    
    
    public final JobServiceClient.ListCustomJobsPagedResponse listCustomJobs(String parent)

Lists CustomJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (CustomJob element : jobServiceClient.listCustomJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the CustomJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListCustomJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListCustomJobsPagedResponse)` |   
  
### listCustomJobsCallable()
    
    
    public final UnaryCallable<ListCustomJobsRequest,ListCustomJobsResponse> listCustomJobsCallable()

Lists CustomJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListCustomJobsRequest request =
           ListCustomJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListCustomJobsResponse response = jobServiceClient.listCustomJobsCallable().call(request);
         for (CustomJob element : response.getCustomJobsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListCustomJobsRequest),[ListCustomJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListCustomJobsResponse)>` |   
  
### listCustomJobsPagedCallable()
    
    
    public final UnaryCallable<ListCustomJobsRequest,JobServiceClient.ListCustomJobsPagedResponse> listCustomJobsPagedCallable()

Lists CustomJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListCustomJobsRequest request =
           ListCustomJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CustomJob> future =
           jobServiceClient.listCustomJobsPagedCallable().futureCall(request);
       // Do something.
       for (CustomJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListCustomJobsRequest),[ListCustomJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListCustomJobsPagedResponse)>` |   
  
### listDataLabelingJobs(@Nullable LocationName parent)
    
    
    public final JobServiceClient.ListDataLabelingJobsPagedResponse listDataLabelingJobs(@Nullable LocationName parent)

Lists DataLabelingJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (DataLabelingJob element : jobServiceClient.listDataLabelingJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The parent of the DataLabelingJob. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListDataLabelingJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListDataLabelingJobsPagedResponse)` |   
  
### listDataLabelingJobs(ListDataLabelingJobsRequest request)
    
    
    public final JobServiceClient.ListDataLabelingJobsPagedResponse listDataLabelingJobs(ListDataLabelingJobsRequest request)

Lists DataLabelingJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListDataLabelingJobsRequest request =
           ListDataLabelingJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (DataLabelingJob element : jobServiceClient.listDataLabelingJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataLabelingJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataLabelingJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListDataLabelingJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListDataLabelingJobsPagedResponse)` |   
  
### listDataLabelingJobs(String parent)
    
    
    public final JobServiceClient.ListDataLabelingJobsPagedResponse listDataLabelingJobs(String parent)

Lists DataLabelingJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (DataLabelingJob element : jobServiceClient.listDataLabelingJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the DataLabelingJob. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListDataLabelingJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListDataLabelingJobsPagedResponse)` |   
  
### listDataLabelingJobsCallable()
    
    
    public final UnaryCallable<ListDataLabelingJobsRequest,ListDataLabelingJobsResponse> listDataLabelingJobsCallable()

Lists DataLabelingJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListDataLabelingJobsRequest request =
           ListDataLabelingJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListDataLabelingJobsResponse response =
             jobServiceClient.listDataLabelingJobsCallable().call(request);
         for (DataLabelingJob element : response.getDataLabelingJobsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataLabelingJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataLabelingJobsRequest),[ListDataLabelingJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataLabelingJobsResponse)>` |   
  
### listDataLabelingJobsPagedCallable()
    
    
    public final UnaryCallable<ListDataLabelingJobsRequest,JobServiceClient.ListDataLabelingJobsPagedResponse> listDataLabelingJobsPagedCallable()

Lists DataLabelingJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListDataLabelingJobsRequest request =
           ListDataLabelingJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<DataLabelingJob> future =
           jobServiceClient.listDataLabelingJobsPagedCallable().futureCall(request);
       // Do something.
       for (DataLabelingJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataLabelingJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataLabelingJobsRequest),[ListDataLabelingJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListDataLabelingJobsPagedResponse)>` |   
  
### listHyperparameterTuningJobs(@Nullable LocationName parent)
    
    
    public final JobServiceClient.ListHyperparameterTuningJobsPagedResponse listHyperparameterTuningJobs(@Nullable LocationName parent)

Lists HyperparameterTuningJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (HyperparameterTuningJob element :
           jobServiceClient.listHyperparameterTuningJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the HyperparameterTuningJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListHyperparameterTuningJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListHyperparameterTuningJobsPagedResponse)` |   
  
### listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request)
    
    
    public final JobServiceClient.ListHyperparameterTuningJobsPagedResponse listHyperparameterTuningJobs(ListHyperparameterTuningJobsRequest request)

Lists HyperparameterTuningJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListHyperparameterTuningJobsRequest request =
           ListHyperparameterTuningJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (HyperparameterTuningJob element :
           jobServiceClient.listHyperparameterTuningJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHyperparameterTuningJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListHyperparameterTuningJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListHyperparameterTuningJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListHyperparameterTuningJobsPagedResponse)` |   
  
### listHyperparameterTuningJobs(String parent)
    
    
    public final JobServiceClient.ListHyperparameterTuningJobsPagedResponse listHyperparameterTuningJobs(String parent)

Lists HyperparameterTuningJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (HyperparameterTuningJob element :
           jobServiceClient.listHyperparameterTuningJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the HyperparameterTuningJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListHyperparameterTuningJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListHyperparameterTuningJobsPagedResponse)` |   
  
### listHyperparameterTuningJobsCallable()
    
    
    public final UnaryCallable<ListHyperparameterTuningJobsRequest,ListHyperparameterTuningJobsResponse> listHyperparameterTuningJobsCallable()

Lists HyperparameterTuningJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListHyperparameterTuningJobsRequest request =
           ListHyperparameterTuningJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListHyperparameterTuningJobsResponse response =
             jobServiceClient.listHyperparameterTuningJobsCallable().call(request);
         for (HyperparameterTuningJob element : response.getHyperparameterTuningJobsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHyperparameterTuningJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListHyperparameterTuningJobsRequest),[ListHyperparameterTuningJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListHyperparameterTuningJobsResponse)>` |   
  
### listHyperparameterTuningJobsPagedCallable()
    
    
    public final UnaryCallable<ListHyperparameterTuningJobsRequest,JobServiceClient.ListHyperparameterTuningJobsPagedResponse> listHyperparameterTuningJobsPagedCallable()

Lists HyperparameterTuningJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListHyperparameterTuningJobsRequest request =
           ListHyperparameterTuningJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<HyperparameterTuningJob> future =
           jobServiceClient.listHyperparameterTuningJobsPagedCallable().futureCall(request);
       // Do something.
       for (HyperparameterTuningJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListHyperparameterTuningJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListHyperparameterTuningJobsRequest),[ListHyperparameterTuningJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListHyperparameterTuningJobsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final JobServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : jobServiceClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = jobServiceClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,JobServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           jobServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListLocationsPagedResponse)>` |   
  
### listModelDeploymentMonitoringJobs(@Nullable LocationName parent)
    
    
    public final JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse listModelDeploymentMonitoringJobs(@Nullable LocationName parent)

Lists ModelDeploymentMonitoringJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ModelDeploymentMonitoringJob element :
           jobServiceClient.listModelDeploymentMonitoringJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The parent of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse)` |   
  
### listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request)
    
    
    public final JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse listModelDeploymentMonitoringJobs(ListModelDeploymentMonitoringJobsRequest request)

Lists ModelDeploymentMonitoringJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListModelDeploymentMonitoringJobsRequest request =
           ListModelDeploymentMonitoringJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (ModelDeploymentMonitoringJob element :
           jobServiceClient.listModelDeploymentMonitoringJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelDeploymentMonitoringJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelDeploymentMonitoringJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse)` |   
  
### listModelDeploymentMonitoringJobs(String parent)
    
    
    public final JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse listModelDeploymentMonitoringJobs(String parent)

Lists ModelDeploymentMonitoringJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ModelDeploymentMonitoringJob element :
           jobServiceClient.listModelDeploymentMonitoringJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the ModelDeploymentMonitoringJob. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse)` |   
  
### listModelDeploymentMonitoringJobsCallable()
    
    
    public final UnaryCallable<ListModelDeploymentMonitoringJobsRequest,ListModelDeploymentMonitoringJobsResponse> listModelDeploymentMonitoringJobsCallable()

Lists ModelDeploymentMonitoringJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListModelDeploymentMonitoringJobsRequest request =
           ListModelDeploymentMonitoringJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListModelDeploymentMonitoringJobsResponse response =
             jobServiceClient.listModelDeploymentMonitoringJobsCallable().call(request);
         for (ModelDeploymentMonitoringJob element :
             response.getModelDeploymentMonitoringJobsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelDeploymentMonitoringJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelDeploymentMonitoringJobsRequest),[ListModelDeploymentMonitoringJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelDeploymentMonitoringJobsResponse)>` |   
  
### listModelDeploymentMonitoringJobsPagedCallable()
    
    
    public final UnaryCallable<ListModelDeploymentMonitoringJobsRequest,JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse> listModelDeploymentMonitoringJobsPagedCallable()

Lists ModelDeploymentMonitoringJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListModelDeploymentMonitoringJobsRequest request =
           ListModelDeploymentMonitoringJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<ModelDeploymentMonitoringJob> future =
           jobServiceClient.listModelDeploymentMonitoringJobsPagedCallable().futureCall(request);
       // Do something.
       for (ModelDeploymentMonitoringJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListModelDeploymentMonitoringJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelDeploymentMonitoringJobsRequest),[ListModelDeploymentMonitoringJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListModelDeploymentMonitoringJobsPagedResponse)>` |   
  
### listNasJobs(@Nullable LocationName parent)
    
    
    public final JobServiceClient.ListNasJobsPagedResponse listNasJobs(@Nullable LocationName parent)

Lists NasJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (NasJob element : jobServiceClient.listNasJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the NasJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListNasJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasJobsPagedResponse)` |   
  
### listNasJobs(ListNasJobsRequest request)
    
    
    public final JobServiceClient.ListNasJobsPagedResponse listNasJobs(ListNasJobsRequest request)

Lists NasJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListNasJobsRequest request =
           ListNasJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (NasJob element : jobServiceClient.listNasJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNasJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListNasJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasJobsPagedResponse)` |   
  
### listNasJobs(String parent)
    
    
    public final JobServiceClient.ListNasJobsPagedResponse listNasJobs(String parent)

Lists NasJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (NasJob element : jobServiceClient.listNasJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the NasJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListNasJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasJobsPagedResponse)` |   
  
### listNasJobsCallable()
    
    
    public final UnaryCallable<ListNasJobsRequest,ListNasJobsResponse> listNasJobsCallable()

Lists NasJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListNasJobsRequest request =
           ListNasJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListNasJobsResponse response = jobServiceClient.listNasJobsCallable().call(request);
         for (NasJob element : response.getNasJobsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNasJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasJobsRequest),[ListNasJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasJobsResponse)>` |   
  
### listNasJobsPagedCallable()
    
    
    public final UnaryCallable<ListNasJobsRequest,JobServiceClient.ListNasJobsPagedResponse> listNasJobsPagedCallable()

Lists NasJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListNasJobsRequest request =
           ListNasJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<NasJob> future = jobServiceClient.listNasJobsPagedCallable().futureCall(request);
       // Do something.
       for (NasJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNasJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasJobsRequest),[ListNasJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasJobsPagedResponse)>` |   
  
### listNasTrialDetails(@Nullable NasJobName parent)
    
    
    public final JobServiceClient.ListNasTrialDetailsPagedResponse listNasTrialDetails(@Nullable NasJobName parent)

List top NasTrialDetails of a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       NasJobName parent = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]");
       for (NasTrialDetail element : jobServiceClient.listNasTrialDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.NasJobName`  
Required. The name of the NasJob resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListNasTrialDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasTrialDetailsPagedResponse)` |   
  
### listNasTrialDetails(ListNasTrialDetailsRequest request)
    
    
    public final JobServiceClient.ListNasTrialDetailsPagedResponse listNasTrialDetails(ListNasTrialDetailsRequest request)

List top NasTrialDetails of a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListNasTrialDetailsRequest request =
           ListNasTrialDetailsRequest.newBuilder()
               .setParent(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (NasTrialDetail element : jobServiceClient.listNasTrialDetails(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNasTrialDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasTrialDetailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListNasTrialDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasTrialDetailsPagedResponse)` |   
  
### listNasTrialDetails(String parent)
    
    
    public final JobServiceClient.ListNasTrialDetailsPagedResponse listNasTrialDetails(String parent)

List top NasTrialDetails of a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String parent = NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString();
       for (NasTrialDetail element : jobServiceClient.listNasTrialDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the NasJob resource. Format: `projects/{project}/locations/{location}/nasJobs/{nas_job}`  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.ListNasTrialDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasTrialDetailsPagedResponse)` |   
  
### listNasTrialDetailsCallable()
    
    
    public final UnaryCallable<ListNasTrialDetailsRequest,ListNasTrialDetailsResponse> listNasTrialDetailsCallable()

List top NasTrialDetails of a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListNasTrialDetailsRequest request =
           ListNasTrialDetailsRequest.newBuilder()
               .setParent(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListNasTrialDetailsResponse response =
             jobServiceClient.listNasTrialDetailsCallable().call(request);
         for (NasTrialDetail element : response.getNasTrialDetailsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNasTrialDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasTrialDetailsRequest),[ListNasTrialDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasTrialDetailsResponse)>` |   
  
### listNasTrialDetailsPagedCallable()
    
    
    public final UnaryCallable<ListNasTrialDetailsRequest,JobServiceClient.ListNasTrialDetailsPagedResponse> listNasTrialDetailsPagedCallable()

List top NasTrialDetails of a NasJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ListNasTrialDetailsRequest request =
           ListNasTrialDetailsRequest.newBuilder()
               .setParent(NasJobName.of("[PROJECT]", "[LOCATION]", "[NAS_JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<NasTrialDetail> future =
           jobServiceClient.listNasTrialDetailsPagedCallable().futureCall(request);
       // Do something.
       for (NasTrialDetail element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNasTrialDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNasTrialDetailsRequest),[ListNasTrialDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.ListNasTrialDetailsPagedResponse)>` |   
  
### pauseModelDeploymentMonitoringJob(@Nullable ModelDeploymentMonitoringJobName name)
    
    
    public final void pauseModelDeploymentMonitoringJob(@Nullable ModelDeploymentMonitoringJobName name)

Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ModelDeploymentMonitoringJobName name =
           ModelDeploymentMonitoringJobName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]");
       jobServiceClient.pauseModelDeploymentMonitoringJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobName`  
Required. The resource name of the ModelDeploymentMonitoringJob to pause. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
  
### pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request)
    
    
    public final void pauseModelDeploymentMonitoringJob(PauseModelDeploymentMonitoringJobRequest request)

Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       PauseModelDeploymentMonitoringJobRequest request =
           PauseModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       jobServiceClient.pauseModelDeploymentMonitoringJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PauseModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PauseModelDeploymentMonitoringJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### pauseModelDeploymentMonitoringJob(String name)
    
    
    public final void pauseModelDeploymentMonitoringJob(String name)

Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           ModelDeploymentMonitoringJobName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
               .toString();
       jobServiceClient.pauseModelDeploymentMonitoringJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ModelDeploymentMonitoringJob to pause. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
  
### pauseModelDeploymentMonitoringJobCallable()
    
    
    public final UnaryCallable<PauseModelDeploymentMonitoringJobRequest,Empty> pauseModelDeploymentMonitoringJobCallable()

Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       PauseModelDeploymentMonitoringJobRequest request =
           PauseModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           jobServiceClient.pauseModelDeploymentMonitoringJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PauseModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PauseModelDeploymentMonitoringJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### resumeModelDeploymentMonitoringJob(@Nullable ModelDeploymentMonitoringJobName name)
    
    
    public final void resumeModelDeploymentMonitoringJob(@Nullable ModelDeploymentMonitoringJobName name)

Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ModelDeploymentMonitoringJobName name =
           ModelDeploymentMonitoringJobName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]");
       jobServiceClient.resumeModelDeploymentMonitoringJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobName`  
Required. The resource name of the ModelDeploymentMonitoringJob to resume. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
  
### resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request)
    
    
    public final void resumeModelDeploymentMonitoringJob(ResumeModelDeploymentMonitoringJobRequest request)

Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ResumeModelDeploymentMonitoringJobRequest request =
           ResumeModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       jobServiceClient.resumeModelDeploymentMonitoringJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ResumeModelDeploymentMonitoringJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### resumeModelDeploymentMonitoringJob(String name)
    
    
    public final void resumeModelDeploymentMonitoringJob(String name)

Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String name =
           ModelDeploymentMonitoringJobName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
               .toString();
       jobServiceClient.resumeModelDeploymentMonitoringJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ModelDeploymentMonitoringJob to resume. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
  
### resumeModelDeploymentMonitoringJobCallable()
    
    
    public final UnaryCallable<ResumeModelDeploymentMonitoringJobRequest,Empty> resumeModelDeploymentMonitoringJobCallable()

Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ResumeModelDeploymentMonitoringJobRequest request =
           ResumeModelDeploymentMonitoringJobRequest.newBuilder()
               .setName(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           jobServiceClient.resumeModelDeploymentMonitoringJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ResumeModelDeploymentMonitoringJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### searchModelDeploymentMonitoringStatsAnomalies(@Nullable ModelDeploymentMonitoringJobName modelDeploymentMonitoringJob, String deployedModelId)
    
    
    public final JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse searchModelDeploymentMonitoringStatsAnomalies(@Nullable ModelDeploymentMonitoringJobName modelDeploymentMonitoringJob, String deployedModelId)

Searches Model Monitoring Statistics generated within a given time window.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ModelDeploymentMonitoringJobName modelDeploymentMonitoringJob =
           ModelDeploymentMonitoringJobName.of(
               "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]");
       String deployedModelId = "deployedModelId-1817547906";
       for (ModelMonitoringStatsAnomalies element :
           jobServiceClient
               .searchModelDeploymentMonitoringStatsAnomalies(
                   modelDeploymentMonitoringJob, deployedModelId)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJob` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobName`  
Required. ModelDeploymentMonitoring Job resource name. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
`deployedModelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The DeployedModel ID of the [ModelDeploymentMonitoringObjectiveConfig.deployed_model_id].  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse)` |   
  
### searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request)
    
    
    public final JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse searchModelDeploymentMonitoringStatsAnomalies(SearchModelDeploymentMonitoringStatsAnomaliesRequest request)

Searches Model Monitoring Statistics generated within a given time window.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       SearchModelDeploymentMonitoringStatsAnomaliesRequest request =
           SearchModelDeploymentMonitoringStatsAnomaliesRequest.newBuilder()
               .setModelDeploymentMonitoringJob(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .setDeployedModelId("deployedModelId-1817547906")
               .setFeatureDisplayName("featureDisplayName-1741181545")
               .addAllObjectives(
                   new ArrayList< searchmodeldeploymentmonitoringstatsanomaliesrequest="" .statsanomaliesobjective="">())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setStartTime(Timestamp.newBuilder().build())
               .setEndTime(Timestamp.newBuilder().build())
               .build();
       for (ModelMonitoringStatsAnomalies element :
           jobServiceClient.searchModelDeploymentMonitoringStatsAnomalies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchModelDeploymentMonitoringStatsAnomaliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse)` |   
  
### searchModelDeploymentMonitoringStatsAnomalies(String modelDeploymentMonitoringJob, String deployedModelId)
    
    
    public final JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse searchModelDeploymentMonitoringStatsAnomalies(String modelDeploymentMonitoringJob, String deployedModelId)

Searches Model Monitoring Statistics generated within a given time window.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       String modelDeploymentMonitoringJob =
           ModelDeploymentMonitoringJobName.of(
                   "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
               .toString();
       String deployedModelId = "deployedModelId-1817547906";
       for (ModelMonitoringStatsAnomalies element :
           jobServiceClient
               .searchModelDeploymentMonitoringStatsAnomalies(
                   modelDeploymentMonitoringJob, deployedModelId)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJob` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ModelDeploymentMonitoring Job resource name. Format: `projects/{project}/locations/{location}/modelDeploymentMonitoringJobs/{model_deployment_monitoring_job}`  
`deployedModelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The DeployedModel ID of the [ModelDeploymentMonitoringObjectiveConfig.deployed_model_id].  
**Returns**  
---  
**Type** | **Description**  
`[JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse)` |   
  
### searchModelDeploymentMonitoringStatsAnomaliesCallable()
    
    
    public final UnaryCallable<SearchModelDeploymentMonitoringStatsAnomaliesRequest,SearchModelDeploymentMonitoringStatsAnomaliesResponse> searchModelDeploymentMonitoringStatsAnomaliesCallable()

Searches Model Monitoring Statistics generated within a given time window.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       SearchModelDeploymentMonitoringStatsAnomaliesRequest request =
           SearchModelDeploymentMonitoringStatsAnomaliesRequest.newBuilder()
               .setModelDeploymentMonitoringJob(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .setDeployedModelId("deployedModelId-1817547906")
               .setFeatureDisplayName("featureDisplayName-1741181545")
               .addAllObjectives(
                   new ArrayList< searchmodeldeploymentmonitoringstatsanomaliesrequest="" .statsanomaliesobjective="">())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setStartTime(Timestamp.newBuilder().build())
               .setEndTime(Timestamp.newBuilder().build())
               .build();
       while (true) {
         SearchModelDeploymentMonitoringStatsAnomaliesResponse response =
             jobServiceClient.searchModelDeploymentMonitoringStatsAnomaliesCallable().call(request);
         for (ModelMonitoringStatsAnomalies element : response.getMonitoringStatsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchModelDeploymentMonitoringStatsAnomaliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesRequest),[SearchModelDeploymentMonitoringStatsAnomaliesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesResponse)>` |   
  
### searchModelDeploymentMonitoringStatsAnomaliesPagedCallable()
    
    
    public final UnaryCallable<SearchModelDeploymentMonitoringStatsAnomaliesRequest,JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse> searchModelDeploymentMonitoringStatsAnomaliesPagedCallable()

Searches Model Monitoring Statistics generated within a given time window.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       SearchModelDeploymentMonitoringStatsAnomaliesRequest request =
           SearchModelDeploymentMonitoringStatsAnomaliesRequest.newBuilder()
               .setModelDeploymentMonitoringJob(
                   ModelDeploymentMonitoringJobName.of(
                           "[PROJECT]", "[LOCATION]", "[MODEL_DEPLOYMENT_MONITORING_JOB]")
                       .toString())
               .setDeployedModelId("deployedModelId-1817547906")
               .setFeatureDisplayName("featureDisplayName-1741181545")
               .addAllObjectives(
                   new ArrayList< searchmodeldeploymentmonitoringstatsanomaliesrequest="" .statsanomaliesobjective="">())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setStartTime(Timestamp.newBuilder().build())
               .setEndTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<ModelMonitoringStatsAnomalies> future =
           jobServiceClient
               .searchModelDeploymentMonitoringStatsAnomaliesPagedCallable()
               .futureCall(request);
       // Do something.
       for (ModelMonitoringStatsAnomalies element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchModelDeploymentMonitoringStatsAnomaliesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesRequest),[SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobServiceClient.SearchModelDeploymentMonitoringStatsAnomaliesPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = jobServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = jobServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = jobServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           jobServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateModelDeploymentMonitoringJobAsync(ModelDeploymentMonitoringJob modelDeploymentMonitoringJob, FieldMask updateMask)
    
    
    public final OperationFuture<ModelDeploymentMonitoringJob,UpdateModelDeploymentMonitoringJobOperationMetadata> updateModelDeploymentMonitoringJobAsync(ModelDeploymentMonitoringJob modelDeploymentMonitoringJob, FieldMask updateMask)

Updates a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       ModelDeploymentMonitoringJob modelDeploymentMonitoringJob =
           ModelDeploymentMonitoringJob.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ModelDeploymentMonitoringJob response =
           jobServiceClient
               .updateModelDeploymentMonitoringJobAsync(modelDeploymentMonitoringJob, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`modelDeploymentMonitoringJob` | `[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob)`  
Required. The model monitoring configuration which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask is used to specify the fields to be overwritten in the ModelDeploymentMonitoringJob resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. For the objective config, the user can either provide the update mask for model_deployment_monitoring_objective_configs or any combination of its nested fields, such as: model_deployment_monitoring_objective_configs.objective_config.training_dataset. Updatable fields: * `display_name` * `model_deployment_monitoring_schedule_config` * `model_monitoring_alert_config` * `logging_sampling_strategy` * `labels` * `log_ttl` * `enable_monitoring_pipeline_logs` . and * `model_deployment_monitoring_objective_configs` . or * `model_deployment_monitoring_objective_configs.objective_config.training_dataset` * `model_deployment_monitoring_objective_configs.objective_config.training_prediction_skew_detection_config` * `model_deployment_monitoring_objective_configs.objective_config.prediction_drift_detection_config`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob),[UpdateModelDeploymentMonitoringJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobOperationMetadata)>` |   
  
### updateModelDeploymentMonitoringJobAsync(UpdateModelDeploymentMonitoringJobRequest request)
    
    
    public final OperationFuture<ModelDeploymentMonitoringJob,UpdateModelDeploymentMonitoringJobOperationMetadata> updateModelDeploymentMonitoringJobAsync(UpdateModelDeploymentMonitoringJobRequest request)

Updates a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       UpdateModelDeploymentMonitoringJobRequest request =
           UpdateModelDeploymentMonitoringJobRequest.newBuilder()
               .setModelDeploymentMonitoringJob(ModelDeploymentMonitoringJob.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ModelDeploymentMonitoringJob response =
           jobServiceClient.updateModelDeploymentMonitoringJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob),[UpdateModelDeploymentMonitoringJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobOperationMetadata)>` |   
  
### updateModelDeploymentMonitoringJobCallable()
    
    
    public final UnaryCallable<UpdateModelDeploymentMonitoringJobRequest,Operation> updateModelDeploymentMonitoringJobCallable()

Updates a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       UpdateModelDeploymentMonitoringJobRequest request =
           UpdateModelDeploymentMonitoringJobRequest.newBuilder()
               .setModelDeploymentMonitoringJob(ModelDeploymentMonitoringJob.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           jobServiceClient.updateModelDeploymentMonitoringJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateModelDeploymentMonitoringJobOperationCallable()
    
    
    public final OperationCallable<UpdateModelDeploymentMonitoringJobRequest,ModelDeploymentMonitoringJob,UpdateModelDeploymentMonitoringJobOperationMetadata> updateModelDeploymentMonitoringJobOperationCallable()

Updates a ModelDeploymentMonitoringJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (JobServiceClient jobServiceClient = JobServiceClient.create()) {
       UpdateModelDeploymentMonitoringJobRequest request =
           UpdateModelDeploymentMonitoringJobRequest.newBuilder()
               .setModelDeploymentMonitoringJob(ModelDeploymentMonitoringJob.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture< modeldeploymentmonitoringjob,="" updatemodeldeploymentmonitoringjoboperationmetadata="">
           future =
               jobServiceClient
                   .updateModelDeploymentMonitoringJobOperationCallable()
                   .futureCall(request);
       // Do something.
       ModelDeploymentMonitoringJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateModelDeploymentMonitoringJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobRequest),[ModelDeploymentMonitoringJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob),[UpdateModelDeploymentMonitoringJobOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
