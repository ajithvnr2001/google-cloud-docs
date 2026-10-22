---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-workload-optimization/
title: Planning for performance use cases \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:55.894679+00:00
---

# Planning for performance use cases  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-workload-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  Planning for performance use cases Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud performance view provides an average performance view for selected region or zone pairs. You can use the Google Cloud performance view in the Network Intelligence Center in the Google Cloud console to plan the performance management of your applications. The Google Cloud performance view helps you to identify the best regions and zones to deploy new resources or to optimize your existing workloads. For example, you are currently running in specific zones and regions, but you know they are accessed by users or other workloads from other regions.

### Scenario: Understand performance in new zones and regions

You want to add workloads to a region, and you want to know which zone best serves your requirements.

You use the source and destination region selection menu to select source-destination pairs where you want to see the global average metrics for latency or packet loss.

To view the zones within a region pair, you select the region pair from the heatmap. In this example, you clicked the heatmap square for the region pair `asia-east1` and `asia-south1` and adjusted the time selector to 30 days.

[ ![Packet loss region pair heatmap.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/gcpd-pl-sum-hm-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/gcpd-pl-sum-hm-blue.png) Packet loss region pair heatmap (click to enlarge)

### Scenario: View historical data for regions or zone pairs

Use the time series chart capability to display historical data for selected zone pairs. In this example, you can see the heatmap square for the zone pair `asia-east1-a` and `asia-northeast3-a` and the time selector adjusted to 30 days.

[ ![Zone pairs historical data.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/gpd-pl-dets-zonepairs.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/gpd-pl-dets-zonepairs.png) Zone pairs historical data (click to enlarge)

## What's next

  * [Project performance use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-project)
  * [Planning for performance across geographies use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-performance-across-geographies)
  * [View project-specific packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-packet-loss)
  * [View Google Cloud packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-packet-loss)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
