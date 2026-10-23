---
url: https://docs.cloud.google.com/monitoring/settings/multiple-projects/
title: Configure a metrics scope \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:14.256121+00:00
---

# Configure a metrics scope  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/settings/multiple-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Configure a metrics scope Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Google Cloud console to configure a Google Cloud project so that you can chart and monitor time-series data stored in multiple projects. This document is intended for developers and system administrators who need to manage time-series data for services and resources that are associated with different projects.

For information about configuring a Google Cloud project programmatically, see [Configure a metrics scope by using the API](https://docs.cloud.google.com/monitoring/settings/manage-api).

The metrics scope of a Google Cloud project determines the time-series data that the project can chart or monitor with alerting policies.

## App Hub applications and metrics scopes

You manage the metrics scope for [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) host projects and management projects for single-project boundaries. You can manage the metrics scope either by using the [Google Cloud console](https://docs.cloud.google.com/monitoring/settings/multiple-projects) or the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/settings/manage-api).

Google Cloud manages the metrics scope for app-enabled folders, unless adding a project to the metrics scope fails due to exhaustion of the metrics scope quota. In that case, you can request a quota increase and then manually add projects to the metrics scope of the management project for your app-enabled folder. To learn more, see [Metrics scopes for app-enabled folders](https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders).

## Before you begin

  * If you aren't familiar with the terms _metrics scope_ and _scoping project_ , then see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).


  * To get the permissions that you need to configure a metrics scope, ask your administrator to grant you the [Monitoring Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.admin) (`roles/monitoring.admin`) IAM role on the scoping project and on each project that you want to add to, or remove from, the metrics scope. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), then you need to consider the order in which you configure a metrics scope and your VPC perimeters. Cloud Monitoring performs the VPC perimeter check when a project is _added_ to a metrics scope:

    * When you create the VPC perimeter first and then try to add a project to the metrics scope, the perimeter validation process runs. This process verifies that the added container is in the same perimeter as the scoping project, or that it is connected to the scoping project by a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters). If the perimeter validation fails, then the addition of the project to the metrics scope also fails.

    * When you configure the metrics scope first and then create your perimeters, the perimeter validation process doesn't run. This approach lets you access time-series data for projects that are in different perimeters.

  * If you configure IAM roles or grant access to projects, then consider the implications of permissions on a project whose metrics scope includes projects other than the scoping project. A role that grants read permission to Monitoring on the scoping project lets the principal view charts and alerting policies that might display data that is stored by a project included in the metrics scope.




## Add projects to a metrics scope

To add projects to a metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) host project configurations, select the host project. 
  3. Select **Metric Scope**.

The **Metric Scope** tab lists the resources monitored by the current Google Cloud project. It also lists the Google Cloud projects whose metrics scope includes the current Google Cloud project.

  4. To add Google Cloud projects to the metrics scope:

     1. In the **Google Cloud Projects** pane, click **Add Projects**.
     2. In the **Add Google Cloud projects** dialog, click **Select Projects** , and then make your selections. To save your changes, click **Add Projects**.

You are returned to the **Settings** page, and the table on that page is updated to list your selections. If you want to remove a Google Cloud project from the list, click _cancel_ **Remove project**.

After you add projects to a metrics scope, it takes about 60 seconds for changes to propagate through all Monitoring systems. Before you create a chart or alerting policy, wait at least 60 seconds. You might need to refresh the Google Cloud console page for the new metrics to be visible. 

The metrics scope of your selected project has been updated to include the Google Cloud projects you selected.




## Remove projects from a metrics scope

You might want to remove projects from a metrics scope to improve performance or to free up quota so that you can add a different project. For example, by default, a metrics scope can include 375 Google Cloud projects. If you've exhausted this quota, then you might remove one project so that you can add another.

After you remove a project from a metrics scope, the time-series data stored in that project can't be charted or monitored by the scoping project. Removing a project from a metrics scope doesn't change the configuration of charts, dashboards, alerting policies, uptime checks, or groups that you defined. However, the time series displayed on charts and the time series monitored by alerting policies might change.

To remove projects from a metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) host project configurations, select the host project. 
  3. Select **Metric Scope**.
  4. In the **Google Cloud Projects** pane, select the projects that you want to remove, click **Remove project** , and then complete the confirmation dialog.



## List projects in a metrics scope

To list the resources in a metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) host project configurations, select the host project. 
  3. Select **Metric Scope**.

The **Metric Scope** tab lists the resources monitored by the current Google Cloud project. It also lists the Google Cloud projects whose metrics scope includes the current Google Cloud project.




## Request a quota increase

By default, a metrics scope can include 375 Google Cloud projects. However, you can request an increase of the "Monitored Projects / Monitoring Metrics Scope" quota. Increasing your quota beyond the default value of 375 Google Cloud projects might cause performance issues.

For instructions about how to request a quota increase, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

## Select a different metrics scope

The project selected in the Google Cloud console project picker is the scoping project of the current metrics scope. There is a one-to-one relationship between a scoping project and a metrics scope.

To select a different metrics scope, select a different project with the Google Cloud console project picker.

## What's next

  * [Quotas and limits](https://docs.cloud.google.com/monitoring/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
