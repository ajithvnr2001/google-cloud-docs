---
url: https://docs.cloud.google.com/cluster-director/docs/release-notes/
title: Cluster Director release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:20.770779+00:00
---

# Cluster Director release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-director/docs/resources)



Send feedback 

#  Cluster Director release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cluster Director. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 21, 2026

Feature

**Generally available** : You can use the C4A machine series for login nodes in clusters that use the A4X Max or A4X machine series for compute nodes. This configuration provides a consistent Arm-based architecture across compute and login nodes in your cluster. For more information, see [C4A machine series](https://docs.cloud.google.com/cluster-director/docs/compute#c4a-series).

## October 13, 2026

Feature

**Generally available** : You can use the `a3-h100-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260805` OS image family for virtual machine (VM) instances that use the A3 Mega machine type. This Ubuntu 22.04 LTS image family is the default for A3 Mega VMs, uses Slurm version 25.05, and includes NVIDIA driver 580 with CUDA Toolkit 13. For more information, see [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images).

## October 12, 2026

Feature

**Generally available** : You can use the following Ubuntu 24.04 LTS OS image families for the compute and login nodes in your cluster:

  * **A4X** : `a4x-ubuntu-2404-arm64-nvidia-595-slurm-2605-v20260903`
  * **A4, A3 Ultra, and N2** : `common-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903`
  * **A3 Mega** : `a3-h100-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903`



These image families use Slurm version 26.05 and include NVIDIA driver 595 with CUDA Toolkit 13. For more information, see [Supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images).

## October 06, 2026

Feature

**Generally available** : When you reserve compute resources for your cluster through your account team, you can include a Hyperdisk pool in the same request or in a subsequent request. This option helps ensure that your artificial intelligence (AI) and machine learning (ML) workloads have the storage resources that they require close to your compute nodes. For more information, see [Reserve capacity through your account team](https://docs.cloud.google.com/cluster-director/docs/reserve-capacity).

## October 01, 2026

Feature

**Generally available** : You can specify custom Slurm settings when you create or modify a cluster. You can apply these settings across a cluster, for specific partitions, or for compute nodes in specific nodesets. These settings let you customize workload scheduling, job preemption, queue priority, and resource limits based on your workload requirements. For more information, see [Supported Slurm settings in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-settings).

## September 30, 2026

Feature

**Generally available** : When you create a cluster by using the gcloud CLI or REST API, you can specify the Slurm version that the controller node uses. This setting helps you align software versions with your workload requirements. For more information, see [Slurm controller versions in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions).

Feature

**Generally available** : You can use existing storage pools or Hyperdisk Exapools with Hyperdisk Balanced disks for the boot disks in your compute and login nodes. Storage pools help you optimize costs because they share capacity and performance across boot disks. For more information, see [Supported storage services for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/storage).

## September 22, 2026

Feature

**Generally available** : When you create a cluster, you can specify the Rapid storage class for the Cloud Storage buckets that you create with the cluster. The Rapid storage class provides low latency and high throughput, which is ideal for artificial intelligence (AI) and machine learning (ML) workloads. For more information, see [Supported storage services for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/storage).

## September 09, 2026

Feature

**Generally available** : You can use Managed Lustre instances that use the Dynamic tier in your clusters. The Dynamic tier provides cost-effective storage for large datasets. For more information, see [Supported storage services for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/storage).

## September 04, 2026

Security

Google addressed a security vulnerability (CVE-2026-65107) in the Slurm `sbcast` tool that affects Cluster Director. For more information, see the [security bulletin](https://docs.cloud.google.com/cluster-director/docs/security-bulletins#gcp-2026-060).

## August 31, 2026

Feature

**Generally available** : You can use prebuilt Cloud Monitoring dashboards to monitor CPU, GPU, and memory usage, node health, and queue status for your Slurm workloads. This information helps you troubleshoot job queue delays, identify performance bottlenecks, and balance compute capacity. For more information, see [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards).

## August 25, 2026

Change

If you create a VM by using an auto-created reservation for a future reservation in calendar mode, then Cluster Director deletes the VM when the reservation reaches its end time. If you specify to stop the VM when the reservation reaches its end time, then Cluster Director ignores this configuration. For more information, see [Use future reservations in calendar mode](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#calendar-mode).

## July 27, 2026

Feature

**Generally available** : You can use Cluster Director built-in metrics for Slurm to monitor resource usage for your clusters and their nodes. Create custom dashboards and alerting policies in Cloud Monitoring with these built-in metrics to identify bottlenecks, optimize resource consumption, and troubleshoot errors. For more information, see [Monitor clusters with custom dashboards or alerts](https://docs.cloud.google.com/cluster-director/docs/monitor/custom-dashboards).

## June 25, 2026

Change

Documentation has been added to explain the states that a cluster node goes through in its lifecycle. Understanding these states helps you manage costs and resources, minimize disruptions, and troubleshoot errors. For more information, see [Node lifecycle](https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle).

## June 23, 2026

Feature

**Preview** : You can use Gemini in the Google Cloud console as an AI-powered interface to evaluate hardware options, estimate deployment costs, and view recommended configurations for your clusters. Interacting with Gemini helps you reach an optimal configuration for your cluster before you create or modify it. For more information, see [Design and optimize your cluster with Gemini](https://docs.cloud.google.com/cluster-director/docs/create/design-with-gemini).

## June 19, 2026

Feature

**Generally available** : You can temporarily mount Cloud Storage buckets on cluster nodes for the duration of a Slurm job. This action helps you read and write data directly to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets).

## June 18, 2026

Feature

**Generally available** : Cluster Director supports the following regions:

  * **APAC** :

    * Tokyo, Japan (`asia-northeast1`)

    * Delhi, India (`asia-south2`)

  * **North America** :

    * Los Angeles, USA (`us-west2`)

    * Salt Lake City, USA (`us-west3`)




For more information, see [Cluster Director locations](https://docs.cloud.google.com/cluster-director/docs/locations).

## June 15, 2026

Feature

**Preview** : Before you create Spot VMs in a cluster partition, you can view the real-time availability, estimated uptime, historical preemption rate, and pricing for a specific machine type and location. This information helps you maximize the chances of successfully creating Spot VMs and choose the configuration that best fits your workload needs and budget. For more information, see [Use Spot](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option#spot).

## June 02, 2026

Change

Documentation has been added to explain the lifecycle for the supported OS image families in Cluster Director. For more information, see [Image family lifecycle](https://docs.cloud.google.com/cluster-director/docs/os-images#lifecycle).

## June 01, 2026

Change

Documentation has been added to list the cluster properties that restart or recreate nodes when you modify a cluster. This information helps you minimize disruptions to your workload. For more information, see [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster).

Feature

**Generally available** : Every two minutes, Slurm runs a background health check on the GPUs attached to your compute nodes to detect errors. If the script finds an error, then it logs the error to the compute node's system logs. This check helps you monitor your GPUs without draining your nodes. For more information, see [Key Slurm capabilities](https://docs.cloud.google.com/cluster-director/docs/orchestration#capabilities).

## May 15, 2026

Change

Documentation has been added to list the available OS image families in Cluster Director, their end of support (EOS) dates, and their patch release notes. For more information, see [Image family release notes](https://docs.cloud.google.com/cluster-director/docs/image-family-release-notes).

## December 17, 2025

Announcement

[Cluster Director](https://docs.cloud.google.com/cluster-director/docs) is generally available ([GA](https://docs.cloud.google.com/products#product-launch-stages)).

Issue

Cluster operations fail if you use a gcloud CLI version earlier than 550.0.0. To resolve this issue, update the gcloud CLI to version 550.0.0 or later. For more information, see [Known issues](https://docs.cloud.google.com/cluster-director/docs/troubleshoot/known-issues).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
