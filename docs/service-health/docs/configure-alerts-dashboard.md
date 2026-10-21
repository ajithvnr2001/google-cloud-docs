---
url: https://docs.cloud.google.com/service-health/docs/configure-alerts-dashboard/
title: Quickstart: Set up an alert \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:16.178942+00:00
---

# Quickstart: Set up an alert  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/configure-alerts-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Quickstart: Set up an alert Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to set up an alert for Personalized Service Health events within the Service Health dashboard. You can set up alerts for scenarios such as new incidents or updates to existing incidents.

An alert uses an alerting policy, which describes the circumstances under which you want to be alerted and how you want to be notified.

## Before you begin

  1. Enable the Service Health API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicehealth.googleapis.com)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions.
  4. Have a Cloud Monitoring notification channel, which defines where an alert is sent. If you don't have a notification channel, you can create one in the [Google Cloud console](https://cloud.google.com/monitoring/support/notification-options) or by using the [Monitoring API](https://cloud.google.com/monitoring/alerts/using-channels-api#api-create-channels).



### Required roles

To get the permissions that you need to set up an alert, ask your administrator to grant you the following IAM roles on the project that you want to set up an alert for: 

  * [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`)
  * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)
  * [Monitoring NotificationChannel Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelViewer) (`roles/monitoring.notificationChannelViewer`)
  * [Personalized Service Health Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicehealth#servicehealth.viewer) (`roles/servicehealth.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an alerting policy within the Service Health dashboard

Personalized Service Health provides alert templates to help you create alerting policies without leaving the Service Health dashboard.

To create an alerting policy from the Service Health dashboard:

  1. Navigate to the [Service Health dashboard](https://console.cloud.google.com/servicehealth).
  2. Select **Create Alert Policy** at the upper-right corner.
  3. Choose one of the example alert policy templates, configure proper notification channels, and select **Create Policies**.



To create your own alerting policy based on an existing template, you can modify one:

  1. Navigate to the [Service Health dashboard.](https://console.cloud.google.com/servicehealth)
  2. Click **Create Alert Policy** at the upper-right corner. The list of alert policy templates appears.
  3. Click the three dots for the template you want to modify, and choose **Customize alert policy**. See the [example alerting policies and conditions](https://docs.cloud.google.com/service-health/docs/example-alerting-policies) for the fields and values you can set.
  4. Follow the prompts to edit the alert policy as needed, and click **Save**.



## Update alerting policies

You can modify alerting policies in the [Monitoring page of the Google Cloud console](https://console.cloud.google.com/monitoring/alerting/policies).

When defining alert conditions, use the values found at [Google Cloud products](https://docs.cloud.google.com/service-health/docs/supported-products-locations) and [locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations#locations).

## What's next

Learn about alternative ways to [set up alerts for service health events in Cloud Logging](https://docs.cloud.google.com/service-health/docs/configure-alerts-cloud-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
