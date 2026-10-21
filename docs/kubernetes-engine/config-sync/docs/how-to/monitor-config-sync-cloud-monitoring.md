---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring/
title: Monitor Config Sync with Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:18.475773+00:00
---

# Monitor Config Sync with Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Monitor Config Sync with Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

Exporting metrics from Config Sync to Cloud Monitoring lets you track synchronization health, detect reconciliation errors, and monitor resource usage across your clusters. Config Sync uses [OpenTelemetry](https://opentelemetry.io/) to record and export its metrics, which you can view with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) or by [using the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics). For examples of how to query these metrics, see Example debugging procedures.

We recommend that you use either Cloud Monitoring or [Prometheus](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-prometheus) to export metrics. You can also export [custom metrics](https://github.com/GoogleContainerTools/config-sync/blob/main/docs/custom-metric-filter.md). Config Sync supports exporting metrics to Cloud Monitoring only from GKE clusters.

## Grant metric-writing permission for Cloud Monitoring

To configure Cloud Monitoring for Config Sync, you must grant metric-writing permission to a service account in your project. Granting this access requires the `resourcemanager.projects.setIamPolicy` permission on the project. The service account configuration depends on whether Workload Identity Federation for GKE is enabled.

### Configure Cloud Monitoring with Workload Identity Federation for GKE

If [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) is enabled, allow Config Sync to send metrics by running this command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
       --role=roles/monitoring.metricWriter \
       --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/config-management-monitoring/sa/default" \
       --condition=None
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `PROJECT_NUMBER`: your project number.



### Configure Cloud Monitoring without Workload Identity Federation for GKE

If Workload Identity Federation for GKE is not enabled and Config Sync is running inside a Google Cloud environment, you can use the Compute Engine default service account. If your organization enforces the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), this service account might not automatically be granted the Editor (`roles/editor`) role on your project. You must grant the Monitoring Metric Writer (`roles/monitoring.metricWriter`) IAM role on the project to the Compute Engine default service account by running the following command:

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
       --role=roles/monitoring.metricWriter \
       --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `PROJECT_NUMBER`: your project number.



## Default list of metrics in Cloud Monitoring

Name | Type  
---|---  
api_duration_seconds | Distribution  
apply_duration_seconds | Distribution  
apply_operations_total | Count  
declared_resources | Last Value  
internal_errors_total | Count  
last_sync_timestamp | Last Value  
pipeline_error_observed | Last Value  
reconciler_errors | Last Value  
resource_fights_total | Count  
reconcile_duration_seconds | Distribution  
resource_group_total | Last Value  
resource_count | Last Value  
ready_resource_count | Last Value  
resource_ns_count | Last Value  
cluster_scoped_resource_count | Last Value  
kcc_resource_count | Gauge  
**Note:** Metrics without data don't appear in Metric Explorer.

To modify the metrics allowlist in Cloud Monitoring, follow the instructions to [patch the otel collector deployment with ConfigMap](https://github.com/GoogleContainerTools/config-sync/blob/main/docs/custom-metric-filter.md).

## Example debugging procedures for Cloud Monitoring

The following Cloud Monitoring examples illustrate some patterns for using OpenCensus metrics to detect and diagnose problems related to Config Sync when you are using the RootSync and RepoSync APIs.

### Metric format

In Cloud Monitoring, metrics have the following format: `custom.googleapis.com/opencensus/config_sync/METRIC`.

This metric name is composed of the following components:

  * `custom.googleapis.com`: all custom metrics have this prefix
  * `opencensus`: this prefix is added because Config Sync uses the OpenCensus library
  * `config_sync/`: metrics that Config Sync exports to Cloud Monitoring have this prefix
  * `METRIC`: the name of the metric that you want to query



### Query metrics by reconciler

RootSync and RepoSync objects are instrumented with high-level metrics that give you useful insight into how Config Sync is operating on the cluster. Almost all metrics are tagged by the reconciler name, so you can see if any errors have occurred and can set up alerts for them in Cloud Monitoring.

A reconciler is a Pod that is deployed as a Deployment. It syncs manifests from a source of truth to a cluster. When you create a RootSync object, Config Sync creates a reconciler called `root-reconciler-ROOT_SYNC_NAME` or `root-reconciler` if the name of RootSync is `root-sync`. When you create a RepoSync object, Config Sync creates a reconciler called `ns-reconciler-NAMESPACE-REPO_SYNC_NAME-REPO_SYNC_NAME_LENGTH` or `ns-reconciler-NAMESPACE` if the name of RepoSync is `repo-sync`, where `NAMESPACE` is the namespace you created your RepoSync object in.

The following diagram shows you how reconciler Pods function when the source of truth is a Git repository:

![Reconciler flow](https://docs.cloud.google.com/static/kubernetes-engine/config-sync/docs/img/reconciler-flow.svg)

For example, to filter by the reconciler name when you are using Cloud Monitoring, complete the following tasks:

  1. In the Google Cloud console, go to **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the **Monitoring** navigation pane, click _leaderboard_ **Metrics explorer**.

  3. In the **Select a metric** drop-down list, add: `custom.googleapis.com/opencensus/config_sync/reconciler_errors`.

  4. In the **Filter** drop-down list, select **reconciler**. A filter fields box appears.

  5. In the filter fields box, select **=** in the first field and the reconciler name (for example, `root-reconciler`) in the second.

  6. Click **Apply**.




You can now see metrics for your RootSync objects.

For more instructions on how to filter by a specific data type, see [Filtering the data](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

### Query Config Sync operations by component and status

When you have enabled the RootSync and RepoSync APIs, importing and sourcing from a source of truth and syncing to a cluster is handled by the reconcilers. The `reconciler_errors` metric is labeled by component so you can see where any errors occurred.

For example, to filter by component when you are using Cloud Monitoring, complete the following tasks:

  1. In the Google Cloud console, go to **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring/)

  2. In the **Monitoring** navigation pane, click _leaderboard_ **Metrics explorer**.

  3. In the **Select a metric** drop-down list, add `custom.googleapis.com/opencensus/config_sync/reconciler_errors`.

  4. In the **Filter** drop-down list, select **component**. A filter fields box appears.

  5. In the filter fields box, select **=** in the first box and **source** in the second.

  6. Click **Apply**.




You can now see errors that occurred when sourcing from a source of truth for your reconcilers.

You can also check the metrics for the source and sync processes themselves by querying the following metrics and filtering by the `status` tag:
    
    
    custom.googleapis.com/opencensus/config_sync/parser_duration_seconds
    custom.googleapis.com/opencensus/config_sync/apply_duration_seconds
    custom.googleapis.com/opencensus/config_sync/remediate_duration_seconds
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
