---
url: https://docs.cloud.google.com/trace/docs/analytics-query-with-bigquery-studio/
title: Query trace data with BigQuery Studio \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:59.047476+00:00
---

# Query trace data with BigQuery Studio  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/analytics-query-with-bigquery-studio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Query trace data with BigQuery Studio Stay organized with collections  Save and categorize content based on your preferences. 

Querying your Cloud Trace data in BigQuery Studio lets you join spans with other business data and use the full feature set of BigQuery. You can open a SQL query directly in BigQuery Studio from the **Observability Analytics** page, which automatically formats the `FROM` clause for your [linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).

If you haven't written queries in Observability Analytics, then first see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

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

  6. To get the permissions that you need to query a linked dataset from BigQuery, ask your administrator to grant you the following IAM roles: 

     * [Observability Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewer) (`roles/observability.viewer`) on the project
     * [Observability View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`) on the observability views that you want to query. This role supports IAM conditions, which let you restrict the grant to a specific view. If you don't attach a condition to the role grant, then the principal can access all observability views.
     * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on the project or the linked BigQuery dataset
     * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  7. Verify that you have a [linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset) on the observability dataset that stores your trace data. If the linked BigQuery dataset doesn't exist, then create it.



## Run queries from BigQuery Studio

To open BigQuery from the Observability Analytics page and then query your trace data, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter or load a query. For more information, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

  3. In the toolbar, expand the menu labeled **Run query** or **Run on BigQuery** , and select **Open in BigQuery**.

BigQuery Studio opens. On this page, the `FROM` statement specifies the linked dataset by using the BigQuery [Table path syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_path). You can perform any supported actions on the query, such as editing it.

If the **Open in BigQuery** option is disabled, then either a linked dataset doesn't exist or you don't have the necessary permissions to open and view the query in BigQuery.

  4. In BigQuery Studio, click **Run query**.




## Pricing

To learn about the costs associated with using BigQuery, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/trace/docs/sql-in-alerting)
  * [Save and share a SQL query](https://docs.cloud.google.com/trace/docs/analytics-save-share-query)
  * [Chart SQL query results](https://docs.cloud.google.com/trace/docs/analytics-chart)
  * [Sample SQL queries](https://docs.cloud.google.com/trace/docs/analytics-samples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
