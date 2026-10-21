---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exclude-logs/
title: Control log ingestion \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:33:27.425827+00:00
---

# Control log ingestion  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exclude-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Control log ingestion Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) let you control the volume of Google Kubernetes Engine (GKE) logs ingested by Cloud Logging while still making verbose logging available for debugging. You can use exclusion filters to exclude matching log entries from being ingested by Cloud Logging or from being routed to the destination of a [sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks).

Create exclusion filters by using the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

Log entries are excluded after they are received by the Logging API and therefore these log entries consume [`entries.write` API quota](https://docs.cloud.google.com/logging/quotas#api-limits). You can't reduce the number of [`entries.write` API calls](https://docs.cloud.google.com/logging/quotas#log-limits) by excluding log entries.

Excluded log entries aren't available in the Logs Explorer or in Error Reporting.

For information about viewing ingestion data, see [View detailed usage in Metrics Explorer](https://docs.cloud.google.com/stackdriver/estimating-bills#metric-exp-usage).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you have a Google Cloud project with logs that you can see in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary).



### Permissions

Verify that you have one of the following IAM roles for the source Google Cloud project from which you're routing logs.

  * **Owner** (`roles/owner`)
  * **Logging Admin** (`roles/logging.admin`)
  * **Logs Configuration Writer** (`roles/logging.configWriter`)



The permissions contained in these roles let you create, delete, or modify sinks. For information on setting IAM roles, see the Logging [Access control guide](https://docs.cloud.google.com/logging/docs/access-control).

## Add an exclusion filter

The following steps describe how to add a Cloud Logging exclusion filter that excludes logs from ingestion into the `Default` Cloud Logging bucket.

  1. In the Google Cloud console, go to the **Logs Router** page:

[Go to Logs Router](https://console.cloud.google.com/logs/router)

  2. Find the row with the `_Default` sink, expand the more_vert **Actions** option, and then click **Edit sink**.

  3. In **Choose logs to filter out of sink** , for **Build an exclusion filter** , click add **Add exclusion**.

  4. Enter a name for your exclusion filter.

  5. In the **Build an exclusion filter** section, enter the filter criteria. For example, you can exclude log entries for a cluster, or specific log entries for a container.

Exclude all log entries from a specific cluster:
         
         resource.labels.cluster_name="CLUSTER_NAME"
         

Exclude log entries with the [log severity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) `DEFAULT`, `DEBUG`, `INFO`, or `NOTICE` for a specific container in a specific cluster:
         
         resource.type="k8s_container"
         resource.labels.container_name="CONTAINER_NAME"
         resource.labels.cluster_name="CLUSTER_NAME"
         severity=(DEFAULT OR DEBUG OR INFO OR NOTICE)
         

  6. Click **Update sink**.




The `_Default` sink is now configured to exclude logs with the filter you added.

## What's next

  * Learn more about [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
