---
url: https://docs.cloud.google.com/monitoring/alerts/target-configuration-library/
title: Settings for common alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:01.437915+00:00
---

# Settings for common alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/target-configuration-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Settings for common alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

To create an alerting policy, you must describe what is to be monitored, when the condition of the alerting policy is met, and how you want to be notified. This page contains settings that you can use to create alerting policies. Most sections in this page have the following elements:

  * **Title** : Lists the relevant product name and a brief description of the alerting policy.
  * **Summary** : A brief description of the alerting policy. For full information, see the product documentation.
  * **Steps to create an alerting policy** : Outline of the steps required to create an alerting policy. For detailed information on these steps, see [Creating an alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy). 
  * **New condition** : These fields specify what is being monitored and how the data is aggregated.

  * **Condition alert trigger** : These fields specify when the condition of an alerting policy is met. By changing the [retest window](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#duration-window), you can reduce how often the condition is met. 

When you only want to configure a chart that displays quota data, you can use the settings in the **New condition** table. Alerting conditions use different notation than charting tools. Charting tools include [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) and configuring charts on [custom dashboards](https://docs.cloud.google.com/monitoring/charts): **New condition** dialog  
field name | Charts  
---|---  
**Rolling window function** | Optimally configured based on selected metric and aggregation settings. To specify the alignment function, do the following: 

  1. In the **Aggregation** element, expand the first menu and select **Configure aligner**. The **Alignment function** and **Grouping** elements are added.
  2. Expand the **Alignment function** element and make a selection.

  
**Rolling window** | **Min Interval**  
(to access, click _add_ **Add query element**)  
**Time series group by**  
(in the **Across time series** section) | **Aggregation** element's second menu  
**Time series aggregation**  
(in the **Across time series** section) | **Aggregation** element's first menu  
  
## Billing

To be notified if your billable or forecasted charges exceed a budget, create an alert by using the **Budgets and alerts** page of the Google Cloud console:

  1. In the Google Cloud console, go to the **Billing** page: 

[Go to **Billing**](https://console.cloud.google.com/billing)

You can also find this page by using the search bar.

If you have more than one Cloud Billing account, then do one of the following:

     * To manage Cloud Billing for the current project, select **Go to linked billing account**.
     * To locate a different Cloud Billing account, select **Manage billing accounts** and choose the account for which you'd like to set a budget.
  2. In the Billing navigation menu, select **Budgets & alerts**.
  3. Click add_box **Create budget**.
  4. Complete the budget dialog. In this dialog, you select Google Cloud projects and products, and then you create a budget for that combination. By default, you are notified when you reach 50%, 90%, and 100% of the budget. For complete documentation, see [Set budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets). **Note:** In the billing dialog, use the following settings: 
     * To create an alert on Cloud Logging usage, select **Cloud Logging**
     * To create an alert on Cloud Monitoring usage, select **Stackdriver Monitoring**
     * To create an alert on Cloud Trace usage, select **Stackdriver Trace**



## BigQuery execution time

To create an alerting policy that triggers when the 99th percentile of the execution time of a [BigQuery](https://docs.cloud.google.com/bigquery/docs) query exceeds a user-defined limit, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **BigQuery Project**.  
In the **Metric categories** menu, select **Query**.  
In the **Metrics** menu, select **Query execution times**.   
**Filter** |   
**Across time series  
Time series group by** | `priority`  
**Across time series  
Time series aggregation** | `99th percentile`  
  
**Rolling window** | `5 m`  
  
**Rolling window function** | `sum`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | You determine this value; however, a threshold of 60 seconds is recommended.  
**Retest window** |  `most recent value`  
  
## BigQuery usage

To create an alerting policy that triggers when the ingested [BigQuery](https://docs.cloud.google.com/bigquery/docs) metrics exceed a user-defined level, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **BigQuery Dataset**.  
In the **Metric categories** menu, select **Storage**.  
Select a metric from the **Metrics** menu. Metrics specific to usage include `Stored bytes`, `Uploaded bytes`, and `Uploaded bytes billed`. For a full list of available metrics, see [BigQuery metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery).   
**Filter** | **project_id** : Your Google Cloud project ID.  
**dataset_id** : Your dataset ID.  
**Across time series  
Time series group by** | **dataset_id** : Your dataset ID.  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `1 m`  
  
**Rolling window function** | `mean`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | You determine the acceptable value.  
**Retest window** | `1 minute`  
  
## Bigtable storage utilization

To create an alerting policy that triggers when the storage utilization for your [Bigtable](https://docs.cloud.google.com/bigtable/docs) cluster is above a recommended threshold, such as 70%, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Cloud Bigtable Cluster**.  
In the **Metric categories** menu, select **Cluster**.  
In the **Metrics** menu, select **Storage utilization**.  
  
(The metric.type is `bigtable.googleapis.com/cluster/storage_utilization`).   
**Filter** | `cluster = YOUR_CLUSTER_ID`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Condition triggers if** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** |  70   
**Retest window** | `10 minutes`  
  
## Compute Engine early boot validation

**Early Boot Validation** shows the pass/fail status of the early boot portion of the last boot sequence. Early boot is the boot sequence from the start of the UEFI firmware until it passes control to the bootloader.

To create an alerting policy that triggers when the early boot sequence fails for any of your [Compute Engine](https://docs.cloud.google.com/compute/docs) VM instances, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **VM Instance**.  
In the **Metric categories** menu, select **Instance**.  
In the **Metrics** menu, select **Early boot validation**.   
**Filter** | `status = failed`  
**Across time series  
Time series group by** | `status`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | Use default.  
  
**Rolling window function** | Use default  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | `0`  
**Retest window** | `1 minute`  
  
## Compute Engine late boot validation

**Late Boot Validation** shows the pass/fail status of the late boot portion of the last boot sequence. Late boot is the boot sequence from the bootloader until completion. This includes the loading of the operating system kernel.

To create an alerting policy that triggers when the late boot sequence fails for any of your [Compute Engine](https://docs.cloud.google.com/compute/docs) VM instances, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **VM Instance**.  
In the **Metric categories** menu, select **Instance**.  
In the **Metrics** menu, select **Late boot validation**.   
**Filter** | `status = failed`  
**Across time series  
Time series group by** | `status`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | Use default.  
  
**Rolling window function** | Use default  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | `0`  
**Retest window** | `1 minute`  
  
## Logging monthly log bytes ingested

To create an alerting policy that triggers when the number of log bytes written to your log buckets exceeds your user-defined limit for [Cloud Logging](https://docs.cloud.google.com/logging/docs), use the following settings.

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
In the **Metric categories** menu, select **Logs-based metric**.  
In the **Metrics** menu, select **Monthly log bytes ingested**.   
**Filter** | None.  
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
**Threshold value** | You determine the acceptable value.  
**Retest window** | Minimum acceptable value is 30 minutes.  
  
## Recommendations prediction

To set up a [Recommendations](https://docs.cloud.google.com/retail/docs) prediction alert, use the following settings in the alerting policy.

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
**Filter** | `service = recommendationengine.googleapis.com  
method = google.cloud.recommendationengine.v1beta1.PredictionService.Predict  
response_code != 200`  
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
**Retest window** | `5 minutes`  
  
## Recommendations user event recording reduction

To set up a [Recommendations](https://docs.cloud.google.com/retail/docs) event recording reduction alert, use the following settings in the alerting policy.

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
**Filter** | `service = recommendationengine.googleapis.com  
method = google.cloud.recommendationengine.v1beta1.PredictionService.CollectUserEvent  
response_code != 200`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `1 m`  
  
**Rolling window function** | `sum`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Metric absence`  
**Alert trigger** | `Any time series violates`  
**Trigger absence time** | `10 minutes`  
  
## Spanner high priority CPU usage

To create an alerting policy that triggers when your high priority cpu utilization for [Spanner](https://docs.cloud.google.com/spanner/docs) is above a recommended threshold, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Spanner Instance**.  
In the **Metric categories** menu, select **Instance**.  
In the **Metrics** menu, select **CPU Utilization by priority**.  
  
(The metric.type is `spanner.googleapis.com/instance/cpu/utilization_by_priority`).   
**Filter** | `instance_id = YOUR_INSTANCE_ID`  
`priority = high`  
**Across time series  
Time series group by** | `location` for multi-region instances;   
leave it blank for regional instances.   
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `10 m`  
  
**Rolling window function** | `mean`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | `45%` for multi-region instances;   
`65%` for regional instances.   
**Retest window** | `10 minutes`  
  
## Spanner 24 hour rolling usage

To create an alerting policy that triggers when the 24 hour rolling average of your cpu utilization for [Spanner](https://docs.cloud.google.com/spanner/docs) is above a recommended threshold, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Spanner Instance**.  
In the **Metric categories** menu, select **Instance**.  
In the **Metrics** menu, select **Smoothed CPU utilization**.  
  
(The metric.type is `spanner.googleapis.com/instance/cpu/smoothed_utilization`).   
**Filter** | `instance_id = YOUR_INSTANCE_ID`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `10 m`  
  
**Rolling window function** | `mean`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold** | `90%`  
**Retest window** | `10 minutes`  
  
## Spanner storage

To create an alerting policy that triggers when your storage for your [Spanner](https://docs.cloud.google.com/spanner/docs) instance is above a recommended threshold, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Spanner Instance**.  
In the **Metric categories** menu, select **Instance**.  
In the **Metrics** menu, select **Storage used**.  
  
(The metric.type is `spanner.googleapis.com/instance/storage/utilization`).   
**Filter** | `instance_id = YOUR_INSTANCE_ID`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `10 m`  
  
**Rolling window function** | `max`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Condition triggers if** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** |  You don't need to set a specific threshold for the maximum storage per node. However, we recommended that you set up an alert for when you are approaching the maximum storage limit. To learn more, see [Storage utilization metrics](https://docs.cloud.google.com/spanner/docs/storage-utilization#recommended-max).   
**Retest window** | `10 minutes`  
  
## Trace over quota on API usage

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
  
## Trace monitor monthly span-usage

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
  
## Trace export errors

To create an alerting policy that triggers if there are errors exporting [Cloud Trace](https://docs.cloud.google.com/trace/docs) data to BigQuery, use the following settings.

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
**Resource and Metric** | In the **Resources** menu, select **Cloud Trace**.  
In the **Metric categories** menu, select **Bigquery_export**.  
In the **Metrics** menu, select **Spans Exported to BigQuert**.   
**Filter** | `status != ok`  
**Across time series  
Time series group by** | `status`  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `1 m`  
  
**Rolling window function** | `rate`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | `0`  
**Retest window** | `1 minute`  
  
## Uptime check monitoring

To create an alerting policy for an uptime check, or to create a chart that displays the success or latency status of an uptime check, see [Alerting on uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
