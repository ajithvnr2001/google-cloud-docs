---
url: https://docs.cloud.google.com/batch/docs/cancel-job/
title: Cancel jobs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:32:31.495211+00:00
---

# Cancel jobs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/cancel-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Cancel jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to cancel Batch jobs. Cancel jobs that you want to stop running or prevent from running.

Ideally, you should configure your jobs to automatically stop running and fail whenever they don't behave as intended. For example, configure your runnables to return a non-zero exit code or [timeout](https://docs.cloud.google.com/batch/docs/set-timeouts). But, in practice, you might still want to manually stop unfinished jobs. For example, cancel a job when you notice you need to troubleshoot or replace a job that hasn't finished yet.

Like succeeded and failed jobs, a cancelled job remains in your project for up to 60 days, after which Google Cloud automatically deletes the job. If you want to cancel a job and don't need to retain the job's information, then you can immediately [delete the job](https://docs.cloud.google.com/batch/docs/delete-job) instead.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to cancel a job, ask your administrator to grant you the [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Cancel a job

You can cancel a job using the gcloud CLI or Batch API.

### gcloud

To cancel a job using the gcloud CLI, use the [`gcloud batch jobs cancel` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/cancel):
    
    
    gcloud batch jobs cancel JOB_NAME --location LOCATION
    

Replace the following:

  * `JOB_NAME`: the name of the job.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.



### API

To cancel a job using the Batch API, use the [`jobs.cancel` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/cancel):
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_NAME:cancel
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
  * `JOB_NAME`: the name of the job.



## What's next

  * Learn how to [limit run times using timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).
  * Learn about [troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn how to manage jobs: 
    * [View the jobs in your project](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
    * [Export job information](https://docs.cloud.google.com/batch/docs/export-job-info).
    * [Delete jobs](https://docs.cloud.google.com/batch/docs/delete-job).
  * [Create another job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
