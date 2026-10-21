---
url: https://docs.cloud.google.com/looker/docs/system-activity-for-looker-reports/
title: Monitoring Looker reports with System Activity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:06:56.123253+00:00
---

# Monitoring Looker reports with System Activity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/system-activity-for-looker-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Monitoring Looker reports with System Activity Stay organized with collections  Save and categorize content based on your preferences. 

Monitor the history and usage of your Looker reports with System Activity Explores. This feature provides insights into saved content, such as Looks (saved reports) and dashboards, user activity, historical query information, and instance performance statistics. You can use this data to optimize your Looker instance and inform operational decisions. System Activity collects high-volume data to supplement your business logs; its granularity and retention are subject to system constraints. When you enable the Looker reports feature on your Looker instance, System Activity dashboards and Explores also track individual report usage and details about users who created or accessed reports.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

[System Activity](https://docs.cloud.google.com/looker/docs/system-activity-pages) is an internal [LookML model](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) that connects to Looker's underlying application database. System Activity [Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) and [dashboards](https://docs.cloud.google.com/looker/docs/system-activity-dashboards) that are built upon this model show information about your Looker instance, which includes the following:

  * All Looks and dashboards that are saved on your instance
  * User and historical query information
  * Instance performance statistics



Both the granularity and retention of System Activity data are subject to system constraints. System Activity is designed for collecting high-volume data, and aggregating it can be used to supplement your business logs.

When [the Looker reports feature](https://docs.cloud.google.com/looker/docs/enabling-looker-reports) is enabled on your Looker instance, System Activity dashboards and Explores also include information about the [Looker reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) that are saved on your Looker instance. This information includes individual report usage data, as well as details about users who have created or accessed reports.

**Note:** To view information for Looker reports in System Activity, your Looker instance must be running Looker 25.4 or later.**Important:** System Activity data can be useful for supplementing monitoring and auditing activities, but it is not intended to replace your current compliance strategy.

## Before you begin

Understand the required roles and permissions and the key considerations and limitations of using System Activity.

### Required roles and permissions

To access System Activity Explores and dashboards, you must have the [`see_system_activity` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_system_activity), or you must have the Admin [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles). Looker admins have access to System Activity by default.

### Key considerations and limitations

Be aware of the following considerations and limitations when using System Activity:

  * System Activity doesn't provide information about reports on private connections Looker (Google Cloud core) instances.
  * The text in filters that are run by users is accessible in System Activity and can be viewed by any user who has permission to view the System Activity model.
  * Looker admins can modify who has view access to the System Activity model. Looker admins have access to System Activity by default. A Looker admin can grant access to System Activity to a non-admin user by giving the user the [`see_system_activity` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_system_activity).
  * System Activity dashboards and Explores are restricted in the number of concurrent queries that can be run. This restriction may increase loading times for System Activity Explores.
  * Time-based data in System Activity is stored in the Looker System time zone. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#system_time_zone) for more information.
  * It is not possible to query System Activity data using SQL Runner, as permissions for Looker's internal database are limited.
  * By default, System Activity data is stored in Looker's internal database. Most tables are truncated on a regular schedule to comply with storage limits. For example, the [History table](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#history) is truncated to the past 90 days of data. Some tables have more stringent data retention policies. To increase data retention, consider using [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity).



## System Activity dashboards

The **System Activity** section of the Looker **Admin** menu displays [built-in dashboards](https://docs.cloud.google.com/looker/docs/system-activity-dashboards) that show usage and performance information about your Looker instance. You can [download](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#downloading_your_dashboard), [schedule](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#scheduling_dashboard_data_delivery), [set alerts on](https://docs.cloud.google.com/looker/docs/alerts-overview), and [drill into](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data) metrics and elements just like on any other dashboard. Data in the System Activity dashboards is updated and cached every 12 hours.

When the Looker reports feature is enabled on your instance, the following System Activity dashboards also display information about Looker reports on your instance, as well as information about report creators and users:

  * User Activity dashboard
  * Content Activity dashboard



### User Activity dashboard

The [**User Activity** dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#user_activity_dashboard) shows information about your users and their usage of your Looker instance.

If the Looker reports feature is enabled on your instance, the **User Activity** dashboard includes additional details about report usage on your Looker instance.

In the **About Your Users** section of the **User Activity** dashboard, the **Top Report Builders** tile shows the users that created the most new reports in the last seven days.

### Content Activity dashboard

The [**Content Activity** dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#content_activity_dashboard) shows information about the dashboards, Looks, Explores, and reports that are being viewed and scheduled on your Looker instance.

If the Looker reports feature is enabled on your instance, the **Content Activity** dashboard includes the following additional details about reports, report usage, and report users and creators on your Looker instance:

  * The **Content Usage** section of the **Content Activity** dashboard includes the following additional tiles: 
    * **Total Reports** tile: Shows the total number of reports on your instance that have not been deleted.
    * **Reports Usage** tile: Shows the percentage of reports that have and that have not been used over the last 30 days.
  * In the **Popular Content and Explores** section of the **Content Activity** dashboard, the **Popular Content** tile includes details about reports. The **Content Type** field, which is used in the **Popular Content** tile, includes a `report` value. This lets you see information about reports, including the report's title, view total, embed total, API total, favorites total, and schedule total over the last 30 days.



## System Activity Explores

Looker admins and users who have been granted the [`see_system_activity`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_system_activity) permission have access to Looker's [System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) in the [**Explore** menu](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration).

When you have enabled the Looker reports feature on your Looker instance, in addition to the standard [System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#using_the_system_activity_explores), you can use the **Report** Explore to analyze data about report usage.

The **Report** Explore includes details about Looker reports, including information about report creation date and last updated date, whether reports have been moved to trash, and details about report users and creators. The cache duration for the **Report** Explore is 12 hours.

See [Using the System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#using_the_system_activity_explores) for some examples of common uses for System Activity Explores.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
