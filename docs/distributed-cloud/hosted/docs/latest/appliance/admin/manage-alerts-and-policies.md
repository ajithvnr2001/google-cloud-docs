---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/manage-alerts-and-policies/
title: Manage configured alerts and policies \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:44.123487+00:00
---

# Manage configured alerts and policies  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/manage-alerts-and-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Manage configured alerts and policies Stay organized with collections  Save and categorize content based on your preferences. 

You can perform the following actions from the GDC console regarding Observability alerts and alerting policies for system monitoring:

  * View configured alerts
  * Silence an alert
  * View alerting policies



## Before you begin

To manage alerts and policies, request the necessary permissions from your administrator.

### Required IAM roles

Contact your Project IAM Admin to request the following roles:

  * **Project Cortex Alertmanager Editor** (`project-cortex-alertmanager-editor`): edit the Cortex `Alertmanager` instance in the project namespace.
  * **Project Cortex Alertmanager Viewer** (`project-cortex-alertmanager-viewer`): access the Cortex `Alertmanager` instance in the project namespace.



## View configured alerts

Obtain a list of the latest alerts in your project and click an alert name for more details. The console shows the most recent alerts.

View the alerts in a project from the GDC console:

  1. In the GDC console, select a project.
  2. In the navigation menu, click **Operations** > **Alerting**.
  3. Click the **Alerts** tab.
  4. View the list of alerts.
  5. Click an alert name to view the alert details.



## Silence an alert

Click an alert and silence it for the length of time you want. When you silence an alert, you temporarily prevent it from opening for a period, even if the condition is met.

Silence the alert from the GDC console:

  1. In the GDC console, select a project.
  2. In the navigation menu, click **Operations** > **Alerting**.
  3. Click the **Alerts** tab.
  4. Click an alert name to view the alert details.
  5. Click **Silence alert**.
  6. In the **Silence duration** field, choose the length of time to silence the alert.
  7. In the **Enter a justification** field, choose a justification.
  8. Click **Confirm**.
  9. To view all silenced alerts, in the **Alerts silenced** section, click **Filter**..
  10. To remove a silence, click the name of a silenced alert and then click **Remove silence**.



## View alerting policies

Obtain a list of all alert group rules in a project and click a group for more details.

View all alert group rules in a project from the GDC console:

  1. In the GDC console, select a project.
  2. In the navigation menu, click **Operations** > **Alerting**.
  3. Click the **Alerting Policy** tab.
  4. View the list of alert rule groups.
  5. Click a rule group name to view its details and the list of its alert rules.
  6. Click an alert rule name to view the alert rule details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
