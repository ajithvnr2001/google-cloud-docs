---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics/
title: Performance Dashboard metrics reference \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:28.378029+00:00
---

# Performance Dashboard metrics reference  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  Performance Dashboard metrics reference Stay organized with collections  Save and categorize content based on your preferences. 

Performance Dashboard exports packet loss and latency metrics to Cloud Monitoring. You can create your own dashboard in Monitoring, and you can create dashboard charts and alerts that use Performance Dashboard metrics.

## Packet loss metrics

Performance Dashboard only exposes certain fields in its packet loss charts. Monitoring exposes all collected metric fields for the resource:

  * Resource type: `gce_zone_network_health`
  * Metric: `networking.googleapis.com/cloud_netslo/active_probing/probe_count`
  * Description: Number of probes

Filter | Description | remote_zone |   
---|---  
remote_region |   
remote_location_type | `cloud` (internal IP address), `external` (external IP address), or `network_peering`  
protocol |   
result | failure or success  



Packet loss is calculated as a ratio of failed probes over total probes:

`metric[failure]/(metric[failure]+metric[success])`

## Latency metrics between VMs

Latency metrics for a specific project are calculated as the round-trip time (RTT) for the following resource type and metric:

  * Resource type: `gce_instance`
  * Metric: `networking.googleapis.com/vm_flow/rtt`
  * Description: A distribution of RTT measured over TCP connections between the local virtual machine (VM) instance.



Latency metrics across all Google Cloud projects between zones are calculated as the round-trip time (RTT) for the following resource type and metric [(Preview)](https://cloud.google.com/products/#product-launch-stages):

  * Resource type: `networking.googleapis.com/Location`
  * Metric: `networking.googleapis.com/all_gcp/vm_traffic/zone_pair_median_rtt`
  * Description: The median RTT (round-trip time) for VM-to-VM traffic, for each zone pair and aggregated across all Google Cloud projects.

Ensure that the **Only show active resources and metrics** option is disabled when using the latency metric in [Dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) or [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) for each zone pair across all Google Cloud projects.

You cannot query latency for each zone pair across all Google Cloud projects using Monitoring Query Language (MQL).




## Latency metrics between VMs and internet endpoints

Latency metrics are calculated as round-trip time (RTT) for the following resource and metric:

  * Resource: `gce_instance`
  * Metric: `networking.googleapis.com/vm_flow/external_rtt`
  * Description: A distribution of RTT measured over TCP connections between the local virtual machine (VM) instance and internet endpoints.



## Create Monitoring custom dashboards

You can create custom Monitoring dashboards for Performance Dashboard metrics. For more information, see [Dashboards](https://docs.cloud.google.com/monitoring/dashboards).

## Create a chart with Metrics Explorer

You can create a chart with Metrics Explorer for the latency metric for your project. For more information, see [Metrics explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## Create a metric-based alerting policy

You can create a metric-based alerting policy on the latency metric for your project. For more information, see [Alerts](https://docs.cloud.google.com/monitoring/alerts).

## Monitor network performance for multiple projects

If you prefer to monitor multiple projects in a single view, you can use Cloud Monitoring or add projects to a metrics scope.

When you access Cloud Monitoring for your Google Cloud project, by default you have access to the metrics for your selected project. However, you can configure Cloud Monitoring to view metrics for up to 375 Google Cloud projects. For more details, see [Monitored project limits](https://docs.cloud.google.com/monitoring/quotas#workspace_limits).

For more information, see [Configuring your project for Cloud Monitoring](https://docs.cloud.google.com/monitoring/settings).

## Change project scope

To view multiple projects in Performance Dashboard, configure a metrics scope and add monitored projects to it.

When you add projects to a metrics scope, then this metrics scope lets you monitor the data for the scoping project and the monitored projects. From this metrics scope, you can access the combined metrics of the scoping project and the monitored projects. For more information, see [Viewing metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

To make use of an existing metrics scope and monitor multiple Google Cloud projects in a single view, select the scoping project by using the Google Cloud console project picker or the **Change Scope** button. You can also use these options to select a single monitoring project.

## What's next

  * [View project-specific packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-packet-loss)
  * [View Google Cloud packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-packet-loss)
  * [View project-specific latency dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-latency)
  * [View Google Cloud latency metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency)
  * [View Performance Dashboard metrics in the Google Cloud console](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
