---
url: https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders/
title: Metrics scopes for app-enabled folders \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:19.501064+00:00
---

# Metrics scopes for app-enabled folders  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Metrics scopes for app-enabled folders Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how the metrics scope of the management project for your app-enabled folder is configured. If you [enable a folder for Application Monitoring](https://docs.cloud.google.com/app-hub/docs/overview), then Google Cloud creates a management project. The management project stores configuration information required by Google Cloud Observability services, and it is the project that you use to view your application's telemetry.

If you aren't using an app-enabled folder, then this document doesn't apply. Instead, see [Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

This page describes how to view your metrics scope quota usage, how to request a quota update, and how to manually update the metrics scope of the management project for your app-enabled folder.

## How the metrics scope for an app-enabled folder is managed

For app-enabled folders, Google Cloud Observability attempts to synchronize the list of projects in your app-enabled folder with the list of projects in the metrics scope. For example, if you add a project to the app-enabled folder, then a command is issued to add that project to the metrics scope.

When the number of projects in your app-enabled folder doesn't exceed your metrics scope quota, which defaults to 375 projects per metrics scope, then Google Cloud Observability can keep the list of projects in the metrics scope synchronized with the list of projects in your app-enabled folder. For example, suppose the quota is 375 projects per metrics scope. If your app-enabled folder contains 100 projects, then the metrics scope lists all projects in your app-enabled folder. If you add projects to your app-enabled folder, then they are also added to the metrics scope.

When the number of projects in your app-enabled folder exceeds your metrics scope quota, then the list of projects in the metrics scope won't include all projects in your app-enabled folder. For example, suppose the quota is 375 projects per metrics scope and suppose your app-enabled folder contains 380 projects. After 375 projects are added to the metrics scope, quota is exhausted and the attempts to add the remaining 5 projects fail. As a result, some application data isn't available to your management project.

If the metrics scope quota is exhausted, then you can do any of the following:

  * Change which projects listed in the metrics scope. For example, you can remove some projects from the metrics scope so that you can add other projects.

  * Request a quota increase and then add then manually add those projects that weren't added automatically. In the previous example, you must manually add the 5 projects that couldn't be added to the metrics scope. Google Cloud Observability won't retry adding a project to a metrics scope when the initial attempt for that project failed.




In both scenarios you must manually modify the metrics scope.

## Before you begin

  * If you aren't familiar with the term _metrics scope_ , then see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).


  * To get the permissions that you need to configure a metrics scope, ask your administrator to grant you the [Monitoring Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.admin) (`roles/monitoring.admin`) IAM role on the management project for your app-enabled folder and on each project that you want to add to, or remove from, the metrics scope. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View your quota usage

To prevent the need to manually manage the metrics scope for an app-enabled folder, make sure that you have quota available before you add projects to the app-enabled folder. This section describes how to view your current quota usage.

To view your metrics scope quota usage. do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select the management project for your app-enabled folder. 
  3. Select **Metric Scope**.

The **Metric Scope quota** pane displays your quota usage and quota. The icons on the **Metrics scope** tab have the following meaning:

     * The error icon, _error_ , indicates that at least 90% of your quota is consumed.

     * The warning icon, _warning_ , indicates that between 70% and 90% of your quota has been consumed.




## Request a quota increase

If your project's usage of your metrics scope quota exceeds 70%, then either a warning icon, _warning_ , or a an error icon, _error_ , is listed with the **Metrics scope** tab. By default, a metrics scope can include 375 Google Cloud projects. If you increase your quota and add more than 375 Google Cloud projects to a metrics scope, then you might experience performance issues.

To request a quota increase, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select the management project for your app-enabled folder. 
  3. Select **Metric Scope**.
  4. In the **Metrics Scope quota** pane, select **Request quota increase** , and complete the dialog.

Ensure that you request an increase of the quota named "Monitored Projects / Monitoring Metrics Scope". For more about quota adjustments, see [About quota adjustments](https://docs.cloud.google.com/docs/quotas/overview#about_increase_requests).




After your quota is increased, you can add projects to your metrics scope.

**Note:** For each project in an app-enabled folder, Google Cloud Observability issues a request to add the project to the metrics scope. If that request fails, then Google Cloud Observability won't issue a retry, even when quota becomes available. However, if quota is available, then you can add the project to the metrics scope.

## Add projects to a metrics scope

To add projects to a metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select the management project for your app-enabled folder. 
  3. Select **Metric Scope**.

The **Metric Scope** tab lists the resources monitored by the current Google Cloud project. It also lists the Google Cloud projects whose metrics scope includes the current Google Cloud project.

  4. To add Google Cloud projects to the metrics scope:

     1. In the **Google Cloud Projects** pane, click **Add Projects**.
     2. In the **Add Google Cloud projects** dialog, click **Select Projects** , and then make your selections. To save your changes, click **Add Projects**.

**Note** : Only projects in the app-enabled folder can be added to the metrics scope.

You are returned to the **Settings** page, and the table on that page is updated to list your selections. If you want to remove a Google Cloud project from the list, click _cancel_ **Remove project**.

After you add projects to a metrics scope, it takes about 60 seconds for changes to propagate through all Monitoring systems. Before you create a chart or alerting policy, wait at least 60 seconds. You might need to refresh the Google Cloud console page for the new metrics to be visible. 

The metrics scope of your selected project has been updated to include the Google Cloud projects you selected.




## Remove projects from a metrics scope

**Note** : If you remove a project from the metrics scope of the management project for your app-enabled folder, then the project you removed won't be automatically added back to the metrics scope, even when quota is available. That is, the synchronization algorithm won't override your actions.

You might want to remove projects from a metrics scope to improve performance or to free up quota so that you can add a different project. For example, by default, a metrics scope can include 375 Google Cloud projects. If you've exhausted this quota, then you might remove one project so that you can add another.

After you remove a project from a metrics scope, the time-series data stored in that project can't be charted or monitored by the scoping project. Removing a project from a metrics scope doesn't change the configuration of charts, dashboards, alerting policies, uptime checks, or groups that you defined. However, the time series displayed on charts and the time series monitored by alerting policies might change.

To remove projects from a metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select the management project for your app-enabled folder. 
  3. Select **Metric Scope**.
  4. In the **Google Cloud Projects** pane, select the projects that you want to remove, click **Remove project** , and then complete the confirmation dialog.



## List projects in a metrics scope

To list the resources in a metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the Google Cloud console, select the management project for your app-enabled folder. 
  3. Select **Metric Scope**.

The **Metric Scope** tab lists the resources monitored by the current Google Cloud project. It also lists the Google Cloud projects whose metrics scope includes the current Google Cloud project.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
