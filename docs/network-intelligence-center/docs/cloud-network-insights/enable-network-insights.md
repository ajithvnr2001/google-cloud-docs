---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/enable-network-insights/
title: Enable Cloud Network Insights \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:17.049545+00:00
---

# Enable Cloud Network Insights  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/enable-network-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Enable Cloud Network Insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable Cloud Network Insights for your organization. Once Cloud Network Insights is enabled, a corresponding AppNeta instance is provisioned to provide telemetry data, more monitoring options, and to allow further configuration.

Cloud Network Insights is enabled for a single project. We highly recommend that you create a dedicated project for enabling Cloud Network Insights where you don't create other Google Cloud resources.

## Before you begin

  * Ensure [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project) for your project.



### Required roles

To get the permissions that you need to enable Cloud Network Insights, ask your administrator to grant you the following IAM roles on the project in which you want to enable Cloud Network Insights: 

  * Enable the Network Management API: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * Enable Cloud Network Insights: [Cloud Network Insights Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsAdmin) (`roles/networkmanagement.CloudNetworkInsightsAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

After you've enabled Cloud Network Insights the first time and accepted the Broadcom Terms of Service, users with the Cloud Network Insights Editor (`roles/networkmanagement.CloudNetworkInsightsEditor`) role can enable or disable Cloud Network Insights in that project.

## Enable Cloud Network Insights

  1. Open the Google Cloud console and navigate to **Network Intelligence** > **Cloud Network Insights**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

If the page fails to load, reach out to your Technical Account Manager to verify that your project has been granted access.

  2. Click **Enable**.

  3. If you haven't enabled the Network Management API already, click **Enable**. This can take up to 10 minutes to complete.

  4. Review the Broadcom Terms of Service.

  5. To enable Cloud Network Insights, accept the Broadcom Terms of Service and then click **Accept**.




## Disable Cloud Network Insights

After you disable Cloud Network Insights, you are no longer billed for your active paths, and the following irreversible changes occur:

  * Network paths, web paths, and alert policies are removed
  * The associated AppNeta instance is deprovisioned
  * Telemetry data is no longer collected



To disable Cloud Network Insights, do the following:

  1. Open the **Settings** page for **Cloud Network Insights**.

[Go to Cloud Network Insights Settings page](https://console.cloud.google.com/net-intelligence/cloud-network-insights/settings)

  2. Click **Disable product**.

  3. Enter `disable` and then click **Confirm**.




After you disable Cloud Network Insights, manually delete any deployed Monitoring Points. For more information, see [Delete a Monitoring Point](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/appliance-overview/managing-monitoring-points/appliance-delete.html) in the AppNeta documentation.

## Re-enable Cloud Network Insights

If you re-enable Cloud Network Insights, you must [deploy new Monitoring Points](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points) using new installation bundles generated from the re-enabled Cloud Network Insights instance. All previous pathes, alert policies, and configuration settings are lost when you disable Cloud Network Insights and must be recreated.

## What's next

  * [Review best practices](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/best-practices)
  * [Learn how to log on to AppNeta](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/access-appneta)
  * [Add a Monitoring Point](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
