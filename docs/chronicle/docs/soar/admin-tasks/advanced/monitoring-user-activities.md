---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/monitoring-user-activities/
title: Monitor SOAR activity \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:03.263174+00:00
---

# Monitor SOAR activity  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/monitoring-user-activities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor SOAR activity

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This guide is for security administrators and security analysts who need to monitor user activities on the SOAR side of the Google Security Operations platform for auditing and compliance purposes. It explains how different API versions log actions and where to find these audit logs. Understanding these logs helps ensure accountability and provides a clear trail of actions taken within the system.

## Before you begin

Before you begin, make sure that you have the necessary permissions to access audit logs, as follows:

  * To view audit logs in Google SecOps **SOAR Settings** , you need a role that includes the `SettingsId` permission in your Identity and Access Management (IAM) permission group.
  * To view logs in the **Logs Explorer** in the Google Cloud console, you need appropriate IAM roles for accessing Cloud Logging, such as `roles/logging.viewer`.



## Key terminology

  * **Audit logs** : Records of events within Google SecOps that provide an audit trail of actions.
  * **Legacy SOAR API** : Refers to the older API framework used in Google SecOps, sometimes documented using Swagger.
  * **Chronicle API** : Refers to the modern API built on the Google Cloud infrastructure.
  * **Cloud Logging** : The centralized logging service in Google Cloud where Google SecOps audit logs are stored. It can be accessed through the **Logs Explorer** in the Google Cloud console.



## Understand audit logging for different APIs

Google SecOps logs user activities differently based on whether the action was performed using the legacy SOAR API or the Chronicle API.

### Legacy API audit logs

Actions performed through the legacy SOAR API had specific auditing behavior:

  * **Audited actions** : Only operations that involved changes or data export were logged. This includes:

    * Creating
    * Editing
    * Deleting
    * Exporting data
  * **Unaudited actions** : `ReadOnly/GET` API calls are _not_ audited in the legacy API framework.




These legacy audit logs are accessible within the Google SecOps platform on the **Audit** page.

### Chronicle API audit logs

SOAR audit logs will become available in Google Cloud once you complete the SOAR permissions migration to Cloud IAM as part of [Stage 2 of the SOAR migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#permissions-iam). These include any user actions in Google SecOps and calls made to the modern Chronicle API. Any calls made to the legacy SOAR API until November 30, 2026 will remain accessible as legacy API audit logs on the **Audit** page of the Google SecOps platform.

All API calls made using the Chronicle API are automatically audited. These audit logs are available in [Cloud Logging](https://docs.cloud.google.com/logging/docs) within your Google Cloud project. For more details on migrating and accessing these logs, see [migrate SOAR audit logs](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#migrate-soar-audit-logs).

## Access audit logs

The method to access audit logs depends on whether you are looking for logs from the legacy SOAR API or the Chronicle API.

### Access legacy API audit logs

You can view and filter the audit records for actions performed using legacy APIs on the **Audit** page of the Google SecOps platform.

  * To open the **Audit** page, go to **Settings > SOAR Settings > Advanced > Audit**.



#### View key user activity metrics

The **Audit** page displays the following key user activity metrics:

  * Most Common Activities
  * Most Common Resolutions
  * Most Active Users
  * Most Active Addresses
  * Most Common Browsers



#### View and filter the activities list

In the **Audit** page, you can filter the activities list by user, count, or group to find specific activities.

To view activity details, follow these steps:

  * To open the **Activity Details** side drawer with more information, click **View More** on any row. This view includes the following information: 
    * **Time** : Time of the activity.
    * **User** : User who performed the activity.
    * **Module** : Affected system module.
    * **Activity Type** : Action performed.
    * **Address** : IP address from which the activity originated.
    * **Browser** : Browser used for the activity.
    * **Screen Size** : Screen resolution used for the activity.
  * To view the information in **New Activity Values** or **Previous Activity Values** , click the required activity value.
  * To view **New Activity Values** and **Previous Activity Values** , click the relevant activity row and click the toggle to the ON position.

**Note:** The **Previous Activity Values** are empty for actions that created a new item.

You can view **New Activity Values** and **Previous Activity Values** side-by-side in a JSON viewer to investigate more efficiently.

### Access Chronicle API audit logs in Cloud Logging

  1. Open the Google Cloud console.
  2. In the navigation menu, go to **Logging** > **Logs Explorer**.
  3. To filter for Google SecOps audit logs, use a query in the **Query builder**. For example, you can filter by `resource.type="audited_resource"` and service name. Example query for Chronicle API audit logs:
         
         resource.type="audited_resource"
         protoPayload.serviceName="chronicle.googleapis.com"
         

  4. Execute the query to view the audit logs generated by the Chronicle APIs.




## Troubleshooting

This section provides guidance on common issues when monitoring user activities.

### Latency and limits

Audit logs in Cloud Logging are typically available within minutes, but latency can vary.

### Error remediation

If you encounter issues accessing logs, consult the following table:

Issue | Description | Fix  
---|---|---  
**Permission denied** | You receive an error indicating you lack permission to view logs. | Contact your administrator to verify that you have the `roles/logging.viewer` IAM role or an equivalent.  
**Logs not found** | Expected audit logs are not appearing in **Logs Explorer**. | Verify the time range and filters in your query. Make sure that you are looking for logs from the correct API type (the legacy SOAR API versus the Chronicle API). Check the [migrate SOAR audit logs](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#migrate-soar-audit-logs) guide to confirm log locations.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
