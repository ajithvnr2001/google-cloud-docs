---
url: https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications/
title: Monitor job status using Pub/Sub notifications and BigQuery \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:55.019348+00:00
---

# Monitor job status using Pub/Sub notifications and BigQuery  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Monitor job status using Pub/Sub notifications and BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how you can monitor job and task state changes by setting up Pub/Sub notifications. You can use the notifications for various use cases—for example, this document explains how stream the notifications to a BigQuery table, which you can use to analyze the data. To learn more about the use cases for Pub/Sub notifications, see [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber) in the Pub/Sub documentation.

Alternatively, if you want to export all the information about a job to BigQuery, see [Export job information](https://docs.cloud.google.com/batch/docs/export-job-info) instead.

**Note:** Pub/Sub and BigQuery are separate Google Cloud products that have their own pricing. For more information, see [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing) and [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. If you want to set up Pub/Sub notifications for your Batch jobs, do the following: 
     1. Enable the Pub/Sub API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub.googleapis.com)

     2. To get the permissions that you need to configure a Pub/Sub topic and subscription, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on a project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** After you configure a Pub/Sub topic and subscription, your administrator will need to grant additional permissions to various principals to allow jobs to send notifications to that topic. Specifically, the required roles are listed on the [Create and run a job that sends Pub/Sub status notifications](https://docs.cloud.google.com/batch/docs/enable-notifications#required-roles) page. 
  3. Additional requirements vary based on the type of subscription that you decide to configure. For example, if you want to stream and analyze notifications to a BigQuery table, you must do the following: 
     1. Enable the BigQuery API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com)

     2. To ensure that the Pub/Sub service account has the necessary permissions to stream Pub/Sub notifications to BigQuery, ask your administrator to grant the [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) IAM role to the Pub/Sub service account on the Pub/Sub topic's project. **Important:** You must grant this role to the Pub/Sub service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

For more information about assigning this role, see [Assign BigQuery roles to the Pub/Sub service account](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#assign_bigquery_service_account).

     3. Ensure that any users who you want to analyze notifications in BigQuery have the required permissions. 

To get the permissions that you need to query Pub/Sub notifications in BigQuery, ask your administrator to grant you the following IAM roles: 

        * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the BigQuery table's project
        * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the BigQuery table




## Set up Pub/Sub notifications for Batch

Batch supports Pub/Sub notifications for changes to job and task states, which you can use for alerts, observability, or analysis.

To set up Pub/Sub notifications for one or more Batch jobs, complete the steps described in the following sections:

  1. Create or identify a Pub/Sub topic for your Batch jobs.
  2. Create at least one subscription for your topic to receive and use its notifications.
  3. Configure jobs to send notifications to your topic.



After you set up Pub/Sub notifications for Batch, you can optionally configure each job to send specific notifications. You can receive notifications any time job or task states change, or you can filter the notifications for specific job or task states. Notably, Pub/Sub doesn't send notifications for the first state a job or task enters; Pub/Sub only sends notifications when a job moves from one state to another.

**Important:** Due to a known issue, Pub/Sub might not send notifications for all intermediate states when a job or task changes very quickly. You can mitigate this issue by viewing state history through status events. For more information, see [Pub/Sub might not send notifications for intermediate states during quick changes](https://docs.cloud.google.com/batch/docs/known-issues#pubsub-missing-quick-states).

For more information about the attributes you can configure for Pub/Sub notifications, see [Create and run a job that sends Pub/Sub status notifications](https://docs.cloud.google.com/batch/docs/enable-notifications).

### Create or identify a Pub/Sub topic for Batch

[Create a new Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) or [identify an existing Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/list-topics) that you want to use for Batch notifications.

As explained later in this document, jobs cannot send notifications to this Pub/Sub topic until your administrator grants additional permissions that allow this.

### Create a subscription to receive and use the notifications

To receive and make use of messages published to a Pub/Sub topic, you must create at least one subscription to that topic.

For example, one option is to configure your topic to stream its notifications to BigQuery. Then, when you are running jobs that publish notifications, you can receive and analyze the notifications in a BigQuery table. For more information, see Example: Receive and use Pub/Sub notifications in BigQuery in this document.

Otherwise, to learn more about subscriptions and other subscription options, see [Subscriptions overview](https://docs.cloud.google.com/pubsub/docs/subscription-overview) in the Pub/Sub documentation.

### Configure jobs to send notifications to your topic

To configure jobs that send Pub/Sub notifications to your topic, follow the instructions on the [Create and run a job that sends Pub/Sub status notifications](https://docs.cloud.google.com/batch/docs/enable-notifications) page. Specifically, do the following:

  1. If you haven't already, ask your administrator to grant all the permissions required for jobs to send notifications to your Pub/Sub topic. These permissions are listed in the [Required roles](https://docs.cloud.google.com/batch/docs/enable-notifications#required-roles) section of that page.
  2. Create and run a job that enables Pub/Sub notifications by defining the job's `notifications` field.



## Example: Receive and use Pub/Sub notifications in BigQuery

The following sections explain an example use case for receiving and using Pub/Sub notifications in BigQuery. By configuring a subscription that streams your topic's Pub/Sub notifications to a BigQuery table, you can retain the history of job and task state changes and query those changes.

### Configure a subscription that streams notifications to BigQuery

Configure a Pub/Sub subscription that streams notifications from a topic to a BigQuery table by doing the following:

  1. If you haven't already done so, create or identify a Pub/Sub topic for Batch.

  2. If you don't already have one, [create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset).

  3. [Create a BigQuery table](https://docs.cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition) with the following schema definition:
         
         [
           {
             "name": "data",
             "type": "STRING"
           },
           {
             "name": "subscription_name",
             "type": "STRING"
           },
           {
             "name": "message_id",
             "type": "STRING"
           },
           {
             "name": "attributes",
             "type": "JSON"
           },
           {
             "name": "publish_time",
             "type": "TIMESTAMP",
             "mode": "NULLABLE"
           }
         ]
         

  4. [Create a Pub/Sub subscription that streams to BigQuery](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#create_a_subscription) and specify the following options:

     * **Topic** : select the Pub/Sub topic for Batch.
     * **Project** : select the project that contains your BigQuery table.
     * **Dataset** : select the dataset that contains your BigQuery table.
     * **Table** : select the table you created in the previous step.
     * Select **Use topic schema**.
     * Select **Write metadata**.



Now, whenever a Pub/Sub notification is sent to that topic, Pub/Sub streams that notification to the BigQuery table. After you configure jobs to send Pub/Sub notifications, you can analyze notifications in BigQuery.

### Analyze notifications in BigQuery

You can analyze notifications in BigQuery after you configure a subscription to a BigQuery table for your topic and run jobs that send notifications to your topic. To analyze the notifications in BigQuery, [run a query](https://docs.cloud.google.com/bigquery/docs/running-queries#queries) on the `attributes` column of the BigQuery table. The attributes that you can query depend on whether you configured notifications for tasks or jobs.

You can query the following attributes of task notifications:

  * `JobUID`
  * `NewTaskState`
  * `Region`
  * `TaskName`
  * `TaskUID`
  * `Type`



You can query the following attributes of job notifications:

  * `JobUID`
  * `JobName`
  * `NewJobState`
  * `Region`
  * `Type`



For example, the following query shows the `JobUID` associated with each notification:
    
    
    select attributes.JobUID from `example-table`
    

## What's next

  * Learn how to [create and run a job that sends Pub/Sub status notifications](https://docs.cloud.google.com/batch/docs/enable-notifications).
  * Learn more about [Pub/Sub subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview).
  * Learn more about [BigQuery analytics](https://docs.cloud.google.com/bigquery/docs/query-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
