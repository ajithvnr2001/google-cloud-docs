---
url: https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies/
title: Create alerting policies for uptime checks \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:47.483507+00:00
---

# Create alerting policies for uptime checks  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create alerting policies for uptime checks Stay organized with collections  Save and categorize content based on your preferences. 

Alerting policies let you receive notifications whenever a public or private uptime check fails. Using the Google Cloud console, you can configure a policy when you first create a check, or add and modify policies for existing checks at any time. If you haven't created an uptime check yet, see [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks) or [Create private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

## Before you begin

Complete the following in the Google Cloud project that stores your uptime checks. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  1. To get the permissions that you need to create and modify alerting policies by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  2. Ensure that you have configured the notification channels that you want to use for the alerting policy. For information about configuring notification channels, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).




## Create an alerting policy

To create an alerting policy that notifies you when an uptime check fails, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the uptime check that you want to monitor, click _more_vert_ **More** , and select **Add alert policy**.

The alerting policy configuration dialog opens and the **Condition** is preconfigured.

  4. In the navigation pane of the dialog, select **Notifications and name**.

  5. Add your notification channels, and enter a name for the alerting policy. You can also add documentation that you want included in notifications.




## View or edit an alerting policy

To view details of the alerting policy, open the details page of the uptime check, go to the **Alert Policies** pane, and then select the policy.

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the alerting policy that you want to view or modify and then select its name.
  4. Optional: To change who is notified, the documentation, or the condition of an alerting policy, click _edit_ **Edit**.



## What's next

For information about charting uptime metrics, see [Chart uptime-check metrics](https://docs.cloud.google.com/monitoring/charts/uptime-charts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
