---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types
title: Package types (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:34.535523+00:00
---

# Package types (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 

API documentation for `batch_v1alpha.types` package.

## Classes 

### [AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy)

A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.

### [CalendarPeriod](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.CalendarPeriod)

A `CalendarPeriod` represents the abstract concept of a time period that has a canonical start. All calendar times begin at 12 AM US and Canadian Pacific Time (UTC-8).

### [CancelJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.CancelJobRequest)

CancelJob Request.

### [CancelJobResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.CancelJobResponse)

Response to the CancelJob request.

### [ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ComputeResource)

Compute resource requirements.

ComputeResource defines the amount of resources required for each task. Make sure your tasks have enough resources to successfully run. If you also define the types of resources for a job to use with the `InstancePolicyOrTemplate <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate>`__ field, make sure both fields are compatible with each other.

### [CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.CreateJobRequest)

CreateJob Request.

### [CreateResourceAllowanceRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.CreateResourceAllowanceRequest)

CreateResourceAllowance Request.

### [DeleteJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.DeleteJobRequest)

DeleteJob Request.

### [DeleteResourceAllowanceRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.DeleteResourceAllowanceRequest)

DeleteResourceAllowance Request.

### [Environment](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Environment)

An Environment describes a collection of environment variables to set when executing Tasks.

### [GCS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.GCS)

Represents a Google Cloud Storage volume.

### [GetJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.GetJobRequest)

GetJob Request.

### [GetResourceAllowanceRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.GetResourceAllowanceRequest)

GetResourceAllowance Request.

### [GetTaskRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.GetTaskRequest)

Request for a single Task by name.

### [Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Job)

The Cloud Batch Job description.

### [JobDependency](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobDependency)

JobDependency describes the state of other Jobs that the start of this Job depends on. All dependent Jobs must have been submitted in the same region.

### [JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification)

Notification configurations.

### [JobStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus)

Job status.

### [LifecyclePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LifecyclePolicy)

LifecyclePolicy describes how to deal with task failures based on different conditions.

### [ListJobsRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListJobsRequest)

ListJob Request.

### [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListJobsResponse)

ListJob Response.

### [ListResourceAllowancesRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListResourceAllowancesRequest)

ListResourceAllowances Request.

### [ListResourceAllowancesResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse)

ListResourceAllowances Response.

### [ListTasksRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListTasksRequest)

ListTasks Request.

### [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListTasksResponse)

ListTasks Response.

### [LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LogsPolicy)

LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout` or `stderr` streams.

### [NFS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.NFS)

Represents an NFS volume.

### [Notification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Notification)

Notification on resource state change.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [PD](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.PD)

Deprecated: please use device_name instead.

### [ResourceAllowance](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceAllowance)

The Resource Allowance description for Cloud Batch. Only one Resource Allowance is supported now under a specific location and project.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResourceAllowanceState](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceAllowanceState)

ResourceAllowance valid state.

### [ResourceUsage](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceUsage)

ResourceUsage describes the resource usage of the job.

### [Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Runnable)

Runnable describes instructions for executing a specific script or container as part of a Task.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceAccount](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ServiceAccount)

Carries information about a Google Cloud service account.

### [StatusEvent](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.StatusEvent)

Status event.

### [Task](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Task)

A Cloud Batch task.

### [TaskExecution](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskExecution)

This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.

### [TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskGroup)

A TaskGroup defines one or more Tasks that all share the same TaskSpec.

### [TaskResourceUsage](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskResourceUsage)

TaskResourceUsage describes the resource usage of the task.

### [TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskSpec)

Spec of a task

### [TaskStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskStatus)

Status of a task.

### [UpdateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UpdateJobRequest)

UpdateJob Request.

### [UpdateResourceAllowanceRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UpdateResourceAllowanceRequest)

UpdateResourceAllowance Request.

### [UsageResourceAllowance](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowance)

UsageResourceAllowance describes the detail of usage resource allowance.

### [UsageResourceAllowanceSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceSpec)

Spec of a usage ResourceAllowance.

### [UsageResourceAllowanceStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus)

Status of a usage ResourceAllowance.

### [Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Volume)

Volume describes a volume and parameters for it to be mounted to a VM.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
