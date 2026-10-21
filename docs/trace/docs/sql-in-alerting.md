---
url: https://docs.cloud.google.com/trace/docs/sql-in-alerting/
title: Monitor your SQL query results with an alerting policy \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.566640+00:00
---

# Monitor your SQL query results with an alerting policy  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/sql-in-alerting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Monitor your SQL query results with an alerting policy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

SQL-based alerting policies in Observability Analytics periodically run SQL queries against your Cloud Trace data and send you notifications when the results satisfy conditions that you specify. These policies run on the BigQuery engine and require a [linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).

For general information about Observability Analytics, see [Query and analyze traces with Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics).

## How alerting policies work

An alerting policy describes the circumstances under which you want to be alerted and how you want to be notified about an alert. There are a few different approaches that you can use to get notified when content or patterns appear in your trace data:

  * To monitor the number of Cloud Trace spans ingested per month, your quota usage, and your rate of span ingestion, create alerting policies in Cloud Monitoring. If you have never created an alerting policy, then see [Create alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) for detailed information about using the Cloud Monitoring console.

  * To view or explore individual traces or spans, or view attributes that are attached to spans, use the **Trace Explorer** page. For information about that page, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

  * To monitor aggregate analysis of your trace data, combine Observability Analytics with alerting policies. In this scenario, you use SQL queries to query the `_AllSpans` view on the observability bucket named `_Trace`. Finally, you create the alerting policy to monitor the SQL-query results. This type of alerting policy is called a _SQL-based alerting policy_.

To learn more about how your trace data is stored, see [Storage overview](https://docs.cloud.google.com/trace/docs/storage-overview).

The remainder of this document describes how to use SQL-based alerting policies.




### Alerting policy components

A SQL-based alerting policy contains a condition and a schedule:

  * The _condition_ contains the _query_ , which is a SQL query that queries your data. The condition also defines the circumstances under which the query result causes Monitoring to create an alert.

  * The _schedule_ defines how frequently the alerting policy runs its query. The schedule also defines the size of the _lookback window_ , which is a filter that selects only data that has been received since the previous time the query was evaluated. For example, if you set the schedule to 60 minutes, then the query is run every 60 minutes using a lookback window that selects the most-recent 60 minutes of data.




Alerting policies also contain a list of [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). When the condition of the alerting policy is met, Cloud Monitoring creates an alert and then sends notifications about the alert through these channels. An _alert_ is a record of the data that caused the condition to be met along with other relevant information. This information can help you troubleshoot the issues that caused the alert. You can view the alert by using the Google Cloud console.

### Evaluation types for SQL-based alerting policies

Conditions that monitor a SQL query result support two types of evaluation:

  * **Row count threshold** : The condition is met when the number of rows in the query result is greater than, equal to, or less than a threshold value.

  * **Boolean** : The condition is met when a specific boolean column in the query result table contains any row with a value of `true`.




Alerting policies that monitor a SQL query result must have only one condition.

### Alerting policies and BigQuery

For an alerting policy to query your trace data, you must configure a [linked BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction#linked_datasets). Linked BigQuery datasets let BigQuery read your trace data, and they let you perform BigQuery functions on the data returned by your SQL query.

When an alerting policy runs a SQL query, that query is run on the BigQuery engine in the Google Cloud project where the alerting policy is defined. By default, queries run on the BigQuery engine use on-demand slots. On-demand slots and reserved slots are subject to [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

You can also choose to configure dedicated BigQuery slot reservations for your project:

  1. [Create a reservation with dedicated slots](https://docs.cloud.google.com/bigquery/docs/reservations-tasks#create_a_reservation_with_dedicated_slots) or identify an existing reservation.
  2. [Create reservation assignments for your project](https://docs.cloud.google.com/bigquery/docs/reservations-assignments#create_reservation_assignments).



### Lookback window and alert propagation time

When an alerting policy is scheduled to evaluate its condition, Observability Analytics delays the SQL query execution by five minutes to provide time for Cloud Logging to index the data received during the lookback window. For example, if the alerting policy uses a lookback window that ends at 2:00 PM, then Observability Analytics doesn't execute the SQL query until 2:05 PM.

If the alert condition is met after the query is executed, then it can take up to two additional minutes for the alert to propagate through the system.

### Query failures

Queries issued by SQL-based alerting policies can fail for various reasons, including the following:

  * The Monitoring Service Account no longer exists or it no longer has the necessary permissions to read the trace data that is being queried.

  * The query execution time exceeds five minutes.

  * An internal error occurs.




A failed query generates a log entry containing the alert policy ID and the error status. You can use a [log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) to create an alert when an error is logged.

## Before you begin

This section assumes that you have a [linked BigQuery dataset for your trace data](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset).

Before you create a SQL-based alerting policy, complete the following steps:

  1. To get the permissions that you need to query trace data and create SQL-based alerting policies, ask your administrator to grant you the following IAM roles: 

     * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) on your project
     * [SQL Alert Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.sqlAlertWriter) (`roles/logging.sqlAlertWriter`) on your project
     * [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`) on your project
     * [Observability View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`) on your project or the observability view
     * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on your project or the linked dataset
     * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`) on your project

  2. Verify that the [Monitoring Service Account](https://docs.cloud.google.com/iam/docs/service-agents#monitoring-service-account) exists and that it has the following roles:

     1. [Monitoring Service Agent (`roles/monitoring.notificationServiceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationServiceAgent) on your project.
     2. [BigQuery Data Viewer (`roles/bigquery.dataViewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) on your linked BigQuery dataset.

If the Monitoring Service Account doesn't exist, then see [Troubleshoot: No Monitoring Service Account](https://docs.cloud.google.com/logging/docs/analyze/troubleshoot#alert-no-service-account).

  3. Configure the notification channels that you want to use to receive notifications for alerts. For redundancy purposes, we recommend that you configure multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). 



## Create a SQL-based alerting policy

To create a SQL-based alerting policy, do the following:

###  Console 

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. On the **Observability Analytics** page, in the query editor, enter a SQL query that queries your trace data.

  3. On the toolbar, click **Run on BigQuery**.

Observability Analytics runs your query on the BigQuery engine and displays the results in the **Results** table.

If **Run on BigQuery** isn't shown, then click _settings_ **Select query engine** and then click **BigQuery**. The **Run query** button changes to **Run on BigQuery**.

  4. On the **Results** table of the **Observability Analytics** page, click _add_alert_ **Create alert**.

The **Observability Analytics** page shows the **Create sql alert policy** window, which shows your query under the **SQL query** section.

  5. In the **Alert condition** section, configure the condition and schedule of your alerting policy.

  6. Configure the alert details of your alerting policy.

     1. Add [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options) and configure notification content, such as a custom subject line.

     2. Optional: Add [alerting policy labels](https://docs.cloud.google.com/monitoring/alerts/labels) and [documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

     3. Click **Next**.

  7. Review your alerting policy and then create it by clicking **Save**.




###  Terraform 

  1. [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) for you project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  2. In the Cloud Shell, go to the directory that contains your Terraform configuration.

  3. In your Terraform configuration, configure an instance of the [google_monitoring_alert_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy) resource, including [condition_sql](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/monitoring_alert_policy#condition_sql-1terraform-alert-sql).

  4. In the Cloud Shell, enter `terraform apply`.




To modify your alerting policy, make your edits and then re-apply the Terraform configuration. For more information, see [Manage alerting policies with Terraform](https://docs.cloud.google.com/monitoring/alerts/manage-alerts-terraform).

For general information about using Google Cloud with Terraform, see [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

###  REST 

Use the [`alertPolicies.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create) method to programmatically create alerting policies. The [`Condition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition) type of your alerting policy must be `MonitoringQueryLanguageCondition`, which is an instance of [`SqlCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#sqlcondition). This condition type allows the conditions of your alerting policy to be defined with SQL.

To define the schedule, set a `periodicity` value for one of the `minutes`, `hours`, or `days` fields. For example, if you want the query to run every 12 hours, then set the periodicity of the `hours` field to 12.

To define the condition, use the following fields:

  * `boolean_test`: Configures the alerting policy so that its condition is met when a row of a boolean column in the query result table contains a true value.
  * `row_count_test`: Configures the alerting policy so that its condition is met when the number of rows in the query result table meets a certain threshold.



For a complete list of fields and definitions, see [`SqlCondition`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#sqlcondition) in the Cloud Monitoring API documentation.

For more information about the Monitoring API for alerting policies, see [Managing alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api).

## Limitations

  * You can have one condition per SQL-based alerting policy.


  * SQL-based alerting policies can't query an [analytics view](https://docs.cloud.google.com/trace/docs/about-analytics-views).


  * Queries issued by SQL-based alerting policies fail when their execution time exceeds five minutes.

  * There is a delay of up to seven minutes, plus the query execution time, between when a query is scheduled and when an alert is created.




For a full list of limits associated with alerting policies, see [Monitoring limits](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

## What's next

  * [Query a linked BigQuery dataset](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)
  * [Sample SQL queries](https://docs.cloud.google.com/trace/docs/analytics-samples)
  * [Save and share a SQL query](https://docs.cloud.google.com/trace/docs/analytics-save-share-query)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
