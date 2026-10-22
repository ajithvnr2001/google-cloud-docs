---
url: https://docs.cloud.google.com/trace/docs/analytics-run-on-bigquery-engine/
title: Run trace queries on BigQuery engine \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:11.438449+00:00
---

# Run trace queries on BigQuery engine  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/analytics-run-on-bigquery-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Run trace queries on BigQuery engine Stay organized with collections  Save and categorize content based on your preferences. 

Configuring Observability Analytics to run your Cloud Trace queries on the BigQuery engine lets you use [reserved slots](https://docs.cloud.google.com/bigquery/docs/reservations-intro#reservations) to avoid queuing delays when default slots are occupied. You must also use the BigQuery engine when you create SQL-based alerting policies or save dashboard charts whose queries join observability data with other business data.

Unless you modify the configuration, the **Observability Analytics** page runs queries on the default query engine, which uses default slots. Both engines let you query observability views, views on log buckets, and analytics views.

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

  6. To get the permissions that you need to run queries from Observability Analytics using the BigQuery engine, ask your administrator to grant you the following IAM roles: 

     * [Observability Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`) on the project
     * [Observability View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`) on the observability views that you want to query. This role supports IAM conditions, which let you restrict the grant to a specific view. If you don't attach a condition to the role grant, then the principal can access all observability views.
     * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on your project or the linked dataset
     * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on your project

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  7. Verify that you have a [linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset) on the observability dataset that stores your trace data. If the linked BigQuery dataset doesn't exist, then create it.



If you configure the **Observability Analytics** page to use the BigQuery engine in a Google Cloud project protected by Virtual Private Cloud (VPC) Service Controls, then use the Enterprise Edition of BigQuery. For more information, see [Understand BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).

## Run queries on the BigQuery engine

To run a query on the BigQuery engine when using the **Observability Analytics** page, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter or load a query. For more information, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

You can save a chart to a dashboard where the chart displays the result of a join between observability data and other business data. For this case, the `FROM` clause must specify either a view on an observability dataset or a view on a log bucket, and there must also be a linked dataset for the data queried. The `JOIN` statement can specify a BigQuery table. However, you must have the required IAM permissions to query the BigQuery table.

  3. Go to the toolbar and verify that a button labeled **Run on BigQuery** is displayed.

If the toolbar displays **Run Query** , then click _settings_ **Settings** and select **BigQuery**.

A disabled **Run on BigQuery** button indicates that there isn't a linked dataset. To resolve this failure, [create the linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).

  4. Click **Run on BigQuery**.




## Pricing

To learn about the costs associated with using BigQuery, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/trace/docs/sql-in-alerting)
  * [Save and share a SQL query](https://docs.cloud.google.com/trace/docs/analytics-save-share-query)
  * [Chart SQL query results](https://docs.cloud.google.com/trace/docs/analytics-chart)
  * [Sample SQL queries](https://docs.cloud.google.com/trace/docs/analytics-samples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
