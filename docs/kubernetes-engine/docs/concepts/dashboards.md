---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards/
title: GKE in the Google Cloud console \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:45.950421+00:00
---

# GKE in the Google Cloud console  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  GKE in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of the Google Kubernetes Engine (GKE) pages available in the Google Cloud console for both administrators and developers.

Before reading this page you should be familiar with the following, as well as [basic Kubernetes concepts](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes):

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [Cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle)



## Overview

The Google Cloud console offers multiple pages that help you manage your project's GKE clusters and their resources. You can use these pages to create, view, inspect, manage, and delete GKE resources. You can also create Kubernetes [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) for stateless applications directly from the [Workloads](https://console.cloud.google.com/kubernetes/workload) page.

In conjunction with the `gcloud` and `kubectl` command-line tools, the GKE pages in the Google Cloud console are helpful for DevOps workflows, troubleshooting issues, quick prototyping, and when working with multiple GKE clusters or [Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Rather than using the command-line to query clusters for information about their resources, you can use these pages to get information about all resources in every cluster quickly and easily.

## Required roles

If you are not a project owner, you must have the following Identity and Access Management (IAM) role at minimum to view clusters in the Google Cloud console:

  * Kubernetes Engine Viewer (`roles/container.viewer`): This role lets users view the GKE **Clusters** page and other container resources in the Google Cloud console. For details about the permissions included in this role, or to grant a role with read or write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.



If your organization has clusters outside Google Cloud, you need [additional permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console) to view and sign in to these clusters and their resources.

## GKE console pages

The following sections discuss each console page and its features.

### GKE overview

The [GKE overview](https://console.cloud.google.com/kubernetes/overview) provides a "big picture" overview of your [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), including any security concerns, estimated fleet costs, your fleet-wide Policy Controller coverage, and the synchronization status of your Config Sync packages. It also gives a fleet-level view of your resource utilization that you can use to help optimize spending, application design, and resource allocation.

To learn more, see [Use the GKE overview dashboard](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard).

### Kubernetes clusters

[Kubernetes clusters](https://console.cloud.google.com/kubernetes/list) shows every Kubernetes cluster you have created in your project. You can use this page to create new clusters, inspect details about clusters, make changes to their settings, connect to them using Cloud Shell, and delete them.

If you have registered a cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), the cluster's fleet is displayed in the **Fleet** column in the cluster list. You can learn more about viewing fleet status in the Google Cloud console in [Get fleet membership status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status).

Each cluster has an **Actions** menu that lets you quickly perform common operations. To use this, click more_vert **Actions** next to the cluster in the cluster list. From this menu, you can:

  * Click **Edit** to make changes to the cluster's settings in its details page.
  * Click **Connect** to connect to the cluster from the command line with `kubectl`, or to open the Workloads page.
  * Click **Delete** to delete the cluster.
  * Click **Register** or **Unregister** to update the cluster's fleet membership.
  * Click **Change tier** to change the [cluster tier](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#cluster_tier).



Clusters outside Google Cloud also have an option to authenticate to the cluster using your chosen identity provider.

You can also click the **Utilization** , **Observability** , and **Cost optimization** tabs to view the following information:

  * **Utilization** : View a list of all clusters and sort them by CPU, memory, or disk utilization. This lets you quickly see which specific clusters are the biggest users of their resources. You can also view how many container restarts and error logs your cluster has. To learn more, see [Fleet resource utilization metrics](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/utilization-metrics).
  * **Observability** : View infrastructure health metrics for your GKE clusters and workloads. To learn more, see [Observability for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).
  * **Cost optimization** : View cluster-level metrics that describe how effectively your GKE clusters and workloads are utilizing the Compute Engine resources you pay for. To learn more, see [View cost-related optimization metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-optimization-metrics).



#### Cluster details

In the **Clusters** page, you can select a cluster to view its details page, which includes the following tab views:

  * **Details** displays the current settings for the cluster and its node pool. Settings with an edit button are editable unless the edit button has been disabled. Settings that can't be edited under any circumstances show a lock icon. You can learn more about cluster settings in [Cluster configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters). You can also request a [cluster upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) from this page: when a new upgrade is available, an **Upgrade Available** notification is displayed.

  * **Nodes** (Standard clusters only) lists all of the cluster's nodes and their requested CPU, memory, and storage resources.

  * **Storage** displays the persistent volumes and storage classes provisioned for the cluster's nodes.

  * **Observability** displays [cluster metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).

  * **Logs** displays cluster and autoscaler logs.

  * **App errors** displays recent application errors from the cluster.




From the **Clusters** page, you can also view the underlying code by clicking the **Equivalent code** button. You can view the code equivalent for Google Cloud CLI, REST API, or Terraform ([Preview](https://cloud.google.com/products#product-launch-stages)).

**Caution:** Because the Terraform code equivalent is in Preview, review it carefully before applying. We recommend using it as a starting point, and should be reviewed for compatibility with your Terraform provider version. You should always test generated code in a safe environment before production use.

### Workloads

The [Workloads](https://console.cloud.google.com/kubernetes/workload) page lists all your running workloads. You can use this page to inspect, manage, edit, and delete workloads deployed to your clusters.

You can use the filter search option at the top of the workload list to list only specific workloads. By default, Kubernetes system objects are filtered out.

If a workload is running on a [fleet member cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), its fleet is displayed in the **Fleet** column. You can learn more about fleet information in the Google Cloud console in [Get fleet membership status](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/get-fleet-status).

You can also deploy stateless applications directly from the Workloads page by clicking **Deploy**. For more information, refer to [Deploying a stateless application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps).

**Note:** The Workloads page hides managed workloads and will only show the top-level resource in a workload. For example, for a Deployment, you won't see the ReplicaSet or Pod objects listed. With sufficient permissions, you can see these objects by clicking into the Deployment.

#### Workload details

If you select a workload from the list, you can view its details page, which includes several tab views:

  * **Overview** displays high level details about the workload, including its resource utilization, the number of Pod replicas, active revisions, and container details. The **Managed pods** list in this view lists the Pods that are managed by the workload. You can select a Pod from the list to view that Pod's details, events, logs, and YAML configuration file.
  * **Details** displays the current settings for the workload, including labels and selectors, annotations, update strategy, autoscaling settings, and Pod specifications. You can configure [autoscaling for Deployments](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps#autoscaling-deployments) from this view.
  * **Observability** displays [workload metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).
  * **Revision history** lists each revision of the workload, including the active revision.
  * **Events** lists human-readable messages for each event affecting the workload.
  * **YAML** displays the workload's live configuration. You can use the YAML-based text editor provided in this menu to make changes to the workload. You can also copy and download the configuration from this menu.



These items might appear differently depending on the type of workload you're viewing.

Some workloads have an **Actions** menu on their details page with convenient buttons for performing common operations. For example, you can autoscale, expose, update, and scale a Deployment from its Actions menu.

### Services

[Services](https://console.cloud.google.com/kubernetes/discovery) displays the load-balancing Service and traffic-routing Ingress objects associated with your project. It also displays the default Kubernetes system objects associated with networking, such as the Kubernetes API server, HTTP backend, and DNS.

You can select a resource from the list to view a page about that resource, which includes several tab views:

  * **Details** displays information about the resource, including its usage metrics, IP, and ports.
  * **Events** lists human-readable messages for each event affecting the resource.
  * **YAML** displays the resource's live configuration. You can use the YAML-based text editor provided in this menu to make changes to the resource. You can also copy and download the configuration from this menu.

**Note:** If your service exposes ports on Pods, the service page will prepopulate a `kubectl port-forward` command, which can be used together with web preview to debug it.

### Secrets & ConfigMaps

[Secrets & ConfigMaps](https://console.cloud.google.com/kubernetes/config) displays configuration files, `Secret` objects, `ConfigMap` objects, environment variables, and other configuration resources associated with your project. It also displays Kubernetes system-level configuration resources, such as tokens used by service accounts.

You can select a resource from this page to view a detailed page about that resource. Sensitive data stored in `Secret` objects are not displayed in the console.

### Storage

[Storage](https://console.cloud.google.com/kubernetes/storage) lists the storage resources provisioned for your clusters. When you create a `PersistentVolumeClaim` or `StorageClass` resource to be used by a cluster's nodes, those resources appear in this page.

This page has the following tab views:

  * **Persistent volume claims** list all `PersistentVolumeClaim` resources in your clusters. You use `PersistentVolumeClaim` resources with StatefulSet workloads to have those workloads claim storage space on a persistent disk in the cluster.
  * **Storage classes** list all `StorageClass` resources associated with your nodes. You use `StorageClass` resources as "blueprints" for using space on a disk: you specify the disk's provisioner, parameters (such as disk type and compute zone), and reclaim policy. You also use `StorageClass` resources for dynamic volume provisioning, which allow you to create storage volumes on demand.



You can select a resource from these dashboards to view a detailed page for that resource.

### Object Browser

[**Object Browser**](https://console.cloud.google.com/kubernetes/object/browser) lists all of the objects running in all of the clusters in your current project. You can list and filter resources by specific API groups and Resource Kinds. You can also preview YAML file for any resource by navigating to its details page.

If you run third-party components that install CustomResourceDefinitions (CRDs) in your cluster, those CRDs might not appear on the **Object Browser** page.

## What's next

  * [Read the GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).
  * [Read about Kubernetes cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
