---
url: https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications/
title: Configure alerts and notifications \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:35.376128+00:00
---

# Configure alerts and notifications  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  Configure alerts and notifications Stay organized with collections  Save and categorize content based on your preferences. 

Unified Maintenance generates logs through Cloud Logging. You can create alerts and notifications based on different log conditions and through the supported webhooks, or other notification channels.

## Configure alert policies

Alert policies for planned maintenance are available through Cloud Logging. You can get notified for any of the following conditions:

  * When new maintenance events are scheduled for resources that your projects use.
  * When the state of a maintenance event changes (for example, from `SCHEDULED` to `STARTED`).
  * When there is a change to the scheduled start or end time of the maintenance.
  * When maintenance impacts resources in a specific location.



Notifications use log-based alerting policies. Once you have configured an alert policy, you will receive a notification each time your conditions are met. Alerts are subject to [Cloud Monitoring limits](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

## Configure notification channels

Log alerts use [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options), which notify you, or your on-call team, when an alerting policy is triggered, and which support a variety of integrations, such as:

  * Email
  * Pub/Sub
  * PagerDuty
  * Slack
  * SMS
  * Webhooks



Unified Maintenance works with Google Cloud Observability to configure third-party integrations. For third-party integrations, use webhooks to send a notification to any public endpoint such as [ServiceNow](https://docs.servicenow.com/bundle/xanadu-it-service-management/page/product/site-reliability-ops/task/sro-configure-google-cloud.html), DataDog, or OpsGenie or use Pub/Sub to send a notification to any private endpoint. You have control over which logs are sent to these third-party tools through logging filters. For more information about writing filters, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

To learn more about webhooks, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options#webhooks) in the Google Cloud Observability documentation.

## Configure notifications with Cloud Logging

You can create a logs-based alert to be notified whenever a log that matches a provided filter is ingested. For more information, see [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

  1. In the Google Cloud console, go to the **Logs Explorer** page:  


[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Select your Google Cloud project.
  3. Click **Create log alert**. Depending on the size of your window, this option might appear in the **Actions** menu.
  4. In the Create logs-based alert policy pane, provide an **Alert Policy Name** and any **Documentation** that you would like included with the notification. Click **Next**.
     * Optional: Choose a severity level for this policy.
  5. Create an inclusion filter to determine which logs are included in the alert by writing a query. For more information about writing queries, see [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language). The following example is an alert for any scheduled maintenance event associated with any Cloud SQL resource: 
         
         log_id("maintenance.googleapis.com/maintenance_events") AND jsonPayload.resource.type = "sqladmin.googleapis.com/Instance" AND jsonPayload.state = "SCHEDULED"

  6. Optional: Click **Preview logs**. If there are no resources that meet the criteria defined, no preview is output.
  7. Optional: Click **Add a label** to create labels from log fields (for example, `description`) if you're integrating with a third-party tool such as Slack. Click **Next**.
  8. Optional: Configure the minimum **Time between notifications** and the **Incident autoclose duration**. Click **Next**.
  9. If you have configured a supported channel, you can select it from the **Notifications Channels** list; otherwise, you can click **Manage Notification Channels** and add a supported channel. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).
  10. Click **Save**. Your log-based alert is now ready to test.



## What's next

  * Log schema [overview](https://docs.cloud.google.com/unified-maintenance/docs/log-schema)
  * Implement [common alert policies](https://docs.cloud.google.com/unified-maintenance/docs/implement-common-alert-policies)
  * Control [maintenance](https://docs.cloud.google.com/unified-maintenance/docs/reschedule-and-on-demand-updates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
