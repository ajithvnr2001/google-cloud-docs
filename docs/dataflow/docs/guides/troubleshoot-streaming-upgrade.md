---
url: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-upgrade/
title: Troubleshoot Streaming pipeline upgrades \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:58.237689+00:00
---

# Troubleshoot Streaming pipeline upgrades  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Troubleshoot Streaming pipeline upgrades Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with upgrading Dataflow streaming pipelines using features such as a [parallel replace job](https://docs.cloud.google.com/dataflow/docs/guides/upgrade-guide).

## Parallel replace jobs

Use the following guidance when you get errors running a parallel replace job to upgrade a pipeline.

### Missing required option `parallel_replace_job_min_parallel_pipelines_duration`

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job requires you to set the parallel_replace_job_min_parallel_pipelines_duration field. Set the field and try your request again.
    

This issue occurs when `parallel_replace_job_name` or `parallel_replace_job_id` is set, but `parallel_replace_job_min_parallel_pipelines_duration` is not.

To resolve this issue, set the `parallel_replace_job_min_parallel_pipelines_duration` option along with the `parallel_replace_job_name` or the `parallel_replace_job_id` option.

### Missing one of required option `parallel_replace_job_name` or `parallel_replace_job_id`

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job requires you to set either the parallel_replace_job_id field or the parallel_replace_job_name field. Set one of these fields, then try your request again.
    

This issue occurs when `parallel_replace_job_min_parallel_pipelines_duration` is set, but neither `parallel_replace_job_name` nor `parallel_replace_job_id` is set.

To resolve this issue, set the `parallel_replace_job_name` or the `parallel_replace_job_id` option along with `parallel_replace_job_min_parallel_pipelines_duration`.

### Invalid duration value for option `parallel_replace_job_min_parallel_pipelines_duration`

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    An invalid duration string VALUE is set for `parallel_replace_job_min_parallel_pipelines_duration`. Set a valid duration string, such as 10s, 1m, or 1h. but not longer than 31 days.
    

This issue occurs because the provided duration value is invalid.

To resolve this issue, set a valid duration string in the `<value><unit>` format, such as `10s`, `1m`, or `1h`. The duration must be between zero and 31 days.

### Parallel replace jobs are only supported for Streaming Engine

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    Parallel replace job is only supported for Streaming Engine. To enable Streaming Engine follow the instructions at https://cloud.google.com/dataflow/docs/streaming-engine#use
    

This issue occurs because Streaming Engine is not enabled for the new job.

To resolve this issue, [enable Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine#use) and rerun the job.

### The parallel replace job ID was not found

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job id JOB_ID was not found.
    

This issue occurs if an invalid job ID is set or if the original job has been purged from the system.

To resolve this issue, make sure a valid, running job ID is used for the `parallel_replace_job_id` option. If the original job has already been terminated, remove the parallel job update options and create a normal new job.

### The parallel replace job name was not found

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job name JOB_NAME was not found.
    

This issue occurs if an invalid job name is set or if the original job has been purged from the system.

To resolve this issue, make sure a valid, running job name is used for the `parallel_replace_job_name` option. If the original job has already been terminated, remove the parallel job update options and create a normal new job.

### Parallel replace job points to a non-active job

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job JOB_ID is not in a active state.
    

This issue occurs because the job being replaced is not an active job.

To resolve this issue, make sure that `parallel_replace_job_name` or `parallel_replace_job_id` point to a valid, running streaming job. If the old job is already terminated, remove the parallel job update options and create a normal new job.

### Parallel replace job points to a batch job

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job must be a streaming job.
    

This issue occurs because the job being replaced is not a streaming job.

To resolve this issue, make sure `parallel_replace_job_name` or `parallel_replace_job_id` points to a running streaming job, not a batch job.

### Parallel replace job options point to different jobs

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel replace job id JOB_ID must point to a job with name JOB_NAME.
    

This issue occurs because the `parallel_replace_job_name` and `parallel_replace_job_id` options point to different jobs.

To resolve this issue, if you use both options, make sure they point to the same running streaming job. Alternatively, use only one of the options, either `parallel_replace_job_name` or `parallel_replace_job_id`.

### Missing max stop duration when cancel on drain timeout is enabled

When you try to run a parallel replace job, the job is rejected with the following error:
    
    
    The parallel_replace_job_cancel_on_drain_timeout service option requires you to set the parallel_replace_job_max_stop_duration service option. Set the parallel_replace_job_max_stop_duration field and try your request again.
    

This issue occurs because the `parallel_replace_job_cancel_on_drain_timeout` option is set to `true`, but the `parallel_replace_job_max_stop_duration` option is not configured.

To resolve this issue, set the `parallel_replace_job_max_stop_duration` option to a valid duration, or remove `parallel_replace_job_cancel_on_drain_timeout`.

### The replacement job started too soon after the previous job

When you try to run a parallel replace job using the same job name, the job is rejected with the following error:
    
    
    The new parallel replace job must start after <var>min_duration</var> from the start of the previous job <var>old_job_id</var>. The current gap has the duration <var>gap_between_job</var>.
    

This issue occurs when you update a job using the same job name (Option 1) and the new replacement job starts within two minutes of the start of the previous job. Dataflow enforces this two-minute minimum gap to prevent duplicate parallel updates that could occur due to repeated client library retries or stale RPCs.

To resolve this issue, wait at least two minutes after the start of the previous job before initiating the update.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
