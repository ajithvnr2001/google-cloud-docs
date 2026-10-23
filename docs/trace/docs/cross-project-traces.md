---
url: https://docs.cloud.google.com/trace/docs/cross-project-traces/
title: View traces across projects \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:51.751780+00:00
---

# View traces across projects  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/cross-project-traces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  View traces across projects Stay organized with collections  Save and categorize content based on your preferences. 

You can view and analyze trace data collected from multiple Google Cloud projects in a single view by configuring a trace scope and the observability scope. A trace scope lists the resources to search for trace data, and the observability scope specifies which trace scope to use by default.

To view trace spans that are stored in multiple projects—for example, when an application in one project calls a service hosted in another project—do the following:

  1. Identify the geographical storage location for the project where you plan to view trace data and for each project that stores trace data. For information about how to display the location of a project's observability bucket named `_Trace`, see [List observability buckets](https://docs.cloud.google.com/trace/docs/storage-manage#list-buckets).

When all projects store trace data in the same location, continue with the steps in this guide. For example, you can see a combined view of data from three projects that all store trace data in the `us` location.

Trace can't combine trace data stored in different locations.

  2. For each project that stores trace data, ask your administrator to grant you the [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`) role on the project. This role lets you view the trace data stored in the project.

  3. For the project where you plan to view trace data, ask your administrator to grant you the following roles on that project:

     * [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)
     * [Observability Scopes Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`)
  4. In the project where you plan to view trace data, do the following:

     1. Create a trace scope and configure it to list the default trace view for each project that stores trace data.

A project's _default trace view_ provides access to all trace data stored in the project and has the path `_Trace/Spans/_AllSpans`, where the fields `_Trace`, `Spans`, and `_AllSpans` refer to an observability bucket, a dataset, and a view. For information about trace scopes, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

     2. [Set your new trace scope as the default](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage#set-default).

When you set a default trace scope, you also update the [observability scope](https://docs.cloud.google.com/stackdriver/docs/observability/scopes#about-obs-scope), which the **Trace Explorer** page uses to identify the resources to search for trace data. Because the observability scope also identifies the default log scope, it lets the system correlate log and trace data.

If you don't perform this step, the **Trace Explorer** page automatically searches only your selected project for trace data, and the system might not be able to correlate log and trace data. For more information, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).




When the **Trace Explorer** page is open, use the **Scope** element in the toolbar to change which resources the page searches for trace data. For more information, see [Configure which views the **Trace Explorer** searches](https://docs.cloud.google.com/trace/docs/finding-traces#refine-scope).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
