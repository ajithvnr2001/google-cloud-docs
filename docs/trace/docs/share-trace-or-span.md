---
url: https://docs.cloud.google.com/trace/docs/share-trace-or-span/
title: Share traces and spans \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:59.654966+00:00
---

# Share traces and spans  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/share-trace-or-span/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Share traces and spans Stay organized with collections  Save and categorize content based on your preferences. 

You can share Cloud Trace data, heatmaps, or specific span details from the **Trace Explorer** page with colleagues to collaborate on investigating performance anomalies, latency spikes, and errors. As you filter, search, or inspect trace data on the **Trace Explorer** page, your browser URL updates automatically to reflect your current settings.

When a recipient opens the shared URL, the **Trace Explorer** page uses the settings in the URL, overriding any default settings. However, the displayed data depends on the recipient's Identity and Access Management (IAM) roles on the projects referenced by the URL.

## Before you begin

**Note:** To view trace data stored by a project, recipients of a shared URL must have the Cloud Trace User role (`roles/cloudtrace.user`) on that project.

To get the permissions that you need to view trace data by using the Google Cloud console, ask your administrator to grant you the [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`) IAM role on the projects that store trace data. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Share trace data

To share trace data, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Configure the **Trace Explorer** page to show the data that you want to share.

For example, you can add filters, update the time-range selector, or change the **Scope** element; the scope controls which resources are searched for trace data. Your project is searched for trace data if the first menu of this element is set to ![](https://docs.cloud.google.com/static/stackdriver/images/gc-project-icon.png)**Project** or ![](https://docs.cloud.google.com/static/stackdriver/images/trace-scope-icon.png)**_Default**. For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

The **Trace Explorer** page displays only the data that you have permission to view. A banner similar to the following indicates that you don't have the permissions needed to view all trace data that was found:
         
         You don't have the required permissions to view trace data for one or more projects listed in the trace scope. Only data stored in projects where you have the required permissions is shown.
         

To resolve this failure, identify the projects where you don't have the required permissions and ask an administrator to grant you the Cloud Trace User role.

  4. To share the URL for the **Trace Explorer** page, go to the toolbar, select _link_ **Copy link** , and then share the URL.

  5. To share the URL for a trace or span, do the following:

     1. Open the **Details** flyout for that trace or span.

You can select a span to open its details view. For traces, enter the trace ID in the _pageview_ **Trace ID** field.

     2. In the toolbar, click **Share** , and then share the URL.




## Troubleshoot

For information about how to resolve problems like a trace missing spans or not seeing any data in the **Trace Explorer** page, see [Troubleshoot](https://docs.cloud.google.com/trace/docs/troubleshooting).

## What's next

  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces)
  * [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage)
  * [View traces across projects](https://docs.cloud.google.com/trace/docs/cross-project-traces)
  * [Troubleshoot](https://docs.cloud.google.com/trace/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
