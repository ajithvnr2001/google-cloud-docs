---
url: https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset/
title: Create a linked BigQuery dataset on a log bucket \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:20.777376+00:00
---

# Create a linked BigQuery dataset on a log bucket  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Create a linked BigQuery dataset on a log bucket Stay organized with collections  Save and categorize content based on your preferences. 

A [linked BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) on a log bucket lets you query and analyze your log data by using BigQuery services such as BigQuery Studio and Data Studio. Because a _linked BigQuery dataset_ is a read-only pointer to your log bucket, you can join log data with other datasets and create SQL-based alerting policies without duplicating data or paying for separate BigQuery storage.

You can't create a linked BigQuery dataset for an [analytics view](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views). If you aren't familiar with Observability Analytics, then see [Observability Analytics overview](https://docs.cloud.google.com/logging/docs/log-analytics).

## When you need a linked BigQuery dataset

You don't need a linked BigQuery dataset when you want to query your log data, or query your log and trace data. For those scenarios, you can use the **Observability Analytics** page. You can also save and share your queries, and you can save the query to a custom dashboard. For information about querying your trace data, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

You do need a linked BigQuery dataset when you want to do any of the following:

  * Join log entry data with other BigQuery datasets.
  * Query log data from another service like BigQuery Studio or Data Studio.
  * Create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) that monitors the result of a SQL query. For more information, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting).



A linked BigQuery dataset for a log bucket lets BigQuery read the data in the log bucket.

## How log buckets and log views map to BigQuery objects

When you create a linked BigQuery dataset for a log bucket, a new dataset becomes available to BigQuery. You specify the name of the linked BigQuery dataset during the linking process. Any log views within the log bucket are automatically mapped to [virtual views](https://docs.cloud.google.com/bigquery/docs/views-intro) in the dataset. The name of a virtual view is the same as the corresponding log view.

For example, suppose the project `my_project` has a log bucket named `example`, and that this log bucket has a log view named `_AllLogs`. If you create a linked BigQuery dataset for that log bucket with the name `my_dataset`, then the **Explorer** page of BigQuery displays a `my_project` entry. A child of the `my_project` entry is a dataset with the name `my_dataset`, and that dataset lists a virtual view named `_AllLogs`.

## Access control implications when using linked BigQuery datasets

When a principal queries a view on a linked BigQuery dataset, that query runs through the BigQuery permission layer, not the Cloud Logging permission layer. Therefore, the BigQuery roles and permissions granted to the principal on the linked BigQuery dataset determine whether they can query the dataset.

You can't restrict a principal to a specific virtual view within a linked dataset. When a principal has been granted access to the linked BigQuery dataset, they can query every view in that dataset.

## System actions that occur when you create a linked dataset

When you create a link on an observability dataset, the following occurs:

  * Google Cloud Observability might create the following service accounts or modify their IAM role grants:

    * [Monitoring Service Account](https://docs.cloud.google.com/iam/docs/service-agents#monitoring-service-account): Required to create a link to a linked BigQuery dataset. The Cloud Monitoring API must be enabled for Google Cloud Observability to create this service account.

    * [Cloud Observability Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-observability-service-account): Required to create a link on an observability dataset.

    * [Cloud Logging Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-logging-service-account): Required to create a link on a log bucket.

  * Audit logs record the request to create a link and the request from the service agent manager to grant the Monitoring Service Account the IAM role of [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent). These logs also record the completion of the long-running operation.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. To get the permissions that you need to create a linked dataset, ask your administrator to grant you the [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  7. Make sure that your log bucket has been upgraded to use Observability Analytics:

     1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

     2. If the log bucket displays **Upgrade** , then click **Upgrade** and complete the dialog.



## Create a linked BigQuery dataset

When you want to use the capabilities of BigQuery to analyze your log data, upgrade a log bucket to use Observability Analytics, and then create a [linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets). With this configuration, Logging stores your log data but BigQuery can read the log data.

**Note:** A log bucket can be linked to at most one BigQuery dataset.

###  Google Cloud console 

To create a link to a BigQuery dataset for an existing log bucket, do the following:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Locate the log bucket and verify that the **Observability Analytics available** column displays **Open**.

If this column displays **Upgrade** , then the log bucket hasn't been upgraded to use Observability Analytics. Configure Observability Analytics:

     1. Click **Upgrade**.
     2. Click **Confirm** in the dialog.

After the upgrade completes, proceed to the next step.

  3. On the log bucket, click **More** _more_vert_ , and then click **Edit bucket**.

The **Edit log bucket** dialog opens.

  4. Select **Create a new BigQuery dataset that links to this bucket** and enter the name for the new dataset.

The dataset name must be unique for each Google Cloud project. If you enter the name of an existing dataset, then you receive the following error: `Dataset name must be unique in the selected region.`

  5. Click **Done** and then click **Update bucket**.

After Logging displays the linked dataset name on the **Logs Storage** page, it might take several minutes before BigQuery recognizes the dataset.




###  gcloud 

To create a linked dataset for a log bucket that is upgraded to use Observability Analytics, run the [`gcloud logging links create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/links/create) command:
    
    
    gcloud logging links create LINK_ID --bucket=BUCKET_ID --location=LOCATION

The LINK_ID that you provide is used as the name of the BigQuery dataset, and the value of this field must be unique for your Google Cloud project.

The `links create` command is asynchronous. The return of an asynchronous method is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object, and it contains information about the progress of the method. When the method completes, the `Operation` object contains the status. For more information, see [Asynchronous API methods](https://docs.cloud.google.com/logging/docs/buckets#async-command).

The `links create` command takes several minutes to complete.

For example, the following command creates a linked dataset named `mylink` for the log bucket named `my-bucket`:
    
    
    gcloud logging links create mylink --bucket=my-bucket --location=global
    

The dataset name must be unique for each Google Cloud project. If you attempt to create a dataset with the same name as an existing dataset, then you receive the following error:

`BigQuery dataset with name "LINK_ID" already exists.`

If you attempt to create a linked dataset for a log bucket that isn't upgraded to use Observability Analytics, then the following error is reported:

`A link can only be created for an analytics-enabled bucket.`

###  REST 

To create a linked a BigQuery dataset for an existing log bucket that is upgraded use Observability Analytics, call the asynchronous [`projects.locations.buckets.links.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.buckets.links/create) method of the Cloud Logging API.

Prepare the arguments to the method as follows:

  1. Construct the request body for the `create` command. The request body is formatted as a [`Link`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.buckets.links#Link) object.
  2. For the query parameter of the command, use `linkId=LINK_ID`. The LINK_ID that you provide is used as the name of the BigQuery dataset, and the value of this field must be unique for your Google Cloud project..



The response to the asynchronous methods is an [`Operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/billingAccounts.locations.operations#Operation) object. This object contains information about the progress of the method. When the method completes, the `Operation` object contains the status. For more information, see [Asynchronous API methods](https://docs.cloud.google.com/logging/docs/buckets#async-command).

The `links.create` method takes several minutes to complete.

The dataset name must be unique for each Google Cloud project. If you attempt to create a dataset with the same name as an existing dataset, then you receive the following error:

`BigQuery dataset with name "LINK_ID" already exists.`

If you attempt to create a linked dataset for a log bucket that isn't upgraded to use Observability Analytics, then the following error is reported:

`A link can only be created for an analytics-enabled bucket.`

## What's next

  * [Query log data with BigQuery Studio](https://docs.cloud.google.com/logging/docs/analyze/query-with-bigquery-studio)
  * [Run log queries on BigQuery engine](https://docs.cloud.google.com/logging/docs/analyze/run-query-on-bigquery-engine)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
