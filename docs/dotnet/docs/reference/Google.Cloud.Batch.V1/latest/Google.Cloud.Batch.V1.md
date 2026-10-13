---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1
title: Batch v1 API - Namespace Google.Cloud.Batch.V1 (2.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:32.884324+00:00
---

# Batch v1 API - Namespace Google.Cloud.Batch.V1 (2.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Batch v1 API - Namespace Google.Cloud.Batch.V1 (2.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.16.0 (latest)  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.0 

## Classes 

### [AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy)

A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.

### [AllocationPolicy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types)

Container for nested types declared in the AllocationPolicy message type.

### [AllocationPolicy.Types.Accelerator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.Accelerator)

Accelerator describes Compute Engine accelerators to be attached to the VM.

### [AllocationPolicy.Types.AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.AttachedDisk)

A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.

### [AllocationPolicy.Types.Disk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.Disk)

A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and <https://cloud.google.com/compute/docs/disks#localssds>.

### [AllocationPolicy.Types.InstancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.InstancePolicy)

InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.

### [AllocationPolicy.Types.InstancePolicyOrTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.InstancePolicyOrTemplate)

InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include optional VM resources such as GPUs and extra disks.

### [AllocationPolicy.Types.LocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.LocationPolicy)

### [AllocationPolicy.Types.NetworkInterface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.NetworkInterface)

A network interface.

### [AllocationPolicy.Types.NetworkInterface.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.NetworkInterface.Types)

Container for nested types declared in the NetworkInterface message type.

### [AllocationPolicy.Types.NetworkPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.NetworkPolicy)

NetworkPolicy describes VM instance network configurations.

### [AllocationPolicy.Types.PlacementPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.PlacementPolicy)

PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.

### [BatchService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchService)

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

### [BatchService.BatchServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchService.BatchServiceBase)

Base class for server-side implementations of BatchService

### [BatchService.BatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchService.BatchServiceClient)

Client for BatchService

### [BatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchServiceClient)

BatchService client wrapper, for convenient use.

### [BatchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchServiceClientBuilder)

Builder class for [BatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchServiceClient) to provide simple configuration of credentials, endpoint etc.

### [BatchServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchServiceClientImpl)

BatchService client wrapper implementation, for convenient use.

### [BatchServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchServiceSettings)

Settings for [BatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.BatchServiceClient) instances.

### [CancelJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.CancelJobRequest)

CancelJob Request.

### [CancelJobResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.CancelJobResponse)

Response to the CancelJob request.

### [ComputeResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.ComputeResource)

Compute resource requirements.

ComputeResource defines the amount of resources required for each task. Make sure your tasks have enough resources to successfully run. If you also define the types of resources for a job to use with the [InstancePolicyOrTemplate](https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate) field, make sure both fields are compatible with each other.

### [CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.CreateJobRequest)

CreateJob Request.

### [DeleteJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.DeleteJobRequest)

DeleteJob Request.

### [Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Environment)

An Environment describes a collection of environment variables to set when executing Tasks.

### [Environment.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Environment.Types)

Container for nested types declared in the Environment message type.

### [Environment.Types.KMSEnvMap](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Environment.Types.KMSEnvMap)

### [GCS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.GCS)

Represents a Google Cloud Storage volume.

### [GetJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.GetJobRequest)

GetJob Request.

### [GetTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.GetTaskRequest)

Request for a single Task by name.

### [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Job)

The Cloud Batch Job description.

### [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobName)

Resource name for the `Job` resource.

### [JobNotification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobNotification)

Notification configurations.

### [JobNotification.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobNotification.Types)

Container for nested types declared in the JobNotification message type.

### [JobNotification.Types.Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobNotification.Types.Message)

Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default. One message should specify either the job or the task level attributes, but not both. For example, job level: JOB_STATE_CHANGED and/or a specified new_job_state; task level: TASK_STATE_CHANGED and/or a specified new_task_state.

### [JobStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobStatus)

Job status.

### [JobStatus.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobStatus.Types)

Container for nested types declared in the JobStatus message type.

### [JobStatus.Types.InstanceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobStatus.Types.InstanceStatus)

VM instance status.

### [JobStatus.Types.TaskGroupStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobStatus.Types.TaskGroupStatus)

Aggregated task status for a TaskGroup.

### [LifecyclePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LifecyclePolicy)

LifecyclePolicy describes how to deal with task failures based on different conditions.

### [LifecyclePolicy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LifecyclePolicy.Types)

Container for nested types declared in the LifecyclePolicy message type.

### [LifecyclePolicy.Types.ActionCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LifecyclePolicy.Types.ActionCondition)

Conditions for actions to deal with task failures.

### [ListJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.ListJobsRequest)

ListJob Request.

### [ListJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.ListJobsResponse)

ListJob Response.

### [ListTasksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.ListTasksRequest)

ListTasks Request.

### [ListTasksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.ListTasksResponse)

ListTasks Response.

### [LogsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LogsPolicy)

LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout` or `stderr` streams.

### [LogsPolicy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LogsPolicy.Types)

Container for nested types declared in the LogsPolicy message type.

### [LogsPolicy.Types.CloudLoggingOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LogsPolicy.Types.CloudLoggingOption)

`CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.

### [NFS](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.NFS)

Represents an NFS volume.

### [OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.OperationMetadata)

Represents the metadata of the long-running operation.

### [Runnable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable)

Runnable describes instructions for executing a specific script or container as part of a Task.

### [Runnable.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable.Types)

Container for nested types declared in the Runnable message type.

### [Runnable.Types.Barrier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable.Types.Barrier)

A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.

### [Runnable.Types.Container](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable.Types.Container)

Container runnable.

### [Runnable.Types.Script](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable.Types.Script)

Script runnable.

### [ServiceAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.ServiceAccount)

Carries information about a Google Cloud service account.

### [StatusEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.StatusEvent)

Status event.

### [Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Task)

A Cloud Batch task.

### [TaskExecution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskExecution)

This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.

### [TaskGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskGroup)

A TaskGroup defines one or more Tasks that all share the same TaskSpec.

### [TaskGroup.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskGroup.Types)

Container for nested types declared in the TaskGroup message type.

### [TaskGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskGroupName)

Resource name for the `TaskGroup` resource.

### [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskName)

Resource name for the `Task` resource.

### [TaskSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskSpec)

Spec of a task

### [TaskStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus)

Status of a task.

### [TaskStatus.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus.Types)

Container for nested types declared in the TaskStatus message type.

### [Volume](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Volume)

Volume describes a volume and parameters for it to be mounted to a VM.

## Enums 

### [AllocationPolicy.Types.AttachedDisk.AttachedOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.AttachedDisk.AttachedOneofCase)

Enum of possible cases for the "attached" oneof.

### [AllocationPolicy.Types.Disk.DataSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.Disk.DataSourceOneofCase)

Enum of possible cases for the "data_source" oneof.

### [AllocationPolicy.Types.InstancePolicyOrTemplate.PolicyTemplateOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.InstancePolicyOrTemplate.PolicyTemplateOneofCase)

Enum of possible cases for the "policy_template" oneof.

### [AllocationPolicy.Types.NetworkInterface.Types.NicType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.NetworkInterface.Types.NicType)

Compute Engine VM instance NIC type.

### [AllocationPolicy.Types.ProvisioningModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.AllocationPolicy.Types.ProvisioningModel)

Compute Engine VM instance provisioning model.

### [JobName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobName.ResourceNameType)

The possible contents of [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobName).

### [JobNotification.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobNotification.Types.Type)

The message type.

### [JobStatus.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.JobStatus.Types.State)

Valid Job states.

### [LifecyclePolicy.Types.Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LifecyclePolicy.Types.Action)

Action on task failures based on different conditions.

### [LogsPolicy.Types.Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.LogsPolicy.Types.Destination)

The destination (if any) for logs.

### [Runnable.ExecutableOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable.ExecutableOneofCase)

Enum of possible cases for the "executable" oneof.

### [Runnable.Types.Script.CommandOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Runnable.Types.Script.CommandOneofCase)

Enum of possible cases for the "command" oneof.

### [TaskGroup.Types.SchedulingPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskGroup.Types.SchedulingPolicy)

How Tasks in the TaskGroup should be scheduled relative to each other.

### [TaskGroupName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskGroupName.ResourceNameType)

The possible contents of [TaskGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskGroupName).

### [TaskName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskName.ResourceNameType)

The possible contents of [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskName).

### [TaskStatus.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.TaskStatus.Types.State)

Task states.

### [Volume.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1/latest/Google.Cloud.Batch.V1.Volume.SourceOneofCase)

Enum of possible cases for the "source" oneof.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
