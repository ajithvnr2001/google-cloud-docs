---
url: https://docs.cloud.google.com/dataform/docs/trigger-execution/
title: Manually trigger runs \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:19.536195+00:00
---

# Manually trigger runs  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/trigger-execution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Manually trigger runs Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to manually trigger runs of your entire workflow or only selected elements in your workflow.

You can trigger a run for the following elements of your workflow:

  * All actions in your workflow
  * Selected actions
  * Actions with selected tags



## Before you begin

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).

  3. Select or [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  4. Develop your workflow.




### Required roles

To get the permissions that you need to manually trigger a run, ask your administrator to grant you the following IAM roles: 

  * [Dataform Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.editor) (`roles/dataform.editor`) on the Dataform repository
  * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the custom service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Important:** If your organization enforces an organization policy constraint that disallows end user credentials by denying setting `end_user_auth_config`, you cannot execute workflows using your Google Account user credentials. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints).

## Manually run all the actions in your workflow

To manually trigger a run of all the actions in your workflow, follow these steps:

  1. Go to a development workspace.
  2. Click **Start execution**.
  3. Click **Actions > Multiple actions**.
  4. In the **Authentication** section, authorize the execution with your Google Account user credentials or a service account.

     * To use your Google Account user credentials, select **Execute with user credentials**.

Optional: In the **Extended access options** section, select the additional scopes that your workflow requires:

       * **Knowledge Catalog** : Allows Google Cloud Knowledge Catalog metadata updates.
       * **Google Drive** : Allows read-only access to Google Drive files.
       * **Bigtable** : Allows read-only access to Google Bigtable data.
     * To use a custom service account, select **Execute with selected service account** , and then select a custom service account.

**Note:** To see service accounts in the menu, you must have the `iam.serviceAccounts.list` permission at the project level, which is available in the [View Service Accounts role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`). If you don't have this permission, you can select the service account by clicking **Enter manually** and entering the service account ID.
  5. Select **All actions**.

  6. Optional: To rebuild all tables from scratch, select the **Run with full refresh** option. Without this option, Dataform updates incremental tables without rebuilding them from scratch.

  7. Optional: Set the BigQuery query job priority with the **Execute as interactive job with high priority (default)** option. By default, BigQuery runs queries as [interactive query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which are intended to start running as quickly as possible. Clearing this option runs the queries as [batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which have lower priority.

  8. Click **Start execution**. If you selected **Execute with user credentials** for your authentication method, you must authorize your Google Account.




## Manually run selected actions

To manually trigger a run of selected actions, follow these steps:

  1. Go to your development workspace.
  2. Click **Start execution** , then do either of the following:

     * Click **Actions** , then select an action that you want to run.
     * Click **Actions > Multiple actions**.
  3. In the **Authentication** section, authorize the execution with your Google Account user credentials or a service account.

     * To use your Google Account user credentials, select **Execute with user credentials**.

Optional: In the **Extended access options** section, select the additional services that your workflow requires:

       * **Knowledge Catalog** : Allows Google Cloud Knowledge Catalog metadata updates.
       * **Google Drive** : Allows read-only access to Google Drive files.
       * **Bigtable** : Allows read-only access to Google Bigtable data.
     * To use a custom service account, select **Execute with selected service account** , and then select a custom service account.

**Note:** To see service accounts in the menu, you must have the `iam.serviceAccounts.list` permission at the project level, which is available in the [View Service Accounts role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`). If you don't have this permission, you can select the service account by clicking **Enter manually** and entering the service account ID.
  4. Verify that **Selection of actions** is selected.

  5. In the **Select actions to execute** menu, select the actions that you want to run.

  6. Optional: To run the selected actions and their dependencies, select the **Include dependencies** option.

  7. Optional: To run the selected actions and the actions that depend on them, select the **Include dependents** option.

  8. Optional: To rebuild all tables from scratch, select the **Run with full refresh** option.

  9. Optional: Set the BigQuery query job priority with the **Execute as interactive job with high priority (default)** option. By default, BigQuery runs queries as [interactive query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which are intended to start running as quickly as possible. Clearing this option runs the queries as [batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which have lower priority.

  10. Click **Start execution**. If you selected **Execute with my user credentials** for your authentication method, you must authorize your Google Account.




## Manually run actions with selected tags

To manually trigger a run of actions with selected tags, follow these steps:

  1. Go to your development workspace.
  2. Click **Start execution** , then do either of the following:

     * Click **Tags** , then select a tag that you want to run.
     * Click **Tags > Multiple tags**.
  3. In the **Authentication** section, authorize the execution with your Google Account user credentials or a service account.

     * To use your Google Account user credentials, select **Execute with user credentials**.

Optional: In the **Extended access options** section, select the additional services that your workflow requires:

       * **Knowledge Catalog** : Allows Google Cloud Knowledge Catalog metadata updates.
       * **Google Drive** : Allows read-only access to Google Drive files.
       * **Bigtable** : Allows read-only access to Google Bigtable data.
     * To use a custom service account, select **Execute with selected service account** , and then select a custom service account.

**Note:** To see service accounts in the menu, you must have the `iam.serviceAccounts.list` permission at the project level, which is available in the [View Service Accounts role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`). If you don't have this permission, you can select the service account by clicking **Enter manually** and entering the service account ID.
  4. Verify that **Selection of tags** is selected.

  5. In the **Select tags to execute** menu, select the tags that you want to run.

  6. Optional: To run the actions with the selected tags and their dependencies, select the **Include dependencies** option.

  7. Optional: To run the actions with the selected tags and the actions that depend on them, select the **Include dependents** option.

  8. Optional: To rebuild all tables from scratch, select the **Run with full refresh** option. Without this option, Dataform updates incremental tables without rebuilding them from scratch.

  9. Optional: Set the BigQuery query job priority with the **Execute as interactive job with high priority (default)** option. By default, BigQuery runs queries as [interactive query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which are intended to start running as quickly as possible. Clearing this option runs the queries as [batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries#interactive-batch), which have lower priority.

  10. Click **Start execution**. If you selected **Execute with my user credentials** for your authentication method, you must authorize your Google Account.




## Authorize your Google Account

To authenticate the resource with your [Google Account](https://docs.cloud.google.com/iam/docs/principals-overview#google-account) user credentials, you must manually grant permission for BigQuery pipelines to get the access token for your Google Account and access the source data on your behalf. You can grant manual approval with the OAuth dialog interface. If you select any **Extended access options** , you must grant access to those services—for example, Google Drive or Knowledge Catalog.

**Note:** Context-Aware Access (CAA) policies—including IP-based, geolocation-based, and device compliance policies—aren't supported when executing or scheduling BigQuery pipelines with user credentials for a Google Account, because the token requests originate from Google infrastructure. CAA policies block these executions unless the Dataform OAuth client ID is [exempted from the policies](https://docs.cloud.google.com/dataform/docs/troubleshooting#euc-permission-denied).

You only need to give permission to BigQuery pipelines once.

To revoke the permission that you granted, follow these steps:

  1. Go to your [Google Account page](https://myaccount.google.com/).
  2. Click **BigQuery Pipelines**.
  3. Click **Remove access**.

**Warning:** Revoking access permissions prevents any future pipeline runs that this Google Account owns across all regions.

## What's next

  * To learn how Dataform runs incremental tables and how to configure an incremental table, see [Configure an incremental table](https://docs.cloud.google.com/dataform/docs/create-tables#configure-incremental-table).
  * To learn how to view execution logs, see [Monitor execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#monitor-execution-logs).
  * To learn how to schedule runs with Workflows and Cloud Scheduler, see [Schedule runs with Workflows and Cloud Scheduler](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflows-cloud-scheduler).
  * To learn how to schedule runs with Managed Service for Apache Airflow, see [Schedule runs with Managed Service for Apache Airflow](https://docs.cloud.google.com/dataform/docs/schedule-runs#composer). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
