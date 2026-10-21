---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/predefined-dashboards/
title: Use predefined dashbboards \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:02.712220+00:00
---

# Use predefined dashbboards  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/reference/predefined-dashboards/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Use predefined dashbboards Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/reference/predefined-dashboards)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/reference/predefined-dashboards)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document describes the predefined monitoring dashboards that are available for Distributed Cloud. You'll also find information and links to resources to help you work with dashboards.

Cloud Monitoring provides a curated set of dashboards that are specific to various Google Cloud services. The charts on these dashboards present a selection of metrics relevant to a specific service. These dashboards are installed automatically when a given service, such as GKE Enterprise is detected.

## Predefined dashboards

When Cloud Monitoring detects that the GKE Enterprise metric `kubernetes.io/anthos/container/uptime` is available, it makes the predefined GKE Enterprise dashboards available in your project. When you create GKE clusters, this metric is available by default, so the dashboard installation is automatic. The following predefined dashboards are added:

Dashboard name | Description  
---|---  
Anthos Cluster Control Plane Uptime | This dashboard has the following charts to indicate the uptime of control plane components: 

  * API Server Uptime
  * Scheduler Uptime
  * Controller Manager Uptime
  * ETCD Uptime

  
Anthos Cluster Node Status | This dashboard has the following charts to indicate the status of your cluster nodes: 

  * Node condition
  * CPU usage
  * Allocatable CPU cores
  * CPU allocatable utilization
  * Memory usage
  * Allocatable memory
  * Memory allocatable utilization
  * Available filesystem size

  
Anthos Cluster Pod Status | This dashboard has the following charts to indicate the status of pods running in your clusters: 

  * Number of Restarts per Container
  * Container Memory Usage Per Container
  * Container CPU Usage Per Container
  * Network Ingress Per Pod (Bytes)
  * Network Egress Per Pod (Bytes)
  * Pod Phase
  * Kubernetes Container - Memory Request Utilization
  * Kubernetes Container - Memory Limit Utilization
  * Kubernetes Container - CPU Request Utilization
  * Kubernetes Container - CPU Limit Utilization
  * Kubernetes Pod - Volume Utilization

  
Anthos Cluster on VMware VM Status | This dashboard has the following charts to indicate the health of VMware VMs: 

  * CPU Readiness Per vCPU (Percentage)
  * Memory Page Fault Latency (Percentage)
  * Average Virtual Disk Read Latency (Seconds)
  * Average Virtual Disk Write Latency (Seconds)

  
Anthos Cluster Utilization Metering | This dashboard has the following charts to indicate the requests and consumption of CPU, Memory, and Ephemeral storage per cluster: 

  * Kubernetes Container - Request Cores [SUM]
  * Kubernetes Container - CPU Usage Time [SUM]
  * Kubernetes Container - Memory Request [SUM]
  * Kubernetes Container - Memory Usage [SUM]
  * Kubernetes Container - Ephemeral Storage Request [SUM]
  * Kubernetes Container - Ephemeral Storage Usage [SUM]

  
  
For more information about predefined dashboards, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards). For information about viewing and working with your dashboards, see [View Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).

## Integrations page

Starting with GKE Enterprise release 1.15.0, a new **GKE Enterprise** integration is available from the Cloud Monitoring **Integration** page. You see this integration if you've [installed GKE clusters](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-create-clusters) or if you've [set up GKE Enterprise on Google Cloud](https://docs.cloud.google.com/anthos/docs/setup/set-up-google-cloud). The GKE Enterprise integration includes information, including previews, for the predefined GKE Enterprise dashboards:

  * Anthos Cluster Control Plane Uptime
  * Anthos Cluster Node Status
  * Anthos Cluster Pod Status 
  * Anthos Cluster on VMware VM Status 
  * Anthos Cluster Utilization Metering



As described in the preceding section, these dashboards are automatically installed when you have GKE Enterprise clusters. You can't edit these dashboards directly, since they're fully managed by Google. However, you can make a copy of the dashboard and customize the copied version, or you can add these dashboards as [custom dashboards](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates) from the Sample library.

## Dashboards for older clusters

If you created clusters with an earlier version of Distributed Cloud, you may have out-of-date dashboards. Starting with Distributed Cloud version 1.16.0, the following custom dashboards will be deprecated:

**Note:** You can find these dashboards in the **Custom** category on the **Dashboards Overview** page. The names of the deprecated dashboards are similar to the names of the current predefined dashboards. In some cases, only the casing is different.
* GKE on-prem node status
* GKE on-prem control plane uptime
* GKE on-prem pod status
* GKE on-prem vSphere vm health status 

These dashboards were installed automatically if you created clusters with Distributed Cloud release 1.15.0 or lower.

We recommend that you remove these deprecated dashboards as described in [Delete a custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards#delete-dashboard).

For more information about dashboards, including how to install and use them, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards) in the Google Cloud Observability documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
