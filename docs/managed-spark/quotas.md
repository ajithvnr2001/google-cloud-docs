---
url: https://docs.cloud.google.com/managed-spark/quotas/
title: Managed Service for Apache Spark cluster quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:36.153211+00:00
---

# Managed Service for Apache Spark cluster quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/quotas/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-spark/docs/resources)



Send feedback 

#  Managed Service for Apache Spark cluster quotas Stay organized with collections  Save and categorize content based on your preferences. 

This page lists Managed Service for Apache Spark API quota limits, which are enforced at the project and region level. The quotas reset every sixty seconds (one-minute).

For cluster optimization strategies to help avoid quota and resource availability issues, see Resource availability and zone strategies.

If you run Managed Service for Apache Spark workloads, see [Managed Service for Apache Spark quotas](https://docs.cloud.google.com/managed-spark/quotas). **Important:** Managed Service for Apache Spark quota exhaustion can result in batch and session creation failures. For more information, see [Troubleshoot Managed Service for Apache Spark batch and session creation failures](https://docs.cloud.google.com/managed-spark/docs/support/batch-session-creation-failures). **Handling Managed Service for Apache Spark Quota Errors** : If you exceed a Managed Service for Apache Spark quota limit, a [RESOURCE_EXHAUSTED](https://docs.cloud.google.com/apis/design/errors#handling_errors) (HTTP code 429) is generated, and the corresponding Managed Service for Apache Spark API request will fail. However, since your project's Managed Service for Apache Spark quota is refreshed every sixty seconds, you can retry your request after one minute has elapsed following the failure.

The following table lists the specific and default per-project Managed Service for Apache Spark API quota types, quota limits, and the methods to which they apply.

Quota Type | Limit | Applicable API Methods  
---|---|---  
AutoscalingOperationRequestsPerMinutePerProjectPerRegion | 400 | CreateAutoscalingPolicy, GetAutoscalingPolicy, ListAutoscalingPolicies, UpdateAutoscalingPolicy, DeleteAutoscalingPolicy  
ClusterOperationRequestsPerMinutePerProjectPerRegion | 200 | CreateCluster, DeleteCluster, UpdateCluster, StopCluster, StartCluster, DiagnoseCluster, RepairCluster  
NodeGroupOperationRequestsPerMinutePerProjectPerRegion | 600 | CreateNodeGroup, DeleteNodeGroup, ResizeNodeGroup, RepairNodeGroup, UpdateLabelsNodeGroup, StartNodeGroup, StopNodeGroup  
GetJobRequestsPerMinutePerProjectPerRegion | 7500 | GetJob  
JobOperationRequestsPerMinutePerProjectPerRegion | 400 | SubmitJob, UpdateJob, CancelJob, DeleteJob  
WorkflowOperationRequestsPerMinutePerProjectPerRegion | 400 | CreateWorkflowTemplate, InstantiateWorkflowTemplate, InstantiateInlineWorkflowTemplate, UpdateWorkflowTemplate, DeleteWorkflowTemplate  
DefaultRequestsPerMinutePerProjectPerRegion | 7500 | All other operations (primarily Get operations)  
**Increasing Resource Quota Limits** : Open the Google Cloud [IAM & admin→Quotas](https://console.cloud.google.com/iam-admin/quotas) page, and select the resources you want to modify. Then click **Edit Quotas** at the top of the page to start the quota increase process. If the resources you are trying to increase aren't displayed on the page and the current filtering is "Quotas with usage," change the filtering to "All quotas" by toggling the "Quota type" drop-down.

The following table lists additional limits on total active operations and jobs at the project and region level.

Quota type | Limit | Description  
---|---|---  
ActiveOperationsPerProjectPerRegion | 5000 | Limit on the total number of concurrent active operations of all types in a single project in a single regional database  
ActiveJobsPerProjectPerRegion | 5000 | Limit on the total number of active jobs in `NON_TERMINAL` state in a single project in a single regional database  
**Increasing limits on the total active operations and jobs** : Open a Google support ticket.

## Other Google Cloud quotas

Managed Service for Apache Spark clusters use other Google Cloud products. These products have project-level quotas, which include quotas that apply to Managed Service for Apache Spark use. Some services are required to use Managed Service for Apache Spark, such as [Compute Engine](https://docs.cloud.google.com/compute "Compute Engine") and [Cloud Storage](https://docs.cloud.google.com/storage "gcs_name"). Other services, such as [BigQuery](https://docs.cloud.google.com/bigquery "bigquery_name") and [Bigtable](https://docs.cloud.google.com/bigtable "Bigtable"), can optionally use Managed Service for Apache Spark.

### Required cluster services

The following services, which enforce quota limits, are required to create Managed Service for Apache Spark clusters.

#### Compute Engine

Managed Service for Apache Spark clusters use Compute Engine virtual machines. The [Compute Engine quotas](https://docs.cloud.google.com/compute/docs/resource-quotas "Compute Engine
Quotas") are split into regional and global limits. These limits apply to clusters that you create. For example, the creation of a cluster with one `n1-standard-4` _-m_ node and two `n1-standard-4` _-w_ nodes uses 12 virtual CPUs (`4 * 3`). This cluster usage counts against the regional quota limit of 24 virtual CPUs.

**Free trial quotas:** If you use the Compute Engine free trial, your project will have a limit of 8 CPUs. To increase this limit, you must enable billing on the project. 

#### Default clusters resources

When you create a Managed Service for Apache Spark cluster with default settings, the following Compute Engine resources are used.

**Resource** | **Usage**  
---|---  
Virtual CPUs | 12  
Virtual Machine (VM) Instances | 3  
Persistent disk | 1500 GB  
  
#### Cloud Logging

Managed Service for Apache Spark saves driver output and cluster logs in [Cloud Logging](https://docs.cloud.google.com/logging "Cloud Logging"). The [Logging quota](https://docs.cloud.google.com/logging/quota-policy "Cloud Logging quota") applies to Managed Service for Apache Spark clusters.

### Optional cluster services

You can optionally use the following services, which have quota limits, with Managed Service for Apache Spark clusters.

#### BigQuery

When reading or writing data into BigQuery, the [BigQuery quota](https://docs.cloud.google.com/bigquery/quota-policy "BigQuery quota") applies.

#### Bigtable

When reading or writing data into Bigtable, the [Bigtable quota](https://docs.cloud.google.com/bigtable/quota "Bigtable quota") applies.

## Resource availability and zone strategies

To optimize clusters for resource availability and mitigate potential stockout errors, consider the following strategies:

  * **Auto Zone Placement:** When creating clusters, use [auto zone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone). This allows Managed Service for Apache Spark to select an optimal zone within your specified region, improving the chances of successful cluster creation.

  * **Regional quotas:** Verify your regional Compute Engine quotas are sufficient since quotas can be exhausted even with auto zone placement if the total regional capacity is insufficient for your requests.

  * **Machine type flexibility:** If you experience persistent stockouts with a specific machine type, use a different, more readily available machine type for your cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
