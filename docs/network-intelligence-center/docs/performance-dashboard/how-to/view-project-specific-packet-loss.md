---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-packet-loss/
title: View project-specific packet loss dashboard \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:48.105274+00:00
---

# View project-specific packet loss dashboard  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-packet-loss/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  View project-specific packet loss dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Performance Dashboard packet loss metrics are automatically collected for your project.

You do not have to do any setup, but you do need a certain number of VMs in your project to get the details in the project performance dashboard. For more information, see [Metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview#metrics).

Events affecting Performance Dashboard packet loss metrics might take up to 10 minutes to appear.

The packet loss graph shows packet loss over time. The vertical axis shows the percentage of packet loss, and the horizontal axis shows when the losses occurred.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `monitoring.timeSeries.list`



**Roles**

  * Monitoring Viewer (`roles/monitoring.viewer`)
  * Monitoring Editor (`roles/monitoring.editor`)
  * Monitoring Admin (`roles/monitoring.admin`)



###  Console 

  1. In the Google Cloud console, go to the **Performance Dashboard** page. 

[Go to Performance Dashboard](https://console.cloud.google.com/net-intelligence/performance/dashboard)

  2. Click **Per Project**.
  3. In the **View options** panel, in the **Traffic type** section, select **Cross-zonal**.
  4. In the **Metric** section, select **Packet loss**.
  5. In the **Time period** section, choose the view interval from **1 hour** to **6 weeks**.
  6. In the **Google Cloud regions** section, select the regions for which you want to view data. You can select up to five regions.
  7. On the horizontal axis, click a time to show a heatmap of **average packet loss between zone pairs** at that time. Slide the time selector to show packet loss at different times.
  8. In the heatmap, click a particular square to see a bidirectional graph of packet loss between those two zones.



In Shared VPC service projects, individual service projects might not be able to access all the information. For example, suppose one service project has VMs in only one zone and another service project has VMs in a different zone only. If the two sets of VMs exchange traffic, each service project can access packet loss details for the traffic heading _toward_ their VMs.

Similarly, in peered Virtual Private Cloud (VPC) networks that sit in different projects, each project can access packet loss information only for the traffic heading toward their VMs.

To learn how you can view information from more than one project, see [Monitor network performance for multiple projects](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics#workspaces).

## What's next

  * [View Google Cloud packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-packet-loss)
  * [View project-specific latency dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-latency)
  * [View Google Cloud latency dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency)
  * [Performance Dashboard metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
