---
url: https://docs.cloud.google.com/monitoring/monitoring-uptime/
title: Quickstart: Get notified if your app stops responding \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:40.961425+00:00
---

# Quickstart: Get notified if your app stops responding  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/monitoring-uptime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get notified if your app stops responding

Learn how to get notified if your application stops responding to HTTP requests by completing the following tasks:

  1. Create an email notification channel.
  2. Create an uptime check and an alerting policy.
  3. View the uptime check dashboard.
  4. Force the uptime check to fail.
  5. View the email notification and the alert.
  6. Clean up.



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/welcome?walkthrough_id=monitoring--monitoring-quickstart-uptime)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Monitoring API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Monitoring API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)




## Create an email notification channel

Before you create an alerting policy, configure the notification channels that you want the alerting policy to use. Cloud Monitoring supports many different types of notification channels, including email, Slack, PagerDuty, and Pub/Sub. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options). To get notifications by e-mail, do the following: 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, click **Edit Notification Channels**.
  3. On the **Notification channels** page, scroll to **Email** , and then click **Add new**.
  4. Enter your email address, a display name such as `My email`, and then click **Save**.



## Create an uptime check and alerting policy

To be notified when an application fails to respond to requests, configure an uptime check to send requests to the application, and then configure an alerting policy to monitor the responses to the uptime check:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, click **Create uptime check**.
  3. For the **Resource Type** , select **URL**.
  4. Use the **Hostname** and **Path** fields to specify the URL to check. If the **Path** field is empty, then the URL specified in the **Hostname** field is checked.

For example, to check the URL `https://example.com/jsonExamples`, set the **Hostname** field to `example.com` and the **Path** field to `/jsonExamples`.

  5. Click **Continue** to advance to the **Response validation** section. 

For information about these settings, see [Validate response data](https://docs.cloud.google.com/monitoring/uptime-checks/response-validation).

  6. Click **Continue** to advance to the **Alert & Notification** section.
  7. Expand the **Notification channels** menu and select your notification channel.
  8. Click **Continue** to advance to the **Review** section.
  9. Enter a title, such as `My check`, for the uptime check.
  10. To verify your uptime check configuration, click **Test**.

If you receive an error, see [Verify your uptime check](https://docs.cloud.google.com/monitoring/alerts/uptime-checks#verify-check).

  11. Click **Create**.



Your uptime check and alerting policy are created, and your new uptime check is listed on the **Uptime checks** page.

## View the uptime check dashboard

The **Uptime checks** page displays a list of your uptime checks and the status of each check. To view the detailed status of the uptime check you created, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the name of the uptime check to open the uptime-check's dashboard.

Because your uptime check hasn't executed, the charts are empty and the status for the uptime check is **No checks have run**.

  3. In the toolbar, enable auto-refresh on the charts by clicking sync_disabled **Enable auto refresh**.

  4. Wait until a few data points appear on the charts, and then refresh the page.

When the status for each location is check_circle **Pass** , proceed to the next step. Otherwise, wait a minute and refresh the page to update the status pane.




## Force the uptime check to fail

To force the uptime-check to fail, modify the **Path** such that the URL tested by the uptime check is invalid:

  1. In the toolbar, click **Edit**.
  2. In the **Path** field, append or enter **HelloWorld**.
  3. Click **Save**.
  4. In the toolbar, enable auto-refresh on the charts by clicking sync_disabled **Enable auto refresh**.
  5. Wait until the data points on the **Passed Checks** chart go to zero, and then refresh the page.

When the status for each location is error **Fail** , proceed to the next step. Otherwise, wait a minute and refresh the page to update the status pane.




## View the notification and alert

After the alerting policy determines that the uptime check has had two consecutive failures, Cloud Monitoring creates an alert and sends notifications. An _alert_ is a record of an alerting policy that triggers, and it contains information that is useful for troubleshooting failures. To view the notification and alert, do the following:

  1. Open your email account, and view the message whose title starts with `[ALERT] Failure of uptime check_id`.
  2. To get details about the failure, in the notification, click **View alert**.

The **Alert details** page opens in a new page of the **Cloud console**.




You have successfully created an uptime check and an alerting policy, you forced the uptime check to fail, and you've received a notification. You can now close the browser page that displays the **Alert details** page.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project and you no longer need the project, then [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing project, then do the following:

  1. Delete the uptime check that you created:

     1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. Select the uptime check that you created, and then click **Delete**. 

When you delete an uptime check, you also delete the alerting policy that monitors that uptime check.




## What's next

  * To learn how to view and customize dashboards for your VMs, see the quickstart [View and customize VM instance dashboards](https://docs.cloud.google.com/monitoring/monitor-compute-engine-dashboards).

  * To learn about testing your applications, see [Synthetic monitoring overview](https://docs.cloud.google.com/monitoring/uptime-checks/introduction).

  * To learn how to install the Ops Agent and collect metrics from an Apache server, see the quickstart [Collect Apache metrics with the Ops Agent](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine).

  * To learn about the Ops Agent, see [Ops Agent overview](https://docs.cloud.google.com/monitoring/agent/ops-agent).

  * To learn about creating custom dashboards, see [Manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
