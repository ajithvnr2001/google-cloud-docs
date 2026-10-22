---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/cloud-logging/
title: Cloud logging \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:56.093828+00:00
---

# Cloud logging  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/cloud-logging/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud logging

This document describes how GKE on Azure integrates with Cloud Logging and shows you how to access your logs.

## Overview

GKE on Azure supports Cloud Logging for workloads and for system components running on control plane and node pool nodes.

GKE on Azure includes a [Fluentbit](https://fluentbit.io/)-based logging agent. On the control plane nodes, the logging agent runs as a system component; on the node pool nodes, it runs as a Daemonset. Data collected by the logging agents can be managed and deleted like any other metric and log data, as described in [Cloud Logging](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#deleting_logs) documentation.

## What data is collected

GKE on Azure logs the following information:

  * Logs for system components on each of the control plane replica.
  * Logs for system services on each of the node pool nodes.
  * Optionally, logs for workloads



## Enable workload logging

To enable workload logging, you must create a new Kubernetes cluster, version 1.22 or later.

By default, when you create a cluster GKE on Azure enables system logging. To enable workload logging, you must create a cluster with the `--logging` flag. You can choose to enable logging for system components, workloads, or both.

For example, to enable both system and workload logging on a new cluster, follow the instructions to [create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster), but include the `--logging` flag in your `gcloud` command:
    
    
    gcloud container azure clusters create CLUSTER_NAME
    ...
    --logging=SYSTEM,WORKLOAD
    

or to [update an existing cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/update-cluster):
    
    
    gcloud container azure clusters update CLUSTER_NAME
    ...
    --logging=SYSTEM,WORKLOAD
    

## Access your logs

There are several ways to access your GKE on Azure logs in Cloud Logging:

  * **Logs Explorer** – You can see your logs directly from the [Logs Explorer](https://console.cloud.google.com/logs) by using the logging filters to select the Kubernetes resources, such as cluster, node, namespace, pod, or container logs.

  * **Google Cloud CLI** – Using the [`gcloud logging read`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command, select the appropriate cluster, node, pod, and container logs.




## Understanding your logs

A log in Cloud Logging is a collection of [log entries](https://docs.cloud.google.com/logging/docs/log-entry-data-model), and each log entry applies to a certain type of [logging resource](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

### Resource types

These are the resource types that are specific to GKE on Azure:

Resource type | Display name  
---|---  
`k8s_control_plane_component` | Control plane component logs  
`k8s_node` | Node pool logs  
`k8s_container` | Workload container logs  
  
When GKE on Azure writes your cluster's logs, each log entry includes the resource type. Understanding where logs appear makes it easier to find logs when you need them.

#### Control Plane logs

Control plane logs use the `k8s_control_plane_component` resource type. These include logs from system components running on the control plane replicas, such as [`kube-apiserver`](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/). 

#### Node logs

Node logs fall under the `k8s_node` resource type. These include logs from critical system component running on the worker nodes, such as [`kubelet`](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet) and [`containerd`](https://containerd.io/). 

#### System apps logs

System apps logs fall under the `k8s_container` resource type. These include logs from pods installed on the worker nodes by GKE on Azure. Specifically, containers running in the following namespaces are included:

  * `kube-system`


  * `gke-connect`
  * `gke-system`
  * `gmp-system`
  * `asm-user-auth`
  * `cnrm-system`
  * `config-management-system`
  * `gatekeeper-system`
  * `gmp-public`
  * `istio-system`
  * `knative-serving`



## Find your logs in the Cloud Logging user interface

You can view your logs using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the Cloud Logging user interface.

### Logs Explorer

Using the Query Builder, you can build a query by adding query parameters manually. For example, if you want to explore logs for system workloads, you can start with selecting or searching for the `k8s_container` resource type, and then select the location and cluster name. You can then refine your search by filtering the container or Pod names.

The Logs Explorer offers an additional way to build your search queries using the **Logs field explorer**. It shows the count of log entries, sorted by decreasing count, for the given log field. Using the **Logs field explorer** is particularly useful for GKE on Azure logs because it provides an easy way to select the Kubernetes values for your resources. For example, you can select logs for a specific cluster, Namespace, Pod name, and container name.

For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Sample queries

This section includes sample queries that you can make on Logs Explorer.

Example 1: Get the logs of `kube-apiserver` on control plane nodes for an Azure cluster CLUSTER_NAME:
    
    
    resource.type="k8s_control_plane_component"
    resource.labels.cluster_name="azureClusters/CLUSTER_NAME"
    resource.labels.component_name="apiserver"
    

Example 2: Get the logs of `kubelet` on worker nodes for an Azure cluster CLUSTER_NAME:
    
    
    resource.type="k8s_node"
    resource.labels.cluster_name="azureClusters/CLUSTER_NAME"
    log_name="projects/PROJECT_ID/logs/kubelet"
    

Example 3: Get the logs of the `cilium-agent` container for an Azure cluster CLUSTER_NAME:
    
    
    resource.type="k8s_container"
    resource.labels.cluster_name="azureClusters/CLUSTER_NAME"
    resource.labels.container_name="cilium-agent"
    

## What's next

  * [Cloud Logging overview](https://docs.cloud.google.com/logging/docs/overview)
  * [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
  * [Building queries for Cloud Logging](https://docs.cloud.google.com/logging/docs/view/building-queries)
  * [Create logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
