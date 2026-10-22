---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations/
title: Get key spending insights for your GKE resource allocation and cluster costs \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:50.595902+00:00
---

# Get key spending insights for your GKE resource allocation and cluster costs  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Get key spending insights for your GKE resource allocation and cluster costs Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to get key spending insights to inform your resource allocation and cost optimization decisions using Google Kubernetes Engine (GKE) cost allocation. Learn about the difference between GKE cost allocation and cluster usage metering, limitations of GKE cost allocation, how to activate GKE cost allocation on both new and existing clusters, and how to filter and query your Cloud Billing BigQuery export.

This document is for Operators, Cloud architects, Developers, and Data administrators who need to manage costs as they create and configure clusters and deploy workloads in GKE. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this document, you might want to familiarize yourself with [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke)

## Potential data volume increase

Enabling GKE cost allocation can increase your storage and querying costs in BigQuery. The exact increase depends on the number of distinct label and namespace combinations you use across Pods and clusters.

Enabling GKE cost allocation does not change the total cost of your GKE usage. The sum of the cost line items in your export is the same and existing queries and reports you have built on the billing export return the same values.

## GKE cost allocation and cluster usage metering

GKE cost allocation is different from [cluster usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) in the following ways:

  * GKE cost allocation provides an alternative to cluster usage metering for getting cluster information.
  * GKE cost allocation calculates cluster costs in your Cloud Billing account instead of aggregating the data in a Data Studio template.
  * GKE cost allocation lets you view a cluster's cost data in the Cloud Billing Google Cloud console and in the Cloud Billing detailed export.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have completed the steps to [Export detailed usage cost data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). If your organization is already exporting data, you must have access to query the tables.
  * Ensure that you have an existing Standard cluster. To create a Standard cluster, see [Create a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).



### Limitations and restrictions

  * You can view GKE cost allocation data only in the Cloud Billing detailed usage cost data export to BigQuery. GKE allocation data isn't available in the standard usage cost data that's exported to BigQuery.
  * If you enable GKE cost allocation, your billing export starts including additional line items for your GKE resources from that date. The billing export does not backfill data.
  * If you disable GKE cost allocation, your billing export stops including additional line items, but does not modify or remove previous line items that were generated while the feature was enabled.
  * GKE cost allocation data is based on resource requests, not resources consumed. To learn more about the differences between resource requests, resource limits, and resource consumption, see [Kubernetes best practices: Resource requests and limits](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-resource-requests-and-limits).
  * GKE cost allocation supports the following resource SKU types: 
    * Compute Engine VM Instance vCPU SKUs
    * Compute Engine VM Instance RAM SKUs
    * Compute Engine VM Custom Extended Instance RAM SKUs
    * Compute Engine VM Instance GPU SKUs
    * Compute Engine PD Capacity SKUs
    * Cloud TPU Instance SKUs
  * If a Pod has more than 50 Kubernetes labels, none of those labels will be available in the Cloud Billing section of the Google Cloud console or the Cloud Billing detailed export.
  * After you enable GKE cost allocation, it can take up to three days for data to appear in Cloud Billing.
  * GKE cost allocation includes data from Persistent Disks with the following exceptions: 
    * Only supports `PersistentVolume` resources provisioned dynamically through `PersistentVolumeClaims` or [Generic Ephemeral Volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes).
    * Only supports `PersistentVolume` resources provisioned by the [Compute Engine persistent disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) or with the deprecated `kubernetes.io/gce-pd` storage plugin with `ReadWriteOnce` or `ReadWriteOncePod` access mode.
    * Persistent Disks with an uptime of less than 30 minutes might not be tracked. Persistent Disks with at least 30 minutes uptime are always tracked.
  * The Cloud TPU version must be Cloud TPU v4 or later.
  * GKE cost allocation does not work with A4 or A4X VM instances, or GPUs attached to those instances.
  * GKE cost allocation is not supported when using external node management solutions that bypass GKE node pools.
  * When using Committed Use Discounts (CUDs) with discount sharing enabled, costs for the instances covered by CUDs might not be fully broken down by GKE cost allocation and might be attributed to a namespace like `goog-k8s-unsupported-sku`.
  * GKE cost allocation does not support [native sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/), which are init containers with `restartPolicy: Always` configuration. Resources requested by sidecar containers are not attributed to the Pod's namespace and are reported in the `kube:unallocated` namespace instead.



## View GKE cluster costs

When you enable GKE cost allocation, the cluster name and namespace of your GKE workloads appear in the `labels` field of the billing export to BigQuery:

| **Resource label key (`labels.key`)** | **Resource label value (`labels.value`)**  
---|---|---  
**Description** |  [ Kubernetes labels ](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) have the following format: `k8s-label/${k8s-label-key}`, where `${k8s-label-key}` is the key of the Pod's Kubernetes label. The billing label `k8s-label/${k8s-label-key}` has the same value as the corresponding Kubernetes Pod label. |  If a Kubernetes label key collides with a VM label key, the Kubernetes label value overrides the VM label value. Cluster and node pool resource labels are applied to resources using the following priority from highest to lowest: 

  * Individual resource, such as instance or storage
  * Node pool
  * Cluster

  
**Cluster name** | `goog-k8s-cluster-name` | [cluster-name]  
**Namespace** | `k8s-namespace` | [namespace]  
**Workload type** | `k8s-workload-type` | [workload-type]   
(e.g. `apps/v1-Deployment`,`apps/v1-StatefulSet`,`apps/v1-DaemonSet`,`apps/v1-ReplicaSet`,`batch/v1-Job`,`batch/v1-CronJob`,`core/v1-Pod`)  
**Workload name** | `k8s-workload-name` | [workload-name]  
  
For more information, see [Schema of the detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#detailed-usage-cost-data-schema).

Additionally, the following namespaces are used to track overhead and unallocated resources:

  * `kube:system-overhead`: This accounts for node resources that are not available to Pods. These resources are set aside by the system for running the Kubernetes framework (including but not limited to kubelet, kube-proxy, containerd). This is the difference between the Node's capacity and allocatable resources.
  * `kube:unallocated`: Resources are neither requested by workloads nor requested for system overhead.



If GKE cannot determine the cost allocation for a resource, the export includes one of the following values:

  * `goog-k8s-unknown`: Cloud Billing couldn't process the SKU. This can occur when a new Compute Engine instance is being provisioned. You can expect some `goog-k8s-unknown` values during node startup and shutdown, for example when GKE autoscales a cluster.
  * `goog-k8s-unsupported-sku`: GKE cost allocation does not support this SKU. Treat this the same as `<blank>`/`NULL`. There is no guarantee that a SKU is always labeled with this value.
  * `<blank>`/`NULL`: GKE cost allocation does not track this resource. This can occur when GKE cost allocation is not enabled, or the resource does not belong to a GKE managed cluster.



Costs for Persistent Disks are tracked when the Persistent Disk's backing `PersistentVolumeClaims` are claimed by Pods. The Persistent Disk costs inherit all of the metadata, such as Pod labels and namespaces, of the claiming Pod, until their `PersistentVolumeClaims` are deleted. For `PersistentVolumeClaims` that are deleted but retain `PersistentVolumes` according to the reclaim policy, costs of the Persistent Disks are tracked as unallocated.

Labels applied directly to `PersistentVolumeClaims` do not appear in the Cloud Billing section of the Google Cloud console or the Cloud Billing detailed export.

For Extended RAM, the same proportion of total cost is allocated to a workload for both the Regular RAM and Extended RAM SKUs based on the resource requested.

### Enable GKE cost allocation

You can enable GKE cost allocation on a new or existing cluster using the gcloud CLI or the Google Cloud console.

### gcloud

Update a cluster using the `--enable-cost-allocation` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-cost-allocation
    

Replace `CLUSTER_NAME` with the name of the cluster.

You can also use the `--enable-cost-allocation` flag when you create a new cluster by using the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-cost-allocation) command.

### Console

To enable GKE cost allocation on an existing cluster, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console. [Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)
  2. Click the name of the cluster you want to modify.
  3. On the **Clusters** page, in the **Features** section, click _edit_ next to **Cost Allocation**.
  4. In the **Edit Cost Allocation** dialog, select the **Enable Cost Allocation** checkbox.
  5. Click **Save changes**.



## Verify GKE cost allocation is enabled

### gcloud

Describe the cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

The output is similar to the following:
    
    
    ...
    costManagementConfig:
      enabled: true
    ...
    

In this output, `costManagementConfig` indicates that GKE cost allocation is enabled.

### Console

To check if GKE cost allocation is enabled on an existing cluster, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console. [Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)
  2. Click the name of the cluster you want to modify.
  3. On the **Clusters** page, in the **Features** section, next to **Cost Allocation** it will show whether GKE cost allocation is enabled.



## View and filter the billing data export

You can use the Kubernetes labels described in this document to filter your costs in the Cloud Billing reports page in the Google Cloud console.

You can filter and group your GKE costs in the BigQuery dataset by using one of the following methods:

  * In BigQuery, [run a query](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * In Cloud Billing, [generate and run a query against your exported billing data](https://docs.cloud.google.com/billing/docs/how-to/reports#generate-query) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).



You can use the following example queries with these methods to filter the exported billing data for information that's specific to GKE:

  * **Get costs after credits by namespace** :
        
        SELECT
          labels.value as namespace,
          SUM(cost) + SUM(IFNULL((SELECT SUM(c.amount) FROM UNNEST(credits) c), 0)) AS cost_after_credits,
        FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
        LEFT JOIN UNNEST(labels) as labels
          ON labels.key = "k8s-namespace"
        GROUP BY namespace
        ;
        

  * **Get cluster costs before credits** :
        
        SELECT
          SUM(cost) AS cost_before_credits,
          labels.value AS cluster_name
        FROM  `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
        LEFT JOIN UNNEST(labels) as labels
          ON labels.key = "goog-k8s-cluster-name"
        GROUP BY labels.value
        ;
        

  * **Get total GKE-related costs by SKU** :
        
        SELECT
          project.id AS project_id,
          labels.value AS cluster_name,
          sku.id AS sku_id,
          sku.description AS sku_description,
          SUM(cost) AS cost
        FROM `project-ID.dataset.gcp_billing_export_resource_v1_XXXXXX-XXXXXX-XXXXXX`
        JOIN UNNEST(labels) AS labels
          ON labels.key = "goog-k8s-cluster-name"
        GROUP BY
          cluster_name, project_id, sku_description, sku_id
        ;
        

  * **Get costs by workload name before credits** :
        
        SELECT
          labels.value as workload_name,
          SUM(cost) AS cost
        FROM `project-ID.dataset.gcp_billing_export_resource_v1_YYYYYY-YYYYYY-YYYYYY`
        LEFT JOIN UNNEST(labels) as labels
          ON labels.key = "k8s-workload-name"
        WHERE labels.value IS NOT NULL
        GROUP BY workload_name
        ORDER BY cost DESC
        ;
        




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this page, disable GKE cost allocation for the cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --no-enable-cost-allocation
    

You can also [delete the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster) that you created.

You can also use the `gcloud` command-line tool to view and manage your labels. For more information, see the [`gcloud resource-manager tags` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags).

## What's next

  * Learn how to [understand cluster resource usage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering).
  * Learn how to [view cost-related optimization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics).
  * Learn more about [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * Learn how to [create and manage cluster and node pool labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels).
  * Learn how to [right-size your workloads at scale](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/right-size-workloads-at-scale).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
