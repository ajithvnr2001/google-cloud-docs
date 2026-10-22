---
url: https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout/
title: Manage rollouts \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:47.090330+00:00
---

# Manage rollouts  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deployment-strategies/manage-rollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Manage rollouts Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Deploy rollout includes phases. A phase is an ordered, logical grouping of jobs to do in a rollout.

Each phase includes jobs, which are the actions to take in each phase (for example, `deploy` or `verify`). And each job can have zero or more job runs. A job run is an instance of a job. If the job hasn't run, there are no job runs.

This document describes [phases](https://docs.cloud.google.com/deploy/docs/terminology#phase), [jobs](https://docs.cloud.google.com/deploy/docs/terminology#job), and [job runs](https://docs.cloud.google.com/deploy/docs/terminology#job_runs), and how to manage them.

## Structure of a rollout

A rollout is a Cloud Deploy resource that associates a [release](https://docs.cloud.google.com/deploy/docs/terminology#release) with a [target](https://docs.cloud.google.com/deploy/docs/terminology#target). 

### Phases

A rollout consists of one or more [phases](https://docs.cloud.google.com/deploy/docs/terminology#phase).

For a [standard](https://docs.cloud.google.com/deploy/docs/deployment-strategies) deployment strategy, there is only one phase: `stable`.

For a [canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary) deployment strategy, There is a separate phase for each configured percentage. For example, if you configure a canary that deploys 25%, then 50%, then 100%, there will be three phases:

  * `canary-25`
  * `canary-50`
  * `stable`



These phase names are standard: `canary-[PERCENTAGE]` for canary stages, and `stable` for the 100% phase. However, if you configure a [custom-automated canary or custom canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#types_of_canary), you can control the phase names.

### Jobs and job runs

Each rollout phase includes one or more jobs.

For a rollout in a [standard](https://docs.cloud.google.com/deploy/docs/deployment-strategies) deployment strategy, with no deployment verification enabled, there is one phase (`stable`).

For a canary rollout, there will be a phase for each part of the canary (for example, `canary-25`, `canary-50`, `stable`), and for each phase there is a `deploy` job. If verification is enabled, there is also a `verify` job for each phase.

A job run is an instance of a job. For example, a job run for a `deploy` job is executed, and if it succeeds, there is no further job run for that job. If it fails, it can be retried as another job run.

## Skipping phases the first time

Some deployment strategies (for example, canary) apportion traffic between the old and new versions. If you're deploying to a target for the first time, there's no old version, so we can't apportion the traffic.

For this reason, when you deploy a canary for the first time, we skip the canary phase or phases and run the `stable` phase. After that, the application is deployed, and future canary deployments will include the canary phases.

In a real-world situation, you will usually execute a canary deployment where your application is already running, so this phase skipping will be rare.

## States within a rollout

Rollouts, phases, jobs, and job runs all have states. This section describes the states for each.

### Rollout states

A rollout will have one of the following states:

  * `APPROVAL_REJECTED`

The rollout [required approval](https://docs.cloud.google.com/deploy/docs/promote-release#require_approval), but the approval was rejected.

  * `CANCELLED`

The terminal state for rollouts that have been canceled by a user.

  * `CANCELLING`

A user has canceled the rollout, but the cancellation has not finished processing.

  * `HALTED`

In a [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel), if one or more child rollouts fail, but at least one child rollout succeeds, the [controller](https://docs.cloud.google.com/deploy/docs/terminology#controller_rollout) rollout is HALTED if there are more phases after the current one.

You can resume a halted controller rollout by doing any of the following:

    * Cancel the controller rollout

    * Retry or ignore any failed jobs on child rollouts

  * `IN_PROGRESS`

A job run is processing.

  * `FAILED`

A job failed, and the user didn't choose to ignore the failure.

  * `PENDING`

The rollout has not begun processing. This state transitions to `IN_PROGRESS` or `CANCELED`.

  * `PENDING_APPROVAL`

The rollout [requires approval](https://docs.cloud.google.com/deploy/docs/promote-release#require_approval), but has not yet been approved.

  * `PENDING_RELEASE`

The rollout is waiting for the [release to be rendered](https://docs.cloud.google.com/deploy/docs/architecture#how_they_fit_together_to_deliver_your_release).

  * `SUCCEEDED`

The rollout has finished, with no failures.




### Phase states

A phase will have one of the following states:

  * `PENDING`

The phase is waiting for another phase in the rollout to finish.

  * `IN_PROGRESS`

The phase has started.

  * `SUCCEEDED`

The phase completed successfully.

  * `FAILED`

A job in the phase failed, and the user didn't choose to ignore the failure.

  * `ABORTED`

A previous phase failed.

  * `SKIPPED`

When you're running a deployment strategy, such as a [canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary), Cloud Deploy skips to the `stable` phase in cases where there isn't yet a running version of the application with which to split traffic. In this case, the state is set to `SKIPPED`.




### Job states

A job will have one of the following states:

  * `ABORTED`

If a phase fails, subsequent phases are aborted.

If a job fails, and that failure is not ignored, subsequent jobs are aborted. For example, if a phase includes a deploy job and a verify job, and the deploy job fails, the verify job is aborted.

  * `DISABLED`

Some jobs in a Phase might be disabled. For example, phases always include verify jobs, whether or not [verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) is enabled. If verification _isn't_ enabled, then the verify job is set to `DISABLED`.

  * `FAILED`

A job run for this job failed, and the user didn't choose to ignore the failure.

The user chose to terminate the job run for this job.

  * `IGNORED`

A job run for this job failed, and the user chose to ignore the failure.

  * `IN_PROGRESS`

A job run for this job is currently running.

  * `PENDING`

The job run for this job is waiting to begin, because another phase or job hasn't finished.

  * `SKIPPED`

When you're running a deployment strategy, such as a [canary](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary), Cloud Deploy skips to the `stable` phase in cases where there isn't yet a running version of the application with which to split traffic. In this case, the state is set to `SKIPPED` on jobs within the skipped phase or phases.

  * `SUCCEEDED`

The job run finished successfully, and the next job in the phase has started, or the next phase has started or is ready to start (possibly pending user input), or the rollout has finished.




### Job run states

  * `FAILED`

The job run failed during execution.

  * `IN_PROGRESS`

The job run has begun, but hasn't finished.

  * `TERMINATED`

The user terminated the job run.

  * `TERMINATING`

The user terminated the job run, but it hasn't finished terminating yet.

  * `SUCCEEDED`

When a job run finishes successfully, without failing or being terminated by a user, it's put into a `SUCCEEDED` state, which




## Manage your rollout

Using the Google Cloud console or the Google Cloud SDK, you can do the following with a Cloud Deploy rollout:

  * Advance the rollout

  * Cancel the rollout

  * Terminate a job run

  * Ignore a job

  * Retry a failed job




If you're using parallel deployment _with_ a canary deployment strategy, see [how to manage parallel canary rollouts](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary#parallel_canary).

### Advance a rollout

For targets configured to use a deployment strategy other than "standard," you need to advance the rollout from phase to phase. 

For example, if you have a target configured to perform a simple canary deploy with 50% and `stable` (100%) phases only, you would need to advance the rollout once, from the `canary-50` phase to the `stable` (100%) phase.

###  gcloud 
    
    
    gcloud deploy rollouts advance ROLLOUT_NAME \
                                   --release=RELEASE_NAME \
                                   --delivery-pipeline=PIPELINE_NAME \
                                   --region=REGION
    

Where:

`ROLLOUT_NAME` is the name of the current rollout which you're advancing to the next phase.

`RELEASE_NAME` is the name of the release that this rollout is part of.

`PIPELINE_NAME` is the name of the delivery pipeline you're using to manage deployment of this release.

`REGION` is the name of the region in which the release was created, for example `us-central1`. This is required.

See the Google Cloud SDK reference for more information about the [`gcloud deploy rollouts advance` command](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/rollouts/advance).

###  Console 

  1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

  2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress.

  3. On the **Rollouts** tab, under **Delivery pipeline details** , click the name of your rollout.

The rollout details page is shown, for that rollout. 

![rollout details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/rollout-details-canary50.png)

Notice that in this example, the rollout has a `canary-50` phase and a `stable` phase. Your rollout might have more phases or different phases.

  4. Click **Advance rollout**.

The rollout is advanced to the next phase.




### Cancel a rollout

You can cancel any rollout which hasn't finished. You can also cancel a failed rollout to prevent further actions on it (such as ignore or retry). The rollout must be in one of the following states:

  * `FAILED`
  * `HALTED`
  * `IN_PROGRESS`
  * `PENDING`
  * `PENDING_APPROVAL`
  * `PENDING_RELEASE`



After you cancel a rollout, that rollout is in a `CANCELLING` state until all outstanding job runs have completed. You can terminate outstanding job runs that you don't want to wait for. Once the rollout is `CANCELLED`, it can no longer be advanced or modified.

To cancel a rollout:

###  gcloud 
    
    
    gcloud deploy rollouts cancel ROLLOUT_NAME \
                                   --release=RELEASE_NAME \
                                   --delivery-pipeline=PIPELINE_NAME \
                                   --region=REGION
    

Where:

`ROLLOUT_NAME` is the name of the current rollout which you're advancing to the next phase.

`RELEASE_NAME` is the name of the release that this rollout is part of.

`PIPELINE_NAME` is the name of the delivery pipeline you're using to manage deployment of this release.

`REGION` is the name of the region in which the release was created, for example `us-central1`. This is required.

See the Google Cloud SDK reference for more information about the [`gcloud deploy rollouts cancel` command](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/rollouts/cancel).

###  Console 

  1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

  2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress.

  3. On the **Rollouts** tab, under **Delivery pipeline details** , click the name of your rollout.

The rollout details page is shown, for that rollout. 

![rollout details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/rollout-details-canary50_cancel.png)

Notice that in this example, the rollout has a `canary-50` phase and a `stable` phase. Your rollout might have more phases or different phases.

  4. Click **Cancel rollout**.

The rollout is canceled.




### Terminate a job run

You can end a job run that's currently in progress. You might want to do this, for example, if a job run appears to be taking too long or not working as expected. The job run must be `IN_PROGRESS` for you to terminate it.

###  gcloud 
    
    
    gcloud deploy job-runs terminate JOB_RUN_ID \
                                   --release=RELEASE_NAME \
                                   --delivery-pipeline=PIPELINE_NAME \
                                   --rollout=ROLLOUT_NAME \
                                   --region=REGION
    

Where:

`JOB_RUN_ID` is the (UUID) of the job run you want to terminate. You can find the job run ID in the Google Cloud console, for Cloud Deploy, on the rollout page:

![Job run ID in the rollout details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/job_run_id.png)

You can also get the job runs ID using the `gcloud deploy rollouts describe` command.

`RELEASE_NAME` is the name of the release that this job run is part of.

`PIPELINE_NAME` is the name of the delivery pipeline you're using to manage deployment of this release.

`ROLLOUT_NAME` is the name of the rollout this job run is part of.

`REGION` is the name of the region in which the release was created, for example `us-central1`. This is required.

See the Google Cloud SDK reference for more information about the [`gcloud deploy job-runs terminate` command](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/job-runs/terminate).

###  Console 

  1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

  2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress.

  3. On the **Rollouts** tab, under **Delivery pipeline details** , click the name of your rollout.

The rollout details page is shown, for that rollout. 

![rollout details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/rollout-details-canary50_terminate.png)

Notice that in this example, the rollout has a `canary-50` phase and a `stable` phase. Your rollout might have more phases or different phases.

  4. Under **Phases** , click the phase that includes the job whose job run you're terminating.

  5. Under **Job runs** select the specific job run you're terminating, then click **Terminate**.

The job run is terminated, and the job status, as shown in the **Phases** table, is `Failure`.




After you terminate a job run, the job is considered failed and you can do any of the following:

  * Leave it that way and disregard the failed rollout
  * Retry the job
  * Ignore the job and continue with the next job or phase in the rollout

**Note:** When you're using a [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel), you can terminate job runs on child rollouts only—not controller rollouts.

### Ignore a job

You can ignore a failed job and move immediately to the next job in the phase. That job might have failed for any reason, including you or someone else terminated a job run for that job.

A failed job means a failed phase and a failed rollout. However if you ignore the failure, both the phase and the rollout can be progressed and can ultimately have `SUCCEEDED` states.

###  gcloud 
    
    
    gcloud deploy rollouts ignore-job ROLLOUT_NAME \
                                   --release=RELEASE_NAME \
                                   --delivery-pipeline=PIPELINE_NAME \
                                   --job-id=JOB_ID \
                                   --phase-id=PHASE_ID \
                                   --region=REGION
    

Where:

`ROLLOUT_NAME` is the name of the rollout this job run is part of.

`RELEASE_NAME` is the name of the current release that includes this job.

`PIPELINE_NAME` is the name of the delivery pipeline you're using to manage deployment of this release.

`JOB_ID` is the name of the job to ignore, for example `DEPLOY`. You can find the job name in the **Phases** table for the rollout, in the Google Cloud console:

![The phases table, in Google Cloud console, with a failed job run ](https://docs.cloud.google.com/static/deploy/images/phases_table_with_failure.png)

`PHASE_ID` is the name of the phase that includes the job you're ignoring.

`REGION` is the name of the region in which the release was created, for example `us-central1`.

See the Google Cloud SDK reference for more information about the [`gcloud deploy rollouts ignore-job` command](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/rollouts/ignore-job).

###  Console 

  1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

  2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress.

  3. On the **Rollouts** tab, under **Delivery pipeline details** , click the name of your rollout.

The rollout details page is shown, for that rollout. 

  4. Select the failed job to ignore.

  5. Click the **Ignore failures** button.

The failed job run is ignored, and the rollout continues as if the job had succeeded. That is, if there are other jobs in the same phase, they are executed. Otherwise, the rollout is ready to advance to the next phase.




![A failed job, ready to be ignored, in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/ignore_failure.png)

**Note:** When you're using a [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel), you can ignore jobs on child rollouts only—not controller rollouts.

### Retry a failed job

You can retry a job run that failed. The job can fail for any of the following reasons:

  * A job run failed to complete.

For example, there could have been a permissions failure.

  * A user terminated a job run from that job.

Terminating a job run results in a failed job, which you can retry.

  * A verification test failed.

For a [verification](https://docs.cloud.google.com/deploy/docs/verify-deployment) job, a verification test failed. Even though the verification job completed correctly, one of your verification tests failed, and we propagate that back to the verification job. In this case, you would retry the job as part of debugging the failed test against your application.




To retry a failed job:

###  gcloud 
    
    
    gcloud deploy rollouts retry-job JOB_NAME \
                           --release=RELEASE_NAME \
                           --delivery-pipeline=PIPELINE_NAME \
                           --rollout=ROLLOUT_NAME \
                           --phase=PHASE_ID \
                           --region=REGION
    

Where:

`JOB_NAME` is the name of the job that you're retrying. For example, if you're retrying the verify job after a failed verification, this would be `verify`.

`RELEASE_NAME` is the name of the release that this job run is part of.

`PIPELINE_NAME` is the name of the delivery pipeline you're using to manage deployment of this release.

`ROLLOUT_NAME` is the name of the rollout this job run is part of.

`PHASE_ID` is name of the phase that this job is part of. For example, `canary-50`, or `stable`.

`REGION` is the name of the region in which the release was created, for example `us-central1`. This is required.

See the Google Cloud SDK reference for more information about the [`gcloud deploy rollouts retry-job` command](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/rollouts/retry-job).

###  Console 

  1. [Open the Delivery pipelines page](https://console.cloud.google.com/deploy/delivery-pipelines).

  2. Click your pipeline shown in the list of delivery pipelines.

The Delivery pipeline details page shows a graphical representation of your delivery pipeline's progress.

  3. On the **Rollouts** tab, under **Delivery pipeline details** , click the name of your rollout.

The rollout details page is shown, for that rollout. 

  4. Under **Phases and Jobs** , click the phase that includes the job you're retrying.

  5. Select the job to retry.

  6. Click **Retry** , and confirm.

![rollout details in Google Cloud console ](https://docs.cloud.google.com/static/deploy/images/rollout-details-canary50_retry_failed_job.png)

The job run is executed again and the job status, as shown in the **Phases** table, is "in progress". If there are other jobs in the same phase, they are executed. Otherwise, the rollout is ready to advance to the next phase.




**Note:** When you're using a [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel), you can retry jobs on child rollouts only—not controller rollouts.

## What's next

  * Find out more about [how deployment strategies work](https://docs.cloud.google.com/deploy/docs/deployment-strategies) in Cloud Deploy.

  * See the [Cloud Deploy service architecture](https://docs.cloud.google.com/deploy/docs/architecture) documentation for more information about how rollouts, phases, jobs, and job runs fit in with the rest of Cloud Deploy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
