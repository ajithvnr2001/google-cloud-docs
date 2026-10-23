---
url: https://docs.cloud.google.com/unified-maintenance/docs/set-up-unified-maintenance/
title: Set up Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:31.896427+00:00
---

# Set up Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/set-up-unified-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  Set up Unified Maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions on how to set up and use Unified Maintenance. It explains how to enable the Unified Maintenance API, query it directly, and how to manage maintenance event logs that are automatically sent to Cloud Logging.

## Enable the Unified Maintenance API

To query the Unified Maintenance API directly, you need to enable the API in your Google Cloud project. If you want to view maintenance activities for [App Hub applications](https://docs.cloud.google.com/app-hub/docs/key-concepts#application), enable the API in the management project.

When you enable the API, you can [view your Unified Maintenance events](https://docs.cloud.google.com/hub/docs/maintenance) in the Unified Maintenance section of GKE Fleet.

Enable the Maintenance API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable maintenance.googleapis.com

**Note:** Unified Maintenance doesn't display historical events scheduled prior to enabling the API.

## Receive maintenance activity logs in Cloud Logging

The Unified Maintenance service sends maintenance logs automatically (independent of whether the Unified Maintenance API is enabled or not). If you have been granted one of the [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (Viewer, Editor, or Owner) in Cloud Logging for your project, you have the necessary permissions to access Unified Maintenance logs.

To learn more about the required permissions, see [Access control with IAM](https://docs.cloud.google.com/unified-maintenance/docs/access-control).

You cannot deactivate Unified Maintenance, but you can opt out of storing logs. To opt out, see [Turn off maintenance logs](https://docs.cloud.google.com/unified-maintenance/docs/turn-off-logs-storage).

To monitor the resource usage of Unified Maintenance logs in your projects, you can create a metric-threshold alerting policy. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) in the Google Cloud Observability documentation.

## What's next

  * [View maintenance activities](https://docs.cloud.google.com/hub/docs/maintenance)
  * Log schema [overview](https://docs.cloud.google.com/unified-maintenance/docs/log-schema)
  * Configure [alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications)
  * Implement [common alert policies](https://docs.cloud.google.com/unified-maintenance/docs/implement-common-alert-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
