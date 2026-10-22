---
url: https://docs.cloud.google.com/batch/docs/view-status-events/
title: View a job's history through status events \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:26.190817+00:00
---

# View a job's history through status events  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/view-status-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  View a job's history through status events Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view status events for Batch jobs and tasks. Status events provide a history that you can use to analyze jobs and often contain useful error messages that you can use for troubleshooting.

Each job and each of its tasks have status events that are automatically created by Batch while the job runs. Each of these status events describe a state change and details about why that state was reached. To learn about job and task states, see [Job lifecycle](https://docs.cloud.google.com/batch/docs/create-run-job#lifecycle). Optionally, you can also configure a job to have custom status events, which describe the progress of runnables. To learn more about custom status events, see [Configure custom status events](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. To get the permissions that you need to view jobs and tasks, ask your administrator to grant you the Batch Job Viewer (`roles/batch.jobsViewer`) or Batch Job Editor (`roles/batch.jobsEditor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View status events

Different status events might appear at the job level ([`statusEvents[]` field for the job](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#JobStatus.FIELDS.status_events)) and task level ([`statusEvents[]` field for each task](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs.taskGroups.tasks#TaskStatus.FIELDS.status_events)).

The following instructions explain how to view status events using the Google Cloud console, gcloud CLI, and Batch API. To use a client-library language, follow the steps to [view the details of a job](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-job) or [view the details of a task](https://docs.cloud.google.com/batch/docs/view-jobs-tasks#describe-task) and then see the corresponding `statusEvents[]` field.

### View the status events of a job

###  Console 

**Note:** The Google Cloud console only lists job-level status events.

To view the status events of a job in the current project using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Job list** page.

[Go to Job list](https://console.cloud.google.com/batch/jobs)

  2. In the **Job name** column, click the name of a job.

The **Job details** page opens.

The **Details** tab is open by default.

  3. Click the **Events** tab.




###  gcloud 

To view the status events of a job using the gcloud CLI, use the [`gcloud batch jobs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/describe), and then see the `statusEvents[]` field.
    
    
    gcloud batch jobs describe JOB_NAME \
        --location=LOCATION
    

Replace the following:

  * `JOB_NAME`: the name of an existing job.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.




###  API 

To view the status events of a job using the Batch API, make a `GET` request to the [`jobs.get` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/get), and then see the `statusEvents[]` field.
    
    
    GET https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_NAME
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the current project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.

  * `JOB_NAME`: the name of an existing job.




### View the status events of a task

###  gcloud 

To view the status events of a task using the gcloud CLI, use the [`gcloud batch tasks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/batch/tasks/describe), and then see the `statusEvents[]` field.
    
    
    gcloud batch tasks describe TASK_INDEX \
      --location=LOCATION \
      --job=JOB_NAME \
      --task_group=TASK_GROUP_NAME
    

Replace the following:

  * `TASK_INDEX`: the index of the task that you want to view the details of. In a task group, the task index starts at 0 for the first task and increases by 1 with each additional task. For example, a task group that contains four tasks has the indexes `0`, `1`, `2`, and `3`.

  * `JOB_NAME`: the name of an existing job.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.

  * `TASK_GROUP_NAME`: the name of the task group that contains the task that you want to view the details of. The value must be set to [`group0`](https://docs.cloud.google.com/batch/docs/get-started#restrictions).




###  API 

To view the status events of a task using the Batch API, make a `GET` request to the [`tasks.get` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs.taskGroups.tasks/get), and then see the `statusEvents[]` field.
    
    
    GET https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_NAME/taskGroups/TASK_GROUP_NAME/tasks/TASK_INDEX
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the current project.

  * `LOCATION`: the [location](https://docs.cloud.google.com/batch/docs/locations) where the job exists.

  * `JOB_NAME`: the name of an existing job.

  * `TASK_GROUP_NAME`: the name of the task group that contains the task that you want to view the details of. The value must be set to [`group0`](https://docs.cloud.google.com/batch/docs/get-started#restrictions).

  * `TASK_INDEX`: the index of the task that you want to view the details of. In a task group, the task index starts at 0 for the first task and increases by 1 with each additional task. For example, a task group that contains four tasks has the indexes `0`, `1`, `2`, and `3`.




## What's next

  * To understand status events from Batch that describe errors, see [Troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).

  * If you want a more detailed history for your job, such as status events for when runnables start and end, [configure custom status events](https://docs.cloud.google.com/batch/docs/create-run-job-custom-status-events).

  * Learn how to [analyze a job by using logs](https://docs.cloud.google.com/batch/docs/analyze-job-using-logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
