---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-examples/
title: Examples of alerts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:34.568151+00:00
---

# Examples of alerts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Examples of alerts Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee lets you create complex alerts based on multiple conditions. The following sections present examples of alerts:

  * Alert for no 200 response code for 5 minutes
  * Traffic spike alert
  * Latency alert



## Alert for no 200 response code for 5 minutes

The next example creates an alert when there is no 200 response code (successful request) for 5 minutes.

**Note:** This alert will be triggered if there no API traffic at all for 5 minutes, which might not be desirable. If so, consider using a longer time interval during which you normally expect to see some traffic.

To create the alert:

  1. In the Google Cloud console, go to the **Monitoring > Alerting > Policies** page.

[Go to Create alerting policy](https://console.cloud.google.com/monitoring/alerting/policies/create)

  2. Click **Select a Metric**.
  3. Deselect the **Active** button. 

**Note:** If there is no recent API traffic data in your organization, the metric in the next step won't be displayed unless this option is unselected.

  4. Select a metric as follows: 
     1. Copy and paste the following in the **Select a metric** field: 
            
            apigee.googleapis.com/proxy/response_count

**Note:** If you are using Apigee hybrid v1.10 or v1.11, use the following metric instead: 
            
            apigee.googleapis.com/proxyv2/response_count

     2. Select **Apigee Proxy**.
     3. In the pane that opens to the right, select **Proxy**.
     4. In the next pane to the right, select **Apigee proxy response count**.
     5. Click **Apply**.
  5. Add a filter for the response code as follows: 
     1. Click **Add filter**.
     2. Click in the **Filter** field and select **response_code** from the drop-down menu.
     3. In the **Comparator** , select **=**.
     4. In the **Value** field, type **200**.
     5. Click **Apply**.



### Configure the alert trigger

To configure the event that triggers the alert, first click **Configure trigger** in the left-hand pane. Then do the following steps:

  1. Under **Condition type** , select **Metric absence**.
  2. In the **Alert trigger** field, select **Any time series violates**.
  3. In the **Metric absence time** field, select **5 min**.
  4. Optionally, in the **Condition name** field, enter a name for the condition.



With these settings, an alert will be triggered when the proxy does not receive a 200 response code for 5 minutes.

Click **Next** to open the **Configure notifications and finalize alert** pane.

### Set up a notification for the alert

In the **Configure notifications and finalize alert** pane, you can set up a notification that will be sent when an alert is triggered. To do so:

  1. Click in the **Notification Channels** field. If you have already created a channel for the notification, such as an email address or SMS number, you can select it under **Notification Channels**. 

Otherwise, you need to add a channel by selecting **Manage Notification Channels**. This opens the **Notification channels** pane, where you can add one or more channels. See [Manage notification channels](https://cloud.google.com/monitoring/support/notification-options) for more information. When you are done, return to the **Configure notifications and finalize alert** pane.

**Note:** You may need to click the refresh button next to **Manage Notification Channels** to display a new channel after you create it.

Once you have selected one or more notification channels, click **OK**.

  2. In the **Documentation** field, you can add a message that will be sent with the notification. For example, the message might describe the reason for the alert, and contain links to documentation explaining how to respond to it.
  3. Click **Next** to review the details of the alert. If you are satisfied with them, click **Create Policy** to create the alerting policy.



## Traffic spike alert

The following sections show how to create an alert that is triggered when the number of API requests over a 1 minute period exceeds 3600.

To create the alert:

  1. In the Google Cloud console, go to the **Monitoring > Alerting > Policies** page.

[Go to Create alerting policy](https://console.cloud.google.com/monitoring/alerting/policies/create)

  2. Click **Select a Metric**.
  3. Deselect the **Active** button. 

**Note:** If there is no recent API traffic data in your organization, the metric in the next step won't be displayed unless this option is unselected.

  4. Select a metric as follows: 
     1. Copy and paste the following in the **Select a metric** field: 
            
            apigee.googleapis.com/proxy/request_count

**Note:** If you are using Apigee hybrid v1.10 or v1.11, use the following metric instead: 
            
            apigee.googleapis.com/proxyv2/request_count

     2. Select **Apigee Proxy**.
     3. In the pane that opens to the right, select **Proxy**.
     4. In the next pane to the right, select **Apigee proxy request count**.
     5. Click **Apply**.
  5. In the **Transform data** pane: 
     * Under **Within each time series** : 
       * In the **Rolling window** field, select **1 min**.
       * In the **Rolling window function** , select **rate**.
     * Under **Across time series** , under **Time series aggregation** , select **sum**.



### Configure the alert trigger

To configure the event that triggers the alert, first click **Configure trigger** in the left-hand pane. Then do the following steps:

  1. Under **Condition type** , select **Threshold**.
  2. In the **Alert trigger** field, select **Any time series violates**.
  3. In the **Threshold position** field, select **Above threshold**.
  4. In the **Threshold value** field, enter **60**.



The reason you set **Threshold value** to 60 (rather than 3600) is that the units of **Threshold value** are per second. So if this threshold is maintained for 1 minute, there will be at least 3600 requests in that time period.

With these settings, an alert will be triggered when the total number of requests over a 1 minute period exceeds 3600.

Click **Next** to open the **Configure notifications and finalize alert** pane and following the steps in  Set up a notification for the alert.

## Latency alert

The following examples show how to create an alert that is triggered when the 95th percentile of the average latencies in the responses, over 10 minute intervals, is greater than 600 ms.

  * Create the alert using Apigee or Apigee hybrid v1.12
  * Create the alert using Apigee hybrid v1.10 or v1.11



###  Create the alert using Apigee or Apigee hybrid v1.12

To create the alert using Apigee:

  1. In the Google Cloud console, go to the **Monitoring > Alerting > Policies** page.

[Go to Create alerting policy](https://console.cloud.google.com/monitoring/alerting/policies/create)

  2. Click **Select a Metric**. 
  3. Deselect the **Active** button. 

**Note:** If there is no recent API traffic data in your organization, the metric in the next step won't be displayed unless this option is unselected.

  4. Select a metric as follows: 
     1. Copy and paste the following in the **Select a metric** field: 
            
            apigee.googleapis.com/proxy/latencies

     2. Select **Apigee Proxy**.
     3. In the pane that opens to the right, select **Proxy**.
     4. In the next pane to the right, select **Apigee proxy latencies**.
     5. Click **Apply**.
  5. In the **Transform data** pane, under **Within each time series** : 
     * In the **Rolling window** field, select **10 min**.
     * In the **Rolling window function** field, enter **95th percentile**. 



See Create the alert trigger to configure the event that triggers the alert.

###  Create the alert using Apigee hybrid v1.10 or v1.11

To create the alert using Apigee hybrid v1.10 or v1.11:

  1. In the Google Cloud console, go to the **Monitoring > Alerting > Policies** page.

[Go to Create alerting policy](https://console.cloud.google.com/monitoring/alerting/policies/create)

  2. Click **Select a Metric**. 
  3. Deselect the **Active** button. 

**Note:** If there is no recent API traffic data in your organization, the metric in the next step won't be displayed unless this option is unselected.

  4. Select a metric as follows: 
     1. Copy and paste the following in the **Select a metric** field: 
            
            apigee.googleapis.com/proxyv2/latencies_percentile

     2. Select **Apigee proxy (v2)**.
     3. In the pane that opens to the right, select **Proxyv2**.
     4. In the next pane to the right, select **Percentile of Apigee proxy response latencies**.
     5. Click **Apply**.
  5. Add a filter as follows:

     1. Click **Add a Filter**.
     2. Click in the **Filter** field and select **percentile** from the drop-down menu.
     3. In the **Comparator** , select **=**.
     4. In the **Value** field, type **95**.
     5. Click **Apply**.
  6. In the **Transform data** pane, under **Within each time series** : 
     * In the **Rolling window** field, select **10 min**.
     * In the **Rolling window function** field, enter **mean**.



See Create the alert trigger to configure the event that triggers the alert.

### Configure the alert trigger

To configure the event that triggers the alert, first click **Configure trigger** in the left-hand pane. Then do the following steps:

  1. Under **Condition type** , select **Threshold**.
  2. In the **Alert trigger** field, select **Any time series violates**.
  3. In the **Threshold position** field, select **Above threshold**.
  4. In the **Threshold value** field, enter **600**.



With these settings, an alert will be triggered when the 95th percentile of the latencies is above the threshold of 600 ms.

Click **Next** to open the **Configure notifications and finalize alert** pane and following the steps in  Set up a notification for the alert.

When you receive a notification and click the **View In Apigee** button in the notification email, the [Investigate dashboard](https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate) will display a latency graph with the threshold, similar to the example shown: ![Select a metric.](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/latency-graph.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
