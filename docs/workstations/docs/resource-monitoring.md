---
url: https://docs.cloud.google.com/workstations/docs/resource-monitoring/
title: Cloud Workstations resource monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:08.273127+00:00
---

# Cloud Workstations resource monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/resource-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Cloud Workstations resource monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor resources such as CPU, disk, and network used by Cloud Workstations.

## Overview

Cloud Workstations uses [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits) to back virtual machines (VMs), which are integrated with Cloud Monitoring by default. The VMs backing workstations are also [labeled](https://docs.cloud.google.com/workstations/docs/label-resources#cloud-workstations-resource-labels) to make them identifiable in Cloud Monitoring.

To view the metrics for the VMs backing your workstations:

  1. Ensure that you have the [Metrics Viewer](https://docs.cloud.google.com/monitoring/access-control#monitoring_roles) IAM role (`roles/roles/monitoring.viewer`).

  2. Go to Cloud Monitoring Metrics explorer: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

  3. Navigate to **Select a metric** and select the metrics that you want to display. For example, select **VM Instance** > **Instance** > **CPU Usage** > **Apply**.

  4. To view metrics for the workstations that you are interested in, filter the VM instance by `workstation_cluster_id`, `workstation_location`, `workstation_id`, and `workstation_config_id`.




For a full metrics list, see [Metrics from Compute Engine](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).

For more about using Metrics explorer, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

**Note:** The monitoring agent monitors the VM—not the Docker containers hosted on the Container-Optimized OS VM. Customizing reported metrics for the built-in agent is not supported.

## What's next

  * Learn more about [Cloud Monitoring metrics dashboards](https://docs.cloud.google.com/monitoring/dashboards).
  * Learn more about [Container-Optimized OS Monitoring](https://docs.cloud.google.com/container-optimized-os/docs/how-to/monitoring#viewing_the_collected_metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
