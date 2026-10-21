---
url: https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset/
title: Create a linked BigQuery dataset \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:57.486176+00:00
---

# Create a linked BigQuery dataset  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Create a linked BigQuery dataset Stay organized with collections  Save and categorize content based on your preferences. 

A linked [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets) on your observability dataset lets you query Cloud Trace data by using BigQuery services. You can then join trace data with business datasets and analyze spans by using BigQuery Studio or the BigQuery API.

If you use Observability Analytics, then you can query trace data with SQL and join your trace and log data without creating a linked BigQuery dataset. For more information, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics) and [Query and analyze logs](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).

## When you need a linked dataset

You need a linked BigQuery dataset when you want to do any of the following:

  * Join trace data with other BigQuery datasets.
  * Query trace data from another service like BigQuery Studio or Data Studio.
  * [Run queries from the **Observability Analytics** page on the BigQuery engine](https://docs.cloud.google.com/trace/docs/analytics-run-on-bigquery-engine).

The **Observability Analytics** page automatically runs queries on the default query engine, which uses free slots. However, you can configure this page to run queries on the BigQuery engine.

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/trace/docs/sql-in-alerting).

  * Run automated data pipelines, continuous analytical queries, or AI agent workflows that programmatically read high volumes of trace data without Trace API rate limits.




## Create a linked BigQuery dataset

This section describes how to create a linked BigQuery dataset on an observability dataset, which lets you use BigQuery services to query your trace data. Each observability dataset supports one linked BigQuery dataset.

When you create a link on an observability dataset, the following occurs:

  * Google Cloud Observability might create the following service accounts or modify their IAM role grants:

    * [Monitoring Service Account](https://docs.cloud.google.com/iam/docs/service-agents#monitoring-service-account): Required to create a link to a linked BigQuery dataset. The Cloud Monitoring API must be enabled for Google Cloud Observability to create this service account.

    * [Cloud Observability Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-observability-service-account): Required to create a link on an observability dataset.

    * [Cloud Logging Service Account](https://docs.cloud.google.com/iam/docs/service-agents#cloud-logging-service-account): Required to create a link on a log bucket.

  * Audit logs record the request to create a link and the request from the service agent manager to grant the Monitoring Service Account the IAM role of [Monitoring Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent). These logs also record the completion of the long-running operation.




### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Monitoring and Observability APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Monitoring and Observability APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com,observability.googleapis.com)

  8. To get the permissions that you need to create a link on an observability dataset, ask your administrator to grant you the [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Create dataset

###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * LINK_ID: The name of the BigQuery dataset.
  * DATASET_ID: The ID of the dataset. Your trace data is stored in a dataset named `Spans`.
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * LOCATION: The location of the observability bucket.
  * PROJECT_ID: The identifier of the project.



Execute the [`gcloud observability buckets datasets links create`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/buckets/datasets/links/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability buckets datasets links create \
      projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID \
     --dataset=DATASET_ID\
     --bucket=BUCKET_ID \
     --location=LOCATION \
     --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability buckets datasets links create `
      projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID `
     --dataset=DATASET_ID`
     --bucket=BUCKET_ID `
     --location=LOCATION `
     --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability buckets datasets links create ^
      projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID ^
     --dataset=DATASET_ID^
     --bucket=BUCKET_ID ^
     --location=LOCATION ^
     --project=PROJECT_ID

The create command initiates a long-running operation. The following is an example of a response when the command is successful: 
    
    
    Create request issued for: [mydataset]
    Waiting for operation [projects/my-project/locations/us/operations/operation-1775164903749-64e80c9817833-9ff804b6-c3e9cbe7] to complete...done.
    Created link [mydataset].
    

###  Terraform 

To create a link on an observability dataset, use the Terraform resource [`google_observability_link`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_link) and set the following fields:

  * `project`: The ID of your project.
  * `location`: The location of the link. This location must match the location of the observability bucket.
  * `bucket`: The ID of the observability bucket. For example, `_Trace`.
  * `dataset`: The ID of the observability dataset. For example, `Spans`.
  * `link_id`: The ID of the BigQuery dataset.



You can also update and delete links.

###  REST 

To create a link to a BigQuery dataset, send a request to the [`projects.locations.buckets.datasets.links.create`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.links/create) endpoint.

You must specify the parent parameter, which has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID
    
    

The fields in the preceding expression have the following meanings:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
  * BUCKET_ID: The ID of the observability bucket. For example, this ID might be `_Trace`.
  * DATASET_ID: The ID of the dataset being queried. For example, this ID might be `Spans`.



This command requires a query parameter and a request body:

  * The query parameter, `linkId`, must be specified and set to the name of the BigQuery dataset. For example, `linkId="my_link"`. The BigQuery dataset name must be unique for your Google Cloud project, and must be limited to 100 characters and can include only letters, digits, and underscores.

  * The request body is a [`Link`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.buckets.datasets.links#Link) object. The value of the `name` field has the following format:
        
        projects/PROJECT_ID/locations/LOCATION/buckets/BUCKET_ID/datasets/DATASET_ID/links/LINK_ID
        

The value you provide for the `name` field must match the linked BigQuery dataset referenced by the query parameter.

The LINK_ID field is the name of the BigQuery dataset.




The response is an [`Operation`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/folders.locations.operations#Operation) object. This object contains information about the progress of the method. When the method completes, the `Operation` object contains status data.

For a complete list of Observability API endpoints, see the [Observability API reference documentation](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest).

If you encounter permission errors when creating a linked dataset, then see [Troubleshoot permission errors](https://docs.cloud.google.com/trace/docs/troubleshooting#linked-dataset-permission-error).

## What's next

  * [Query trace data with BigQuery Studio](https://docs.cloud.google.com/trace/docs/analytics-query-with-bigquery-studio)
  * [Run queries on BigQuery engine](https://docs.cloud.google.com/trace/docs/analytics-run-on-bigquery-engine)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
