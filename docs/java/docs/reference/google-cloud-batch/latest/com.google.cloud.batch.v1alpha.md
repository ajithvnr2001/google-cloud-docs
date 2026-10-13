---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha
title: Package com.google.cloud.batch.v1alpha (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:20.340430+00:00
---

# Package com.google.cloud.batch.v1alpha (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.batch.v1alpha (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-batch/google-cloud-batch/src/main/java/com/google/cloud/batch/v1alpha)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.batch.v1](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1) for new applications.

## Prerelease Implications

This package is a prerelease version! Use with caution.

Prerelease versions are considered unstable as they may be shut down and/or subject to breaking changes when upgrading. Use them only for testing or if you specifically need their experimental features.

## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.cloud.batch.v1alpha.BatchServiceClient](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient) |  Service Description: Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs. This class provides the ability to make remote calls to the backing service through method  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.batch.v1alpha.BatchServiceSettings](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings) |  Settings class to configure an instance of BatchServiceClient. The default instance has everything set to sensible defaults:   
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.batch.v1alpha.AllocationPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy) |  A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.Accelerator](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.Accelerator) |  Accelerator describes Compute Engine accelerators to be attached to the VM.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.Accelerator.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.Accelerator.Builder) |  Accelerator describes Compute Engine accelerators to be attached to the VM.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDisk](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDisk) |  A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDisk.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDisk.Builder) |  A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.Builder) |  A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.Disk](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.Disk) |  A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and  
[com.google.cloud.batch.v1alpha.AllocationPolicy.Disk.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.Disk.Builder) |  A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and  
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceFlexibilityPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceFlexibilityPolicy) |  Allows creating VMs from multiple types of machines. Instance flexibility configuration overrides instances configuration.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceFlexibilityPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceFlexibilityPolicy.Builder) |  Allows creating VMs from multiple types of machines. Instance flexibility configuration overrides instances configuration.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicy) |  InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicy.Builder) |  InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplate](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplate) |  InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include  
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplate.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplate.Builder) |  InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include  
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceSelection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceSelection) |  Defines an instance selection for a given instance flexibility policy.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceSelection.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceSelection.Builder) |  Defines an instance selection for a given instance flexibility policy.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicy) |  Protobuf type `google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicy`  
[com.google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicy.Builder) |  Protobuf type `google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicy`  
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterface](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterface) |  A network interface.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterface.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterface.Builder) |  A network interface.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkPolicy) |  NetworkPolicy describes VM instance network configurations.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkPolicy.Builder) |  NetworkPolicy describes VM instance network configurations.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.PlacementPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.PlacementPolicy) |  PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.PlacementPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.PlacementPolicy.Builder) |  PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.   
[com.google.cloud.batch.v1alpha.BatchProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchProto) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsFixedSizeCollection) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPage) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPagedResponse) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsFixedSizeCollection) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPage) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPagedResponse) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesFixedSizeCollection) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPage) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksFixedSizeCollection) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPage) |   
[com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse) |   
[com.google.cloud.batch.v1alpha.BatchServiceGrpc](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceGrpc) |  Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.  
[com.google.cloud.batch.v1alpha.BatchServiceGrpc.BatchServiceImplBase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceGrpc.BatchServiceImplBase) |  Base class for the server implementation of the service BatchService. Google Batch Service.  
[com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder) |  Builder for BatchServiceSettings.  
[com.google.cloud.batch.v1alpha.CancelJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest) |  CancelJob Request.   
[com.google.cloud.batch.v1alpha.CancelJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest.Builder) |  CancelJob Request.   
[com.google.cloud.batch.v1alpha.CancelJobResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse) |  Response to the CancelJob request.   
[com.google.cloud.batch.v1alpha.CancelJobResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse.Builder) |  Response to the CancelJob request.   
[com.google.cloud.batch.v1alpha.ComputeResource](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ComputeResource) |  Compute resource requirements. ComputeResource defines the amount of resources required for each task.  
[com.google.cloud.batch.v1alpha.ComputeResource.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ComputeResource.Builder) |  Compute resource requirements. ComputeResource defines the amount of resources required for each task.  
[com.google.cloud.batch.v1alpha.CreateJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateJobRequest) |  CreateJob Request.   
[com.google.cloud.batch.v1alpha.CreateJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateJobRequest.Builder) |  CreateJob Request.   
[com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest) |  CreateResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest.Builder) |  CreateResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.DeleteJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest) |  DeleteJob Request.   
[com.google.cloud.batch.v1alpha.DeleteJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest.Builder) |  DeleteJob Request.   
[com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest) |  DeleteResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest.Builder) |  DeleteResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.Environment](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Environment) |  An Environment describes a collection of environment variables to set when executing Tasks.   
[com.google.cloud.batch.v1alpha.Environment.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Environment.Builder) |  An Environment describes a collection of environment variables to set when executing Tasks.   
[com.google.cloud.batch.v1alpha.Environment.KMSEnvMap](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Environment.KMSEnvMap) |  Protobuf type `google.cloud.batch.v1alpha.Environment.KMSEnvMap`  
[com.google.cloud.batch.v1alpha.Environment.KMSEnvMap.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Environment.KMSEnvMap.Builder) |  Protobuf type `google.cloud.batch.v1alpha.Environment.KMSEnvMap`  
[com.google.cloud.batch.v1alpha.](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GCS) |  Represents a Google Cloud Storage volume.   
[com.google.cloud.batch.v1alpha.GCS.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GCS.Builder) |  Represents a Google Cloud Storage volume.   
[com.google.cloud.batch.v1alpha.GetJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetJobRequest) |  GetJob Request.   
[com.google.cloud.batch.v1alpha.GetJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetJobRequest.Builder) |  GetJob Request.   
[com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest) |  GetResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest.Builder) |  GetResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.GetTaskRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetTaskRequest) |  Request for a single Task by name.   
[com.google.cloud.batch.v1alpha.GetTaskRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetTaskRequest.Builder) |  Request for a single Task by name.   
[com.google.cloud.batch.v1alpha.Job](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job) |  The Cloud Batch Job description.   
[com.google.cloud.batch.v1alpha.Job.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job.Builder) |  The Cloud Batch Job description.   
[com.google.cloud.batch.v1alpha.JobDependency](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobDependency) |  JobDependency describes the state of other Jobs that the start of this Job depends on. All dependent Jobs must have been submitted in the same region.  
[com.google.cloud.batch.v1alpha.JobDependency.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobDependency.Builder) |  JobDependency describes the state of other Jobs that the start of this Job depends on. All dependent Jobs must have been submitted in the same region.  
[com.google.cloud.batch.v1alpha.JobName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobName) |   
[com.google.cloud.batch.v1alpha.JobName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobName.Builder) |  Builder for projects/{project}/locations/{location}/jobs/{job}.  
[com.google.cloud.batch.v1alpha.JobNotification](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotification) |  Notification configurations.   
[com.google.cloud.batch.v1alpha.JobNotification.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotification.Builder) |  Notification configurations.   
[com.google.cloud.batch.v1alpha.JobNotification.Message](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotification.Message) |  Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default.  
[com.google.cloud.batch.v1alpha.JobNotification.Message.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotification.Message.Builder) |  Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default.  
[com.google.cloud.batch.v1alpha.JobProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobProto) |   
[com.google.cloud.batch.v1alpha.JobStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus) |  Job status.   
[com.google.cloud.batch.v1alpha.JobStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.Builder) |  Job status.   
[com.google.cloud.batch.v1alpha.JobStatus.InstanceStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.InstanceStatus) |  VM instance status.   
[com.google.cloud.batch.v1alpha.JobStatus.InstanceStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.InstanceStatus.Builder) |  VM instance status.   
[com.google.cloud.batch.v1alpha.JobStatus.TaskGroupStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.TaskGroupStatus) |  Aggregated task status for a TaskGroup.   
[com.google.cloud.batch.v1alpha.JobStatus.TaskGroupStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.TaskGroupStatus.Builder) |  Aggregated task status for a TaskGroup.   
[com.google.cloud.batch.v1alpha.LifecyclePolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy) |  LifecyclePolicy describes how to deal with task failures based on different conditions.   
[com.google.cloud.batch.v1alpha.LifecyclePolicy.ActionCondition](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy.ActionCondition) |  Conditions for actions to deal with task failures.   
[com.google.cloud.batch.v1alpha.LifecyclePolicy.ActionCondition.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy.ActionCondition.Builder) |  Conditions for actions to deal with task failures.   
[com.google.cloud.batch.v1alpha.LifecyclePolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy.Builder) |  LifecyclePolicy describes how to deal with task failures based on different conditions.   
[com.google.cloud.batch.v1alpha.ListJobsRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequest) |  ListJob Request.   
[com.google.cloud.batch.v1alpha.ListJobsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequest.Builder) |  ListJob Request.   
[com.google.cloud.batch.v1alpha.ListJobsResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsResponse) |  ListJob Response.   
[com.google.cloud.batch.v1alpha.ListJobsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsResponse.Builder) |  ListJob Response.   
[com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest) |  ListResourceAllowances Request.   
[com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest.Builder) |  ListResourceAllowances Request.   
[com.google.cloud.batch.v1alpha.ListResourceAllowancesResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesResponse) |  ListResourceAllowances Response.   
[com.google.cloud.batch.v1alpha.ListResourceAllowancesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesResponse.Builder) |  ListResourceAllowances Response.   
[com.google.cloud.batch.v1alpha.ListTasksRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequest) |  ListTasks Request.   
[com.google.cloud.batch.v1alpha.ListTasksRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequest.Builder) |  ListTasks Request.   
[com.google.cloud.batch.v1alpha.ListTasksResponse](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksResponse) |  ListTasks Response.   
[com.google.cloud.batch.v1alpha.ListTasksResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksResponse.Builder) |  ListTasks Response.   
[com.google.cloud.batch.v1alpha.LocationName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LocationName) |   
[com.google.cloud.batch.v1alpha.LocationName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LocationName.Builder) |  Builder for projects/{project}/locations/{location}.  
[com.google.cloud.batch.v1alpha.LogsPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicy) |  LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout`  
[com.google.cloud.batch.v1alpha.LogsPolicy.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicy.Builder) |  LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout`  
[com.google.cloud.batch.v1alpha.LogsPolicy.CloudLoggingOption](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicy.CloudLoggingOption) |  `CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.   
[com.google.cloud.batch.v1alpha.LogsPolicy.CloudLoggingOption.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicy.CloudLoggingOption.Builder) |  `CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.   
[com.google.cloud.batch.v1alpha.](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.NFS) |  Represents an NFS volume.   
[com.google.cloud.batch.v1alpha.NFS.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.NFS.Builder) |  Represents an NFS volume.   
[com.google.cloud.batch.v1alpha.Notification](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Notification) |  Notification on resource state change.   
[com.google.cloud.batch.v1alpha.Notification.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Notification.Builder) |  Notification on resource state change.   
[com.google.cloud.batch.v1alpha.NotificationProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.NotificationProto) |   
[com.google.cloud.batch.v1alpha.OperationMetadata](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata) |  Represents the metadata of the long-running operation.   
[com.google.cloud.batch.v1alpha.OperationMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata.Builder) |  Represents the metadata of the long-running operation.   
[com.google.cloud.batch.v1alpha.](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.PD) |  Deprecated: please use device_name instead.   
[com.google.cloud.batch.v1alpha.PD.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.PD.Builder) |  Deprecated: please use device_name instead.   
[com.google.cloud.batch.v1alpha.ResourceAllowance](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance) |  The Resource Allowance description for Cloud Batch. Only one Resource Allowance is supported now under a specific location and project.  
[com.google.cloud.batch.v1alpha.ResourceAllowance.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance.Builder) |  The Resource Allowance description for Cloud Batch. Only one Resource Allowance is supported now under a specific location and project.  
[com.google.cloud.batch.v1alpha.ResourceAllowanceName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowanceName) |   
[com.google.cloud.batch.v1alpha.ResourceAllowanceName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowanceName.Builder) |  Builder for projects/{project}/locations/{location}/resourceAllowances/{resource_allowance}.  
[com.google.cloud.batch.v1alpha.ResourceAllowanceProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowanceProto) |   
[com.google.cloud.batch.v1alpha.ResourceUsage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceUsage) |  ResourceUsage describes the resource usage of the job.   
[com.google.cloud.batch.v1alpha.ResourceUsage.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceUsage.Builder) |  ResourceUsage describes the resource usage of the job.   
[com.google.cloud.batch.v1alpha.Runnable](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable) |  Runnable describes instructions for executing a specific script or container as part of a Task.   
[com.google.cloud.batch.v1alpha.Runnable.Barrier](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Barrier) |  A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.   
[com.google.cloud.batch.v1alpha.Runnable.Barrier.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Barrier.Builder) |  A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.   
[com.google.cloud.batch.v1alpha.Runnable.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Builder) |  Runnable describes instructions for executing a specific script or container as part of a Task.   
[com.google.cloud.batch.v1alpha.Runnable.Container](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Container) |  Container runnable.   
[com.google.cloud.batch.v1alpha.Runnable.Container.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Container.Builder) |  Container runnable.   
[com.google.cloud.batch.v1alpha.Runnable.Script](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Script) |  Script runnable.   
[com.google.cloud.batch.v1alpha.Runnable.Script.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Script.Builder) |  Script runnable.   
[com.google.cloud.batch.v1alpha.ServiceAccount](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ServiceAccount) |  Carries information about a Google Cloud service account.   
[com.google.cloud.batch.v1alpha.ServiceAccount.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ServiceAccount.Builder) |  Carries information about a Google Cloud service account.   
[com.google.cloud.batch.v1alpha.StatusEvent](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.StatusEvent) |  Status event.   
[com.google.cloud.batch.v1alpha.StatusEvent.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.StatusEvent.Builder) |  Status event.   
[com.google.cloud.batch.v1alpha.Task](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task) |  A Cloud Batch task.   
[com.google.cloud.batch.v1alpha.Task.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task.Builder) |  A Cloud Batch task.   
[com.google.cloud.batch.v1alpha.TaskExecution](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskExecution) |  This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.   
[com.google.cloud.batch.v1alpha.TaskExecution.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskExecution.Builder) |  This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.   
[com.google.cloud.batch.v1alpha.TaskGroup](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskGroup) |  A TaskGroup defines one or more Tasks that all share the same TaskSpec.   
[com.google.cloud.batch.v1alpha.TaskGroup.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskGroup.Builder) |  A TaskGroup defines one or more Tasks that all share the same TaskSpec.   
[com.google.cloud.batch.v1alpha.TaskGroupName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskGroupName) |   
[com.google.cloud.batch.v1alpha.TaskGroupName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskGroupName.Builder) |  Builder for projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}.  
[com.google.cloud.batch.v1alpha.TaskName](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskName) |   
[com.google.cloud.batch.v1alpha.TaskName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskName.Builder) |  Builder for projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}/tasks/{task}.  
[com.google.cloud.batch.v1alpha.TaskProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskProto) |   
[com.google.cloud.batch.v1alpha.TaskResourceUsage](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskResourceUsage) |  TaskResourceUsage describes the resource usage of the task.   
[com.google.cloud.batch.v1alpha.TaskResourceUsage.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskResourceUsage.Builder) |  TaskResourceUsage describes the resource usage of the task.   
[com.google.cloud.batch.v1alpha.TaskSpec](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskSpec) |  Spec of a task   
[com.google.cloud.batch.v1alpha.TaskSpec.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskSpec.Builder) |  Spec of a task   
[com.google.cloud.batch.v1alpha.TaskStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskStatus) |  Status of a task.   
[com.google.cloud.batch.v1alpha.TaskStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskStatus.Builder) |  Status of a task.   
[com.google.cloud.batch.v1alpha.UpdateJobRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateJobRequest) |  UpdateJob Request.   
[com.google.cloud.batch.v1alpha.UpdateJobRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateJobRequest.Builder) |  UpdateJob Request.   
[com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest) |  UpdateResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest.Builder) |  UpdateResourceAllowance Request.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowance](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowance) |  UsageResourceAllowance describes the detail of usage resource allowance.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowance.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowance.Builder) |  UsageResourceAllowance describes the detail of usage resource allowance.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec) |  Spec of a usage ResourceAllowance.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Builder) |  Spec of a usage ResourceAllowance.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Limit](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Limit) |  UsageResourceAllowance limitation.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Limit.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Limit.Builder) |  UsageResourceAllowance limitation.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus) |  Status of a usage ResourceAllowance.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.Builder) |  Status of a usage ResourceAllowance.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReport](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReport) |  ConsumptionReport is the report of ResourceAllowance consumptions in a time period.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReport.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReport.Builder) |  ConsumptionReport is the report of ResourceAllowance consumptions in a time period.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatus](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatus) |  UsageResourceAllowanceStatus detail about usage consumption.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatus.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatus.Builder) |  UsageResourceAllowanceStatus detail about usage consumption.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption) |  Protobuf type `google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption`  
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption.Builder) |  Protobuf type ` google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption`  
[com.google.cloud.batch.v1alpha.Volume](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Volume) |  Volume describes a volume and parameters for it to be mounted to a VM.   
[com.google.cloud.batch.v1alpha.Volume.Builder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Volume.Builder) |  Volume describes a volume and parameters for it to be mounted to a VM.   
[com.google.cloud.batch.v1alpha.VolumeProto](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.VolumeProto) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.batch.v1alpha.AllocationPolicy.AcceleratorOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.AcceleratorOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDiskOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDiskOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.DiskOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.DiskOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceFlexibilityPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceFlexibilityPolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplateOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplateOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceSelectionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstanceSelectionOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.LocationPolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterfaceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterfaceOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkPolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.PlacementPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.PlacementPolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.AllocationPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.BatchServiceGrpc.AsyncService](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceGrpc.AsyncService) |  Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.  
[com.google.cloud.batch.v1alpha.CancelJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.CancelJobResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponseOrBuilder) |   
[com.google.cloud.batch.v1alpha.ComputeResourceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ComputeResourceOrBuilder) |   
[com.google.cloud.batch.v1alpha.CreateJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateJobRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.DeleteJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.Environment.KMSEnvMapOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Environment.KMSEnvMapOrBuilder) |   
[com.google.cloud.batch.v1alpha.EnvironmentOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.EnvironmentOrBuilder) |   
[com.google.cloud.batch.v1alpha.GCSOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GCSOrBuilder) |   
[com.google.cloud.batch.v1alpha.GetJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetJobRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.GetResourceAllowanceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetResourceAllowanceRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.GetTaskRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetTaskRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobDependencyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobDependencyOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobNotification.MessageOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotification.MessageOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobNotificationOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotificationOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobStatus.InstanceStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.InstanceStatusOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobStatus.TaskGroupStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.TaskGroupStatusOrBuilder) |   
[com.google.cloud.batch.v1alpha.JobStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatusOrBuilder) |   
[com.google.cloud.batch.v1alpha.LifecyclePolicy.ActionConditionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy.ActionConditionOrBuilder) |   
[com.google.cloud.batch.v1alpha.LifecyclePolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.ListJobsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.ListJobsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsResponseOrBuilder) |   
[com.google.cloud.batch.v1alpha.ListResourceAllowancesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.ListResourceAllowancesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesResponseOrBuilder) |   
[com.google.cloud.batch.v1alpha.ListTasksRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.ListTasksResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksResponseOrBuilder) |   
[com.google.cloud.batch.v1alpha.LogsPolicy.CloudLoggingOptionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicy.CloudLoggingOptionOrBuilder) |   
[com.google.cloud.batch.v1alpha.LogsPolicyOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicyOrBuilder) |   
[com.google.cloud.batch.v1alpha.NFSOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.NFSOrBuilder) |   
[com.google.cloud.batch.v1alpha.NotificationOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.NotificationOrBuilder) |   
[com.google.cloud.batch.v1alpha.OperationMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadataOrBuilder) |   
[com.google.cloud.batch.v1alpha.PDOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.PDOrBuilder) |   
[com.google.cloud.batch.v1alpha.ResourceAllowanceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowanceOrBuilder) |   
[com.google.cloud.batch.v1alpha.ResourceUsageOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceUsageOrBuilder) |   
[com.google.cloud.batch.v1alpha.Runnable.BarrierOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.BarrierOrBuilder) |   
[com.google.cloud.batch.v1alpha.Runnable.ContainerOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.ContainerOrBuilder) |   
[com.google.cloud.batch.v1alpha.Runnable.ScriptOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.ScriptOrBuilder) |   
[com.google.cloud.batch.v1alpha.RunnableOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.RunnableOrBuilder) |   
[com.google.cloud.batch.v1alpha.ServiceAccountOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ServiceAccountOrBuilder) |   
[com.google.cloud.batch.v1alpha.StatusEventOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.StatusEventOrBuilder) |   
[com.google.cloud.batch.v1alpha.TaskExecutionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskExecutionOrBuilder) |   
[com.google.cloud.batch.v1alpha.TaskGroupOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskGroupOrBuilder) |   
[com.google.cloud.batch.v1alpha.TaskOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskOrBuilder) |   
[com.google.cloud.batch.v1alpha.TaskResourceUsageOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskResourceUsageOrBuilder) |   
[com.google.cloud.batch.v1alpha.TaskSpecOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskSpecOrBuilder) |   
[com.google.cloud.batch.v1alpha.TaskStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskStatusOrBuilder) |   
[com.google.cloud.batch.v1alpha.UpdateJobRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateJobRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequestOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.LimitOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.LimitOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpecOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpecOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReportOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReportOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatusOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumptionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumptionOrBuilder) |   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatusOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceStatusOrBuilder) |   
[com.google.cloud.batch.v1alpha.VolumeOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.VolumeOrBuilder) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDisk.AttachedCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.AttachedDisk.AttachedCase) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.Disk.DataSourceCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.Disk.DataSourceCase) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase) |   
[com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterface.NicType](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.NetworkInterface.NicType) |  Compute Engine VM instance NIC type.   
[com.google.cloud.batch.v1alpha.AllocationPolicy.ProvisioningModel](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.AllocationPolicy.ProvisioningModel) |  Compute Engine VM instance provisioning model.   
[com.google.cloud.batch.v1alpha.CalendarPeriod](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CalendarPeriod) |  A `CalendarPeriod` represents the abstract concept of a time period that has a canonical start. All calendar times begin at 12 AM US and Canadian Pacific Time (UTC-8).  
[com.google.cloud.batch.v1alpha.Job.SchedulingPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job.SchedulingPolicy) |  The order that TaskGroups are scheduled relative to each other. Not yet implemented.  
[com.google.cloud.batch.v1alpha.JobDependency.Type](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobDependency.Type) |  Dependency type.   
[com.google.cloud.batch.v1alpha.JobNotification.Type](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobNotification.Type) |  The message type.   
[com.google.cloud.batch.v1alpha.JobStatus.State](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.JobStatus.State) |  Valid Job states.   
[com.google.cloud.batch.v1alpha.LifecyclePolicy.Action](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LifecyclePolicy.Action) |  Action on task failures based on different conditions.   
[com.google.cloud.batch.v1alpha.LogsPolicy.Destination](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.LogsPolicy.Destination) |  The destination (if any) for logs.   
[com.google.cloud.batch.v1alpha.ResourceAllowance.ResourceAllowanceCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance.ResourceAllowanceCase) |   
[com.google.cloud.batch.v1alpha.ResourceAllowanceState](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowanceState) |  ResourceAllowance valid state.   
[com.google.cloud.batch.v1alpha.Runnable.ExecutableCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.ExecutableCase) |   
[com.google.cloud.batch.v1alpha.Runnable.Script.CommandCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Runnable.Script.CommandCase) |   
[com.google.cloud.batch.v1alpha.TaskGroup.SchedulingPolicy](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskGroup.SchedulingPolicy) |  How Tasks in the TaskGroup should be scheduled relative to each other.   
[com.google.cloud.batch.v1alpha.TaskStatus.State](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.TaskStatus.State) |  Task states.   
[com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Limit.DurationCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.Limit.DurationCase) |   
[com.google.cloud.batch.v1alpha.Volume.SourceCase](https://cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Volume.SourceCase) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
