---
url: https://docs.cloud.google.com/batch/docs/automate-task-retries/
title: Automate task retries \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:01.086867+00:00
---

# Automate task retries  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/automate-task-retries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Automate task retries Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to automatically retry tasks after all or some failures.

A Batch job fails when at least one of its tasks fails, which can happen for various reasons. By default, each task in a job only runs once; if a task fails, it is not retried. However, some issues that cause a task to fail can be easily resolved just by retrying the task. In these cases, configuring the job to automatically retry tasks can substantially help reduce troubleshooting friction and the overall run time of your jobs.

Automatic retries are well-suited to [loosely coupled (independent) tasks](https://docs.cloud.google.com/batch/docs/create-run-job-mpi-library) and can help with a variety of issues. For example, automatic task retries can resolve time-sensitive issues like following:

  * preemption of [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
  * [VM maintenance events and host errors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview)
  * transient networking errors



You can configure automatic task retries for each task when you create a job. Specifically, for each task, you can use one of the following configuration options:

  * By default, each task is not retried when it fails.
  * Retry tasks for all failures: You can configure the maximum times to automatically retry failed tasks. You can specify between 0 (default) and 10 retries.
  * Retry tasks for some failures: You can configure different task actions—either automatic retry or fail without retry—for specific failures. The opposite action is taken for all unspecified failures. Specific failures can each be identified by an exit code that is defined by your application or Batch.



## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to create a job, ask your administrator to grant you the following IAM roles: 

     * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the [job's service account](https://docs.cloud.google.com/batch/docs/create-run-job-custom-service-account#create-job-service-account), which by default is the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Retry tasks for all failures

You can define the [maximum number of automatic retries (`maxRetryCount` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.max_retry_count) for a job's failed tasks using the gcloud CLI or Batch API.

### gcloud

  1. Create a JSON file that specifies the job's configuration details and the `maxRetryCount` field.

For example, to create a basic script job that specifies the maximum retries for failed tasks, create a JSON file with the following contents:
         
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
                 ],
                 **        "maxRetryCount": MAX_RETRY_COUNT
                 **
               },
               "taskCount": 3
             }
           ],
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

Replace `MAX_RETRY_COUNT` with the maximum number of retries for each task. For a job to be able to retry failed tasks, this value must be set to an integer between `1` and `10`. If the `maxRetryCount` field is not specified, the default value is `0`, which means to not retry any tasks.

  2. To create and run the job, use the [`gcloud batch jobs submit` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit):
         
         gcloud batch jobs submit JOB_NAME \
           --location LOCATION \
           --config JSON_CONFIGURATION_FILE
         

Replace the following:

     * `JOB_NAME`: the name of the job.

     * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

     * `JSON_CONFIGURATION_FILE`: the path for a JSON file with the job's configuration details.




### API

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that specifies the `maxRetryCount` field.

For example, to create a basic script job that specifies the maximum retries for failed tasks, make the following request:
    
    
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
            ],
            **        "maxRetryCount": MAX_RETRY_COUNT
            **
          },
          "taskCount": 3
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `MAX_RETRY_COUNT`: The maximum number of retries for each task. For a job to be able to retry failed tasks, this value must be set to an integer between `1` and `10`. If the `maxRetryCount` field is not specified, the default value is `0`, which means to not retry any tasks.




## Retry tasks for some failures

You can define how you want a job to handle different task failures by using [lifecycle policies (`lifecyclePolicies[]` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.lifecycle_policies).

A lifecycle policy consists of an [action (`action` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LifecyclePolicy.FIELDS.action), [action condition (`actionCondition` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#LifecyclePolicy.FIELDS.action_condition), and [exit code (`exitCodes[]` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#ActionCondition.FIELDS.exit_codes). The specified action is taken whenever the action condition—a specific exit code—occurs. You can specify one the following actions:

  * `RETRY_TASK`: retry tasks that fail with the exit codes specified in the `exitCodes[]` field. Tasks that fail with any unspecified exit codes are not retried.
  * `FAIL_TASK`: do not retry tasks that fail with the exit codes specified in the `exitCodes[]` field. Tasks that fail with any unspecified exit codes are retried.



Notably, any tasks that fail with unspecified exit codes take the opposite action—some exit codes are retried and some are failed. Consequently, for the lifecycle policy to work as expected, you also need to define the [maximum number of automatic retries (`maxRetryCount` field)](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#TaskSpec.FIELDS.max_retry_count) to allow the job to automatically retry failed tasks at least once.

Each exit code represents a specific failure that is defined either by your application or Batch. The exit codes from 50001 to 59999 are reserved and defined by Batch. For more information about the reserved exit codes, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting#reserved-exit-codes).

You can specify for a job to retry or fail tasks after specific failures using gcloud CLI or Batch API.

###  gcloud 

  1. Create a JSON file that specifies the job's configuration details, the `maxRetryCount` field, and the `lifecyclePolicies[]` subfields.

To create a basic script job that retries failed tasks only for some exit codes, create a JSON file with the following contents:
         
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
                 ],
                 **        "maxRetryCount": MAX_RETRY_COUNT,
                 "lifecyclePolicies": [
                   {
                     "action": "ACTION",
                     "actionCondition": {
                        "exitCodes": [EXIT_CODES]
                     }
                   }
                 ]**
               }
             }
           ],
           "logsPolicy": {
             "destination": "CLOUD_LOGGING"
           }
         }
         

Replace the following:

     * `MAX_RETRY_COUNT`: the maximum number of retries for each task. For a job to be able to retry failed tasks, this value must be set to an integer between `1` and `10`. If the `maxRetryCount` field is not specified, the default value is `0`, which means to not retry any tasks.

     * `ACTION`: the action, either `RETRY_TASK` or `FAIL_TASK`, that you want for tasks that fail with the specified exit codes. Tasks that fail with unspecified exit codes take the other action.

     * `EXIT_CODES`: a comma-separated list of one or more exit codes that you want to trigger the specified action—for example, `50001, 50002`.

Each exit code can be defined by your application or Batch. The exit codes from `50001` to `59999` are reserved by Batch. For more information about the reserved exit codes, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting#reserved-exit-codes).

For example, the following job only retries tasks that fail due to the preemption of Spot VMs.
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "sleep 30"
                }
              }
            ],
            "maxRetryCount": 3,
            "lifecyclePolicies": [
              {
                 "action": "RETRY_TASK",
                 "actionCondition": {
                   "exitCodes": [50001]
                }
              }
            ]
          }
        }
      ],
      "allocationPolicy": {
        "instances": [
          {
            "policy": {
              "machineType": "e2-standard-4",
              "provisioningModel": "SPOT"
            }
          }
        ]
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




###  API 

Make a `POST` request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) that specifies the `maxRetryCount` field and `lifecyclePolicies[]` subfields.

To create a basic script job that retries failed tasks only for some exit codes, make the following request:
    
    
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
            ],
            **        "maxRetryCount": MAX_RETRY_COUNT,
            "lifecyclePolicies": [
              {
                "action": "ACTION",
                "actionCondition": {
                    "exitCodes": [EXIT_CODES]
                }
              }
            ]**
          }
        }
      ],
      "logsPolicy": {
        "destination": "CLOUD_LOGGING"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) of the job.

  * `JOB_NAME`: the name of the job.

  * `MAX_RETRY_COUNT`: the maximum number of retries for each task. For a job to be able to retry failed tasks, this value must be set to an integer between `1` and `10`. If the `maxRetryCount` field is not specified, the default value is `0`, which means to not retry any tasks.

  * `ACTION`: the action, either `RETRY_TASK` or `FAIL_TASK`, that you want for tasks that fail with the specified exit codes. Tasks that fail with unspecified exit codes take the other action.

  * `EXIT_CODES`: a comma-separated list of one or more exit codes that you want to trigger the specified action—for example, `50001, 50002`.

Each exit code can be defined by your application or Batch. The exit codes from `50001` to `59999` are reserved by Batch. For more information about the reserved exit codes, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting#reserved-exit-codes).




For example, the following job only retries tasks that fail due to the preemption of Spot VMs.
    
    
    POST https://batch.googleapis.com/v1/projects/example-project/locations/us-central1/jobs?job_id=example-job
    
    {
      "taskGroups": [
        {
          "taskSpec": {
            "runnables": [
              {
                "script": {
                  "text": "sleep 30"
                }
              }
            ],
            "maxRetryCount": 3,
            "lifecyclePolicies": [
              {
                 "action": "RETRY_TASK",
                 "actionCondition": {
                   "exitCodes": [50001]
                }
              }
            ]
          }
        }
      ],
      "allocationPolicy": {
        "instances": [
          {
            "policy": {
              "machineType": "e2-standard-4",
              "provisioningModel": "SPOT"
            }
          }
        ]
      }
    }
    

## Modify task behavior based on the number of retries

Optionally, after you've enabled automatic retries for a task as described in the previous sections on this page, you can update your runnables to use the `BATCH_TASK_RETRY_ATTEMPT` predefined environment variable. The `BATCH_TASK_RETRY_ATTEMPT` variable describes the number of times that this task has already been attempted. Use the `BATCH_TASK_RETRY_ATTEMPT` variable in your runnables if you want a task to behave differently based on the number of retries. For example, when a task is being retried, you might want to confirm which commands were already successfully executed in the previous attempt. For more information, see [Predefined environment variables](https://docs.cloud.google.com/batch/docs/create-run-basic-job#predefined-environment-variables).

## What's next

  * If you have issues creating or running a job, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).
  * [View jobs and tasks](https://docs.cloud.google.com/batch/docs/view-jobs-tasks).
  * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
