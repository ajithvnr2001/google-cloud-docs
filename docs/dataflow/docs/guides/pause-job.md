---
url: https://docs.cloud.google.com/dataflow/docs/guides/pause-job/
title: Pause a Dataflow job \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:14.207321+00:00
---

# Pause a Dataflow job  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/pause-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Pause a Dataflow job Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is supported for batch pipeline jobs only.

Use the pause-on-failure service option to preserve the state of your Dataflow batch jobs. This feature lets you pause job execution, address issues that are external to the pipeline, and resume processing without losing completed work. When a job is paused using this feature, you can't change pipeline code or worker VM configurations, like machine type.

By enabling this capability, you can better manage resource costs and improve job reliability during temporary outages or quota constraints. You can further maintain control over your pipeline lifecycle by configuring maximum pause durations when you enable pause-on-failure. You can also manually pause or resume pipelines that have the pause-on-failure flag enabled.

## Benefits of pause-on-failure

The pause-on-failure service option lets you preserve batch job progress during interruptions, reducing total compute time and resource expenditure.

  * **Checkpoint retention:** When a job fails, you can resume it from the last recorded checkpoint rather than restarting from the beginning. This avoids the need to re-process completed data blocks, which means you don't have to pay to redo work that was successfully completed.
  * **Mitigate external dependencies:** Protect your pipelines from transient issues, such as temporary outages or rate limits in external services. Pausing the job gives you the opportunity to address the root cause before resuming execution without losing completed work.
  * **Handle non-deterministic failures:** For workloads prone to intermittent or non-deterministic failures, this option lets you secure incremental progress on each sequential attempt, preventing total job failure.
  * **Manage resources and quota:** Pause lower-priority batch jobs to temporarily free up quota or reallocate high-value resources, such as GPUs or TPUs, to urgent workloads like machine learning model training or inference without losing their baseline progress.



## Support and limitations

Pausing a job (manually or on failure) has the following requirements and limitations:

  * The Dataflow job must be a batch job.
  * The job must use [Dataflow shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch).
  * You must specify the [`pause_on_failure`](https://docs.cloud.google.com/dataflow/docs/reference/service-options) service option when you [run the job](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline).
  * The job must not have previously failed to pause.
  * The contents of the job's temporary directory must not be deleted while the job is paused.



## Pause-on-failure job behavior

When you enable the pause-on-failure feature, your job automatically pauses after a work item fails four times. These failures are identified in your logs as job messages containing `Error message from worker` and worker messages containing `Completed work item ITEM_NUMBER UNSUCCESSFULLY`. Other types of failures, such as stockouts and quota errors, don't trigger an automatic pause. Instead, these failures cause the job to fail as normal. Enabling pause-on-failure also lets you manually pause a job.

### Job state transitions

When a Dataflow job pauses, it moves through the following states:

  1. **Pausing** : An intermediate state where the job halts processing, deletes your worker VMs, and archives backend state. You are still billed for the VMs until the service finishes deleting them.
  2. **Paused** : The job is fully halted. At this point, you are only billed for [archived Shuffle data](https://cloud.google.com/skus?filter=Shuffle%20Data%20Archived).



### Exceptional behaviors

Pause-on-failure might behave unexpectedly in the following scenarios:

  * If you manually pause a job that is close to completion, the job might complete instead of pausing.
  * In rare circumstances, a job might fail to pause. In these cases, the job returns to a running state if you manually paused it, or the job enters a failed state if the job is pausing due to an error.



### Resuming processing

When the job resumes, the service handles work items as follows:

  * **Completed work** : The service doesn't reprocess any stages or work items that were fully finished when the job paused.
  * **In-progress work** : Any work items that were in-progress when the job paused are reprocessed from the beginning.
  * **Failure counts** : All work item failure counts are reset to zero, which means your job won't automatically pause again until a work item fails an additional four times.



## Enable pause-on-failure

To enable pause-on-failure for your job, use the `pause_on_failure` Dataflow service option when you run your job.

###  Java 

`--dataflowServiceOptions=**pause_on_failure**`

###  Python 

`--dataflow_service_options=**pause_on_failure**`

###  Go 

`--dataflow_service_options=**pause_on_failure**`

### Specify a maximum pause duration

By default, your job will remain paused for up to 7 days (`7d`). You can manually configure this maximum pause duration to be between 1 hour (`1h`) and 7 days (`7d`).

Only `d` (days) and `h` (hours) are supported. A day is defined as 24 hours. This might not match the length of a calendar day because of factors like daylight saving time.

If the maximum pause duration passes, your job will be cancelled within the next hour. After the job is cancelled, you can't resume the job.

For example, the following example sets the maximum pause duration to 1 day:

###  Java 

`--dataflowServiceOptions=**pause_on_failure=pause_duration:1d**`

###  Python 

`--dataflow_service_options=**pause_on_failure=pause_duration:1d**`

###  Go 

`--dataflow_service_options=**pause_on_failure=pause_duration:1d**`

## Manually pause a Dataflow job

To manually pause a job, perform the following steps.

### Console

  1. Go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click the job that you want to pause.

To pause a job, the status of the job must be **running**.

  3. In the job details page, click **Pause**.

If you don't see the Pause button, your job can't be paused due to the pause-on-failure limitations.




### gcloud

To pause a Dataflow job, you can use the [`gcloud dataflow jobs` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs) in the Cloud Shell or a local terminal installed with the gcloud CLI.

  1. Open your shell.

  2. List the job IDs for the Dataflow jobs that are running, and then note the job ID for the job that you want to pause:
         
         gcloud dataflow jobs list
         

If you don't set the `--region` flag, Dataflow jobs from all available regions are displayed.

  3. Execute the following:
         
         gcloud dataflow jobs pause JOB_ID --region=REGION
         

Replace JOB_ID with the job ID you noted and REGION with the job region.




### API

To pause a job using the [Dataflow REST API](https://docs.cloud.google.com/dataflow/docs/reference/rest), use the [`projects.locations.jobs.update`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/update) endpoint, and pass the following request body:
    
    
    {
      "requestedState": "JOB_STATE_PAUSING"
    }
    

**Important** : Don't accidentally pass `JOB_STATE_PAUS**ED**` as the `requestedState`.

## Cancel a pausing or paused Dataflow job

You can [cancel](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline#stop-job) a pausing or paused Dataflow job as normal. After you cancel a job, you are no longer billed for it, but the job can no longer be resumed.

A paused job is automatically cancelled after its maximum pause duration expires.

## Resume a Dataflow job

To manually resume your paused job, follow these steps:

### Console

  1. Go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow)

  2. Click the job that you want to resume.

To resume a job, the status of the job must be **paused** (not **pausing**).

  3. In the job details page, click **Resume**.




### gcloud

To resume a Dataflow job, you can use the [`gcloud dataflow jobs` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list) in the Cloud Shell or a local terminal installed with the gcloud CLI.

  1. Open your shell.

  2. List the job IDs for the Dataflow jobs that are paused, and then note the job ID for the job that you want to resume:
         
         gcloud dataflow jobs list
         

If you don't set the `--region` flag, Dataflow jobs from all available regions are displayed.

  3. Execute the following:
         
         gcloud dataflow jobs resume JOB_ID --region=REGION
         

Replace JOB_ID with the job ID and REGION with the job region.




### API

To resume a job using the [Dataflow REST API](https://docs.cloud.google.com/dataflow/docs/reference/rest), use the [`projects.locations.jobs.update`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/update) endpoint, and pass the following request body:
    
    
    {
      "requestedState": "JOB_STATE_RUNNING"
    }
    

## What's next

  * Learn about [stopping a running pipeline](https://docs.cloud.google.com/dataflow/docs/guides/stopping-a-pipeline).
  * Understand [Dataflow Shuffle for batch jobs](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch), which is required to use this feature.
  * See the [Troubleshoot pipelines](https://docs.cloud.google.com/dataflow/docs/guides/troubleshooting-your-pipeline) guide to resolve errors.
  * Learn how to [troubleshoot slow or stuck batch jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-batch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
