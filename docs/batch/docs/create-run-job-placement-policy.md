---
url: https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy/
title: Reduce latency by using compact placement policies \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:58.392664+00:00
---

# Reduce latency by using compact placement policies  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Reduce latency by using compact placement policies Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to reduce network latency among a job's VMs by specifying a compact placement policy.

Having VM hosts that are physically closer to each other within a [zone](https://docs.cloud.google.com/compute/docs/regions-zones#zones_and_clusters) can reduce network latency between VMs. This performance benefit can be especially useful for jobs with tightly coupled tasks, such as [tasks that communicate using MPI libraries](https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library). When you create a job, you can optionally require a job's VMs to be located closer to each other by specifying a compact placement policy. Otherwise, default VM placement typically distributes VMs across separate hosts to help minimize the impact of power failures.

To learn more about compact placement policies, see [About placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) in the Compute Engine documentation.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Restrictions

In addition to the [general restrictions for compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions-compact-policies), Batch also has the following restrictions:

  * When you specify for a job to use a compact placement policy, Batch automatically creates and deletes a compact placement policy for the job's VMs. You can't specify an existing compact placement policy for a job.
  * You can't specify a number of VMs for the compact placement policy. The compact placement policy for a job applies regardless of how many VMs the job runs on.



## Create and run a job that uses a placement policy

You can specify for a job to use a compact placement policy by setting the [`collocation` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#PlacementPolicy.FIELDS.collocation) to `COLLOCATED` using the gcloud CLI or Batch API.

### gcloud

  1. Create a JSON file that specifies the job's configuration details and sets the `collocation` field to `COLLOCATED`.

For example, to create a basic script job that specifies a compact placement policy, create a JSON file with the following contents:
         
         {
           "taskGroups": [
             {
               "taskSpec": {
                 "runnables": [
                   {
                     "script": {
                       "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                     }
                   }
                 ]
               },
               "taskCount": 3
             }
           ],
           "allocationPolicy": {
             "placement": {
               **"collocation" : "COLLOCATED"**
             }
           },
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that sets the `collocation` field to `COLLOCATED`.

For example, to create a basic script job that specifies a compact placement policy, make the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_NAME
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "echo Hello world from task ${BATCH_TASK_INDEX}"
                }
              }
            ]
          },
          "taskCount": 3
        }
      ],
      "allocationPolicy": {
        "placement": {
          **"collocation" : "COLLOCATED"**
        }
      },
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.




## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
