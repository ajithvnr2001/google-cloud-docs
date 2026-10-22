---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/understanding-training-service/
title: Understand the serverless training service \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:44.364881+00:00
---

# Understand the serverless training service  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/understanding-training-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Understand the serverless training service Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the state of a training cluster through the lifecycle of a training job, and how Agent Platform handles training errors. You can use this information to adapt your training code accordingly.

## Lifecycle of a training job

This section explains how Agent Platform handles worker VMs through the lifecycle of a training job.

### Queue a new job

When you create a `CustomJob` or `HyperparameterTuningJob`, the job might remain in the [`JOB_STATE_QUEUED` state](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/JobState) for some time before Agent Platform runs it. This period is usually brief, but if your Google Cloud project does not have sufficient remaining [custom training quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/quotas#training) for your job, then Agent Platform keeps the job queued until you have sufficient quotas.

### Start workers in parallel

When a training job starts, Agent Platform schedules as many workers as possible in a short amount of time. As a result, workers may start up in parallel instead of sequentially. In order to reduce startup latency, Agent Platform starts running your code on each worker as soon as it becomes available. When all the workers are available, Agent Platform sets the job state to `JOB_STATE_RUNNING`.

In most cases, your machine learning framework automatically handles the workers starting in parallel. If you're using a distribution strategy in your training code, you may need to adjust it manually to handle workers starting in parallel. Learn more about distribution strategies in [TensorFlow](https://www.tensorflow.org/guide/distributed_training) and in [PyTorch](https://pytorch.org/tutorials/intermediate/dist_tuto.html).

### Restart workers during the training job

During a training job, Agent Platform can restart your workers from any worker pool with the same hostname. This can occur for the following reasons:

  * _VM maintenance_ : When the VM running a worker is subjected to VM maintenance, Agent Platform restarts the worker on another VM. Learn more about [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration) for VM maintenance.
  * _Non-zero exits_ : If any worker exits with a non-zero exit code, Agent Platform restarts that worker immediately in the same VM.

    * If a worker fails due to a common error, it is treated as a _permanent error_ , and Agent Platform shuts down the entire job. If any containers restart before Agent Platform shuts down the entire job, these containers may produce logs in Cloud Logging.
    * If a worker fails due to a _non-permanent error_ (any error not listed in the common errors), Agent Platform allows the restarted worker to continue running, with up to five restarts per worker. After five restarts, if a worker fails again, Agent Platform retries the entire job up to three times before failing the entire job.



To handle worker restarts in your training code, save checkpoints regularly during training so that you can restore from checkpoints when a worker restarts. If you expect training to take more than four hours, we recommend that you save a checkpoint at least once every four hours. Learn how to use training checkpoints in [TensorFlow](https://www.tensorflow.org/guide/checkpoint) and in [PyTorch](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html).

### Successfully completing a job

A training job completes successfully when its primary replica exits with exit code 0. At that point, Agent Platform shuts down all the other running workers.

## How Agent Platform handles training job errors

This section explains how Agent Platform handles common training job errors and internal errors.

About one minute after a job ends, Agent Platform sets the error code on the training job object, based on the exit code.

### Handle common errors

Agent Platform shuts down all workers if it encounters any of the following issues:

**Error Type** | **Error Message/Log** | **Note**  
---|---|---  
User code exception | The replica REPLICA_NAME exited with a non-zero status of EXIT_CODE. Termination reason: REASON.  | If the job encountered exit codes that could be transient, Agent Platform tries to restart the job up to three times. The potentially transient error codes that prompt Agent Platform to retry the job include the following: 

  * `SIGABRT`
    * `ExitCode 6`
    * `ExitCode 134` (custom containers)
  * `SIGSEGV`
    * `ExitCode 11`
    * `ExitCode 139` (custom containers)

  
Out-of-memory | The replica REPLICA_NAME ran out of memory and exited with a non-zero status of EXIT_CODE.  |  GKE reserves memory on Agent Platform nodes. On the smallest machine types (such as `n1-standard-4`), Agent Platform system agents can take up to 40% of total memory. For larger VMs, the overhead is relatively small. Compare [ allocatable memory for `n1-standard` machine types](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#memory_cpu).   
Insufficient capacity in your region (Compute Engine stockout) | Resources are insufficient in region: REGION_NAME. Try a different region or use a different accelerator.  | A _stockout_ happens when Compute Engine is at capacity for your selected CPU or GPU in your region. It is unrelated to your project quota. When this happens, Agent Platform attempts to restart the job up to three times.   
  
For jobs running on A2 and A3 VMs, Dynamic Workload Scheduler lets you schedule jobs that run when the requested GPU resources become available, rather than failing with a stockout error. For more information, see [Schedule training jobs based on resource availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/schedule-jobs-dws).   
  
### Handle internal errors

If Agent Platform has an internal error, it attempts to restart a job twice (three attempts in total). If the restart attempts also fail, Agent Platform returns an internal error with the message: `Internal error occurred for the current attempt`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
