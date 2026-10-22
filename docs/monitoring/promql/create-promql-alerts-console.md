---
url: https://docs.cloud.google.com/monitoring/promql/create-promql-alerts-console/
title: Create PromQL-based alerting policies (Console) \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:39.802026+00:00
---

# Create PromQL-based alerting policies (Console)  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/promql/create-promql-alerts-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create PromQL-based alerting policies (Console) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create PromQL-based alerting policies by using the Google Cloud console.

## Before you begin

  1. To get the permissions that you need to create PromQL-based alerting policies in the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  2. Ensure that you're familiar with the general concepts of alerting policies and PromQL in Cloud Monitoring. For more information, see the following topics:

     * [Alerting overview](https://docs.cloud.google.com/monitoring/alerts)
     * [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql)
  3. Configure the notification channels that you want to use to receive any alerts. For redundancy purposes, we recommend that you create multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  4. If the PromQL query in your alerting policy references any metrics, then the metrics must already exist in Monitoring when you create the alerting policy.




## Create PromQL alerting policies

To create a PromQL-based alerting policy from the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. On the **Alerting** page, click **Create Policy**.

  3. Under **Policy configuration mode** , select **Code editor (MQL or PromQL)**.

  4. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

  5. Enter the PromQL query that selects the data you want to monitor. If **Auto-run** isn't enabled, then click **Run Query**.

For example, the following query summarizes the rate of billing logging data ingested over a 60-second interval and determines whether the summarized rate is over 300 bytes:
         
         sum(rate(logging_googleapis_com:billing_bytes_ingested{monitored_resource="global"}[60s]))>300
         

After you run your query, you see a chart. For one project, this query produced the following result:

![Chart from a PromQL alerting condition after specifying the alert.](https://docs.cloud.google.com/static/monitoring/images/promql-chart.png)

  6. Click **Next** , and then do the following:

     1. Select a **Retest window**. This field defines for how long the condition must be satisfied before the alerting policy is triggered.

The default value is **0 sec**. With this setting, a single measurement can result in a notification. For more information and an example, see [Alignment period and duration settings](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration).

     2. To select how often alerting evaluates the PromQL query, choose a value for the **Evaluation interval**.

**Note:** Alerts created by a PromQL-based alerting policy don't follow the alerting policy autoclose duration. Instead, the alert is automatically closed when it reaches a set time after the last time the condition was met. This time is the larger of 270 seconds and twice the condition's evaluation interval. 
     3. Enter a name for the condition and click **Next**.

  7. Click **Next** , and then do the following:

     1. Add [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

     2. Choose a severity level for alerts.

     3. Optional: Add [alerting policy labels](https://docs.cloud.google.com/monitoring/alerts/labels) and [documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

     4. Enter a name for the alerting policy.

  8. Click **Create policy**.




For complete steps, see [Managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
