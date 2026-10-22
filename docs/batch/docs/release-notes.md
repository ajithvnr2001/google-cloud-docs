---
url: https://docs.cloud.google.com/batch/docs/release-notes/
title: Batch release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:04.524221+00:00
---

# Batch release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Resources ](https://docs.cloud.google.com/batch/docs/resources)



Send feedback 

#  Batch release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Batch. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/batch-release-notes.xml) directly. 

## September 15, 2026

Issue

A workaround has been added for the known issue that [jobs might fail when specifying Compute Engine (or custom) VM OS images with outdated kernels](https://docs.cloud.google.com/batch/docs/known-issues#jobs-fail-specify-compute-images-outdated-kernels).

## August 19, 2026

Deprecated

The Batch Debian 11 operating system (OS) image family has reached end of development due to the [end of support (EOS) for Compute Engine Debian 11 images on August 31, 2026](https://docs.cloud.google.com/compute/docs/images/os-details#debian). The last Batch Debian 11 images—any image versions with the `batch-debian-11-official` prefix—are only supported until August 31, 2026. Before then, migrate any job that uses a Batch Debian 11 image to a Batch Debian 12 image (or other image) as follows:

  * For job definitions that use the `batch-debian` image prefix (which is the default image for jobs with any script runnables), the image that Batch automatically selects during job creation is gradually migrating to Debian 12 no later than August 31, 2026. For any jobs created before August 31, 2026, you can check whether the job uses Debian 11 or Debian 12 by describing the job.

  * For job definitions that specify either the `batch-debian-11-official` image family or an image version with that prefix, specify a different image during job creation. For example, to migrate to Debian 12, specify either the `batch-debian-12-official` image family or an image version with that prefix.




Learn more about [OS images](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview), [viewing OS images](https://docs.cloud.google.com/batch/docs/view-os-images), and [specifying OS images](https://docs.cloud.google.com/batch/docs/specify-vm-os-image).

## July 20, 2026

Breaking

Starting on the following dates, you can no longer create a job that locates its Compute Engine resources outside of the job's location.

  * For projects that have successfully submitted before July 31, 2026 at least one job that uses the `allowedLocations[]` field with any region or zones outside of the job's location, changes are starting on _June 30, 2027_.
  * For all other projects, changes are starting on _July 31, 2026_.



If none of your jobs specify the `allowedLocations[]` field, then no action is required. Otherwise, ensure that any region or zones specified in the `allowedLocations[]` field are in the same region as the job's location before these dates. For more information, see [Batch locations](https://docs.cloud.google.com/batch/docs/locations).

## July 17, 2026

Feature

[Instance flexibility](https://docs.cloud.google.com/batch/docs/create-run-job-instance-flexibility) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Instance flexibility lets you allow a job to run on multiple machine types that you specify and can optionally rank. Use instance flexibility to improve _obtainability_ —the probability that resources are available to run your job. For example, by allowing multiple machine types, you can reduce the probability of resource availability errors and try to obtain Spot VMs that are less likely to be preempted.

To get started, see [Improve resource obtainability for jobs](https://docs.cloud.google.com/batch/docs/improve-obtainability-overview).

## March 20, 2026

Feature

Flex-start VMs and calendar-mode reservations are generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Both consumption options use [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing), which offers discounts of up to 53% off of on-demand pricing. For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus) and [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation).

## October 30, 2025

Change

Dynamic Workload Scheduler for Batch ([Preview](https://cloud.google.com/products#product-launch-stages)) has been replaced with the following consumption options:

  * **Flex-start VMs ([Preview](https://cloud.google.com/products#product-launch-stages))**: We recommend Flex-start VMs if your job can withstand best-effort availability in exchange for discounted pricing and up to 7 days to finish running.

  * **Calendar-mode reservations ([Preview](https://cloud.google.com/products#product-launch-stages))**: We recommend calendar-mode reservations if your job needs a very high level of assurance of resource availability for at least 1 day and up to 90 days.




Both consumption options use [Dynamic Workload Scheduler pricing](https://cloud.google.com/products/dws/pricing), which offers discounts of up to 53% off of on-demand pricing. For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

Change

Documentation has been updated to clarify the [machine types that jobs can use](https://docs.cloud.google.com/batch/docs/get-started#machine-types).

## July 24, 2025

Issue

Pub/Sub might not send notifications for all intermediate states when a job or task changes very quickly. You can mitigate this issue by viewing state history through status events. For more information, see [Known issues](https://docs.cloud.google.com/batch/docs/known-issues#pubsub-missing-quick-states).

## March 10, 2025

Feature

[Cancelling jobs](https://docs.cloud.google.com/batch/docs/cancel-job) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## January 07, 2025

Feature

You can use the Google Cloud console to [create jobs that use GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

## November 14, 2024

Feature

[Dependent jobs](https://docs.cloud.google.com/batch/docs/create-run-dependent-job) are available in [Preview](https://cloud.google.com/products#product-launch-stages). Dependent jobs let you schedule an automated chain of jobs, which can help you optimize resource consumption—for example, separate the types of VMs used for data preparation and compute-intensive data processing.

## October 28, 2024

Feature

Dynamic Workload Scheduler for Batch is available in Preview. We recommend using Dynamic Workload Scheduler to improve resource availability for jobs that run on A3 GPU VMs when you don't intend to use a reservation. For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

## August 16, 2024

Change

Documentation has been added to explain how to export job information. Exporting a job's information is useful when you want to retain the information after a job is deleted or analyze the information outside of Batch. For more information, see [Export job information](https://docs.cloud.google.com/batch/docs/export-job-info).

## August 13, 2024

Change

The documentation has been updated to clarify that a Batch OS stops being supported when its base Compute Engine OS is deprecated. This restriction only applies to Batch OSes that have not already reached the end of development as of the date of this notice. 

For more information, see [Restrictions for VM OS images](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview#vm-os-image-restrictions).

Deprecated

Batch CentOS (`batch-centos`) and Batch HPC CentOS (`batch-hpc-centos`) have reached end of development due to the [end of support (EOS) of Compute Engine CentOS 7 images on June 30, 2024](https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance).

The final image versions of these Batch OSes—`batch-centos-7-official-20240628-00-p00` and `batch-hpc-centos-7-official-20240628-00-p00` from June 28, 2024—are only supported until August 27, 2024. By then, migrate any job that uses Batch CentOS or Batch HPC CentOS to a different OS.

Feature

[Cancel jobs](https://docs.cloud.google.com/batch/docs/cancel-job) is available in Preview.

## June 17, 2024

Change

Documentation has been added to explain how to view resource metrics for your jobs in Cloud Monitoring. The metrics provide resource utilization and performance information, which you can use to help optimize the performance and costs of future jobs. For more information, see [Monitor and optimize job resources by viewing metrics](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

Feature

You can configure a job to automatically install the Ops Agent, which provides additional resource metrics in Cloud Monitoring. For more information, see [Collect additional resource metrics using the Ops Agent](https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent).

## April 03, 2024

Issue

When a job fails due to exceeding a timeout, the job's logs don't indicate whether the failure was caused by the relevant task's timeout or the relevant runnable's timeout. For more information, including a workaround, see [Known issues](https://docs.cloud.google.com/batch/docs/known-issues#timeout).

Feature

You can set maximum time limits for tasks and runnables. For more information, see [Limit run times for tasks and runnables using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).

## February 22, 2024

Change

In the Google Cloud console, the **Job list** page has been updated to reduce latency. Although the console no longer summarizes the statuses of your jobs, you can filter based on job state when you [view a list of your jobs](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-jobs).

Fixed

Fixed the issue causing latency when listing jobs in projects that contain more than 10,000 jobs.

## February 01, 2024

Feature

You can configure custom status events, which describe important events for a job's runnables. By providing additional information about a job's progress, custom status events can help make a job easier to analyze and troubleshoot.

For more information, see [Configure custom status events to describe runnables](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events) and [View a job's history through status events](https://docs.cloud.google.com/batch/docs/view-status-events).

Feature

You can run Batch jobs as a non-root user to meet workload or security requirements. For more information, see [Create and run jobs as a non-root user](https://docs.cloud.google.com/batch/docs/non-root-job).

Feature

You can write unstructured and structured task logs:

  * An _unstructured task log_ lets you define a log's message.
  * A _structured task log_ lets you define multiple details for a log such as the message, the severity, custom fields, and a custom status event.



By allowing you to surface custom information in Cloud Logging, task logs can help make a job easier to analyze and troubleshoot.

For more information, see [Write task logs](https://docs.cloud.google.com/batch/docs/write-task-logs).

## January 25, 2024

Issue

Jobs that try to consume reserved VMs might be incorrectly delayed or prevented from running. For more information, including workarounds, see [Known issues](https://docs.cloud.google.com/batch/docs/known-issues#underestimated-reservations-quota).

## January 02, 2024

Change

The limit for concurrent VMs per job now varies based on the number of zones allowed for a job's VMs:

  * The limit for concurrent VMs per single-zone job remains 2,000.
  * The limit for concurrent VMs per multi-zone job has increased to 4,000.



Learn more about [Quotas and limits](https://docs.cloud.google.com/batch/quotas) and [Batch locations](https://docs.cloud.google.com/batch/docs/locations).

## December 21, 2023

Feature

You can use Image streaming to enable Batch jobs to initialize without waiting for a container image to finish downloading. For more information, see [Use Image streaming to reduce container startup time](https://docs.cloud.google.com/batch/docs/use-image-streaming).

## December 20, 2023

Breaking

Logs from Batch jobs created after December 19, 2023 will no longer use the general-purpose `generic_task` monitored resource type and instead use the new `batch.googleapis.com/Job` monitored resource type. The `batch.googleapis.com/Job` monitored resource type is specific to Batch, which makes it simpler to query Cloud Logging for logs only from Batch.

When querying Cloud Logging for logs from Batch, update any filters that require the `generic_task` monitored resource type to specify the `batch.googleapis.com/Job` monitored resource type accordingly. Alternatively, you can enable the [`use_generic_task_monitored_resource` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#CloudLoggingOption.FIELDS.use_generic_task_monitored_resource) for your jobs to continue using the `generic_task` monitored resource type instead.

For more information, see the documentation for [Cloud Logging monitored resources types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list) and [Batch job logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs).

## November 27, 2023

Change

Documentation has been added to explain how to configure jobs that can run on reserved VMs. Using reserved VMs helps minimize a job's scheduling time and prevent resource availability errors.

For more information, see [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation)

## November 08, 2023

Issue

You might experience latency when listing jobs in projects that contain more than 10,000 jobs. For more information, see [Known issues](https://docs.cloud.google.com/batch/docs/known-issues#latency).

Change

Documentation has been added to explain how to configure jobs to send status notifications using Pub/Sub and how to query those notifications using BigQuery.

For more information, see the following pages:

  1. To configure your project to support status notifications, see [Monitor job status using Pub/Sub notifications and BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications).

  2. To configure a job to send status notifications, see [Create and run a job that sends Pub/Sub status notifications](https://docs.cloud.google.com/batch/docs/enable-notifications).




## October 26, 2023

Change

Documentation has been added to explain how to run [`dsub`](https://github.com/databiosphere/dsub) pipelines on Batch. For more information, see [Orchestrate jobs by running dsub pipelines on Batch](https://docs.cloud.google.com/batch/docs/dsub).

## October 19, 2023

Change

Documentation has been added to explain how to colocate the VMs for a job by using a compact placement policy. For example, use compact placement policies to reduce the latency between VMs for jobs with tightly coupled tasks, such as tasks that communicate using MPI libraries.

For more information, see [Reduce latency by using compact placement policies](https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy).

## October 18, 2023

Change

Documentation has been added to explain how to securely reference sensitive data in a job by using Secret Manager secrets for encryption. For example, use secrets to protect sensitive data when defining custom environment variables or protect login credentials when accessing private container images from Docker Registry.

For more information, see [Protect sensitive data using Secret Manager with Batch](https://docs.cloud.google.com/batch/docs/create-run-job-secret-manager).

## October 09, 2023

Change

Job limits have increased to 100,000 tasks per task group and 5,000 parallel tasks per job. Learn more about [Quotas and limits](https://docs.cloud.google.com/batch/quotas).

## October 05, 2023

Feature

Batch is available in the following regions:

  * `australia-southeast2` (Melbourne)
  * `europe-west8` (Milan)
  * `europe-west12` (Turin)
  * `me-west1` (Tel Aviv)
  * `northamerica-northeast2` (Toronto)
  * `southamerica-east1` (São Paulo)
  * `us-east5` (Columbus)



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## September 19, 2023

Change

Documentation has been updated to reflect new default options for jobs that use GPUs:

  * Defining the machine type of the job's VMs is optional.
  * Jobs that use software from June 3, 2023 and later don't need to mount GPUs to containers.



For more information, see [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus).

## September 05, 2023

Change

Documentation has been added to explain how to automatically retry some or all of the failed tasks for a job. For example, automatic task retries can help prevent job failures from temporary issues like Spot VM preemption, host events, and transient networking errors.

For more information, see [Automate task retries](https://docs.cloud.google.com/batch/docs/automate-task-retries).

## August 29, 2023

Change

Documentation has been added to explain the VM OS environment for Batch. For a job's VMs, you can optionally configure the OS image and/or boot disk properties. Otherwise, a job uses the default configuration.

For more information, see the following pages:

  * [VM OS environment overview](https://docs.cloud.google.com/batch/docs/vm-os-environment-overview)
  * [Specify the VM OS image for a job](https://docs.cloud.google.com/batch/docs/specify-vm-os-image)
  * [Customize the boot disks for a job](https://docs.cloud.google.com/batch/docs/create-run-job-custom-boot-disks)
  * [View VM OS images for Batch](https://docs.cloud.google.com/batch/docs/view-os-images)
  * [Control access to VM OS images for Batch](https://docs.cloud.google.com/batch/docs/control-access-vm-os-images)



## August 25, 2023

Feature

Batch is available in the `europe-west10` (Berlin) region.

For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## August 22, 2023

Feature

Batch is available in the following regions:

  * `asia-south2` (Delhi)
  * `asia-southeast2` (Jakarta)
  * `europe-southwest1` (Madrid)
  * `me-central1` (Doha) 



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## August 17, 2023

Breaking

Batch is enforcing a 60-day retention policy for all finished (failed or succeeded) jobs:

  * Any existing jobs that have finished before August 17, 2023 are automatically deleted 60 days after, on October 16, 2023.

  * All new and existing jobs that are not yet finished on August 17, 2023 are automatically deleted 60 days after they finish running.




If you need to retain the information for a job for more than 60 days, you can export the job. For more information, see [Delete and export jobs](https://docs.cloud.google.com/batch/docs/delete-job).

## July 18, 2023

Feature

VPC Service Controls support for Batch is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

VPC Service Controls lets you create perimeters that protect the resources and data of Google Cloud services that you explicitly specify. For more information, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [Use VPC Service Controls with Batch](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls).

## July 17, 2023

Change

Documentation has been added for Cloud Life Sciences users to explain how to migrate to Batch. For more information, see [Migrate to Batch from Cloud Life Sciences](https://docs.cloud.google.com/batch/docs/migrate-to-batch-from-cloud-life-sciences).

## July 08, 2023

Change

Documentation has been added to explain how to apply labels to a Batch job and its resources. Labels are key-value pairs that can be used to group and organize Batch and Compute Engine resources. For more information, see [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).

## July 07, 2023

Feature

Batch is available in the following regions:

  * `asia-northeast2` (Osaka)
  * `asia-northeast3` (Seoul)
  * `australia-southeast1` (Sydney)
  * `europe-west1` (Belgium)
  * `europe-west9` (Paris)



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## July 03, 2023

Feature

Samples in C++ are available for Batch. Documentation has been updated to include the following samples:

  * [Create a basic container job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-container-job)
  * [Create a basic script job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-script)
  * [Create and run a job that uses storage volumes](https://docs.cloud.google.com/batch/docs/create-run-job-storage#c++)
  * [Define job resources using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template#c++)
  * [Delete a job](https://docs.cloud.google.com/batch/docs/delete-job#c++)
  * [View a list of your jobs](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-jobs)
  * [View the details of a job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-job)
  * [View a list of a job's tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-tasks)
  * [View the details of a task](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-task)
  * [View logs for a job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#c++)



For more information, see [All Batch code samples](https://docs.cloud.google.com/batch/docs/samples).

## June 20, 2023

Feature

Cloud Client Libraries for C++ are available for the Batch API. For more information, see the [reference documentation](https://docs.cloud.google.com/cpp/docs/reference/batch/latest).

## June 05, 2023

Feature

Batch is available in the following regions:

  * `asia-east2` (Hong Kong)
  * `europe-central2` (Warsaw)
  * `us-south1` (Dallas)
  * `us-west2` (Los Angeles)
  * `us-west3` (Salt Lake City)
  * `us-west4` (Las Vegas)



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## May 22, 2023

Change

Documentation has been added to explain how to use Terraform to run a Cloud Scheduler cron job that creates Batch jobs. For more information, see [Create and run Batch jobs using Terraform and Cloud Scheduler](https://docs.cloud.google.com/batch/docs/create-run-job-using-terraform-and-cloud-scheduler).

## May 17, 2023

Feature

**[Preview](https://cloud.google.com/products#product-launch-stages)** : Integrate a job into a workflow using the [Batch API connector for Workflows](https://docs.cloud.google.com/workflows/docs/reference/googleapis/batch/Overview).

## May 09, 2023

Change

Documentation has been added to explain how to run [Nextflow](https://www.nextflow.io/) pipelines on Batch. For more information, see [Orchestrate jobs by running Nextflow pipelines on Batch](https://docs.cloud.google.com/batch/docs/nextflow).

## April 27, 2023

Change

Documentation has been added for an overview page that summarizes Batch content including pages, code samples, and videos. For more information, see [Overview](https://docs.cloud.google.com/batch/docs).

## April 13, 2023

Change

Documentation for pricing has been added to explain how you can visualize the costs associated with your Batch jobs by using Cloud Billing reports. For more information, see [Pricing](https://cloud.google.com/batch/pricing).

## April 12, 2023

Change

Documentation has been added to explain networking concepts and how to configure networking for Batch. For more information, see the following pages:

  * [Networking overview](https://docs.cloud.google.com/batch/docs/networking-overview)
  * [Specify the network for a job](https://docs.cloud.google.com/batch/docs/specify-job-network)
  * [Block external access for a job](https://docs.cloud.google.com/batch/docs/job-without-external-access)
  * [Use VPC Service Controls](https://docs.cloud.google.com/batch/docs/use-vpc-service-controls)



## April 11, 2023

Feature

Batch is available in the following regions:

  * `asia-northeast1` (Tokyo)
  * `europe-west4` (Netherlands)



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## March 13, 2023

Change

In the Google Cloud console, the **Job details** page has been updated to include an **Events** tab, which lists the job's [status events](https://docs.cloud.google.com/batch/docs/reference/rest/v1/StatusEvent) and contains a link to the job's logs. 

To view the **Events** tab, follow the steps to [describe a job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-job) using the console.

## March 06, 2023

Feature

Batch is available in the following regions:

  * `asia-south1` (Mumbai)
  * `asia-east1` (Taiwan)
  * `europe-west3` (Frankfurt)
  * `southamerica-west1` (Santiago)
  * `us-east4` (Northern Virginia)



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## February 15, 2023

Change

The documentation for how to create and run a job has been split into the following pages:

  * [Job creation and execution overview](https://docs.cloud.google.com/batch/docs/create-run-job)
  * [Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job)
  * Create and run advanced jobs 
    * [Define job resources using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template)
    * [Control access for a job using a custom service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account)
    * [Configure task communication using an MPI library](https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library)
    * [Create and run a job that uses GPUs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus)
    * [Create and run a job that uses storage volumes](https://docs.cloud.google.com/batch/docs/create-run-job-storage)



## February 02, 2023

Change

Documentation has been updated to include new samples. The following samples are available in Java:

  * [Create and submit a job using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-instance-template)
  * [Create and submit a job that uses a Cloud Storage bucket](https://docs.cloud.google.com/batch/docs/create-run-job#use-bucket)
  * [List tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-tasks)
  * [Describe a task](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-task)
  * [View logs from Cloud Logging for a job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs)



For more information, see [All Batch code samples](https://docs.cloud.google.com/batch/docs/samples).

## January 17, 2023

Feature

Batch is available in the following regions:

  * `northamerica-northeast1` (Montréal)
  * `europe-west2` (London)



For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## December 22, 2022

Change

Documentation has been updated to include new samples. The following samples are available in Go, Node.js, and Python:

  * [Create and submit a job using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-instance-template)
  * [Create and submit a job that uses a Cloud Storage bucket](https://docs.cloud.google.com/batch/docs/create-run-job#use-bucket)
  * [List tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-tasks)
  * [Describe a task](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-task)



The following sample is available in Go and Python:

  * [View logs from Cloud Logging for a job](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs#view-job-logs)



For more information, see [All Batch code samples](https://docs.cloud.google.com/batch/docs/samples).

## December 15, 2022

Feature

**Preview:** Batch supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), which lets you create perimeters that protect the resources and data of Google Cloud services that you explicitly specify. For more information about using VPC Service Controls with Batch, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_batch).

Change

Any job can use a [custom machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types). (Before, you could only use custom machine types by [creating a job from a Compute Engine instance template](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types).)

## October 21, 2022

Feature

Samples in Go are available for Batch. Documentation has been updated to include the following samples:

  * [Create a basic container job](https://docs.cloud.google.com/batch/docs/create-run-job#create-basic-container-job)
  * [Create a basic script job](https://docs.cloud.google.com/batch/docs/create-run-job#create-basic-script)
  * [List jobs](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-jobs)
  * [Describe a job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-job)
  * [Delete a job](https://docs.cloud.google.com/batch/docs/delete-job#delete_a_job)



For more information, see [All Batch code samples](https://docs.cloud.google.com/batch/docs/samples).

## October 12, 2022

Feature

Samples in Java, Node.js, and Python are available for Batch. Documentation has been updated to include the following samples:

  * [Create a basic container job](https://docs.cloud.google.com/batch/docs/create-run-job#create-basic-container-job)
  * [Create a basic script job](https://docs.cloud.google.com/batch/docs/create-run-job#create-basic-script)
  * [List jobs](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#list-jobs)
  * [Describe a job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-job)
  * [Delete a job](https://docs.cloud.google.com/batch/docs/delete-job#delete_a_job)



For more information, see [All Batch code samples](https://docs.cloud.google.com/batch/docs/samples).

## October 11, 2022

Announcement

**Batch is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).** Batch jobs can be created in the supported [locations](https://docs.cloud.google.com/batch/docs/locations) and resources can be created in any location supported by Compute Engine. With this release the Terms of Service in the [Cloud Services Summary](https://cloud.google.com/terms/services) fully apply.

The release includes additional capabilities such as support for [user-defined service accounts](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-service-account), [VPC Service Control](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_batch), and [HIPAA compliance](https://cloud.google.com/security/compliance/hipaa-compliance).

The documentation has been updated to include the following new content:

  * Create a job that uses [environment variables](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-environment-variables), [a custom service account](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-service-account), [Message Passing Interface (MPI)](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-uses-mpi), [GPUs](https://docs.cloud.google.com/batch/docs/create-run-job#create-job-gpu), or [storage](https://docs.cloud.google.com/batch/docs/create-run-job-storage).

  * [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting)

  * [Get support](https://docs.cloud.google.com/batch/docs/get-started#get-support)




## October 03, 2022

Breaking

Starting today, to submit a job, you must also have the Service Account User (`roles/iam.serviceAccountUser`) IAM role on the service account used by a job. For details, see [the permissions required to submit a job](https://docs.cloud.google.com/batch/docs/create-run-job#before-you-begin).

Change

The new Batch Job Editor (`roles/batch.jobsEditor`) IAM role is intended to replace the existing Batch Job Administrator (`roles/batch.jobsAdmin`) role. Although the Batch Job Administrator role currently still has the same permissions as the Batch Job Editor role, you can now only grant users the Batch Job Editor role. Additionally, it is recommended to update any existing users with the Batch Job Administrator role to have the Batch Job Editor role instead. For more information about IAM roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## September 21, 2022

Change

The [Quotas and limits](https://docs.cloud.google.com/batch/quotas) are now documented for Batch.

## September 14, 2022

Feature

**Preview** : Data Access audit logs are now available for Batch. For more information, see [Batch audit logging information](https://docs.cloud.google.com/batch/docs/audit-logging).

## September 12, 2022

Change

The documentation page [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) has been rewritten. Information that was previously on that page has been relocated to the following new pages:

  * [Batch locations](https://docs.cloud.google.com/batch/docs/locations)
  * [Authenticate to Batch](https://docs.cloud.google.com/batch/docs/authentication)
  * [Create and run a job](https://docs.cloud.google.com/batch/docs/create-run-job)
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks)
  * [Analyze a job using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs)
  * [Delete a job](https://docs.cloud.google.com/batch/docs/delete-job)



## September 07, 2022

Feature

Batch is now available in the following regions: `asia-southeast1` and `europe-west6`. For more information, see [Locations](https://docs.cloud.google.com/batch/docs/locations).

## July 13, 2022

Announcement

Batch is now available in [Preview](https://cloud.google.com/products#product-launch-stages)! For more information about using Batch, see the [documentation](https://docs.cloud.google.com/batch/docs/quickstart).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
