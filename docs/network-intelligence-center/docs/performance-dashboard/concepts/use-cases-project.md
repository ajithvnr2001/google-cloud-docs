---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-project/
title: Project performance use cases \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:55.365271+00:00
---

# Project performance use cases  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  Project performance use cases Stay organized with collections  Save and categorize content based on your preferences. 

The following sections describe various ways that Performance Dashboard can help you. This page describes project performance use cases. For Google Cloud performance, see [Google Cloud performance use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-google-cloud).

## Current performance diagnostics: Is it the network or the application?

Performance Dashboard gives you live visibility into the network performance underlying your project. It helps you to determine whether application issues are the result of software or network problems. If you see significant packet loss or high latency, it is possible that a Google Cloud network problem is at least part of the issue. If packet loss and latency look normal, it is likely a problem with the application.

### Scenario: Investigate an issue happening right now

You open Performance Dashboard and see a big spike in the **Packet loss summary** chart within the last hour. Because this chart summarizes packet loss across all zones, you don't yet know where the packet loss took place.

#### Select the regions and zones

  * To view data for specific regions, you select the regions from the **Locations** menu. You can select up to five regions.

  * To view zone-to-zone data for a region pair, you click the square in the regional heatmap that corresponds to the region pair.


[ ![Current packet loss.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-now-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-now-blue.png) Current packet loss (click to enlarge)

#### View the data for the selected time

To investigate further, you click the time that the spike took place. Doing so opens a heatmap specific to the selected time.

You can adjust your selection by dragging your cursor on the time axis of the summary chart.

[ ![Click a time to see details for that time.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-now-click-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-now-click-blue.png) Click a time to see details for that time (click to enlarge)

The heatmap that is displayed shows you data for the time that you selected. The heatmap squares are color-coded. As summarized in the legend to the left of the heatmap, each color reflects a different percentage of packet loss.

[ ![Packet loss heatmap for a specific time.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-heatmap-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-heatmap-blue.png) Packet loss heatmap for a specific time (click to enlarge)

Packet loss is measured in one direction only. A square showing packet loss indicates packet loss _from_ the zone indicated in the source axis _to_ the zone indicated in the destination axis.

To see a chart specifically for a zone pair, you click the blue square for source zone `us-central1-c`. The details chart keeps your time selection from the previous page.

[ ![Packet loss for a selected timeframe.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-details-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-details-blue.png) Packet loss for a selected timeframe (click to enlarge)

You see two lines on the chart, one for each direction of data flow. In this example, the purple line shows packet loss for traffic from source zone `us-central1-c`.

#### View further details

The chart shows that this spike in packet loss is an outlier. You can change the time window of data displayed for this zone pair by clicking the time selector on the top right. You can view up to six weeks of data. In this example, you click **7 days** to see the packet loss trend for the selected zone pair.

[ ![Packet loss for a 7-day timeframe.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-details-7-days-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-pl-details-7-days-blue.png) Packet loss for a 7-day timeframe (click to enlarge)

## Historical performance diagnostics

Performance Dashboard lets you view the network performance within your project over a specific period of time in the past. You can view up to six weeks worth of historical data.

### Scenario: Investigate an issue that happened in the recent past

You are investigating an issue with latency that happened earlier this week.

#### Identify the zone with latency issues

You can use the historical performance data in the Performance Dashboard to examine the zone in question.

To change the view, you click the **Latency** tab.

[ ![Latency tab.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-latency-tab-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-latency-tab-blue.png) Latency tab (click to enlarge)

#### View the latency data for the selected time

To adjust the time window of the **Latency summary** chart, you use the time selector on the top right. In this example, it is set to **1 hour**. To see the heatmap for latency at a certain time, you click that time on the chart's time axis.

[ ![Select a time.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-chart-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-chart-blue.png) Select a time (click to enlarge)

Because there are consistently higher values on the left of the chart, you click the time axis to see the heatmap for latency at that time.

[ ![Latency heatmap.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-chart-heatmap-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-chart-heatmap-blue.png) Latency heatmap (click to enlarge)

The dark blue squares in the heatmap show that the latency was 102 milliseconds (ms) between zones `us-central-1c` and `europe-west1-b`. To investigate further, you click a dark blue square. The latency details chart that opens keeps your time selection from the previous page showing the blue pin.

[ ![Latency spike.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-time-selection-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-time-selection-blue.png) Latency spike (click to enlarge)

The blue line shows a spike in latency for traffic traveling from `us-central-1c` to `europe-west1-b`.

To zoom in on the spike, you drag your mouse.

You can now see that the spike lasted for two to three minutes, reaching a peak at 7:18 PM.

[ ![Latency spike details.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-spike-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-spike-blue.png) Latency spike details (click to enlarge)

#### View further details

You can also see the details for the VMs, their projects, and the aggregate hourly latency in the Latency between VMs and zones table. Thus, you can identify exactly which VMs are contributing to the spike and reconsider your existing configuration or deploy new resources to address this issue.

[ ![Latency between VMs and zones.](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-table-blue.png)](https://docs.cloud.google.com/static/network-intelligence-center/docs/performance-dashboard/images/pd-lat-table-blue.png) Latency between VMs and zones table (click to enlarge)

## What's next

  * [Google Cloud performance use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-google-cloud)
  * [Planning for performance across geographies use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-performance-across-geographies)
  * [Planning for performance use cases](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/use-cases-workload-optimization)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
