---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.AsyncService
title: Interface BatchServiceGrpc.AsyncService (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:10.416283+00:00
---

# Interface BatchServiceGrpc.AsyncService (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchServiceGrpc.AsyncService (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static interface BatchServiceGrpc.AsyncService

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

## Methods 

### cancelJob(CancelJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void cancelJob(CancelJobRequest request, StreamObserver<Operation> responseObserver)

Cancel a Job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createJob(CreateJobRequest request, StreamObserver<Job> responseObserver)
    
    
    public default void createJob(CreateJobRequest request, StreamObserver<Job> responseObserver)

Create a Job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job)>`  
  
  
### deleteJob(DeleteJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteJob(DeleteJobRequest request, StreamObserver<Operation> responseObserver)

Delete a Job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.DeleteJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getJob(GetJobRequest request, StreamObserver<Job> responseObserver)
    
    
    public default void getJob(GetJobRequest request, StreamObserver<Job> responseObserver)

Get a Job specified by its resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job)>`  
  
  
### getTask(GetTaskRequest request, StreamObserver<Task> responseObserver)
    
    
    public default void getTask(GetTaskRequest request, StreamObserver<Task> responseObserver)

Return a single Task.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetTaskRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task)>`  
  
  
### listJobs(ListJobsRequest request, StreamObserver<ListJobsResponse> responseObserver)
    
    
    public default void listJobs(ListJobsRequest request, StreamObserver<ListJobsResponse> responseObserver)

List all Jobs for a project within a region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsResponse)>`  
  
  
### listTasks(ListTasksRequest request, StreamObserver<ListTasksResponse> responseObserver)
    
    
    public default void listTasks(ListTasksRequest request, StreamObserver<ListTasksResponse> responseObserver)

List Tasks associated with a job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
