---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/install-cloud-logging/
title: Install Cloud Logging on EKS attached clusters \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:52.457436+00:00
---

# Install Cloud Logging on EKS attached clusters  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/install-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/concepts/overview)



Send feedback 

#  Install Cloud Logging on EKS attached clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how GKE attached clusters integrates with Cloud Logging and shows you how to access your logs.

## Overview

GKE attached clusters supports Cloud Logging for workloads and for system components running on worker nodes.

GKE attached clusters includes a [Fluentbit](https://fluentbit.io/)-based logging agent that runs on worker nodes as a Daemonset. Data collected by the logging agents can be managed and deleted like any other metric and log data, as described in [Cloud Logging](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging#deleting_logs) documentation.

## Before you begin

  1. Fulfill the [prerequisites for GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/reference/cluster-prerequisites).

  2. [Authorize Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster#telemetry-agent-auth) to set up permissions for Google Cloud Observability.




## What data is collected

You can configure GKE attached clusters to capture any or all of the following information:

  * Logs for workloads



## Enable logging

If you don't specify a logging mode when you attach your cluster, GKE attached clusters enables system logging by default. For workload logging, your cluster must be at Kubernetes version 1.23 or later.

To enable workload logging when attaching a cluster, follow the instructions to [attach your EKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster), and include the optional `--logging` flag in the [`gcloud container attached clusters register` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register):
    
    
    gcloud container attached clusters register CLUSTER_NAME
    ...
    --logging=LOGGING_FLAG
    

To enable workload logging on a cluster that's already attached, follow the instructions to [update your EKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/update-cluster), and include the optional `--logging` flag in the [`gcloud container attached clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update):
    
    
    gcloud container attached clusters update CLUSTER_NAME
    ...
    --logging=LOGGING_FLAG
    

Replace LOGGING_FLAG with a flag indicating what kind of logging you want to enable:

  * `NONE`: disable logging.
  * `SYSTEM`: enable logging of system workloads running in specific namespaces.
  * `SYSTEM,WORKLOAD`: enable logging of both system and workload activity on your cluster's worker nodes.



## Access your logs

There are several ways to access your GKE attached clusters logs in Cloud Logging:

  * **Logs Explorer** – You can see your logs directly from the [Logs Explorer](https://console.cloud.google.com/logs) by using the logging filters to select the Kubernetes resources, such as cluster, node, namespace, pod, or container logs.

  * **Google Cloud CLI** – Using the [`gcloud logging read`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command, select the appropriate cluster, node, pod, and container logs.




## Understanding your logs

A log in Cloud Logging is a collection of [log entries](https://docs.cloud.google.com/logging/docs/log-entry-data-model), and each log entry applies to a certain type of [logging resource](https://docs.cloud.google.com/logging/docs/api/v2/resource-list).

### Resource types

These are the resource types that are specific to GKE attached clusters:

Resource type | Display name  
---|---  
`k8s_container` | Workload container logs  
  
When GKE attached clusters writes your cluster's logs, each log entry includes the resource type. Understanding where logs appear makes it easier to find logs when you need them.

#### System apps logs

System apps logs fall under the `k8s_container` resource type. These include logs from pods installed on the worker nodes by GKE attached clusters. Specifically, containers running in the following namespaces are included:

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

The Logs Explorer offers an additional way to build your search queries using the **Logs field explorer**. It shows the count of log entries, sorted by decreasing count, for the given log field. Using the **Logs field explorer** is particularly useful for GKE attached clusters logs because it provides an easy way to select the Kubernetes values for your resources. For example, you can select logs for a specific cluster, Namespace, Pod name, and container name.

For more information, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Sample queries

This section includes sample queries that you can make on Logs Explorer.

Example 1: Get the logs of the `gke-connect-agent` container for an Google Cloud cluster CLUSTER_NAME:
    
    
    resource.type="k8s_container"
    resource.labels.cluster_name="attachedClusters/CLUSTER_NAME"
    resource.labels.container_name="gke-connect-agent"
    

## What's next

  * [Cloud Logging overview](https://docs.cloud.google.com/logging/docs/overview)
  * [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
  * [Building queries for Cloud Logging](https://docs.cloud.google.com/logging/docs/view/building-queries)
  * [Create logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
