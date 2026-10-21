---
url: https://docs.cloud.google.com/application-integration/docs/alerts/
title: Configure alerts \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:52.661393+00:00
---

# Configure alerts  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure alerts

You can configure alerts to notify you when an event occurs. For example, you can create an alert to notify you when there is an authentication failure by an integration.

You can set alerts in the following two ways:

  * Alerts in Cloud Monitoring
  * Alerts in Cloud Logging



## Alerts in Cloud Monitoring

You can create and configure Cloud Monitoring alerts to notify you when an Application Integration resource exceeds a specified threshold. For example, you can create an alert to notify you when the total data processed for an integration exceeds a specified threshold value or if integration execution count reaches beyond a certain limit.

For more information about alerting in Cloud Monitoring, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

### Before you begin

  * Make sure that you have the **Monitoring Editor (`roles/monitoring.editor`)** IAM role granted on your Google Cloud project. For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn about the general concepts of alerting policies, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).
  * Configure notification channels to receive alerts, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). 



### Create an alert

  1. In the Google Cloud console, go to the **Monitoring > Alerting** page. 

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)

  2. Click **\+ Create Policy**.
  3. To select the resource, metric, and filters for Application Integration, follow these steps: 
     1. Click **Select a metric**.
     2. In the **Filter by resource or metric name** input field, enter `Integration Version` and select it.
     3. In the **Active metric categories** menu, select a metric type, and then **Active Metrics**. For a list of metric types, see [integrations metric type](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-integrations).
     4. Click **Apply**.
  4. Click **Next** to open the **Configure alert trigger** section. 
  5. Set a threshold value to trigger the alert.
  6. Click **Next** to open the **Configure notifications and finalize alert** section.
  7. (Optional) To add notifications to your alerting policy, click **Notification channels** and select one or more notification channels from the drop-down list. Click **OK**. 

To be notified when incidents are opened and closed, check **Notify on incident closure**. By default, notifications are sent only when incidents are opened.

  8. (Optional) Use the **Documentation** text field to enter any information that you want included in a notification message.
  9. Click **Alert policy name** and enter a name for the alerting policy.
  10. Click **Create Policy**.



For more sample alerts, see [Alert policy templates for Application Integration](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/alerts/google-application-integration).

The alerts are sent to the essential contacts configured in your Google Cloud Project. For more information on adding essential contacts, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## Alerts in Cloud Logging

You can create and configure log-based alerts to notify you whenever a specific message appears in your included logs. For example, the following lists some use cases for which you can create a log-based alert: messages that match a specific pattern, failed integration execution status, specific severity log, and integrations with an execution time time higher than certain value.

### Create an alert

You can create log-based alerts from the **Logs Explorer** page in the Google Cloud console or by using the Monitoring API. For detailed instructions, see the following sections:

  * [Create a log-based alert by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition)
  * [Create a log-based alert by using the Monitoring API](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api)

**Note:** You may incur additional charges for using Cloud Monitoring API directly. For more information, see [Cloud Monitoring pricing](https://docs.cloud.google.com/monitoring#section-7).

## What's next

  * Learn more about [configuring log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
