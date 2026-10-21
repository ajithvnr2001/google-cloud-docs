---
url: https://docs.cloud.google.com/monitoring/support/troubleshooting/
title: Troubleshoot \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:55.634364+00:00
---

# Troubleshoot  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud Monitoring.

## Unable to select project with a billing alerting policy

You are creating a budget and have selected the option **Link Monitoring email notification channels to this budget**. You expect to be able to select the Google Cloud project that contains the notification channels by using the _arrow_drop_down_ **Menu** of the **Select workspace** dialog. However, the project that you want to use isn't listed.

The cause of this failure is that the project you want to select has a _virtual_ [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope). In general, whether a metrics scope is virtual or instantiated has no impact to usability; however, only projects with an instantiated metrics scope are listed in this dialog.

Our engineering team is working to resolve this issue.

To have your project listed in the **Select workspace** dialog, do the following:

  1. Convert the virtual metrics scope to an instantiated metrics scope. For detailed steps, see Instantiate a metrics scope.
  2. Restart the create budget process.



### Instantiate a metrics scope

Assume that `MyNotificationsProject` contains the notification channels that you want to use in the budget. To instantiate the metrics scope for this project, you can add a second project as a monitored project. In the following steps, the second project is named `TestProject`. After the metrics scope is instantiated, you can remove `TestProject` from the list of monitored projects.

To ensure this project has an instantiated metrics scope, do the following:

  1. Create a second project. In this example, the name of this project is `TestProject`.

You can use an existing project as the second project; however, you can't use the project named `MyNotificationsProject`.

  2. Select `MyNotificationsProject` with the Google Cloud console project picker.

  3. Go to **Monitoring** and then select **Settings**.

  4. Click **Add GCP Projects**.

  5. In the table, check `TestProject`, and then click **Add projects**.

When these steps are complete, `TestProject` is listed as a monitored project of `MyNotificationsProject`. This action forces the metrics scope of `MyNotificationsProject` to be instantiated.

  6. After the metrics scope is instantiated, you can remove `TestProject` from the list of monitored projects if desired. To remove `TestProject` from the list of monitored projects, in the **GCP Projects** table, check `TestProject` and then click **Remove projects**.

  7. If you created a second project in the first step, then you can now delete that project.




## Can't add a project to a metrics scope

You attempt to add a project to a metrics scope, but the attempt fails.

To resolve this failure, try the following:

  * Make sure that you have the required permissions on the scoping project and on the project being added to the metrics scope.

For information about these permissions, see the "Before you begin" section of [Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

  * Make sure that quota is available.

By default, a metrics scope can include 375 Google Cloud projects. However, you can request an increase of the "Monitored Projects / Monitoring Metrics Scope" quota. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

  * Make sure that the project being added to the metrics scope is eligible.

The metrics scope of a management project can only list child projects in the folder associated with the management project. To learn more about management projects, see [App Hub](https://docs.cloud.google.com/app-hub/docs/overview).




## Merge button isn't visible

The **Merge** and **Move** buttons have been removed because this functionality isn't required now that Monitoring Workspaces have been replaced with [metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope). With the Workspace data model, the merge functionality was required because a Google Cloud project could only be in a single Workspace. If you wanted to change which Workspace could view a project's metrics, you had to use the merge option. With the metrics scope data model, this functionality isn't required because a Google Cloud project can be included in multiple metrics scopes.

For information about how to view metrics for multiple projects, see [Configure a metrics scope for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

## AWS logs aren't accessible.

To access logs for your AWS account, use Cloud Logging with your [AWS hosting project](https://docs.cloud.google.com/logging/docs/agent/logging/authorization#before_you_begin) selected.

## AWS metrics are missing.

AWS account metrics are stored in the Google Cloud project being used as the [AWS hosting project](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#before_you_begin). For this project to receive metrics or logs, it must be a monitored project:

  * If you've removed an AWS hosting project from a Workspace, and as a result that AWS hosting project is no longer a monitored project, then new metric and log ingestion stops immediately.

  * If you've removed an AWS hosting project from a metrics scope, and as a result that AWS hosting project is no longer a monitored project, then new metric and log ingestion stops after 2 hours.




## Unable to access Cloud Monitoring.

If you aren't able to access Cloud Monitoring, then either you don't have a role that lets you view monitoring data or the Google Cloud project hasn't been configured for Cloud Monitoring. For more information about the required permissions and roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## Project resources are missing from Monitoring.

If you add or remove resources, such as VM instances, and then immediately go to Monitoring to view your resources, your recent changes aren't consistent with the listed resources.

To resolve this issue, wait at least 10 minutes for Monitoring to discover the change in resources.

## Services are missing from Monitoring.

If you start a new service and then immediately go to Monitoring to view that service, it isn't listed in the list of services.

To resolve this issue, wait at least one hour for the new service to be discovered.

## Troubleshoot alerting policies

For information about how alerting policies are affected by the metrics and resources monitored by conditions, the duration window for conditions, and when alerts are created, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

For guidance with issues that might arise with specific alerting policies, see [Troubleshoot alerting policies](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts).

## Troubleshoot charts and metrics

For guidance with issues specific to charts or dashboards, see [Troubleshoot charts and dashboards](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts).

## Troubleshoot using the Cloud Monitoring API

For guidance with issues that might arise when you use the Cloud Monitoring API v3, see [Troubleshoot the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/troubleshooting).

## Troubleshoot uptime checks

For guidance with issues specific to uptime checks, see [Troubleshoot uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot).

## Troubleshoot the legacy Cloud Monitoring agent

For guidance on diagnosing problems with the installation or running of the legacyCloud Monitoring agent, see [Troubleshoot agent installation](https://docs.cloud.google.com/monitoring/agent/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
