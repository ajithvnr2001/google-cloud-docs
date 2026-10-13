---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1
title: Package com.google.cloud.batch.v1 (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:38.651802+00:00
---

# Package com.google.cloud.batch.v1 (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.batch.v1 (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-batch/google-cloud-batch/src/main/java/com/google/cloud/batch/v1)  
---  
  
## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.cloud.batch.v1.BatchServiceClient](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient) |  Service Description: Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs. This class provides the ability to make remote calls to the backing service through method  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.batch.v1.BatchServiceSettings](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceSettings) |  Settings class to configure an instance of BatchServiceClient. The default instance has everything set to sensible defaults:   
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.batch.v1.AllocationPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy) |  A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.   
[com.google.cloud.batch.v1.AllocationPolicy.Accelerator](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator) |  Accelerator describes Compute Engine accelerators to be attached to the VM.   
[com.google.cloud.batch.v1.AllocationPolicy.Accelerator.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Accelerator.Builder) |  Accelerator describes Compute Engine accelerators to be attached to the VM.   
[com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk) |  A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.   
[com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.Builder) |  A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.   
[com.google.cloud.batch.v1.AllocationPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Builder) |  A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.   
[com.google.cloud.batch.v1.AllocationPolicy.Disk](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk) |  A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and  
[com.google.cloud.batch.v1.AllocationPolicy.Disk.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.Builder) |  A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and  
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy) |  InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.   
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy.Builder) |  InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.   
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate) |  InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include  
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.Builder) |  InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include  
[com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy) |  Protobuf type `google.cloud.batch.v1.AllocationPolicy.LocationPolicy`  
[com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy.Builder) |  Protobuf type `google.cloud.batch.v1.AllocationPolicy.LocationPolicy`  
[com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface) |  A network interface.   
[com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.Builder) |  A network interface.   
[com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy) |  NetworkPolicy describes VM instance network configurations.   
[com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy.Builder) |  NetworkPolicy describes VM instance network configurations.   
[com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy) |  PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.   
[com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy.Builder) |  PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.   
[com.google.cloud.batch.v1.BatchProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchProto) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListJobsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListJobsFixedSizeCollection) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListJobsPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListJobsPage) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListJobsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListJobsPagedResponse) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListLocationsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListLocationsFixedSizeCollection) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListLocationsPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListLocationsPage) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListLocationsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListLocationsPagedResponse) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListTasksFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListTasksFixedSizeCollection) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListTasksPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListTasksPage) |   
[com.google.cloud.batch.v1.BatchServiceClient.ListTasksPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceClient.ListTasksPagedResponse) |   
[com.google.cloud.batch.v1.BatchServiceGrpc](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc) |  Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.  
[com.google.cloud.batch.v1.BatchServiceGrpc.BatchServiceImplBase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.BatchServiceImplBase) |  Base class for the server implementation of the service BatchService. Google Batch Service.  
[com.google.cloud.batch.v1.BatchServiceSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceSettings.Builder) |  Builder for BatchServiceSettings.  
[com.google.cloud.batch.v1.CancelJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobRequest) |  CancelJob Request.   
[com.google.cloud.batch.v1.CancelJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobRequest.Builder) |  CancelJob Request.   
[com.google.cloud.batch.v1.CancelJobResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobResponse) |  Response to the CancelJob request.   
[com.google.cloud.batch.v1.CancelJobResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobResponse.Builder) |  Response to the CancelJob request.   
[com.google.cloud.batch.v1.ComputeResource](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource) |  Compute resource requirements. ComputeResource defines the amount of resources required for each task.  
[com.google.cloud.batch.v1.ComputeResource.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResource.Builder) |  Compute resource requirements. ComputeResource defines the amount of resources required for each task.  
[com.google.cloud.batch.v1.CreateJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest) |  CreateJob Request.   
[com.google.cloud.batch.v1.CreateJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequest.Builder) |  CreateJob Request.   
[com.google.cloud.batch.v1.DeleteJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.DeleteJobRequest) |  DeleteJob Request.   
[com.google.cloud.batch.v1.DeleteJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.DeleteJobRequest.Builder) |  DeleteJob Request.   
[com.google.cloud.batch.v1.Environment](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment) |  An Environment describes a collection of environment variables to set when executing Tasks.   
[com.google.cloud.batch.v1.Environment.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.Builder) |  An Environment describes a collection of environment variables to set when executing Tasks.   
[com.google.cloud.batch.v1.Environment.KMSEnvMap](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.KMSEnvMap) |  Protobuf type `google.cloud.batch.v1.Environment.KMSEnvMap`  
[com.google.cloud.batch.v1.Environment.KMSEnvMap.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.KMSEnvMap.Builder) |  Protobuf type `google.cloud.batch.v1.Environment.KMSEnvMap`  
[com.google.cloud.batch.v1.](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCS) |  Represents a Google Cloud Storage volume.   
[com.google.cloud.batch.v1.GCS.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCS.Builder) |  Represents a Google Cloud Storage volume.   
[com.google.cloud.batch.v1.GetJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetJobRequest) |  GetJob Request.   
[com.google.cloud.batch.v1.GetJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetJobRequest.Builder) |  GetJob Request.   
[com.google.cloud.batch.v1.GetTaskRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetTaskRequest) |  Request for a single Task by name.   
[com.google.cloud.batch.v1.GetTaskRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetTaskRequest.Builder) |  Request for a single Task by name.   
[com.google.cloud.batch.v1.Job](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job) |  The Cloud Batch Job description.   
[com.google.cloud.batch.v1.Job.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Job.Builder) |  The Cloud Batch Job description.   
[com.google.cloud.batch.v1.JobName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobName) |   
[com.google.cloud.batch.v1.JobName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobName.Builder) |  Builder for projects/{project}/locations/{location}/jobs/{job}.  
[com.google.cloud.batch.v1.JobNotification](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification) |  Notification configurations.   
[com.google.cloud.batch.v1.JobNotification.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Builder) |  Notification configurations.   
[com.google.cloud.batch.v1.JobNotification.Message](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Message) |  Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default.  
[com.google.cloud.batch.v1.JobNotification.Message.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Message.Builder) |  Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default.  
[com.google.cloud.batch.v1.JobProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobProto) |   
[com.google.cloud.batch.v1.JobStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus) |  Job status.   
[com.google.cloud.batch.v1.JobStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.Builder) |  Job status.   
[com.google.cloud.batch.v1.JobStatus.InstanceStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.InstanceStatus) |  VM instance status.   
[com.google.cloud.batch.v1.JobStatus.InstanceStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.InstanceStatus.Builder) |  VM instance status.   
[com.google.cloud.batch.v1.JobStatus.TaskGroupStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus) |  Aggregated task status for a TaskGroup.   
[com.google.cloud.batch.v1.JobStatus.TaskGroupStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatus.Builder) |  Aggregated task status for a TaskGroup.   
[com.google.cloud.batch.v1.LifecyclePolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicy) |  LifecyclePolicy describes how to deal with task failures based on different conditions.   
[com.google.cloud.batch.v1.LifecyclePolicy.ActionCondition](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicy.ActionCondition) |  Conditions for actions to deal with task failures.   
[com.google.cloud.batch.v1.LifecyclePolicy.ActionCondition.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicy.ActionCondition.Builder) |  Conditions for actions to deal with task failures.   
[com.google.cloud.batch.v1.LifecyclePolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicy.Builder) |  LifecyclePolicy describes how to deal with task failures based on different conditions.   
[com.google.cloud.batch.v1.ListJobsRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsRequest) |  ListJob Request.   
[com.google.cloud.batch.v1.ListJobsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsRequest.Builder) |  ListJob Request.   
[com.google.cloud.batch.v1.ListJobsResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsResponse) |  ListJob Response.   
[com.google.cloud.batch.v1.ListJobsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsResponse.Builder) |  ListJob Response.   
[com.google.cloud.batch.v1.ListTasksRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksRequest) |  ListTasks Request.   
[com.google.cloud.batch.v1.ListTasksRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksRequest.Builder) |  ListTasks Request.   
[com.google.cloud.batch.v1.ListTasksResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksResponse) |  ListTasks Response.   
[com.google.cloud.batch.v1.ListTasksResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksResponse.Builder) |  ListTasks Response.   
[com.google.cloud.batch.v1.LocationName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LocationName) |   
[com.google.cloud.batch.v1.LocationName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LocationName.Builder) |  Builder for projects/{project}/locations/{location}.  
[com.google.cloud.batch.v1.LogsPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy) |  LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout`  
[com.google.cloud.batch.v1.LogsPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Builder) |  LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout`  
[com.google.cloud.batch.v1.LogsPolicy.CloudLoggingOption](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.CloudLoggingOption) |  `CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.   
[com.google.cloud.batch.v1.LogsPolicy.CloudLoggingOption.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.CloudLoggingOption.Builder) |  `CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.   
[com.google.cloud.batch.v1.](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.NFS) |  Represents an NFS volume.   
[com.google.cloud.batch.v1.NFS.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.NFS.Builder) |  Represents an NFS volume.   
[com.google.cloud.batch.v1.OperationMetadata](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.OperationMetadata) |  Represents the metadata of the long-running operation.   
[com.google.cloud.batch.v1.OperationMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.OperationMetadata.Builder) |  Represents the metadata of the long-running operation.   
[com.google.cloud.batch.v1.Runnable](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable) |  Runnable describes instructions for executing a specific script or container as part of a Task.   
[com.google.cloud.batch.v1.Runnable.Barrier](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Barrier) |  A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.   
[com.google.cloud.batch.v1.Runnable.Barrier.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Barrier.Builder) |  A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.   
[com.google.cloud.batch.v1.Runnable.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Builder) |  Runnable describes instructions for executing a specific script or container as part of a Task.   
[com.google.cloud.batch.v1.Runnable.Container](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container) |  Container runnable.   
[com.google.cloud.batch.v1.Runnable.Container.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Container.Builder) |  Container runnable.   
[com.google.cloud.batch.v1.Runnable.Script](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script) |  Script runnable.   
[com.google.cloud.batch.v1.Runnable.Script.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.Builder) |  Script runnable.   
[com.google.cloud.batch.v1.ServiceAccount](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ServiceAccount) |  Carries information about a Google Cloud service account.   
[com.google.cloud.batch.v1.ServiceAccount.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ServiceAccount.Builder) |  Carries information about a Google Cloud service account.   
[com.google.cloud.batch.v1.StatusEvent](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.StatusEvent) |  Status event.   
[com.google.cloud.batch.v1.StatusEvent.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.StatusEvent.Builder) |  Status event.   
[com.google.cloud.batch.v1.Task](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task) |  A Cloud Batch task.   
[com.google.cloud.batch.v1.Task.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Task.Builder) |  A Cloud Batch task.   
[com.google.cloud.batch.v1.TaskExecution](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskExecution) |  This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.   
[com.google.cloud.batch.v1.TaskExecution.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskExecution.Builder) |  This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.   
[com.google.cloud.batch.v1.TaskGroup](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup) |  A TaskGroup defines one or more Tasks that all share the same TaskSpec.   
[com.google.cloud.batch.v1.TaskGroup.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.Builder) |  A TaskGroup defines one or more Tasks that all share the same TaskSpec.   
[com.google.cloud.batch.v1.TaskGroupName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroupName) |   
[com.google.cloud.batch.v1.TaskGroupName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroupName.Builder) |  Builder for projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}.  
[com.google.cloud.batch.v1.TaskName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskName) |   
[com.google.cloud.batch.v1.TaskName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskName.Builder) |  Builder for projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}/tasks/{task}.  
[com.google.cloud.batch.v1.TaskProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskProto) |   
[com.google.cloud.batch.v1.TaskSpec](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec) |  Spec of a task   
[com.google.cloud.batch.v1.TaskSpec.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpec.Builder) |  Spec of a task   
[com.google.cloud.batch.v1.TaskStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskStatus) |  Status of a task.   
[com.google.cloud.batch.v1.TaskStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskStatus.Builder) |  Status of a task.   
[com.google.cloud.batch.v1.Volume](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume) |  Volume describes a volume and parameters for it to be mounted to a VM.   
[com.google.cloud.batch.v1.Volume.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.Builder) |  Volume describes a volume and parameters for it to be mounted to a VM.   
[com.google.cloud.batch.v1.VolumeProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.VolumeProto) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.batch.v1.AllocationPolicy.AcceleratorOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AcceleratorOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.AttachedDiskOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDiskOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.DiskOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.DiskOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplateOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplateOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.LocationPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicyOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.NetworkInterfaceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterfaceOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicyOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicyOrBuilder) |   
[com.google.cloud.batch.v1.AllocationPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicyOrBuilder) |   
[com.google.cloud.batch.v1.BatchServiceGrpc.AsyncService](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.BatchServiceGrpc.AsyncService) |  Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.  
[com.google.cloud.batch.v1.CancelJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobRequestOrBuilder) |   
[com.google.cloud.batch.v1.CancelJobResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CancelJobResponseOrBuilder) |   
[com.google.cloud.batch.v1.ComputeResourceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ComputeResourceOrBuilder) |   
[com.google.cloud.batch.v1.CreateJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.CreateJobRequestOrBuilder) |   
[com.google.cloud.batch.v1.DeleteJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.DeleteJobRequestOrBuilder) |   
[com.google.cloud.batch.v1.Environment.KMSEnvMapOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.KMSEnvMapOrBuilder) |   
[com.google.cloud.batch.v1.EnvironmentOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.EnvironmentOrBuilder) |   
[com.google.cloud.batch.v1.GCSOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GCSOrBuilder) |   
[com.google.cloud.batch.v1.GetJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetJobRequestOrBuilder) |   
[com.google.cloud.batch.v1.GetTaskRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.GetTaskRequestOrBuilder) |   
[com.google.cloud.batch.v1.JobNotification.MessageOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.MessageOrBuilder) |   
[com.google.cloud.batch.v1.JobNotificationOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotificationOrBuilder) |   
[com.google.cloud.batch.v1.JobOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobOrBuilder) |   
[com.google.cloud.batch.v1.JobStatus.InstanceStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.InstanceStatusOrBuilder) |   
[com.google.cloud.batch.v1.JobStatus.TaskGroupStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.TaskGroupStatusOrBuilder) |   
[com.google.cloud.batch.v1.JobStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatusOrBuilder) |   
[com.google.cloud.batch.v1.LifecyclePolicy.ActionConditionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicy.ActionConditionOrBuilder) |   
[com.google.cloud.batch.v1.LifecyclePolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicyOrBuilder) |   
[com.google.cloud.batch.v1.ListJobsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsRequestOrBuilder) |   
[com.google.cloud.batch.v1.ListJobsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListJobsResponseOrBuilder) |   
[com.google.cloud.batch.v1.ListTasksRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksRequestOrBuilder) |   
[com.google.cloud.batch.v1.ListTasksResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ListTasksResponseOrBuilder) |   
[com.google.cloud.batch.v1.LogsPolicy.CloudLoggingOptionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.CloudLoggingOptionOrBuilder) |   
[com.google.cloud.batch.v1.LogsPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicyOrBuilder) |   
[com.google.cloud.batch.v1.NFSOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.NFSOrBuilder) |   
[com.google.cloud.batch.v1.OperationMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.OperationMetadataOrBuilder) |   
[com.google.cloud.batch.v1.Runnable.BarrierOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.BarrierOrBuilder) |   
[com.google.cloud.batch.v1.Runnable.ContainerOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ContainerOrBuilder) |   
[com.google.cloud.batch.v1.Runnable.ScriptOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ScriptOrBuilder) |   
[com.google.cloud.batch.v1.RunnableOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.RunnableOrBuilder) |   
[com.google.cloud.batch.v1.ServiceAccountOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ServiceAccountOrBuilder) |   
[com.google.cloud.batch.v1.StatusEventOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.StatusEventOrBuilder) |   
[com.google.cloud.batch.v1.TaskExecutionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskExecutionOrBuilder) |   
[com.google.cloud.batch.v1.TaskGroupOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroupOrBuilder) |   
[com.google.cloud.batch.v1.TaskOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskOrBuilder) |   
[com.google.cloud.batch.v1.TaskSpecOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskSpecOrBuilder) |   
[com.google.cloud.batch.v1.TaskStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskStatusOrBuilder) |   
[com.google.cloud.batch.v1.VolumeOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.VolumeOrBuilder) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.AttachedCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.AttachedDisk.AttachedCase) |   
[com.google.cloud.batch.v1.AllocationPolicy.Disk.DataSourceCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.Disk.DataSourceCase) |   
[com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase) |   
[com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.NicType](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkInterface.NicType) |  Compute Engine VM instance NIC type.   
[com.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.ProvisioningModel) |  Compute Engine VM instance provisioning model.   
[com.google.cloud.batch.v1.JobNotification.Type](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobNotification.Type) |  The message type.   
[com.google.cloud.batch.v1.JobStatus.State](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.JobStatus.State) |  Valid Job states.   
[com.google.cloud.batch.v1.LifecyclePolicy.Action](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LifecyclePolicy.Action) |  Action on task failures based on different conditions.   
[com.google.cloud.batch.v1.LogsPolicy.Destination](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.LogsPolicy.Destination) |  The destination (if any) for logs.   
[com.google.cloud.batch.v1.Runnable.ExecutableCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.ExecutableCase) |   
[com.google.cloud.batch.v1.Runnable.Script.CommandCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Runnable.Script.CommandCase) |   
[com.google.cloud.batch.v1.TaskGroup.SchedulingPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskGroup.SchedulingPolicy) |  How Tasks in the TaskGroup should be scheduled relative to each other.   
[com.google.cloud.batch.v1.TaskStatus.State](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.TaskStatus.State) |  Task states.   
[com.google.cloud.batch.v1.Volume.SourceCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Volume.SourceCase) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
