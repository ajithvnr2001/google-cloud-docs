---
url: https://docs.cloud.google.com/batch/docs/export-job-info/
title: Export job information \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:30.135534+00:00
---

# Export job information  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/export-job-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Export job information Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export the information for your jobs that is stored in Batch to a BigQuery table by using Workflows. Specifically, learn how to run the sample _export-jobs workflow_ and how to view the resulting job information in BigQuery.

Exporting a job's information is useful when you want to retain the information after [a job is automatically or manually deleted](https://docs.cloud.google.com/batch/docs/delete-job) or analyze the information outside of Batch. Alternatively, if you want to export only task and job state-change information to BigQuery, see [Monitor jobs using notifications](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications) instead.

To learn how to export job information that is stored in other Google Cloud services, see the export documentation for that service. For example, see the following pages:

  * [Export Cloud Logging logs](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-compliance-requirements).
  * [Export Cloud Monitoring metrics](https://docs.cloud.google.com/architecture/monitoring-metric-export).

**Note:** Workflows and BigQuery are separate Google Cloud products that have their own pricing. For more information, see [Workflows pricing](https://cloud.google.com/workflows/pricing) and [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. Enable the BigQuery and Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,workflows.googleapis.com)

  3. Optional: [Identify an existing BigQuery dataset or table in your project](https://docs.cloud.google.com/bigquery/docs/listing-datasets) where you want to store the job information. An existing table must have a matching schema.

Otherwise, you can use the export-jobs workflow to create a new dataset or table. 

  4. Prepare a service account for the export-jobs workflow by doing the following:

     1. [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) or [identify an existing service account](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit).
     2. To ensure that the service account has the necessary permissions to execute the export-jobs workflow, ask your administrator to grant the following IAM roles to the service account on the project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 
        * Write logs: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) 
        * Create and edit BigQuery datasets and tables: [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) 
        * View and delete Batch jobs: [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 



* To get the permissions that you need to create, deploy, and execute the export-jobs workflow, ask your administrator to grant you the following IAM roles on the project: 

  * View jobs: [Batch Job Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsViewer) (`roles/batch.jobsViewer`) 
  * View service accounts: [View Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`) 
  * View BigQuery datasets and tables: [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) 
  * Create, deploy, and execute workflows: [Workflows Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.editor) (`roles/workflows.editor`) 



* Ensure that users in your project can view the exported job information.

To ensure that a user has the necessary permissions to export job information, ask your administrator to grant the [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) IAM role to a user on the table, dataset, or project. 

**Note:** You can only grant access to existing resources. Unless you plan to export job information to a pre-existing table or dataset, you must grant this access either on the project or after exporting the job information. 

## Export job information

This section explains how to export job information by using the _export-jobs workflow_ , which is from the [`export-to-bigquery` code sample](https://github.com/GoogleCloudPlatform/batch-samples/tree/main/workflows-samples/export-to-bigquery). The export-jobs workflow exports the information for your project's jobs that are in the specified region and meet the specified filter criteria.

**Important:** The export-jobs workflow can only export job information from one region at a time. If you want to export information for jobs in multiple regions or multiple subsets in a region, then configure, create, deploy, and execute a dedicated export-jobs workflow for each use case.

We recommend that you create dedicated workflows for each use case. Although you can modify and re-execute one workflow, dedicated workflows make it easier to track when you last exported which jobs and to schedule workflows to automatically export your jobs. 

The export-jobs workflow exports job information to a specified table in a specified dataset, which are automatically created by the workflow if they don't already exist in your project. By default, the export-jobs workflow also deletes the exported jobs from Batch, but you can optionally edit the export-jobs workflow to not delete the jobs.

For each export-jobs workflow that you want to use, do the following:

  1. Configure the workflow definition.
  2. Create and deploy the workflow.
  3. Execute the workflow. Repeat this step each time you want to export the specified jobs.



### Configure the workflow definition

  1. Download the [`export-to-bigquery-delete-batch-jobs.yaml` file from GitHub](https://github.com/GoogleCloudPlatform/batch-samples/blob/main/workflows-samples/export-to-bigquery/export-to-bigquery-delete-batch-jobs.yaml).

  2. Open the `export-to-bigquery-delete-batch-jobs.yaml` file in a text editor. Then, make the following edits:

     1. Replace `sys.get_env("GOOGLE_CLOUD_PROJECT_ID")` with your project ID formatted as a string—for example, `"my-project-id"`.

     2. Replace `sys.get_env("GOOGLE_CLOUD_LOCATION")` with the region that contains the jobs that you want to export, formatted as a string—for example, `"us-central1"`.

     3. Optional: Edit the filter criteria that specifies which jobs to export.

By default, the export-jobs workflow specifies the filter criteria `"(status.state:SUCCEEDED OR status.state:FAILED OR status.state:CANCELLED) AND create_time<=\"2023-05-01T00:00:00Z\""`. This default filter criteria exports information only for jobs that are in the `SUCCEEDED`, `FAILED`, or `CANCELLED` state and were created before or by the `2023-05-01T00:00:00Z` [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp.

     4. Optional: Replace `default_dataset_id` with a different name for the dataset that you want the export-jobs workflow to use or create.

     5. Optional: Replace `default_table_id` with a different name of the table that you want the export-jobs workflow to use or create.

     6. If you don't want the exported jobs to be deleted by the workflow, then do the following:

**Tip:** If you don't delete exported jobs, then re-executing the same export-jobs workflow might create duplicate rows. To avoid this, you can update the `create_time` filter criteria before each re-execution to only include jobs that were created after the previous execution. To learn how to see when a workflow was previously executed, see [Access workflow execution results](https://docs.cloud.google.com/workflows/docs/access-execution-results).
        1. Remove the following lines:
               
               - log_delete_step:
                           call: sys.log
                           args:
                             text: ${"Deleting Batch job " + j.name}
                             severity: NOTICE
                       - delete_job:
                           call: googleapis.batch.v1.projects.locations.jobs.delete
                           args:
                             name: ${j.name}
               

        2. Remove `+ " and deleted"`.

     7. Save the file. Keep the file open.




### Create and deploy the workflow

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, click add**Create**.

  3. In the **Workflow name** field, enter a name for the workflow—for example, `export-batch-jobs-us-central1`.

  4. In the **Service account** list, select the service account that you prepared.

  5. Click **Next**.

  6. In the workflow editor, replace the sample workflow with the contents of the `export-to-bigquery-delete-batch-jobs.yaml` file. Then, you can close the file.

  7. Click **Deploy**. The **Workflow details** page opens.




### Execute the workflow

**Tip:** If you want to automatically execute the export-jobs workflow, then see [Schedule a workflow using Cloud Scheduler](https://docs.cloud.google.com/workflows/docs/schedule-workflow) in the Workflows documentation instead. For example, because each job is automatically deleted 60 days after it finishes, you can export all your jobs (that aren't manually deleted) by scheduling one or more export-jobs workflows to export and delete jobs every 59 days.

  1. On the **Workflow details** page, click play_arrow**Execute**. The **Execute workflow** page opens.

  2. On the **Execute workflow** page that opens, click **Execute**.

  3. On the **Execution details** that page opens, wait for the workflow to finish executing. For example, the execution time to export and delete a few jobs is usually a few seconds, but execution might take longer if you are exporting and deleting many jobs.

When the workflow has finished executing, the **Output** pane displays the results.




## View the exported job information

This section introduces how to view the table data created by the export-jobs workflow. For example, you can use the following steps to verify that workflow was executed successfully and browse the table data. For more information about how to view and use your exported job information, such as writing queries, see [Managing table data](https://docs.cloud.google.com/bigquery/docs/managing-table-data) in the BigQuery documentation.

  1. In the Google Cloud console, go to the **BigQuery** page:

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** panel, open the table for your exported job information:

     1. In the **Search BigQuery resources** field, enter the name of the table from your export-jobs workflow. For example, the default table name is `default_table_id`.
     2. Click the name of the table. The table details page opens.
     3. On the table details page, click the **Details** tab.

On **Details** tab, note the **Last modified** timestamp and the **Number of rows**.

     4. On the table details page, click the **Preview** tab.




## What's next

  * Learn more about [Workflows](https://docs.cloud.google.com/workflows/docs/overview).
  * Learn more about [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction).
  * Learn more about Batch: 
    * [View the jobs in your project](https://docs.cloud.google.com/batch/docs/view-jobs-tasks)
    * [Delete jobs](https://docs.cloud.google.com/batch/docs/delete-job)
    * [Create another job](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
