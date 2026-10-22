---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/manage-alert-rules-and-groups/
title: Manage alerting policies and groups \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:15.372598+00:00
---

# Manage alerting policies and groups  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/manage-alert-rules-and-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage alerting policies and groups Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to manage a project's alerting policies, alert status, and groups in Google Distributed Cloud (GDC) air-gapped appliance. These operations let you monitor and modify the conditions and rules of your configured alerts, giving you awareness and control of critical events in your system.

An alerting policy is a set of rules and conditions that dictate how and when you're notified about important events or changes in your project. These policies define the situations and actions for receiving notifications about an event through an alert.

Alerting policies consist of alert rule groups, which refer to a collection of individual alert rules grouped together based on some criteria. The criteria include the system, application, severity, or other relevant factors. Alert rule groups help you manage and maintain many alert rules by grouping them logically.

The GDC console lets you view configured alerts and policies, silence alerts, and update or delete alert rules and groups.

**Note:** Some alert rules are read-only because the system generates them, so you cannot edit or delete them. Ensure the alert rules display editable permissions when updating or deleting rule groups and alerts.

For information about creating alert rules, see [Create alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-alert-rules). To view and filter open alerts, see [Query and view open alerts](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-alerts).

## Before you begin

To get the permissions that you need to manage alerts and policies, ask your Project IAM Admin to grant you one of the associated Project Cortex Alertmanager roles in your project namespace. Depending on the level of access and permissions you need, you might obtain editor or viewer roles in a project.

For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

## View configured alerts

Obtain a list of the latest alerts in your project and click an alert name for more details. The GDC console shows the most recent alerts.

View the alerts in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerts** tab.
  5. View the list of alerts.
  6. Click an alert name to view the alert details.



## Silence an alert

Silence an alert for a specific time. When you silence an alert, you temporarily prevent it from opening for a period, even if the condition is met.

Silence an alert from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerts** tab.
  5. Click an alert name to view the alert details.
  6. Click **Silence alert**.
  7. In the **Silence duration** field, choose the length of time to silence the alert.
  8. In the **Enter a justification** field, choose a justification.
  9. Click **Confirm**.
  10. To view all silenced alerts, click **Filter** in the **Alerts silenced** section of the **Alerts** tab.
  11. To remove a silence from an alert, click the name of the silenced alert and then click **Remove silence**.



## View alerting policies

Obtain a list of all alert group rules in a project and select a group for more details.

View all alert group rules in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerting Policy** tab.
  5. View the list of alert rule groups.
  6. Click a rule group name to view its details and the list of its alert rules.
  7. Click an alert rule name to view the alert rule details.



## Update alert rule groups

Alert rule groups contain alert rules. Select a rule group and edit the rule group details.

Update alert rule groups in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerting Policy** tab.
  5. View the list of alert rule groups.
  6. Click a rule group name that has the **Editable** value in the **Permissions** column.
  7. In the rule group details page, click _edit_ **Edit** next to the field that you want to update, such as **Limit**.
  8. Edit the value and click **Save**.



## Delete alert rule groups

Select a rule group and delete it. When you delete an alert rule group, the alert rules associated with the group are also deleted.

Delete alert rule groups in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerting Policy** tab.
  5. Click the name of the rule group that you want to delete. The rule group must have the **Editable** value in the **Permissions** column so you can delete it.
  6. Click **Delete**.
  7. In the confirmation dialog, click **Confirm** to delete.



## Update alert rules

Select a rule group and edit an alert rule that belongs to the group.

Update alert rules in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerting Policy** tab.
  5. Click the name of the rule group that contains the rule that you want to update. The rule group must have the **Editable** value in the **Permissions** column so you can update its alert rules.
  6. In the **Alert rules** section, click a rule that is editable.
  7. In the **Edit alert rule** page, edit the values and click **Save**.



## Delete alert rules

Select a rule group and delete an alert rule that belongs to the group.

Delete alert rules in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select a project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Click the **Alerting Policy** tab.
  5. Click the name of the rule group that contains the rule that you want to delete. The rule group must have the **Editable** value in the **Permissions** column so you can delete its alert rules.
  6. In the **Alert rules** section, select the checkbox for the rule that you want to delete.
  7. Click **Delete**.
  8. In the confirmation dialog, click **Confirm** to delete.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
