---
url: https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library/
title: Configure task communication using an MPI library \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:19.639207+00:00
---

# Configure task communication using an MPI library  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Configure task communication using an MPI library Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure a Batch job with tightly coupled tasks that communicate with each other across different VMs by using a [Message Passing Interface (MPI)](https://www.mpi-forum.org/docs/mpi-3.1/mpi31-report/mpi31-report.htm) library.

For Batch jobs, [coupling](https://en.wikipedia.org/wiki/Coupling_\(computer_programming\)) describes the interdependency tasks; this influences how you configure the number of tasks that can run in parallel (instead of sequentially) using a job's [`parallelism` field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#taskgroup). Tasks can be described using the following types of coupling:

  * **Loosely coupled tasks:** tasks that can run independently.
  * **Tightly coupled tasks:** tasks that are dependent on each other to run.



Optionally, you can create a job that uses an MPI library to let tightly coupled tasks communicate with each other across different VM instances. A common use case for MPI is tightly coupled high-performance computing (HPC) workloads.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. If you [specify the network for this job](https://docs.cloud.google.com/batch/docs/specify-job-network), make sure the network has a firewall rule that allows connections between the job's VMs. Learn how to [Configure VPC firewall rules for common use cases](https://docs.cloud.google.com/vpc/docs/using-firewalls#rules-for-common-use-cases). 



## Create and run a job that uses MPI for tightly coupled tasks

**Important:** This section only describes how to use MPI for jobs with script runnables.

This section provides examples for how to create a job that can use MPI. Notably, the example job has 3 runnables:

  * The first runnable is a script that prepares the job for MPI by [disabling simultaneous multithreading](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#disable_simultaneous_multithreading) and [installing Intel MPI](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#install_intel_mpi_2018).
  * The second runnable is an empty [barrier runnable](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#barrier) (formatted as `{ "barrier": {} }`), which ensures that all tasks finish setting up MPI before continuing to future runnables.
  * The third runnable (and any subsequent runnables) is available for the job's workload.



You can create a job that uses MPI for tightly coupled tasks using the gcloud CLI or Batch API.

### gcloud

To create a script job that uses MPI for tightly coupled tasks by using the gcloud CLI, do the following:

  1. Create a JSON configuration file with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "google_mpi_tuning --nosmt; google_install_mpi --intel_mpi;"
                                 }
                             },
                             { "barrier": {} },
                             {
                                 "script": {
                                     SCRIPT
                                 }
                             }
                         ]
                     },
                     "taskCount": TASK_COUNT,
                     "taskCountPerNode": TASK_COUNT_PER_NODE,
                     "requireHostsFile": REQUIRE_HOSTS_FILE,
                     "permissiveSsh": PERMISSIVE_SSH
                 }
             ]
         }
         

Replace the following:

     * `SCRIPT`: a [script](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#script) runnable for a workload that uses MPI.
     * `TASK_COUNT`: the number of tasks for the job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits). To use the MPI libraries provided by Batch, this field is required and must be set to `2` or higher.
     * `TASK_COUNT_PER_NODE`: the number of tasks that a job can run concurrently on a VM instance. To use the MPI libraries provided by Batch, this field is required and must be set to `1`, which equals to running one VM instance per task.
     * `REQUIRE_HOSTS_FILE`: when set to `true`, the job creates a file listing the VM instances running in a task group. The file path is stored in the `BATCH_HOSTS_FILE` environment variable. To use the MPI libraries provided by Batch, this field must be set to true.
     * `PERMISSIVE_SSH`: when set to `true`, Batch configures SSH to allow passwordless communication among the VM instances running in a task group. To use the MPI libraries provided by Batch, this field must be set to true.
  2. To create the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit).
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.
     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.



Optionally, you can increase the performance of the MPI libraries provided by Batch by doing the following:

  * [Create and run a job using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template) and specify an [HPC-ready VM instance template](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm) in your job's resources.
  * Specify [Cloud Logging](https://docs.cloud.google.com/logging/docs/how-to) as the destination for your job's logging information in your job's resources.



For example, to create a script job from an instance template that uses MPI and makes 1 task output the hostname of the 3 tasks in the task group:

  1. Create a JSON file in the current directory named `example-job-uses-mpi.json` with the following contents:
         
         {
             "taskGroups": [
                 {
                     "taskSpec": {
                         "runnables": [
                             {
                                 "script": {
                                     "text": "google_mpi_tuning --nosmt; google_install_mpi --intel_mpi;"
                                 }
                             },
                             { "barrier": {} },
                             {
                                 "script": {
                                     "text":
                                         "if [ $BATCH_TASK_INDEX = 0 ]; then
                                         mpirun -hostfile $BATCH_HOSTS_FILE -np 3 hostname;
                                         fi"
                                 }
                             },
                             { "barrier": {} }
                         ]
                     },
                     "taskCount": 3,
                     "taskCountPerNode": 1,
                     "requireHostsFile": true,
                     "permissiveSsh": true
                 }
             ],
             "allocationPolicy": {
                 "instances": [
                     {
                         "instanceTemplate": "example-template-job-uses-mpi"
                     }
                 ]
             },
             "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
             }
         }
         

  2. Run the following command:
         
         gcloud batch jobs submit example-template-job-uses-mpi \
           --location us-central1 \
           --config example-job-uses-mpi.json
         




### API

To create a script job that uses a MPI for tightly coupled tasks by using the Batch API, use the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) and specify the `permissiveSsh`, `requireHostsFile`, `taskCount`, and `taskCountPerNode` fields.
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?job_id=JOB_ID
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "google_mpi_tuning --nosmt; google_install_mpi --intel_mpi;"
                            }
                        },
                        { "barrier": {} },
                        {
                            "script": {
                                SCRIPT
                            }
                        }
                    ]
                },
                "taskCount": TASK_COUNT,
                "taskCountPerNode": TASK_COUNT_PER_NODE,
                "requireHostsFile": REQUIRE_HOSTS_FILE,
                "permissiveSsh": PERMISSIVE_SSH
            }
        ]
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.
  * `JOB_NAME`: the name of the job.
  * `SCRIPT`: the [script](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#script) runnable for a workload that uses MPI.
  * `TASK_COUNT`: the number of tasks for the job. The value must be a whole number between `1` and the [tasks per task group limit](https://docs.cloud.google.com/batch/quotas#job_limits). To use the MPI libraries provided by Batch, this field is required and must be set to `2` or higher.
  * `TASK_COUNT_PER_NODE`: the number of tasks that a job can run concurrently on a VM instance. To use the MPI libraries provided by Batch, this field is required and must be set to `1`, which equals to running one VM instance per task.
  * `REQUIRE_HOSTS_FILE`: when set to `true`, the job creates a file listing the VM instances running in a task group. The file path is stored in the `BATCH_HOSTS_FILE` environment variable. To use the MPI libraries provided by Batch, this field must be set to true.
  * `PERMISSIVE_SSH`: when set to `true`, Batch configures SSH to allow passwordless communication among the VM instances running in a task group. To use the MPI libraries provided by Batch, this field must be set to true.



Optionally, you can increase the performance of the MPI libraries provided by Batch by doing the following:

  * [Create and run a job using a VM instance template](https://docs.cloud.google.com/batch/docs/create-run-job-vm-template) and specify an [HPC-ready VM instance template](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm) in your job's resources.
  * Specify [Cloud Logging](https://docs.cloud.google.com/logging/docs/how-to) as the destination for your job's logging information in your job's resources.



For example, to create a script job from an instance template that uses MPI and makes 1 task output the hostname of the 3 tasks in the task group, use the following request:
    
    
    POST https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs?job_id=example-template-job-uses-mpi
    
    {
        "taskGroups": [
            {
                "taskSpec": {
                    "runnables": [
                        {
                            "script": {
                                "text": "google_mpi_tuning --nosmt; google_install_mpi --intel_mpi;"
                            }
                        },
                        { "barrier": {} },
                        {
                            "script": {
                                "text":
                                    "if [ $BATCH_TASK_INDEX = 0 ]; then
                                    mpirun -hostfile $BATCH_HOSTS_FILE -np 3 hostname;
                                    fi"
                            }
                        },
                        { "barrier": {} }
                    ]
                },
                "taskCount": 3,
                "taskCountPerNode": 1,
                "requireHostsFile": true,
                "permissiveSsh": true
            }
        ],
        "allocationPolicy": {
            "instances": [
                {
                    "instanceTemplate": "example-template-job-uses-mpi"
                }
            ]
        },
        "logsPolicy": {
            "destination": "CLOUD_LOGGING"
        }
    }
    

where `PROJECT_ID` is the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

## What's next

  * For a more detailed example of a job that uses MPI for tightly coupled tasks, see [Running the Weather Research and Forecasting model with Batch](https://github.com/GoogleCloudPlatform/batch-samples/tree/main/wrf).
  * Learn how to [reduce latency for jobs with tightly coupled tasks](https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy).
  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
