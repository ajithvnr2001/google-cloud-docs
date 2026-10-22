---
url: https://docs.cloud.google.com/batch/docs/non-root-job/
title: Create and run jobs as a non-root user \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:30.686451+00:00
---

# Create and run jobs as a non-root user  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/non-root-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run jobs as a non-root user Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create and run a Batch job as a non-root user.

By default, Batch executes runnables as the root user. If you want Batch to execute runnables as a non-root user—for example, to run an application that doesn't allow root users or to meet security requirements—create a Batch job that uses [OS Login](https://docs.cloud.google.com/compute/docs/oslogin). When you enable OS Login in a Batch job, OS Login configures a user account for you on the VMs that your job runs on. All runnables in the job are then executed by your user account on the VM instead of by the root user.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. If you haven't done so already, enable the [OS Login API](https://docs.cloud.google.com/compute/docs/oslogin/rest) by running the following command:
         
         gcloud services enable oslogin.googleapis.com
         

  3. To get the permissions that you need to create and run a job as a non-root user, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the default Compute Engine service account
     * [Compute OS Login](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLogin) (`roles/compute.osLogin`) or [Compute OS Admin Login](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osAdminLogin) (`roles/compute.osAdminLogin`) on the project
     * If you are from a different organization than the project: [Compute OS Login External User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLoginExternalUser) (`roles/compute.osLoginExternalUser`) on the project's organization 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Users with the Compute OS Admin Login role have sudo permissions, but Batch doesn't execute jobs using those permissions. 



## Create a job that runs as a non-root user

Create a Batch job that runs executables through your own user account by doing the following:

Use the Google Cloud CLI or REST API to [create a job](https://docs.cloud.google.com/batch/docs/create-run-basic-job#create-basic-job) that includes the [`runAsNonRoot` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskGroup.FIELDS.run_as_non_root) set to `true` in the main body of the JSON file:
    
    
    "runAsNonRoot": true
    

For example, a job that runs executables as a non-root user would have a JSON configuration file similar to the following:
    
    
    {
        "taskGroups": [
          {
            "taskSpec": {
              "runnables": [
                {
                  "script": {
                    "text": "echo Hello World! This is task $BATCH_TASK_INDEX executed by $(whoami)."
                  }
                }
              ]
            },
            "taskCount": 3,
            **"runAsNonRoot" : true**
          }
        ],
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
