---
url: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics/
title: View AI developer tools metrics \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:42.930707+00:00
---

# View AI developer tools metrics  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  View AI developer tools metrics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

This document describes how to view usage metrics and telemetry for [AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview) in your organization, such as Google Antigravity and the Antigravity CLI. These metrics show user adoption, token consumption, API calls, and tool execution.

## Before you begin

Before you view AI developer tools metrics, make sure you meet the following prerequisites:

  * **Turn on AI developer tools** : To view AI developer tools metrics, your organization must turn on AI developer tools for the project. See [Turn on AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings#enable-ai-developer-tools).

  * **Invoiced Cloud Billing account** : Your project needs Cloud Billing enabled and an invoiced account. See [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

  * **Supported editions** : Users need a subscription to the Gemini Enterprise Standard, Plus, Standard Emerging Market, or Pay-as-you-go edition.

**Note:** Gemini Enterprise Standard Emerging Market edition is available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility.
  * **Required roles** : To access the **Developer tools metrics** page in the Google Cloud console, you need the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) role.




## Access the metrics dashboard

To view AI developer tools metrics in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Go to Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise)

  2. Select the Google Cloud project where you enabled AI developer tools.

  3. In the navigation menu, click **Developer tools metrics**.

  4. Use the time-range controls in the top-right corner of the dashboard to adjust the reporting timeframe:

Control | Description  
---|---  
schedule **Time-range selector menu** |  By default, the dashboard displays data for **Last 1 day** with automatic live refreshing enabled. Click the menu to do any of the following: 
     * Type a custom duration directly into the **Relative time** filter field (for example, `15m`, `1h`, `1d`, or `1w`). 
     * Select a preset relative timeframe: **Today** , **Yesterday** , **Last 15 minutes** , **Last 30 minutes** , **Last 1 hour** , **Last 3 hours** , **Last 6 hours** , **Last 12 hours** , **Last 1 day** , **Last 2 days** , **Last 7 days** , or **Last 14 days**. 
     * Click **Start and end times** to specify a custom start and end date and time for the reporting window. 
     * Click **Around a time** to specify a date and time and display metrics centered around that timestamp. 
     * Click **Time zone** to select a different display timezone for the charts (for example, **PDT (UTC-7)**).   
chevron_left chevron_right **Left and right arrows** |  Shift the reporting timeframe backward (`chevron_left`) or forward (`chevron_right`) in time by the duration selected in the menu. For example, if **Last 1 day** is selected, clicking `chevron_left` shifts the charts backward by one day.   
search **Zoom out of time range** |  Click search to zoom out of a specific time range. All charts update to show data for the zoomed-out time range. To zoom in and reset the view, select a duration from the **Time-range selector menu**.   
sync sync_disabled **Auto-refresh** |  Toggle automatic live refreshing of dashboard data on or off when viewing a relative timeframe. When an absolute time range is selected (such as custom start and end times or a historical window), auto-refresh is disabled because auto-refresh isn't supported for absolute time ranges.   



## Explore chart data

Each chart on the **Developer tools metrics** dashboard provides interactive controls to help you inspect time series, correlate metrics with logs, and analyze underlying data:

Control | Description  
---|---  
info **Information** |  Next to the chart title, click **Information** to view details about the filters, groupings, and aggregation properties applied to the chart's metric query.   
add_alert **Create alert policy** |  On metric line charts, click **Create alert policy** in the chart toolbar to open the [alerting workflow](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) in Cloud Monitoring pre-populated with the chart's time-series query. You can then configure threshold conditions and notification channels for the metric.   
query_stats **Explore data** |  In the chart toolbar, click **Explore data** to open the metric query in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). In Metrics Explorer, you can inspect, filter, group, and modify the underlying time-series query across different dimensions, or save customized views to a custom dashboard.   
more_vert **View in full screen** |  In the chart toolbar, click **More chart options** , and then select **View in full screen** to expand the chart to fill your screen for detailed inspection of time series and legend data.   
more_vert **Inspect related logs** |  You can correlate metric data with log entries written around the same timeframe to troubleshoot activity and errors: 

  * **Dashboard view** : In the chart toolbar, click **More chart options** , and then select **Inspect related logs** to open a split-view panel displaying the chart alongside correlated log entries. 
  * **Data-point tooltip** : On any chart time series, hold your pointer over a specific data point, and then select **Inspect related logs** from the tooltip. In this mode, the split-view panel filters log entries to a window five minutes before and after the selected timestamp. 

  
  
## Available metrics

The following table lists all metrics available on the dashboard.

**Note:** Metrics typically appear on the dashboard within 5 to 15 minutes of user activity.Section | Metric name | Description  
---|---|---  
Active Users (Adoption) |  An active user is a unique user who initiated at least one AI developer tool action (such as an API request, prompt, or tool execution) during the reporting timeframe.   
**Hourly active users (average)** |  Displays the average number of unique active users per hour over the selected timeframe.   
**Daily active users (average)** |  Displays the average number of unique active users per day over the selected timeframe.   
**Weekly active users (average)** |  Displays the average number of unique active users per week over the selected timeframe.   
**Monthly active users (average)** |  Displays the average number of unique active users per month (28-day active users) over the selected timeframe.   
**Hourly Active Users** |  A trend line chart that shows the number of unique active users by hour over the selected timeframe.   
**Daily Active Users** |  A trend line chart that shows the number of unique active users by day over the selected timeframe.   
**Weekly Active Users** |  A trend line chart that shows the number of unique active users by week over the selected timeframe.   
**Monthly Active Users** |  A trend line chart that shows the number of unique active users by month (28-day active users) over the selected timeframe.   
Tools & API calls | **Total Tokens** |  The total number of combined input and output tokens consumed by AI developer tools over the selected timeframe.   
**Daily Token Usage** |  A line chart showing daily token consumption over time.   
**Daily API Calls** |  A line chart showing the daily count of API calls made by AI developer tools, including an error breakdown by `error_type` label (for example, quota limits, authentication errors, or client errors).   
**Daily Tool Calls** |  A line chart showing the daily count of tool calls initiated by AI developer tools.   
**Daily Tool Calls Accepted** |  A line chart showing the daily count of agent-proposed tool call suggestions that users accepted and executed.   
  
## What's next

  * Learn more about available tools and capabilities in the [AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview).
  * Learn how to configure developer tools settings. For more information, see [Configure AI developer tools settings](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings).
  * Learn how to manage access with custom roles. For more information, see [Create custom roles for AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
