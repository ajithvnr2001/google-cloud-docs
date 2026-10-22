---
url: https://docs.cloud.google.com/artifact-registry/docs/configure-monitoring-notifications/
title: Configure monitoring notifications for repository growth \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:42.069696+00:00
---

# Configure monitoring notifications for repository growth  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/configure-monitoring-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure monitoring notifications for repository growth Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an alerting policy that can notify you when the Artifact Registry repository growth exceeds a limit. These instructions are for the Google Cloud console.

For more information about alerting policies, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

## Before you begin

  1. To get the permissions that you need to create and modify alerting policies by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  2. Ensure that you're familiar with the general concepts of alerting policies. For information about these topics, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

  3. Configure the notification channels that you want to use to receive any notifications. For redundancy purposes, we recommend that you create multiple types of notification channels. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).




## Create an alerting policy

To get notified when your Artifact Registry repository size grows beyond a specific size, create an alerting policy. The alerting policy monitors the size of your repository and when that size exceeds the threshold you specify, notifications are sent to all notification channels attached to the alerting policy. 

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **Artifact Registry Repository**.  
In the **Metric categories** menu, select **Repository**.  
In the **Metrics** menu, select **Repository size**.   
  
To show all metric types, even those without data, click **Active**. By default, the menus only show metric types with data. For more information, see [Metric not listed in menu](https://cloud.google.com/monitoring/alerts/using-alerting-ui#not-listed).   
**Filter** | Optional.  


  * Use the `resource_container` label to alert for a project or organization by entering the project ID or organization ID.
  * Use the `repository_id` label to alert for a specific repository. For more information, see [Filter the selected time series](https://cloud.google.com/monitoring/alerts/using-alerting-ui#filter-option).

  
**Across time series  
Time series aggregation** | `none`  
  
**Rolling window** | Use default.  
  
**Rolling window function** | `max`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | Set to the size of the repository in bytes that triggers the alert. For example, to trigger an alert if repository size grows larger than 0.5GB, set the threshold value to `500000000`.  
**Retest window** | The default value is `No retest`. With this setting, a single measurement can result in a notification. For more information and an example, see [Alignment period and duration settings.](https://cloud.google.com/monitoring/alerts/concepts-indepth#duration)  
  
## What's next

  * To learn more about metric-threshold alerting policies, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).
  * To view available Artifact Registry metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-artifactregistry)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
