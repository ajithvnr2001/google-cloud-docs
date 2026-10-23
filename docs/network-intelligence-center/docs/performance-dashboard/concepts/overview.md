---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview/
title: Performance Dashboard overview \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:08.564423+00:00
---

# Performance Dashboard overview  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  Performance Dashboard overview Stay organized with collections  Save and categorize content based on your preferences. 

Performance Dashboard gives you visibility into the performance of the entire Google Cloud network, as well as to the performance of your project's resources.

With these performance-monitoring capabilities, you can distinguish between a problem in your application and a problem in the underlying Google Cloud network. You can also investigate historical network performance problems.

Performance Dashboard also exports data to Cloud Monitoring. You can use Monitoring to query the data and get access to additional information. For details, see [Performance Dashboard metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics).

## Project performance view

In the _project_ performance view, Performance Dashboard shows packet loss or latency metrics only for zones where you have project virtual machine (VM) instances. For example, VM-to-VM traffic and VM-to-internet traffic. You can select up to five regions where the workloads are deployed. The dashboard lets you see and understand the following:

  * Packet loss summary
  * Packet loss average between region pairs of the regions selected
  * Packet loss average between zone pairs of selected regions
  * Latency summary
  * Latency median between region pairs of the regions selected
  * Latency median between zone pairs of the regions selected



### Traffic between VM instances

Performance Dashboard shows packet loss and latency metrics (in summary charts and heatmap views) for zones where you have Compute Engine virtual machine (VM) instances. It provides current data and metrics for the past six weeks. For example, your project has a Virtual Private Cloud (VPC) network with VMs in zones A and B. In such a case, Performance Dashboard provides packet loss and latency metrics for your project between those two zones.

You can also view the aggregated latency metrics from a sample of your actual VM-to-VM traffic in a tabular view depending on the selected time period. The latency details table lists the VMs and their corresponding latency details.

### Traffic between Google Cloud and internet locations

Performance Dashboard shows latency metrics for regions where you have Compute Engine virtual machine (VM) instances and the internet locations of the end devices that communicate with the VMs. It provides the current latency metrics and six weeks worth of historical data. For example, your project has a Virtual Private Cloud network with VMs in region A that receive traffic from clients in cities X and Y. In such a case, Performance Dashboard provides latency metrics for your project between region A and cities X and Y.

To view project metrics, click **View project performance** at the top of the Performance Dashboard page. For more examples and details about what is measured, see [Metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/metrics-views#metrics).

## Google Cloud performance view

In the _Google Cloud_ performance view, Performance Dashboard shows zone-to-zone packet loss and latency metrics across all Google Cloud. For example, VM-to-VM traffic and Google Cloud to internet traffic. The dashboard shows the status of the Google Cloud network and lets you compare the performance across all of Google Cloud to the performance observed in your projects. You can select up to five Google Cloud regions to see and understand the following:

  * Packet loss summary. This view can show up to 50 zone pairs with VM-to-VM packet loss in all of Google Cloud.
  * Packet loss average between zone pairs.
  * Latency summary. This view can show up to 50 zone pairs with VM-to-VM round trip time (RTT) in all of Google Cloud.
  * Median latency between zone pairs.



### Traffic between VM instances

Performance Dashboard shows the packet loss and latency metrics across all of Google Cloud. These metrics can help you understand whether issues evident in the per-project dashboard are unique to your project.

The Google Cloud performance view shows time series data for up to 50 zone pairs for the selected time window, which by default is one hour.

You can view network performance for any Google Cloud zone pair, even if your project is not deployed in those zones. You can view the performance at both the region level and the zone level. A summary time series chart shows up to 50 zone pairs with the highest aggregated VM-to-VM packet loss or latency across all of Google Cloud.

### Traffic between Google Cloud and internet locations

Performance Dashboard shows latency metrics between VMs across all Google Cloud regions and internet endpoints. You can aggregate the traffic to city, geographic region, and country levels. You can view the latency metrics that correspond to specific region-geographic location pairs if there is sufficient Google Cloud traffic for that pair.

These metrics can help you assess whether issues apparent in the per-project dashboard are unique to your project. The global metrics can also help you plan future deployments.

To view the Google Cloud performance metrics, click **View performance for all of Google Cloud** at the top of the Performance Dashboard page. To view the Google Cloud performance metrics from the _project performance view_ , you can hold the pointer over the specific zone pairs. For more examples and details about what is measured, see [Metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/metrics-views#metrics).

**Note:** The information shown on the dashboards doesn't represent network performance targets. Increased packet loss or increased latency is not a _downtime_ according to the [Google Cloud SLA](https://cloud.google.com/compute/sla), especially for a single zone.

## Permissions

To access Performance Dashboard data, either through the Google Cloud console or through Monitoring, you must have the `monitoring.timeSeries.list` permission. This permission is included in the [Monitoring roles](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) listed in the following table.

Role name | Role ID  
---|---  
Monitoring Viewer | `roles/monitoring.viewer`  
Monitoring Editor | `roles/monitoring.editor`  
Monitoring Admin | `roles/monitoring.admin`  
  
For information about other roles that include the `monitoring.timeSeries.list` permission, see [Understanding roles](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Change project scope

To make use of an existing metrics scope and monitor multiple Google Cloud projects in a single view, select the scoping project by using the Google Cloud console project picker or the **Change Scope** button. You can also select a single monitoring project by using these options. For more information, see [Performance Dashboard metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics#project-scope).

## Recommended alerts

You can create alerts for high packet loss based on predefined conditions. The alerting policy for packet loss is triggered when the packet loss exceeds 5% for 5 minutes for any region pair.

Alerting gives timely awareness to problems in your cloud applications so that you can resolve the problems quickly. An alerting policy describes the circumstances under which you want to be alerted and how you want to be notified. For more information about creating and managing alerting policies, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

## What's next

  * [Project performance use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases)
  * [View project-specific packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-packet-loss)
  * [View Google Cloud packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-packet-loss)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)
  * [Learn more about packet sampling](https://sflow.org/packetSamplingBasics/index.htm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
