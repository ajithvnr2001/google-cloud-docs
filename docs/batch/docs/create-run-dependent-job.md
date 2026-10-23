---
url: https://docs.cloud.google.com/batch/docs/create-run-dependent-job/
title: Schedule dependent jobs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:21.620279+00:00
---

# Schedule dependent jobs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-dependent-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Schedule dependent jobs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create and run a job that isn't scheduled until specific jobs have succeeded or failed. To learn more about job states, see [Job creation and execution overview](https://docs.cloud.google.com/batch/docs/create-run-job).

If you have a workload with varying resource requirements, consider using dependent jobs to create an automated chain of jobs that each use separate VMs. For example, separate the types of VMs used for low-demand operations (like data preparation) and compute-intensive operations (like data processing). By using dependent jobs to help optimize resource consumption, you can reduce costs and quota usage.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Restrictions

Dependent jobs have the following restrictions:

  * A dependent job can have up to four dependencies. Each dependency must contain a unique job name and one of the following required states:

    * `SUCCEEDED`: succeeded
    * `FAILED`: failed
    * `FINISHED`: succeeded or failed
  * When you create a dependent job, all of its dependency jobs must exist.

  * A dependent job can't enter the scheduled (`SCHEDULED`) state until each dependency job has entered its required state. If it becomes impossible for a dependency job to enter its required state, then the dependent job immediately fails without being scheduled.

**Note:** You don't need to wait to delete finished dependency jobs. A dependent job automatically remembers if a deleted dependency job reached its required state.
  * Like all jobs, a dependent job can't enter the scheduled (`SCHEDULED`) state if the job exceeds the [maximum wait time in the queue](https://docs.cloud.google.com/batch/quotas#max-job-queue). Batch enforces this limit to prevent your jobs from becoming stale. Consequently, if you expect the remaining time required for any of the dependency jobs to finish might exceed this limit, then consider doing one or more of the following:

    * If you haven't created a dependency job yet, try to reduce the expected run time of the dependency job. For example, you might increase the parallelism of the workload or [limit the run time](https://docs.cloud.google.com/batch/docs/set-timeouts) of any tasks and runnables that you don't need to succeed.
    * Wait to create the dependent job until the expected run time of the dependency jobs is lower than the limit.



### Create a dependent job

You can [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that is dependent using the following methods:

  * For the Google Cloud CLI, use the [`gcloud alpha batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch/jobs/submit).
  * For the Batch API, use the [v1alpha `jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs/create).



To specify that a job is dependent, include the [`dependencies[].items` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/projects.locations.jobs#Job.FIELDS.dependencies), which supports one or more dependencies specified as key-value pairs, in the main body in the JSON file:
    
    
    "dependencies": [
      {
        "items": {
          "DEPENDENCY_JOB_NAME": "REQUIRED_STATE"
        }
      }
    ]
    

Replace the following:

  * `DEPENDENCY_JOB_NAME`: the name of a dependency job, which must reach its required state before this dependent job is allowed to be scheduled.

  * `REQUIRED_STATE`: the required state for the corresponding dependency job, which must be `SUCCEEDED`, `FAILED`, or `FINISHED`.




For example, a dependent job with three dependencies can have a JSON configuration file that is similar to the following:
    
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello World! This is task $BATCH_TASK_INDEX."
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "dependencies": [
        {
          "items": {
            "DEPENDENCY_JOB_NAME_1": "REQUIRED_STATE_1",
            "DEPENDENCY_JOB_NAME_2": "REQUIRED_STATE_2",
            "DEPENDENCY_JOB_NAME_3": "REQUIRED_STATE_3"
          }
        }
      ]
    }
    

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * Learn how to [view jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
