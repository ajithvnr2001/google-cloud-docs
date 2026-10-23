---
url: https://docs.cloud.google.com/logging/docs/analyze/run-query-on-bigquery-engine/
title: Run log queries on BigQuery engine \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:22.014882+00:00
---

# Run log queries on BigQuery engine  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/run-query-on-bigquery-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Run log queries on BigQuery engine Stay organized with collections  Save and categorize content based on your preferences. 

Configuring the **Observability Analytics** page to run your log queries on the BigQuery engine lets you use [reserved slots](https://docs.cloud.google.com/bigquery/docs/reservations-intro#reservations) instead of free slots. You must also use the BigQuery engine when you create SQL-based alerting policies or save dashboard charts whose queries join observability data with other business data.

By default, the **Observability Analytics** page runs queries on the default query engine, which checks your Logging permissions. When you switch to the BigQuery engine, BigQuery permissions are checked instead. Both query engines let you query observability views, views on log buckets, and analytics views.

To learn more, see [Choose your Observability Analytics query engine](https://docs.cloud.google.com/logging/docs/analyze/data-security-with-analytics#choose-engine).

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

     * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) on the project or on the view that you want to query
     * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on your project or the linked dataset
     * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on your project

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  7. Verify that you have a [linked BigQuery dataset](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset) on your log bucket. If the dataset doesn't exist, then create it.



If you plan to configure the **Observability Analytics** page to run queries on the BigQuery engine in projects that use Virtual Private Cloud (VPC) Service Controls, then verify that you're using the Enterprise Edition of BigQuery. For more information, see [Understand BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).

## Run Observability Analytics queries on the BigQuery engine

When you want to [monitor the results of your SQL query with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting), run your queries on the BigQuery engine by doing the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Log views** list, find the view, and then select **Query** or enter a query.

If the query pane displays an error message that references the `FROM` statement, then the table can't be resolved to a specific log view. For information about how to resolve this failure, see [Error `FROM clause must contain exactly one log view`](https://docs.cloud.google.com/logging/docs/analyze/troubleshoot#bad-table-name).

  3. Go to the toolbar and verify that a button labeled **Run on BigQuery** is displayed.

If the toolbar displays **Run Query** , then click _settings_ **Settings** and select **BigQuery**.

If the **Run on BigQuery** button is disabled, then you need to create a linked dataset.

  4. Run your query.

You can use the toolbar options to format your query, clear the query, and open the BigQuery SQL reference documentation.




## Pricing

To learn about the costs associated with using BigQuery, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

## What's next

  * [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)
  * [Save and share a SQL query](https://docs.cloud.google.com/logging/docs/analyze/save-share-query)
  * [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples)
  * [Chart SQL query results](https://docs.cloud.google.com/logging/docs/analyze/charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
