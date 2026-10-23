---
url: https://docs.cloud.google.com/kubernetes-engine/quotas/
title: Quotas and limits \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:32.896818+00:00
---

# Quotas and limits  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Google Kubernetes Engine.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on GKE resources. System limits can't be changed. 

## Quotas per project

GKE has the following quotas:

  * [**Zonal clusters**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters): 100 per zone
  * [**Regional clusters**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters): 100 per region

**Note:** All [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) are regional clusters.
  * **API reads** : 600,000 requests per minute

  * **API writes** : 600 requests per minute

  * **Token exchange requests for workload and agent identities** : 6,000 requests per minute in a region. All of the zonal and regional clusters in a specific region share this quota.




### Check your quota

Quotas can be view in Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

For more information on managing quotas, see [view and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

## Limits per cluster

The following tables describe the limits per GKE cluster.

Any GKE versions specified in the following table apply to both cluster nodes and the control plane.

Limits | GKE Standard cluster | GKE Autopilot cluster  
---|---|---  
[**Nodes per cluster**](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com/quota/nodes_per_cluster) |  **65,000 nodes** Not all node quota increases are automatic. Depending on your target node count (such as up to 5,000 nodes, up to 15,000 nodes, or up to 65,000 nodes), there are specific infrastructure requirements and you might need to contact Cloud Customer Care. For detailed information, see [Cluster size limits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes). |  **5,000 nodes** If you plan to use this limit, consider the following recommendations when designing your GKE architecture:

  * If you plan to run more than 1,000 nodes, use GKE Autopilot version 1.23 or newer.
  * Running more than 400 nodes may require lifting a cluster size quota for clusters that were created on earlier versions. [Contact support](https://cloud.google.com/support-hub) for assistance.

  
[**Nodes per node pool**](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com/quota/nodes_per_node_pool) | **1,000 nodes per zone**  
  
**2,000 TPU nodes per zone** \- requires the following or newer versions: 1.28.5-gke.135500, 1.29.1-gke.1206000, 1.30 | Not applicable  
Nodes in a zone | 

  * **No node limitations** for [container-native load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native_load_balancing) with NEG-based Ingress, which is recommended whenever possible. In GKE versions 1.17 and later, NEG-based Ingress is the default mode. 
  * **[1,000 nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#limitations)** if you are using Instance Group-based Ingress.

| Not applicable  
Pods per node1 |  **512 Pods** | Set dynamically to any value between 8 and 256. GKE considers the cluster size and the number of workloads to provision the maximum Pods per node.

  * For GKE versions earlier than 1.28, the limit is 32 Pods.
  * For GPU Pods and Performance class Pods, the limit is one Pod per node.

  
[**Pods per cluster**](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com/quota/pods_per_cluster_autopilot&metric=container.googleapis.com/quota/pods_per_cluster_standard&pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service%2520ID_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22container.googleapis.com_5C_22_22_2C_22i_22_3A_22serviceName_22%257D_2C%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22container.googleapis.com%252Fquota%252Fpods_per_cluster_autopilot_5C_22_22_2C_22i_22_3A_22metricName_22%257D_2C%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22OR_5C_22_22_2C_22o_22_3Atrue_2C_22s_22_3Atrue%257D_2C%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22container.googleapis.com%252Fquota%252Fpods_per_cluster_standard_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22,%22c%22:%5B%5D\)\))2 | **200,000 Pods**1 | **200,000 Pods**  
[**Containers per cluster**](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com/quota/nodes_per_node_pool) | **400,000 containers** | **400,000 containers**  
**Single resource size** |  **1.5 MiB** **Note:** The Kubernetes API server updates some resources before their deletion. This update can cause an increase in resource size that might permanently prevent the deletion of the resource. |  **1.5 MiB** **Note:** The Kubernetes API server updates some resources before their deletion. This update can cause an increase in resource size that might permanently prevent the deletion of the resource.  
[**Cluster state database size**](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com/quota/etcd_database_size_bytes) | **6 GB** | **6 GB**  
[**Concurrent operations**](https://console.cloud.google.com/iam-admin/quotas?service=container.googleapis.com&metric=container.googleapis.com%2Fquota%2Fpods_per_cluster_autopilot&metric=container.googleapis.com%2Fquota%2Fpods_per_cluster_standard&pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Service%2520ID_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22container.googleapis.com_5C_22_22_2C_22i_22_3A_22serviceName_22%257D_2C%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22container.googleapis.com%252Foperations_per_regional_cluster_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D_2C%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22OR_5C_22_22_2C_22o_22_3Atrue_2C_22s_22_3Atrue%257D_2C%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22container.googleapis.com%252Foperations_per_zonal_cluster_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22,%22c%22:%5B%5D\)\)) | **100 operations** | **100 operations**  
  
As a platform administrator, we recommend you to get familiar with how quotas affect large workloads that run on GKE. For additional recommendations, best practices, limits, and quotas for large workloads, see [Guidelines for creating scalable clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability).

## Resource quotas

**Note:** GKE doesn't enforce the following Kubernetes resource quotas for clusters running version 1.28 or later, however GKE doesn't restrict you from applying your own Kubernetes resource quotas.

For clusters with under 100 nodes, GKE applies [Kubernetes resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) to every namespace. These quotas protect the cluster's control plane from instability caused by potential bugs in applications deployed to the cluster. You cannot remove these quotas because they are enforced by GKE.

GKE automatically updates resource quota values in proportion to the number of nodes. For clusters with over 100 nodes, GKE removes the resource quota.

To examine resource quotas, use the following command:
    
    
    kubectl get resourcequota gke-resource-quotas -o yaml
    

To view the values for a given namespace, specify the namespace by adding the `--namespace` option.

## Notes

  1. The maximum number of Pods per GKE Standard cluster includes system Pods. The number of system Pods varies depending on cluster configuration and enabled features. ↩

  2. The maximum number of Pods that can fit in a node depends on the size of your Pod resource requests and the capacity of the node. You might not reach every limit at the same time. As a best practice, we recommend that you load test large deployments. ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
