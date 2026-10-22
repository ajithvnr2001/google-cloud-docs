---
url: https://docs.cloud.google.com/armor/docs/monitoring/
title: Monitor security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:55.775806+00:00
---

# Monitor security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Monitor security policies Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor exports monitoring data from security policies to Cloud Monitoring. You can use monitoring metrics to check whether your policies are working as intended or to troubleshoot problems. For example, you can view the traffic that was blocked or allowed for each backend service. You can monitor the metrics of a single security policy (which can be applied to multiple backend services) or a single backend service.

In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alert policies, and query the metrics through the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api).

On the Monitoring dashboard, **Open incidents** are driven by the alerting policies that you configure. Alerts appear as _incidents_ on the dashboard when the alert is triggered. These are general functions of Monitoring.

There are no Monitoring logs for Security Command Center.

For complete information about Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

## Viewing the monitoring dashboard

You can monitor the status and request traffic volumes (allowed, denied, or previewed) on a per-policy and per-backend-service basis by using the preconfigured **Cloud Armor policies overview** resource dashboard in Cloud Monitoring.

To view the dashboard, follow these steps:

  1. In the Google Cloud console, go to **Monitoring**.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane on the left, select **Dashboards**.

  3. Under **Name** , select **Cloud Armor policies overview**.

  4. Click the name of your policy.




When you access the dashboard, you see overall metrics on the right. These include request volume metrics for requests evaluated by a security policy broken down by outcome: allowed, denied, previewed allowed, previewed denied. Metrics can be observed at varying levels of granularity, including per-project, per-policy, and per-backend-service.

When you click a policy name, you see details about the policy.

[ ![Example of the Cloud Armor monitoring dashboard showing request metrics.](https://docs.cloud.google.com/static/armor/images/monitoring-dashboard.svg)](https://docs.cloud.google.com/static/armor/images/monitoring-dashboard.svg) Cloud Armor monitoring dashboard (click to enlarge)

## Defining custom dashboards

To create custom Monitoring dashboards over Network Security Policy metrics, follow these steps:

### Console

  1. In the Google Cloud console, go to **Monitoring**.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Click **Dashboards** , and then click **Create dashboard**.

  3. Create a name for your dashboard, and then click **Confirm**.

  4. Click **Add chart**.

  5. Give the chart a title.

  6. Select metrics and filters. For metrics, the resource type is **Network Security Policy**.

  7. Click **Save**.




## Defining alerting policies

### Console

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Network Security Policy` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **Network Security Policy**.
     3. Select a **Metric category** and a **Metric** , and then select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

## Metric reporting frequency and retention

Metrics for the Cloud Armor security policies are exported to Cloud Monitoring in one-minute granularity batches. Monitoring data is retained for six weeks. The dashboard provides data analysis in the following default intervals:

  * 1H (one hour)
  * 6H (six hours)
  * 1D (one day)
  * 1W (one week)
  * 6W (six weeks)



To manually request analysis in any interval from 6W to 1 minute, use the Google Cloud console controls on the **Monitoring** page.

## Monitoring metrics for security policies

The following metrics are reported on the **Cloud Armor policies overview** dashboard:

Metric | Description  
---|---  
**Requests** count | The number of requests processed by a Cloud Armor security policy.  
**Previewed Requests** count |  The number of requests that match preview-mode rules. **Previewed Requests** are logged, but the corresponding action is not enforced. The **Previewed Requests** counts are included in the preceding **Requests** count metric because all requests are expected to match a configured non-preview rule or the default rule.  
  
## Filtering dimensions for security policies

Metrics are aggregated for each Cloud Armor security policy. You can filter aggregated metrics by the following dimensions:

Dimension | Description  
---|---  
backend_target_name | Track requests based on the backend target (service) that the traffic was destined to.  
blocked | Track requests based on whether they were allowed or blocked by the security policy rules.  
  
## What's next

  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)
  * [Use the custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
