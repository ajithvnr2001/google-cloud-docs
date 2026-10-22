---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards/
title: View dashboards \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:20.059407+00:00
---

# View dashboards  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  View dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Dashboards provide high-level insights into your network that you can use to further troubleshoot it. You can view metrics from network paths and web paths. 

## Network paths dashboard

The default network paths dashboard is automatically filtered to the paths you selected before you clicked **Open Dashboard**.

For paths where the target is not another Monitoring Point (single-ended), the dashboard includes the following key metrics:

  * Average Loss
  * Average RTT for NetworkPath (MEAN)
  * Maximum RTT for NetworkPath (MAX)
  * Data Loss (Single-ended)
  * Total Jitter for NetworkPath (Single-ended) (SUM)
  * Test Error for NetworkPath (SUM)
  * Data packets received and sent (Single-ended)



For paths where the target is another Monitoring Point (dual-ended), the dashboard includes the following key metrics:

  * Average Loss (Inbound)
  * Average Loss (Outbound)
  * Average RTT for NetworkPath (MEAN)
  * Maximum RTT for NetworkPath (MAX)
  * Data Loss (Inbound)
  * Data Loss (Outbound)
  * Test Errors
  * Outbound Jitter for NetworkPath (Dual-ended)
  * Inbound Jitter for NetworkPath (Dual-ended)
  * Total Voice Mean Opinion Score (MOS) (Dual-ended)
  * Outbound voice packets received and sent (Dual-ended)
  * Inbound voice packets received and sent (Dual-ended)
  * Inbound data packets received and sent (Dual-ended)
  * Outbound data packets received and sent (Dual-ended)



## Web paths dashboard

The default web paths dashboard is automatically filtered to the paths you selected before you click **Open Dashboard**. It includes the following key metrics:

  * Mean Total HTTP response time
  * Mean Total transaction time
  * Failed Browser test status for Web Path
  * Failed HTTP test status for Web Path (SUM)
  * Mean HTTP download size for Web Path
  * Maximum HTTP download size for Web Path
  * HTTP download size for Web Path
  * HTTP download speed for Web Path (MEAN)
  * DNS Lookup HTTP response time for Web Path (MEAN)
  * Request Receive HTTP response time for Web Path (MEAN)
  * SSL Connect HTTP response time for Web Path (MEAN)
  * TCP Connect HTTP response time for Web Path (MEAN)



## Access the Cloud Network Insights dashboards

Cloud Network Insights provides predefined dashboards prepopulated with common troubleshooting metrics for your selected network or web paths.

  1. Open the Google Cloud console and go to **Network Intelligence** > **Cloud Network Insights**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. Open either the **Network Paths** tab or the **Web Paths** tab.

  3. Select one or more paths, and then click **Open Dashboard**.




## Update dashboards

To modify the dashboard, or to perform more in-depth analysis, you can also create [custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) using the Metrics Explorer in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

Cloud Network Insights metrics are listed with the `*networkmanagement.googleapis.com/insights/*` prefix.

  * Network Metrics: `networkmanagement.googleapis.com/insights/network/`
  * Web Metrics: `networkmanagement.googleapis.com/insights/web/`



See [Monitoring metrics](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/monitoring-metrics) for a full list and descriptions.

### Monitoring scale limits

Cloud Monitoring has a soft scale limit of 10,000 total MonitoredResources per project. For Cloud Network Insights, this total includes all Monitoring Points, network paths, and web paths combined.

Exceeding this limit can result in significant performance degradation within Cloud Monitoring, including slow query results, dashboard failures, or unreliable alerting. Operating beyond this threshold is not recommended, as monitoring tools may not function as expected.

## View additional analytics in AppNeta

Use AppNeta when you need information like hop-by-hop analysis to identify which router in a path is dropping packets or waterfall charts for seeing which specific component of a web page is slow to load.

You can view additional details in AppNeta by doing one of the following:

  * Click the **Actions** menu on any Path or Monitoring Point in the Cloud Network Insights UI and select **Open in AppNeta**.
  * In Cloud Logging, every alarm entry includes a `provider_link` in the `jsonPayload`. Clicking this link takes you directly to the diagnostic view for that specific incident in AppNeta.



For more information about the information you can view in AppNeta, see [Analyze Network Monitoring Results](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/analyze-results/network-performance-monitoring-delivery.html) in the AppNeta documentation. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
