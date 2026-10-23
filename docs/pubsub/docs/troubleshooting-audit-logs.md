---
url: https://docs.cloud.google.com/pubsub/docs/troubleshooting-audit-logs/
title: Troubleshoot Pub/Sub issues with audit logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:13.986912+00:00
---

# Troubleshoot Pub/Sub issues with audit logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/troubleshooting-audit-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshoot Pub/Sub issues with audit logs Stay organized with collections  Save and categorize content based on your preferences. 

Pub/Sub generates audit logs that capture administrative and access activities of Pub/Sub resources. Some examples of these activities include creating a topic, updating a subscription, or deleting a snapshot. You can use these logs for troubleshooting issues and ensuring the security of your messaging infrastructure.

Here are some important points to remember regarding audit logs in Pub/Sub:

  * Pub/Sub audit logs use the service name `pubsub.googleapis.com`.

  * Pub/Sub has different types of logs. These include the following:

    * Admin activity logs record actions like creating, deleting, or updating topics and subscriptions.

    * Data access logs record actions like retrieving a topic or listing subscriptions.

    * System event logs record events like removing inactive subscriptions.

  * Pub/Sub does not log message operations like publishing, subscribing, or acknowledging messages.




For more information about audit logs for Pub/Sub, see [Audit logging](https://docs.cloud.google.com/pubsub/docs/audit-logging).

## View Pub/Sub audit logs

**Logs Explorer** provides a centralized location to access all your log data within Google Cloud. You can use **Logs Explorer** to view Pub/Sub logs.

  1. Get the required permissions to view **Logs Explorer**.

For more information, see [Before you begin](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#before-you-begin).

  2. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  3. Select an existing Google Cloud project, folder, or organization.

  4. To display all audit logs related to Pub/Sub, enter the following query into the query-editor field:
         
         protoPayload.serviceName="pubsub.googleapis.com"
         

![Figure showing how to enter the query into the query-editor field.](https://docs.cloud.google.com/static/pubsub/images/audit-log-query.png)**Figure 1** Enter a query. 
  5. Click **Run query**.

  6. To display the audit logs for a specific resource and audit log type, in the Query builder pane, do the following:

     1. For **All resources** , select the Google Cloud resource whose audit logs you want to see. For example, select **Cloud Pub/Sub Topic** and then select the topic name.

     2. For **All log names** , select the audit log type that you want to see.

For example:

        * For Admin activity audit logs, select `activity`.

        * For System event audit logs, select `system_event`.




The query runs automatically.

## How to use audit logs to troubleshoot Pub/Sub issues

  1. Determine the specific problem that you're investigating. Here is a list of potential issues:

     * Identify who created, deleted, or modified topics, subscriptions, snapshots, or schemas.

     * Track changes to topic or subscription settings.

     * Verify if a topic or subscription exists and its current status.

However, you cannot use audit logs to troubleshoot issues related to message publishing and delivery. You won't find logs for message delivery failures, message duplication, or message ordering problems. Audit logs also won't help you identify slow subscribers or issues with message acknowledgments. For troubleshooting message-level issues, you'll need to rely on other tools like monitoring metrics, dead-letter queues, and application logs.

  2. Based on the issue, construct a query to filter the audit logs. For example, to find out who deleted a subscription, filter by `protoPayload.methodName="google.pubsub.v1.Publisher.DeleteSubscription"`.

To investigate a potential error with creating a subscription, filter by `protoPayload.methodName="google.pubsub.v1.Subscriber.CreateSubscription"`.

  3. Examine the timestamps, principals, and resource names in the log entries to understand the sequence of events and identify any anomalies.




For more information on how to construct an audit log query for Pub/Sub, see [Audit logging](https://docs.cloud.google.com/pubsub/docs/audit-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
