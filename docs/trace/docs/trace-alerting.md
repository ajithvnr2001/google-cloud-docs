---
url: https://docs.cloud.google.com/trace/docs/trace-alerting/
title: Monitor trace quota usage and spans ingested \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:11.182723+00:00
---

# Monitor trace quota usage and spans ingested  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-alerting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Monitor trace quota usage and spans ingested Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring alerting policies let you track Cloud Trace monthly span volume, API quota limits, and span ingestion rates so that you receive notifications before exceeding quotas or incurring unexpected ingestion costs. If you're new to alerting, see [Create and manage alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

For information about how to monitor the result of a SQL query that you run in Observability Analytics, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/trace/docs/sql-in-alerting).

## Monitor over-quota Cloud Trace API usage

To create an alerting policy that triggers when your monthly [Cloud Trace](https://docs.cloud.google.com/trace/docs) spans ingested exceeds your quota, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Consumed API**.  
In the **Metric categories** menu, select **Api**.  
In the **Metrics** menu, select **Request count**.  
  
(The metric.type is `serviceruntime.googleapis.com/api/request_count`).   
**Filter** | `service = cloudtrace.googleapis.com  
response_code = 429`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `1 m`  
  
**Rolling window function** | `sum`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | `0`  
**Retest window** | `1 minute`  
  
## Monitor monthly span ingestion

To create an alerting policy that triggers when your monthly [Cloud Trace](https://docs.cloud.google.com/trace/docs) spans ingested exceeds a user-defined limit, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Global**.  
In the **Metric categories** menu, select **Billing**.  
In the **Metrics** menu, select **Monthly trace spans ingested**.   
**Filter** |   
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `60 m`  
  
**Rolling window function** | `max`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**`Threshold value`** | You determine the acceptable value.  
**Retest window** | Minimum acceptable value is 30 minutes.  
  
## Monitor rate of span ingestion

You can also monitor the rate at which spans are ingested. To monitor ingestion rates, select the metric type **Trace spans ingested**. The default settings in the **Transform data** and **Across time series** sections are appropriate for this metric type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
