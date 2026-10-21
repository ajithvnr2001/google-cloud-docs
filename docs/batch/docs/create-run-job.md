---
url: https://docs.cloud.google.com/batch/docs/create-run-job/
title: Job creation and execution overview \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:18.924861+00:00
---

# Job creation and execution overview  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Job creation and execution overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the execution process and creation options for jobs. Batch jobs let you run batch-processing workloads on Google Cloud. To learn about the components of a job and the prerequisites for using Batch, see [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started).

## How job creation and execution works

To use Batch, you create a job that specifies your workload and its requirements, and then Batch automatically runs it.

The details of how job creation and execution works are described in the following sections:

  * Job lifecycle: understand the states that a job progresses through from creation to deletion.
  * Job queuing and scheduling: understand the factors that affect how long it takes for a job to start running.
  * Job execution: understand how a job's tasks run on its resources during execution.



### Job lifecycle

This section describes the lifecycle of a job and its tasks from creation to deletion.

For each workload you want to run on Batch, you go through the following basic process:

  1. **Create a job:** You define the workload you want to run by specifying a job's runnables, tasks, and any other requirements. The details for creating a job are introduced in the Job creation options section in this document.
  2. **Monitor and troubleshoot the job:** When you finish creating a job, the job is automatically queued, scheduled, and executed on the specified resources. You can view the details of a created job or any of its task to see the current state. If needed, you can cancel a job to stop it or prevent it from running. After a job is running or finished, you can also monitor and analyze the job using logs. If a job fails, you can troubleshoot it using any error messages, status events, or logs to diagnose the issue before recreating the job.
  3. **Delete or export the job:** A job's information in Batch remains available until you or Google Cloud deletes it. Google Cloud automatically deletes a job 60 days after it finishes. Before then, you can optionally delete the job yourself, or, if you need to retain the info, you can export the job's information in Batch before the job is deleted. Any information about a job that's stored in other Google Cloud services aren't affected when a job is deleted and have separate retention policies. For example, a job's logs are automatically retained and deleted according to the Cloud Logging retention policy.



After you create a job, it progresses through the following states:

  1. **Queued (`QUEUED`):** the job request has been admitted and is waiting in the queue. The job remains in your project's queue until it can be scheduled, which happens when the required resources are available and the jobs ahead of it have been assessed. However, to prevent your jobs from becoming stale, if a job exceeds the [maximum wait time in the queue](https://docs.cloud.google.com/batch/quotas#max-job-queue), Batch automatically fails the job instead of scheduling it.
  2. **Scheduled (`SCHEDULED`):** the job has been selected from the queue to start running and the resources are being allocated.
  3. **Running (`RUNNING`):** the resources for the job have been created successfully and its tasks can start running.

When a job is running, each of its tasks progresses through the following states:

     1. **Pending (`PENDING`):** the task is waiting for a VM to run on.
     2. **Assigned (`ASSIGNED`):** the task has been assigned a VM to run on.
     3. **Running (`RUNNING`):** the task is running on a VM.
     4. A task finishes in one of the following states:

        * **Succeeded (`SUCCEEDED`):** the task succeeded because each of its runnables met one of the following conditions:

          * The runnable _succeeded_ (returned an [exit code](https://docs.cloud.google.com/batch/docs/troubleshooting#reserved-exit-codes) of zero).
          * The runnable _failed_ (returned a nonzero exit code) but was a _noncritical runnable_ (you enabled the runnable's [`ignoreExitStatus` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Runnable.FIELDS.ignore_exit_status)).
          * The runnable didn't finish but was a _background runnable_ (you enabled the runnable's [`background` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Runnable.FIELDS.background)).
        * **Failed (`FAILED`):** the task failed and stopped running because at least one runnable didn't meet the preceding conditions.

The resources for the job are deleted before the job finishes.

  4. A job finishes in one of the following states:

     * **Succeeded (`SUCCEEDED`):** the job succeeded because all of its tasks succeeded.
     * **Failed (`FAILED`):** the job failed and stopped running because at least one of its tasks failed.
     * **Cancelled (`CANCELLED`):** A user [cancelled the job](https://docs.cloud.google.com/batch/docs/cancel-job) before it succeeded or failed.



For more information, see [job states](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#State) and [task states](https://docs.cloud.google.com/batch/docs/reference/rest/v1/State) in the reference documentation.

### Job queuing and scheduling

Generally, jobs are more likely to run and finish sooner if they are smaller and require only a few common resources. For the example jobs in Batch documentation, which are typically very small and use minimal resources, you might see them finish running in as little as a few minutes.

Specifically, the time a job takes to finish queueing and scheduling varies for different jobs and at different times based on the following factors:

  * **User-specified job prerequisites:** any prerequisites that you require to be met before the job is scheduled.

By default, a job doesn't have any prerequisites. Optionally, you can specify that a job can't be scheduled until one or more existing jobs have succeeded or failed. For more information, see [Schedule dependent jobs](https://docs.cloud.google.com/batch/docs/create-run-dependent-job) ([Preview](https://cloud.google.com/products/#product-launch-stages)).

  * **Job priority:** the priority for a job relative to the priorities of other jobs in your project.

You can optionally specify the priority of a job by including the [`--priority` flag for gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--priority) or the [`priority` JSON field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs). You can define the priority of a job as a number between `0` (lowest priority) and `99` (highest priority). Setting a higher priority can help a job to run sooner than lower-priority jobs in your project.

If you don't configure the priority of a job, it defaults to using the lowest priority, `0`. If two queued jobs have the same priority, the job that was created first has the higher priority.

  * **Job resource availability:** the availability of the job's required resources within the allowed locations.

Firstly, a job cannot run if you happen to specify any resources that aren't offered in that location—when this happens, the job fails with a [zone availability error](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#zone_availability).

Secondly, a job is more likely to be delayed or fail if any of its required resources are in low capacity relative to the current demand due to [resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability). As a result, your job might run sooner when you require fewer, more-common resources and don't restrict the job from running in any zones in a region.

For more information about the resources for a job, see Job execution in this document. For more information about the locations you can specify for a Batch job and its resources, see the [Locations](https://docs.cloud.google.com/batch/docs/locations) page.

  * **Quotas and limits:** the thresholds that your project has for Google Cloud resources and requests.

A job cannot run if it exceeds a limit or your project's quota for any of the required resources or requests. When this happens, Batch might delay a job and retry it at a later time or fail the job and display a related error.

You can help prevent delays and errors for your job by creating jobs that comply with all relevant limits and ensuring your project has enough relevant quota. For more information, see [Batch quotas and limits](https://docs.cloud.google.com/batch/quotas).




### Job execution

The time a job takes to be executed can vary based on task scheduling and the job's resources.

#### Task scheduling

When a job runs, its tasks are scheduled according to the [scheduling policy (`schedulingPolicy`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskGroup.FIELDS.scheduling_policy), which lets you specify one of the following options:

  * **As soon as possible (`AS_SOON_AS_POSSIBLE`) (default):** tasks run as soon as resources are available and can run in parallel. The amount of tasks that run at a time depends on the parallel tasks per VM allowed by the job's resources and other configuration options as explained in Job resources in this document.
  * **In order (`IN_ORDER`):** tasks run one at a time in increasing index order.



#### Job resources

Each Batch job runs on a regional managed instance group (MIG), which is a group of one or more matching Compute Engine virtual machine (VM) instances that are each located in one of the included zones. Each VM has dedicated hardware for CPU cores (specifically [virtual CPUs (vCPUs)](https://docs.cloud.google.com/compute/docs/cpu-platforms)) and memory—which affect the performance of your job—and a boot disk—which stores an operating system (OS) image and instructions for running your job.

During a job's run time, Batch automatically creates and deletes resources that meet your specifications. When you create a job, you configure its resources by specifying the following:

  * **Compute resources per task:** unless the default values are sufficient, you must specify the compute resources—vCPUs, memory, and (if required) extra boot disk storage—required for each task to run. For more information, see the [compute resources per task (`computeResource`) fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#ComputeResource).

  * **VM resources:** optionally, you can also specify the job's VMs—such as the machine type and OS, and additional resources such as GPUs and storage volumes—primarily by using the [VM resource policy (`instances[].policy`) fields](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicyOrTemplate) or the alternative `instances[].instanceTemplate` field. (Optionally, you can also use the `instanceFlexibilityPolicy` fields if you want to allow multiple machine types for a job.)

If you leave these fields undefined (which isn't possible when creating a job using the Google Cloud console), Batch automatically tries to select compatible VMs and doesn't add any additional resources.

**Important:** If you specify the VM resources for a job (any `instances[].policy`, `instances[].instanceTemplate`, or `instanceFlexibilityPolicy` field), you must ensure these fields are compatible with each other and the job. For example, do all the following:

    * Ensure all the VM resources that you specify are available in the location of your job's VMs. For more information, see the [Locations](https://docs.cloud.google.com/batch/docs/locations) page.
    * If you specify the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of the job's VMs, ensure that machine type has enough vCPUs and memory for the job's task requirements: each task's required vCPUs and memory (`cpuMilli` and `memoryMib` fields) fields and your preferred maximum parallel tasks per VM (`taskCountPerNode` field). Additionally, ensure that any additional resources that you specify, like disks and GPUs, are supported for the machine type.



The number of VMs and the number of tasks that can run simultaneously on each VM vary for different jobs based on the task scheduling and your specified hardware requirements. If you specify for a job's tasks to run `IN_ORDER`, the job has one VM and only runs one task at a time. Otherwise, if a job's tasks run `AS_SOON_AS_POSSIBLE`, then you can estimate the number of VMs and the number simultaneous tasks using the following formula: 

\\[{vmsPerJob}=\frac{taskCount}{parallelTasksPerVm}\\]

This formula has the following values:

  * \\({vmsPerJob}\\): the maximum number of VMs for a job. The actual amount of VMs created for a job might be smaller than this—for example, if Batch expects it's faster to run a job on fewer resources than to wait for more resources. This value is also limited by the [concurrent VMs per job limits](https://docs.cloud.google.com/batch/quotas#job_limits).
  * \\({taskCount}\\): the total number of tasks for the job, which you define using the [task count (`taskCount`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskGroup.FIELDS.task_count).
  * \\({parallelTasksPerVM}\\): the maximum number of tasks that can run on a VM simultaneously.

This value is determined by all of the following criteria:

    * The minimum value is 1 task.

    * The maximum value is the smaller of 20 tasks and, if defined, the value of the [max parallel tasks per job (`parallelism`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#taskgroup).

    * If the [maximum parallel tasks per VM (`taskCountPerNode`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#taskgroup) is defined, that value is used.

Otherwise, if `taskCountPerNode` is undefined, Batch decides a value by dividing the total number of compute resources—specifically vCPUs—per VM into the amount required for each task:

\\[{parallelTasksPerVm}=\frac{vcpusPerVm}{vcpusPerTask}\\]

This formula has the following values:

      * \\({vcpusPerVm}\\): the total number of vCPUs per VM, which is determined by the machine type of your job's VMs.

      * \\({vcpusPerTask}\\): the number of vCPUs per task, which is determined by converting the units of the [vCPUs per task (`cpuMilli`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#computeresource).




## Job creation options

[Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job) explains the fundamentals, including how to define a runnable using either a script or container image and how to configure predefined and custom environment variables.

After you understand the fundamentals for job creation, consider creating a job that uses one or more of the following additional configuration options:

**Important:** Some options for job creation are not available in the Google Cloud console. For details, see the documentation for each feature. For more features and flexibility for creating jobs, use the gcloud CLI or Batch API instead.

  * Control access for a job:

    * [Control access for a job using a custom service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account) explains how to specify a job's service account, which influences the resources and applications that a job's VMs can access. If you don't specify a custom service account, jobs default to using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

    * [Networking overview](https://docs.cloud.google.com/batch/docs/networking-overview) provides an overview of when and how you can customize the networking configuration for a job, including specifying the job's network, blocking external connections, and protecting data and resources by using VPC Service Controls.

    * [Protect sensitive data using Secret Manager](https://docs.cloud.google.com/batch/docs/create-run-job-secret-manager) explains how to securely define sensitive data, such as custom environment variables and login credentials, by using Secret Manager secrets to specify encrypted information when you create a job.

  * Configure additional options for a job:

    * [Configure task communication using an MPI library](https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library) explains how to configure a job with interdependent tasks that communicate with each other across different VMs by using a Message Passing Interface (MPI) library. A common use case for MPI is tightly coupled, high performance computing (HPC) workloads.

    * Customize the resources that a job runs on:

      * [Define job resources using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template) explains how to specify a Compute Engine VM template to define a job's resources when you create a job. This is an alternative to specifying a job's resources directly by using the [`instances[].policy` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#InstancePolicy).

      * [Use GPUs for a job](https://docs.cloud.google.com/batch/docs/create-run-job-gpus) explains how to define a job that uses one or more graphics processing units (GPUs). Common use cases for jobs that use GPUs include intensive data processing or machine learning (ML) workloads.

      * [Use storage volumes for a job](https://docs.cloud.google.com/batch/docs/create-run-job-storage) explains how to define a job that can access one or more external storage volumes. Storage options include new or existing persistent disks, new local SSDs, existing Cloud Storage buckets, and an existing network file system (NFS) such as a Filestore file share.

      * [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview) provides an overview of when and how you can customize the VM operating system (OS) environment for a job, including the job's VM OS image and boot disks.

    * Optimize various aspects of a job:

      * Improve monitoring and analysis:

        * [Write task logs](https://docs.cloud.google.com/batch/docs/write-task-logs) explains how to configure a job's runnables to write task logs. Writing task logs lets you surface custom information in Cloud Logging, which can help make jobs easier to analyze and troubleshoot.

        * [Configure custom status events](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events) explains how to configure custom status events for a job's runnables. Custom status events let you describe important events that happen for runnables and appear when you [view a job's history of status events](https://docs.cloud.google.com/batch/docs/view-status-events), which can help make jobs easier to analyze and troubleshoot.

        * [Enable status notifications](https://docs.cloud.google.com/batch/docs/enable-notifications) explains how you can configure a job to send Pub/Sub notifications about its status, which you can optionally store and query in a BigQuery table. Before reading this document, configure your project to [monitor job status using Pub/Sub notifications and BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications) first.

        * [Enable Ops Agent metrics](https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent) explains how to configure a job to automatically install the Ops Agent. The Ops Agent collects additional metrics about the performance and utilization of a job's resources. For more information about viewing and using resource metrics, see [Monitor and optimize job resources by viewing metrics](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

      * [Schedule dependent jobs](https://docs.cloud.google.com/batch/docs/create-run-dependent-job) ([Preview](https://cloud.google.com/products/#product-launch-stages)) explains how to specify a job that doesn't run until one or more existing dependency jobs have succeeded or failed. If you have a workload with varying resource requirements, you can reduce costs and quota usage by separating the types of VMs used for low-demand operations (like data preparation) and compute-intensive operations (like data processing).

      * [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries) explains how to automatically retry a job's tasks after all or specified failures. Automated retries can help reduce troubleshooting friction and the overall run time required for jobs that experience temporary errors. For example, use automatic retries for a job that runs on Spot VMs, which provide significant discounts but might not always be available and can be preempted at any time.

      * [Limit run times using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts) explains how to limit the amount of time that a task or runnable is permitted to run. By preventing excess run times, you might reduce unexpected costs and delays.

      * Improve resource obtainability:

        * [Improve resource obtainability](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview) explains what resource obtainability is and provides recommendations for how to improve obtainability when you create and run jobs.

        * [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation) explains how to configure a job that can run on reserved VMs. Using reserved VMs can help you minimize a job's scheduling time, prevent resource availability errors, and optimize costs.

        * [Improve obtainability by using instance flexibility](https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility) explains how to allow a job to run on multiple machine types that you specify and can rank. Using instance flexibility might help increase parallelism, delay preemption of Spot VMs, and prevent resource availability errors.

      * Reduce latency:

        * [Colocate VMs to reduce latency](https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy) explains how to reduce network latency between a job's VMs by requiring the VMs to be located physically close to each other. This performance benefit can be especially useful for jobs that have frequent network communications across VMs, such as tasks that communicate using MPI libraries.

        * [Use Image streaming](https://docs.cloud.google.com/batch/docs/use-image-streaming) explains how to improve job startup time by streaming container images from Artifact Registry.

  * Use additional services to create and run jobs:

    * [Orchestrate jobs using Workflows](https://docs.cloud.google.com/workflows/docs/tutorial-batch-and-workflows) explains how to use [Workflows](https://docs.cloud.google.com/workflows) to execute a job's tasks in an order that you define using the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax).

    * [Orchestrate jobs using Nextflow](https://docs.cloud.google.com/batch/docs/nextflow) explains how to run a Batch job through a [Nextflow](https://www.nextflow.io/) pipeline, which you can use to orchestrate bioinformatics workflows.

    * [Orchestrate jobs using dsub](https://docs.cloud.google.com/batch/docs/dsub) explains how to run a Batch job through a [`dsub`](https://github.com/databiosphere/dsub) pipeline, which you can use to orchestrate batch-processing workflows on Google Cloud services.

    * [Create and run Batch jobs using Terraform and Cloud Scheduler](https://docs.cloud.google.com/batch/docs/create-run-job-using-terraform-and-cloud-scheduler) explains how to incorporate Batch jobs into Terraform. [Terraform](https://registry.terraform.io/) lets you provision and manage infrastructure by specifying the preferred state in configuration files, which can be treated as code and stored in version control systems like GitHub.




## What's next

  * Learn the fundamentals of job creation:

    1. Optional: [Create and run an example job](https://docs.cloud.google.com/batch/docs/create-run-example-job).

    2. [Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
