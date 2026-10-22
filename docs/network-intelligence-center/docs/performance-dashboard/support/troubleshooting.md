---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting/
title: Troubleshoot Performance Dashboard \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:43.194652+00:00
---

# Troubleshoot Performance Dashboard  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  Troubleshoot Performance Dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Use the following guidance to troubleshoot common issues with Performance Dashboard.

## Short spikes in packet loss that last a few minutes

Certain short spikes lasting for a few minutes are expected or possible. Check for sustained loss that lasts for greater than five minutes. If you see such loss, or if the loss impacts your network or application performance, see [Getting support](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/getting-support).

## Spikes in latency

Latency is measured over Layer 4 traffic and is impacted by the TCP/IP stack running on the remote VM. Some applications with unique TCP/IP stack implementations (such as VPN applications) might artificially increase latency in Performance Dashboard. If latency spikes despite the absence of custom applications that might impact the TCP/IP stack, see [Getting support](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/getting-support).

## No data in the project Performance Dashboard

If you can't see packet loss information, make sure that you have virtual machine (VM) instances in the Virtual Private Cloud (VPC) or Shared VPC network that you are viewing. Performance Dashboard uses active probes to measure packet loss between zones. The number of active probes is related to the number of VMs in the network. If the network that you are viewing has no VMs, there are no active probes and no packet loss measurement.

If you can't see latency information, make sure that you have VM instances generating enough traffic.

## Packet loss by zone heatmap has empty cells (marked as `N/A`)

This is possible if a project is part of a Shared VPC. In such a case, the matrix might include data for source zones where the project itself doesn't have VMs, but other projects in the same Shared VPC do have VMs. Packet loss between two projects that use Shared VPC is measured toward the destination service project.

## Packet loss seen in Performance Dashboard but not in application

Packet loss is based on active probing, which covers the entire mesh of VMs that can communicate with each other. Your traffic pattern might only use a subset of this mesh. It might be that your application is not utilizing the problematic network path.

Another possibility is that not enough measurements are available to give high confidence results. This might happen if there are very few VMs in a zone or if the number of VMs fluctuates.

Performance Dashboard also includes preemptible VMs in the packet loss calculation. Projects with a high percentage of such VMs might show a higher packet loss rate when VMs are getting preempted. Check if the higher packet loss rate corresponds to the time window when preemptible VMs are being shut down.

## Constant value seen for latency between two zones or between a region and an Internet location

Latency data is stored as a distribution. This means that if all measurements consistently fall in the same bucket in the distribution (which is more likely to happen with higher latency values), the resulting graph displays a constant value that is the mean of the bucket interval.

For example, if there is a bucket for every 10 ms (0 ms-10 ms, 10 ms-20 ms, 20 ms-30 ms, and so on), and there are three different latency measurements of 251 ms, 256 ms, and 253 ms, all of them are in the 250 ms-260 ms bucket. The latency is displayed as 255 ms, which is the mean of the 250 ms-260 ms bucket interval. If a new measurement of 259 ms is recorded, the latency still displays as 255 ms.

## Troubleshooting Google Cloud performance metrics

### Google Cloud performance appears more stable than project performance

Because the Google Cloud performance metrics are aggregated across all Google Cloud projects, they show fewer variations. This indicates that the typical performance in a zone pair or a region, Internet location pair remains stable even though the performance of individual projects might show greater variation due to randomness, natural variation, and measurement noise.

### Can choose Google Cloud zones in the Google Cloud performance view but not in project view

For your project-specific view, you can only choose zones where the project is deployed. The Google Cloud performance view enables you to view performance from any Google Cloud zone to any other Google Cloud zone.

For Internet to Google Cloud traffic type, you can only choose regions where there is traffic between VMs and Internet endpoints.

### No project data in a zone pair but the Google Cloud performance data exists

Google Cloud performance metrics are estimated by aggregating across all Google Cloud projects and are always available.

## No project data in a (Google Cloud region, internet endpoint) pair but the Google Cloud performance data exists

Google Cloud performance metrics are estimated by aggregating across a wide range of Google Cloud to internet connections. The per project view shows only data for connections which were seen in your project with sufficient traffic.

## What's next

  * [Get support](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/getting-support)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
