---
url: https://docs.cloud.google.com/unified-maintenance/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:53.958520+00:00
---

# Access control with IAM  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

To get the permissions that you need to fully access Unified Maintenance in GKE Fleet, ask your administrator to grant you the following IAM roles on your project: 

  * [Maintenance API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/maintenance#maintenance.viewer) (`roles/maintenance.viewer`)
  * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)
  * [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`)
  * [Monitoring NotificationChannel Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.notificationChannelViewer) (`roles/monitoring.notificationChannelViewer`)
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
  * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)
  * [Monitoring AlertPolicy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertPolicyEditor) (`roles/monitoring.alertPolicyEditor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to fully access Unified Maintenance in GKE Fleet. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to fully access Unified Maintenance in GKE Fleet:

  * To view upcoming, ongoing and completed maintenance on resources: Maintenance API Viewer (`roles/maintenance.viewer`) 
  * To view logs: Logs Viewer (`roles/logging.viewer`) 
  * To view alerting policies: Monitoring AlertPolicy Viewer (`roles/monitoring.alertPolicyViewer`) 
  * To create alerting policies: 
    * Logs Configuration Writer (`roles/logging.configWriter`)
    * Monitoring AlertPolicy Editor (`roles/monitoring.alertPolicyEditor`)
  * To edit alerting policies: Monitoring AlertPolicy Editor (`roles/monitoring.alertPolicyEditor`) 
  * To create an alerting policy with a notification: Monitoring NotificationChannel Viewer (`roles/monitoring.notificationChannelViewer`) * 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
