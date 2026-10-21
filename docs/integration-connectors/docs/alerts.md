---
url: https://docs.cloud.google.com/integration-connectors/docs/alerts/
title: Configure alerts \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:36.964526+00:00
---

# Configure alerts  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure alerts

You can configure alerts to notify you when an event occurs. For example, you can create an alert to notify you when there is an authentication failure by a connector.

Integration Connectors supports the following two types of alert notifications:

  * Alerts in Cloud Monitoring
  * Alerts in Cloud Logging



## Alerts in Cloud Monitoring

You can create and configure Cloud Monitoring alerts to notify you when an Integration Connectors resource exceeds or drops below a specified threshold. For example, you can create an alert to notify you when the total data processed by a connector exceeds a specified threshold value. 

For more information about alerting in Cloud Monitoring, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

### Before you begin

* Make sure that you have the **Monitoring Editor (`roles/monitoring.editor`)** IAM role granted on your Google Cloud project. For information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
* Learn about the general concepts of alerting policies, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).
* Configure notification channels to receive alerts, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). 

### Create an alert

  1. In the Google Cloud console, go to the **Monitoring > Alerting** page. 

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)

  2. Click **\+ Create Policy**.
  3. To select the resource, metric, and filters for Application Integration, click **Select a metric** and enter `Connectors` in the **Filter by resource or metric name** input field. 
  4. Click **Apply**.
  5. Click **Next** to open the **Configure alert trigger** section. 
  6. Set a threshold value to trigger the alert.
  7. Click **Next** to open the **Configure notifications and finalize alert** section.
  8. (Optional) To add notifications to your alerting policy, click **Notification channels** and select one or more notification channels from the drop-down list. Click **OK**. 

To be notified when incidents are opened and closed, check **Notify on incident closure**. By default, notifications are sent only when incidents are opened.

  9. (Optional) Use the **Documentation** text field to enter any information that you want included in a notification message.
  10. Click **Alert policy name** and enter a name for the alerting policy.
  11. Click **Create Policy**.



The alerts are sent to the essential contacts configured in your Google Cloud Project. For more information on adding essential contacts, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## Alerts in Cloud Logging

You can create and configure log-based alerts to notify you whenever a specific message appears in your included logs. For example, you can create a log-based alert for messages that match a specific pattern.

### Create an alert

You can create log-based alerts from the **Logs Explorer** page in the Google Cloud console or by using the Monitoring API. For detailed instructions, see the following sections:

  * [Create a log-based alert by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition)
  * [Create a log-based alert by using the Monitoring API](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-by-api)

**Note:** You may incur additional charges for using Cloud Monitoring API directly. For more information, see [Cloud Monitoring pricing](https://docs.cloud.google.com/monitoring#section-7).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
