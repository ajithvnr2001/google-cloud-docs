---
url: https://docs.cloud.google.com/error-reporting/docs/release-notes/
title: Error Reporting release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:46.197304+00:00
---

# Error Reporting release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Resources ](https://docs.cloud.google.com/error-reporting/quotas)



Send feedback 

#  Error Reporting release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Error Reporting. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

For a combined list of all release notes for the products in Google Cloud Observability, see [Consolidated release notes](https://docs.cloud.google.com/stackdriver/docs/release-notes).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/stackdriver-release-notes.xml) directly. 

## August 13, 2026

Announcement

Error Reporting can report stack traces collected from Rust applications using [`std::backtrace`](https://doc.rust-lang.org/std/backtrace/index.html). To enable, set the `RUST_BACKTRACE=1` environment variable and make sure debug symbols are enabled.

For more information, see [ReportedErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report.html?rep_location=global#reportederrorevent).

## May 28, 2026

Announcement

You can view the available regional endpoints for the Error Reporting API on the REST reference pages. For an example, see [Method: projects.events.list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/list?rep_location=global).

## March 26, 2026

Feature

You can use the [Error Reporting API MCP server](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp) to let agents and AI applications interact with your error data. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

## August 16, 2024

Feature

Error Reporting can now analyze log entries that have been routed to a log bucket in a non-global region, provided the log sink is in the same project as the log bucket.

## March 11, 2024

Change

Error Reporting can now analyze logs routed by project sinks to different projects than the source project. For more information, see [Route logs to supported destinations](https://cloud.google.com/logging/docs/export/configure_export_v2).

## January 16, 2024

Change

Announcing a common navigation pane in the Cloud console for Logging, Monitoring, Trace, and Error Reporting. When you are troubleshooting an issue, the new navigation pane simplifies accessing the pages you need to explore different types of telemetry:

  * The **Explore** section list the pages to view and analyze telemetry data.
  * The **Detect** section lists the pages you use to ensure that you are notified when errors occur.
  * The **Configure** section lists configuration and management pages.



You can continue to use the search bar to locate pages in the Cloud console and to find documentation.

## December 20, 2023

Change

The Error Reporting API is now [generally available](https://cloud.google.com/products/#product-launch-stages). For more information about the API, see [Overview](https://cloud.google.com/error-reporting/reference).

## November 01, 2023

Feature

[Troubleshooting errors with Duet AI assistance](https://cloud.google.com/error-reporting/docs/troubleshoot-errors-duet-ai) is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## October 17, 2023

Feature

You can now view error groups on your custom dashboards. This feature is GA. For information when using the Cloud Console, see [Display logs and errors on a custom dashboard](https://cloud.google.com/monitoring/charts/view-logs). For information about using the API, see [Dashboard with an ErrorReportingPanel widget](https://cloud.google.com/monitoring/dashboards/api-examples#dashboard_with_er_panel).

## September 11, 2023

Change

Error Reporting now supports Cloud Run Jobs as a monitored resource type. For more information, see [Supported monitored resources](https://cloud.google.com/error-reporting/docs/formatting-error-messages#supported_monitored_resources).

## September 05, 2023

Feature

[Troubleshooting errors with Duet AI assistance](https://cloud.google.com/error-reporting/docs/troubleshoot-errors-duet-ai) is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## August 14, 2023

Feature

Error Reporting now reports recent application errors for Google Kubernetes Engine services and clusters on a new **App Errors** tab.

  * To view service errors, go to **Kubernetes Engine** in the Google Cloud console and select **Services & Ingress**, then select a specific service and click the **App Errors** tab.
  * To view cluster errors, go to **Kubernetes Engine** in the Google Cloud console and select **Clusters** , then select a specific cluster and click the **App Errors** tab.



## August 10, 2023

Feature

In the Error Reporting page's resource filter, you can now filter GKE resources by location, cluster, namespace, and container or pod. For more information, see [Filter errors](https://cloud.google.com/error-reporting/docs/viewing-errors#filtering).

## February 03, 2023

Feature

Error Reporting now reports recent application errors for Google Kubernetes Engine workloads of type `Deployment` or `Pod`. Go to **Kubernetes Engine** in the Google Cloud console, and select **Workloads**. From the overview list, select an entry with type "Deployment" or "Pod" to see details about the workload, including recent application errors.

## January 12, 2023

Change

Errors generated by GKE applications (that is, applications with a [`MonitoredResource`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) type of `k8s_container`) now support additional labels for metadata extraction. The values of the following labels will now appear in the resource filter and in various tables and displays on **Error Reporting** pages in the Google Cloud console:

  * The `app` value from your [GKE YAML configuration](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) is now used for the primary resource label (also referred to as "service").
  * The `pod_name` label of the [`k8s_container`](https://cloud.google.com/logging/docs/api/v2/resource-list#tag_k8s_container) monitored-resource type is now used for the secondary resource label (also referred to as "version").



We continue to support the use of the YAML `metadata` labels `k8s-pod/serving_knative_dev/service` and `k8s-pod/serving_knative_dev/revision`. These labels are prioritized for users already using them over the `k8s-pod/app` and `pod_name` labels described in this note. But we encourage users to begin using the new labels.

If you do not set the `k8s-pod/app` label, GKE application errors continue to use the default service name of `gke_instances`.

## December 06, 2022

Feature

On the Error Reporting page, use the new resource filter to filter error groups by resource type. For more information, see [Filter errors](https://cloud.google.com/error-reporting/docs/viewing-errors#filtering).

## December 01, 2022

Feature

Error Reporting is a Virtual Private Cloud (VPC) supported service.

## July 11, 2022

Feature

The Logs Explorer now shows an Error Group button for log entries that are part of error groups. Click the button to access grouping details or to change which log entries the Logs Explorer shows. For more information, see [Find log entries with error groups](https://cloud.google.com/logging/docs/analyze/find-logs-error-groups).

## April 28, 2022

Feature

**Preview** : You can now get notification recommendations and insights for Error Reporting. For more information, see [Error Reporting notification recommender and insights](https://cloud.google.com/recommender/docs/error-reporting/notification-recommender).

## March 28, 2022

Change

Error Reporting now supports Webhooks and Slack as notification channels. For more information, see [Create notification channel](https://cloud.google.com/error-reporting/docs/notifications).

## July 08, 2021

Change

Error Reporting notifications has been upgraded to use the Alerting infrastructure. For more information, see the [Notifications](https://cloud.google.com/error-reporting/docs/notifications) guide.

## March 31, 2021

Change

Service Errors is now available Generally Available (GA). Service Errors automatically captures and groups Google Cloud service errors and notifies you when these errors occur. For more information, refer to the [Managing Service Errors](https://cloud.google.com/error-reporting/docs/service-errors) documentation.

## March 03, 2021

Change

Error Reporting has been updated to only analyze logs that are stored in global buckets in the same project where they are ingested. For more information, see [Using Error Reporting with regionalized logs](https://cloud.google.com/error-reporting/docs/regionalization).

## December 13, 2019

Change

Error Reporting now infers the service name and version from the `logEntry` fields named `k8s-pod/serving_knative_dev/service` and `k8s-pod/serving_knative_dev/revision` for Knative Serving labels on Cloud Run on Google Kubernetes Engine. This replaces the current default value of `gke_instances` for service name.

## May 08, 2019

Feature

**API**

Error events written as instances of [`ReportedErrorEvent`](https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent) generate properly formatted error messages in Stackdriver Logging.

## January 18, 2019

Feature

**Error detection for Python applications** has been improved. You might see more newly detected error groups or receive more notifications.

## December 19, 2017

Feature

**Resolution Status** features are now Generally Available. You can now assign a status to your error groups, making it easier to triage errors.

## June 05, 2017

Feature

**IAM roles** : Stackdriver Error Reporting IAM roles are now available. See [Error Reporting IAM roles](https://cloud.google.com/error-reporting/docs/iam#iam_roles).

## May 01, 2017

Feature

**Error filters** : You can now filter errors by custom text in addition to filtering by time, service, and version.

## October 20, 2016

Feature

**Cloud Functions** : Cloud Functions automatically reports unhandled JavaScript exceptions to Stackdriver Error Reporting.

## September 08, 2016

Feature

**C++** and **Ruby** are now supported.

Fixed

**PHP** stack traces are better supported.

## August 16, 2016

Feature

[**Cloud Console mobile app**](https://cloud.google.com/console-app) now supports Error Reporting.

## July 18, 2016

Feature

**App Engine** : Error Reporting is now generally available for Google App Engine standard environment.

## July 12, 2016

Feature

**API** : The Stackdriver Error Reporting API has a new endpoint to report errors: [`projects.events.report`](https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report).

## June 27, 2016

Feature

The Google Cloud console home page now has an Error Reporting card.

## March 17, 2016

Feature

**Beta release** of Stackdriver Error Reporting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
