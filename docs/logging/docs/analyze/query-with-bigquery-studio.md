---
url: https://docs.cloud.google.com/logging/docs/analyze/query-with-bigquery-studio/
title: Query log data with BigQuery Studio \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:39.052910+00:00
---

# Query log data with BigQuery Studio  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/query-with-bigquery-studio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Query log data with BigQuery Studio Stay organized with collections  Save and categorize content based on your preferences. 

Querying your log data in BigQuery Studio lets you join logs with other business data and use commands, workflows, and datasets available only in BigQuery. You can open a SQL query directly in BigQuery Studio from the **Observability Analytics** page. The query automatically formats the `FROM` clause for your [linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset).

If you aren't familiar with Observability Analytics, then see [Observability Analytics overview](https://docs.cloud.google.com/logging/docs/log-analytics).

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

  6. To get the permissions that you need to query a linked dataset from BigQuery Studio, ask your administrator to grant you the following IAM roles: 

     * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) on the project or on the view that you want to query
     * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the project or on the linked BigQuery dataset
     * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  7. Verify that you have a [linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset) on your log bucket. If the dataset doesn't exist, then create it.



## Run queries from BigQuery Studio

To open BigQuery from the Observability Analytics page and then query your log data, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Log views** list, find and select the log view.

  3. In the **Schema** pane, select **Query**.

The **Query** pane is populated with a default query. You can also enter a query in the **Query** pane, or edit a displayed query.

  4. In the toolbar, expand the button labeled **Run query** or **Run on BigQuery** , and select **Open in BigQuery**.

BigQuery Studio opens. The `FROM` statement of the query is modified to specify the path to the log view on the linked dataset by using the BigQuery [Table path syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_path).

You can also edit the displayed query.

  5. In BigQuery Studio, click **Run query**.




## Pricing

To learn about the costs associated with using BigQuery, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)
  * [Save and share a SQL query](https://docs.cloud.google.com/logging/docs/analyze/save-share-query)
  * [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples)
  * [Chart SQL query results](https://docs.cloud.google.com/logging/docs/analyze/charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
