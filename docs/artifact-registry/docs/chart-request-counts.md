---
url: https://docs.cloud.google.com/artifact-registry/docs/chart-request-counts/
title: Chart request counts per repository in the Metrics Explorer \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:30.732990+00:00
---

# Chart request counts per repository in the Metrics Explorer  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/chart-request-counts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Chart request counts per repository in the Metrics Explorer Stay organized with collections  Save and categorize content based on your preferences. 

Metrics Explorer lets you chart Artifact Registry request-count metrics so that you can monitor API traffic across your repositories. You can filter this data by metric labels to troubleshoot traffic spikes and analyze usage patterns.

## Required roles

To get the permissions that you need to view monitoring data and configuration information, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on the Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about controlling access to monitoring data, read [Control access with IAM](https://docs.cloud.google.com/monitoring/access-control#grant-monitoring-access).

## Chart API request counts per repository

When using Metrics Explorer, you can select the data to chart by making selections in the menus or by entering a PromQL query. For more information about creating charts, see [Create a chart in the Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Artifact Registry` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Artifact Registry Repository**.
     2. In the **Active metric categories** menu, select **Repository**.
     3. In the **Active metrics** menu, select **Data plane API request count per repository**. Data plane API requests are made by tools like Docker, Maven, Pip, Twine, or Gradle tools that make requests to the data-plane API. You can view all methods that create requests to the data-plane API in [Data plane API](https://docs.cloud.google.com/artifact-registry/docs/audit-logging#Data%20plane%20API). 

If you want to view control plane API requests made by methods listed in [`google.devtools.artifactregistry.v1.ArtifactRegistry`](https://docs.cloud.google.com/artifact-registry/docs/audit-logging#google.devtools.artifactregistry.v1.ArtifactRegistry), then select **Control plane API request count per repository**. 

     4. Click **Apply**.
The fully qualified name for this metric is `artifactregistry.googleapis.com/repository/request_count`. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. To specify a subset of data to display, in the **Filter** element, select **Add filter** , and then complete the dialog. 

For example, you can view data for the following:

     * Read requests: apply a filter for the **Metric label** `type` equal to the value `READ`.
     * Write requests: apply a filter for the **Metric label** `type` equal to the value `WRITE`.
     * Method: apply a filter for the **Metric label** `method` with a value from the methods listed in the [Data plane API](https://docs.cloud.google.com/artifact-registry/docs/audit-logging#Data%20plane%20API). For example, apply a filter `method` equal to the value of `Docker-DeleteBlob` to filter for image layer deletion.
     * Repository ID: apply a filter for the **Metric label** `repository_id` equal to the repository ID. For example `my-repo`. 

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




You can add multiple filters. For more information on filtering data, see [Filter charted data](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option) and the labels descriptions for Artifact Registry metrics in the list of [Google Cloud Metrics](https://cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-artifactregistry).

For more information on selecting data, see [Select the data to chart](https://docs.cloud.google.com/monitoring/charts/metrics-selector).

## What's next

  * Learn how to [save a chart for future reference](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#save-a-chart).
  * View Artifact Registry data-plane and control-plane methods that you can use as filters in [API interface audit logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging#api-interface-reference).
  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
