---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/summary_class/
title: Package Classes (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:21.107249+00:00
---

# Package Classes (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 

Summary of entries of Classes for batch.

## Classes 

### [BatchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceAsyncClient)

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

### [BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.BatchServiceClient)

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

### [ListJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListJobsAsyncPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) object, and provides an `__aiter__` method to iterate through its `jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListJobsPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) object, and provides an `__iter__` method to iterate through its `jobs` field.

If there are more pages, the `__iter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListTasksAsyncPager)

A pager for iterating through `list_tasks` requests.

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) object, and provides an `__aiter__` method to iterate through its `tasks` field.

If there are more pages, the `__aiter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListTasksPager)

A pager for iterating through `list_tasks` requests.

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) object, and provides an `__iter__` method to iterate through its `tasks` field.

If there are more pages, the `__iter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy)

A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.

### [Accelerator](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.Accelerator)

Accelerator describes Compute Engine accelerators to be attached to the VM.

### [AttachedDisk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.AttachedDisk)

A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Disk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.Disk)

A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and <https://cloud.google.com/compute/docs/disks#localssds>.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicy)

InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.

### [InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.InstancePolicyOrTemplate)

InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include optional VM resources such as GPUs and extra disks.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.LabelsEntry)

The abstract base class for a message.

### [LocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.LocationPolicy)

### [NetworkInterface](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.NetworkInterface)

A network interface.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NicType](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.NetworkInterface.NicType)

Compute Engine VM instance NIC type.

### [NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.NetworkPolicy)

NetworkPolicy describes VM instance network configurations.

### [PlacementPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.PlacementPolicy)

PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.

### [ProvisioningModel](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.AllocationPolicy.ProvisioningModel)

Compute Engine VM instance provisioning model.
    
    
        Above SPOT VM is the preferable model for
        preemptible VM instances: the old preemptible VM
        model (indicated by this field) is the older
        model, and has been migrated to use the SPOT
        model as the underlying technology. This old
        model will still be supported.
    RESERVATION_BOUND (4):
        Bound to the lifecycle of the reservation in
        which it is provisioned.
    FLEX_START (5):
        Instance is provisioned with DWS Flex Start
        and has limited max run duration.
    

### [CancelJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CancelJobRequest)

CancelJob Request.

### [CancelJobResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CancelJobResponse)

Response to the CancelJob request.

### [ComputeResource](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ComputeResource)

Compute resource requirements.

ComputeResource defines the amount of resources required for each task. Make sure your tasks have enough resources to successfully run. If you also define the types of resources for a job to use with the `InstancePolicyOrTemplate <https://cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate>`__ field, make sure both fields are compatible with each other.

### [CreateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.CreateJobRequest)

CreateJob Request.

### [DeleteJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.DeleteJobRequest)

DeleteJob Request.

### [Environment](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Environment)

An Environment describes a collection of environment variables to set when executing Tasks.

### [KMSEnvMap](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Environment.KMSEnvMap)

### [SecretVariablesEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Environment.SecretVariablesEntry)

The abstract base class for a message.

### [VariablesEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Environment.VariablesEntry)

The abstract base class for a message.

### [GCS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.GCS)

Represents a Google Cloud Storage volume.

### [GetJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.GetJobRequest)

GetJob Request.

### [GetTaskRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.GetTaskRequest)

Request for a single Task by name.

### [Job](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job)

The Cloud Batch Job description.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Job.LabelsEntry)

The abstract base class for a message.

### [JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification)

Notification configurations.

### [Message](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.Message)

Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default. One message should specify either the job or the task level attributes, but not both. For example, job level: JOB_STATE_CHANGED and/or a specified new_job_state; task level: TASK_STATE_CHANGED and/or a specified new_task_state.

### [Type](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobNotification.Type)

The message type.

### [JobStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus)

Job status.

### [InstanceStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.InstanceStatus)

VM instance status.

### [State](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.State)

Valid Job states.

### [TaskGroupStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.TaskGroupStatus)

Aggregated task status for a TaskGroup.

### [CountsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.TaskGroupStatus.CountsEntry)

The abstract base class for a message.

### [TaskGroupsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.JobStatus.TaskGroupsEntry)

The abstract base class for a message.

### [LifecyclePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LifecyclePolicy)

LifecyclePolicy describes how to deal with task failures based on different conditions.

### [Action](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LifecyclePolicy.Action)

Action on task failures based on different conditions.

### [ActionCondition](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LifecyclePolicy.ActionCondition)

Conditions for actions to deal with task failures.

### [ListJobsRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsRequest)

ListJob Request.

### [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse)

ListJob Response.

### [ListTasksRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksRequest)

ListTasks Request.

### [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse)

ListTasks Response.

### [LogsPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy)

LogsPolicy describes if and how a job's logs are preserved. Logs include information that is automatically written by the Batch service agent and any information that you configured the job's runnables to write to the `stdout` or `stderr` streams.

### [CloudLoggingOption](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.CloudLoggingOption)

`CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.

### [Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.LogsPolicy.Destination)

The destination (if any) for logs.

### [NFS](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.NFS)

Represents an NFS volume.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable)

Runnable describes instructions for executing a specific script or container as part of a Task.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Barrier](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Barrier)

A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.

### [Container](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Container)

Container runnable.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.LabelsEntry)

The abstract base class for a message.

### [Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Runnable.Script)

Script runnable.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceAccount](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ServiceAccount)

Carries information about a Google Cloud service account.

### [StatusEvent](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.StatusEvent)

Status event.

### [Task](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Task)

A Cloud Batch task.

### [TaskExecution](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskExecution)

This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.

### [TaskGroup](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup)

A TaskGroup defines one or more Tasks that all share the same TaskSpec.

### [SchedulingPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskGroup.SchedulingPolicy)

How Tasks in the TaskGroup should be scheduled relative to each other.
    
    
        Tasks might be executed in parallel depending on parallelism
        and task_count values.
    IN_ORDER (2):
        Run Tasks sequentially with increased task
        index.
    

### [TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec)

Spec of a task

### [EnvironmentsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskSpec.EnvironmentsEntry)

The abstract base class for a message.

### [TaskStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskStatus)

Status of a task.

### [State](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.TaskStatus.State)

Task states.

### [Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.Volume)

Volume describes a volume and parameters for it to be mounted to a VM.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.BatchServiceAsyncClient)

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

### [BatchServiceClient](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.BatchServiceClient)

Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

### [ListJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers.ListJobsAsyncPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListJobsResponse) object, and provides an `__aiter__` method to iterate through its `jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers.ListJobsPager)

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListJobsResponse) object, and provides an `__iter__` method to iterate through its `jobs` field.

If there are more pages, the `__iter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceAllowancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers.ListResourceAllowancesAsyncPager)

A pager for iterating through `list_resource_allowances` requests.

This class thinly wraps an initial [ListResourceAllowancesResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse) object, and provides an `__aiter__` method to iterate through its `resource_allowances` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceAllowances` requests and continue to iterate through the `resource_allowances` field on the corresponding responses.

All the usual [ListResourceAllowancesResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceAllowancesPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers.ListResourceAllowancesPager)

A pager for iterating through `list_resource_allowances` requests.

This class thinly wraps an initial [ListResourceAllowancesResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse) object, and provides an `__iter__` method to iterate through its `resource_allowances` field.

If there are more pages, the `__iter__` method will make additional `ListResourceAllowances` requests and continue to iterate through the `resource_allowances` field on the corresponding responses.

All the usual [ListResourceAllowancesResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListResourceAllowancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers.ListTasksAsyncPager)

A pager for iterating through `list_tasks` requests.

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListTasksResponse) object, and provides an `__aiter__` method to iterate through its `tasks` field.

If there are more pages, the `__aiter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers.ListTasksPager)

A pager for iterating through `list_tasks` requests.

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListTasksResponse) object, and provides an `__iter__` method to iterate through its `tasks` field.

If there are more pages, the `__iter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AllocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy)

A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job.

### [Accelerator](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.Accelerator)

Accelerator describes Compute Engine accelerators to be attached to the VM.

### [AttachedDisk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.AttachedDisk)

A new or an existing persistent disk (PD) or a local ssd attached to a VM instance.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Disk](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.Disk)

A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and <https://cloud.google.com/compute/docs/disks#localssds>.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstanceFlexibilityPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceFlexibilityPolicy)

Allows creating VMs from multiple types of machines. Instance flexibility configuration overrides instances configuration.

### [InstanceSelectionsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceFlexibilityPolicy.InstanceSelectionsEntry)

The abstract base class for a message.

### [InstancePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstancePolicy)

InstancePolicy describes an instance type and resources attached to each VM created by this InstancePolicy.

### [InstancePolicyOrTemplate](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstancePolicyOrTemplate)

InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include optional VM resources such as GPUs and extra disks.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InstanceSelection](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.InstanceSelection)

Defines an instance selection for a given instance flexibility policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.LabelsEntry)

The abstract base class for a message.

### [LocationPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.LocationPolicy)

### [NetworkInterface](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.NetworkInterface)

A network interface.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NicType](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.NetworkInterface.NicType)

Compute Engine VM instance NIC type.

### [NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.NetworkPolicy)

NetworkPolicy describes VM instance network configurations.

### [PlacementPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.PlacementPolicy)

PlacementPolicy describes a group placement policy for the VMs controlled by this AllocationPolicy.

### [ProvisioningModel](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.AllocationPolicy.ProvisioningModel)

Compute Engine VM instance provisioning model.
    
    
        Above SPOT VM is the preferable model for
        preemptible VM instances: the old preemptible VM
        model (indicated by this field) is the older
        model, and has been migrated to use the SPOT
        model as the underlying technology. This old
        model will still be supported.
    RESERVATION_BOUND (4):
        Bound to the lifecycle of the reservation in
        which it is provisioned.
    FLEX_START (5):
        Instance is provisioned with DWS Flex Start
        and has limited max run duration.
    

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

### [KMSEnvMap](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Environment.KMSEnvMap)

### [SecretVariablesEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Environment.SecretVariablesEntry)

The abstract base class for a message.

### [VariablesEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Environment.VariablesEntry)

The abstract base class for a message.

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

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Job.LabelsEntry)

The abstract base class for a message.

### [SchedulingPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Job.SchedulingPolicy)

The order that TaskGroups are scheduled relative to each other. Not yet implemented.

### [JobDependency](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobDependency)

JobDependency describes the state of other Jobs that the start of this Job depends on. All dependent Jobs must have been submitted in the same region.

### [ItemsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobDependency.ItemsEntry)

The abstract base class for a message.

### [Type](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobDependency.Type)

Dependency type.

### [JobNotification](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification)

Notification configurations.

### [Message](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification.Message)

Message details. Describe the conditions under which messages will be sent. If no attribute is defined, no message will be sent by default. One message should specify either the job or the task level attributes, but not both. For example, job level: JOB_STATE_CHANGED and/or a specified new_job_state; task level: TASK_STATE_CHANGED and/or a specified new_task_state.

### [Type](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobNotification.Type)

The message type.

### [JobStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus)

Job status.

### [InstanceStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.InstanceStatus)

VM instance status.

### [State](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.State)

Valid Job states.

### [TaskGroupStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.TaskGroupStatus)

Aggregated task status for a TaskGroup.

### [CountsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.TaskGroupStatus.CountsEntry)

The abstract base class for a message.

### [TaskGroupsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.JobStatus.TaskGroupsEntry)

The abstract base class for a message.

### [LifecyclePolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LifecyclePolicy)

LifecyclePolicy describes how to deal with task failures based on different conditions.

### [Action](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LifecyclePolicy.Action)

Action on task failures based on different conditions.

### [ActionCondition](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LifecyclePolicy.ActionCondition)

Conditions for actions to deal with task failures.

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

### [CloudLoggingOption](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LogsPolicy.CloudLoggingOption)

`CloudLoggingOption` contains additional settings for Cloud Logging logs generated by Batch job.

### [Destination](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.LogsPolicy.Destination)

The destination (if any) for logs.

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

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceAllowance.LabelsEntry)

The abstract base class for a message.

### [ResourceAllowanceState](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceAllowanceState)

ResourceAllowance valid state.

### [ResourceUsage](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.ResourceUsage)

ResourceUsage describes the resource usage of the job.

### [Runnable](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Runnable)

Runnable describes instructions for executing a specific script or container as part of a Task.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Barrier](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Runnable.Barrier)

A barrier runnable automatically blocks the execution of subsequent runnables until all the tasks in the task group reach the barrier.

### [Container](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Runnable.Container)

Container runnable.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Runnable.LabelsEntry)

The abstract base class for a message.

### [Script](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Runnable.Script)

Script runnable.

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

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskGroup.LabelsEntry)

The abstract base class for a message.

### [SchedulingPolicy](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskGroup.SchedulingPolicy)

How Tasks in the TaskGroup should be scheduled relative to each other.
    
    
        Tasks might be executed in parallel depending on parallelism
        and task_count values.
    IN_ORDER (2):
        Run Tasks sequentially with increased task
        index.
    

### [TaskResourceUsage](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskResourceUsage)

TaskResourceUsage describes the resource usage of the task.

### [TaskSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskSpec)

Spec of a task

### [EnvironmentsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskSpec.EnvironmentsEntry)

The abstract base class for a message.

### [TaskStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskStatus)

Status of a task.

### [State](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.TaskStatus.State)

Task states.

### [UpdateJobRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UpdateJobRequest)

UpdateJob Request.

### [UpdateResourceAllowanceRequest](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UpdateResourceAllowanceRequest)

UpdateResourceAllowance Request.

### [UsageResourceAllowance](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowance)

UsageResourceAllowance describes the detail of usage resource allowance.

### [UsageResourceAllowanceSpec](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceSpec)

Spec of a usage ResourceAllowance.

### [Limit](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceSpec.Limit)

UsageResourceAllowance limitation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UsageResourceAllowanceStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus)

Status of a usage ResourceAllowance.

### [ConsumptionReport](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.ConsumptionReport)

ConsumptionReport is the report of ResourceAllowance consumptions in a time period.

### [LatestPeriodConsumptionsEntry](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.ConsumptionReport.LatestPeriodConsumptionsEntry)

The abstract base class for a message.

### [LimitStatus](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.LimitStatus)

UsageResourceAllowanceStatus detail about usage consumption.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PeriodConsumption](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.UsageResourceAllowanceStatus.PeriodConsumption)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Volume](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.types.Volume)

Volume describes a volume and parameters for it to be mounted to a VM.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers)

API documentation for `batch_v1.services.batch_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1alpha.services.batch_service.pagers)

API documentation for `batch_v1alpha.services.batch_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
