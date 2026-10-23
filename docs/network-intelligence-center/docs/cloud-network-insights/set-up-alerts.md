---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts/
title: Set up alerts and notifications \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:59.603924+00:00
---

# Set up alerts and notifications  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Set up alerts and notifications Stay organized with collections  Save and categorize content based on your preferences. 

Once you've configured AppNeta [alarm rules](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/alarms-set-up/alarms-rules.html) to identify specific network events or performance issues, the alarms send structured logs to Cloud Logging. You can then create [log-based alert policies](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging) in Google Cloud to act on these logs.

These alerts and notifications help you proactively respond to network incidents before customers start to call in, understand where and when troublespots developer, and surface hidden issues in your network.

Cloud Network Insights alerting is based on logs received from AppNeta's alarms. A log entry of structured data is sent from AppNeta to Cloud Logging.

Once received by Cloud Logging, logs are evaluated by log-based alert policies that filter logs for specific alarms. When a log matches an alert policy, an [incident](https://docs.cloud.google.com/monitoring/alerts/incidents-events) is created. After an incident is created, Google Cloud can send notifications through selected notification channels (email, Slack, PagerDuty, or Pub/Sub) when an incident occurs.

Cloud Network Insights provides alert policy templates for common alerting scenarios, such as when a Monitoring Point is offline or if there's an outage on a monitored network path, to simplify your alert policy setup. If you want to alert on incidents beyond the predefined templates, create an alert in Cloud Logging.

## Before you begin

Alerts and notifications are only triggered when [logging](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging) is set up in AppNeta and Cloud Logging receives alarm logs (`insights_alarm`) or event logs (`insights_event`).

### Required roles

To get the permissions that you need to create log-based alert policies, ask your administrator to grant you the following IAM roles on the project in which Cloud Network Insights is enabled: 

  * [Cloud Network Insights Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsViewer) (`roles/networkmanagement.CloudNetworkInsightsViewer`)
  * [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`)
  * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)
  * [Monitoring NotificationChannel Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelViewer) (`roles/monitoring.notificationChannelViewer`)
  * Add a notification channel to an alert policy: [Monitoring NotificationChannel Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelEditor) (`roles/monitoring.notificationChannelEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create log-based alert policies

Once you have [Alarm Rules](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/alarms-set-up/alarms-rules.html) configured in AppNeta, create alert policies in Google Cloud to receive notifications.

### Use predefined templates

You can create alert policies using the predefined templates in Cloud Network Insights.

  1. Open the Google Cloud console and navigate to **Network Intelligence** > **Cloud Network Insights** > **Alert Policies**.

[Go to Alert Policies](https://console.cloud.google.com/net-intelligence/cloud-network-insights/alert-policies)

  2. Click **Create alert policy**.

  3. Select an alert policy template.

  4. Optionally, customize the alert policy.

     * Click more_vert **View more actions** and select **Customize alert policy** to change which logs are included in the alert or the notification frequency and autoclose duration.
     * Click **show options** and modify the notification frequency and autoclose duration.
  5. Optionally choose where to receive notifications. If you don't have notification channels set up, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  6. Click **Create**.




### Use the Logs Explorer

You can also create log-based alerts in [Logs Explorer](https://console.cloud.google.com/logs) using the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

Cloud Network Insights logs use one of the following for `logName`:

  * Alarm logs - `networkmanagement.googleapis.com/insights_alarm`
  * Event logs - `networkmanagement.googleapis.com/insights_event`



The following is an example query that identifies when a critical alarm is raised on a specific path. This query is entered in the Logs Explorer **Query** pane.
    
    
        logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com/insights_alarm"
        resource.labels.path_id="np-abcdef"
        jsonPayload.severity="CRITICAL"
        jsonPayload.state="RAISED"
      

For more information, see [Build and save queries by using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries) and [Create a log-based alerting policy by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
