---
url: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-latency/
title: View project-specific latency dashboard \u00a0|\u00a0 Network Intelligence Center - Performance Dashboard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:42.268127+00:00
---

# View project-specific latency dashboard  |  Network Intelligence Center - Performance Dashboard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-latency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Performance Dashboard ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/using-performance-dashboard)



Send feedback 

#  View project-specific latency dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Performance Dashboard metrics are automatically collected for your project for the following traffic types:

  * Latency metrics for each possible Google Cloud zone pair
  * Latency metrics between regions where you have virtual machine (VM) instances and the internet locations that communicate with the VMs



You do not have to do any setup, but you do need a certain number of VMs in your project to get the details in the project performance dashboard. For more information, see [Metrics](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview#metrics).

Events affecting Performance Dashboard metrics might take up to 10 minutes to appear.

## View project-specific latency data for traffic between zones

The latency graph shows the median latency across all project zones over time. The vertical axis shows the median latency in milliseconds (ms), and the horizontal axis shows the change over time.

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
  3. In the **View options** panel, in the **Traffic type** section, select **Cross-zonal** to view latency data between VMs.

To view the latency data between VMs and internet endpoints, see View latency information for **Internet to Google Cloud** traffic type.

  4. In the **Metric** section, select **Latency (RTT)**.

  5. In the **Time period** section, choose the view interval from **1 hour** to **6 weeks**.

  6. In the **Google Cloud regions** section, select the regions for which you want to view data. You can select up to five regions.

  7. On the horizontal axis, click a time to show a heatmap of **median latency between zone pairs** at that time. Slide the time selector to show latency at different times.

  8. In the latency view between zones heatmap, click a particular square. In the **Latency details for your project** page that appears, you can view the bidirectional latency graph between those two zones and a table that shows the latency between the VMs and zones. The latency table lists the VMs, their projects, and the corresponding latency details.

  9. To narrow your results for the VMs and view their latency details, use a property to create an advanced filter query.

  10. To view the latency details of the VM on the monitoring page, click **View Monitoring**.




The latency heatmap only shows zone pairs with enough traffic to provide latency information.

In Shared VPC service projects, individual service projects don't have access to the latency metrics of the host project.

Similarly, in peered VPC networks that sit in different projects, the individual projects don't have access to the latency metrics for traffic moving between the networks.

For more details, see [Latency](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview#latency).

## View project-specific latency data for traffic between Google Cloud regions and internet endpoints

The project-specific latency views show the median round-trip time (RTT) between selected geographic areas and regions that contain VM instances in your project. The latency summary is available in three views: **Table** view, **Map** view, and **Timeline** view. Select the specific locations or regions to view the latency graph.

The latency graph shows the median latency between Google Cloud regions and internet endpoints. The vertical axis shows the median latency in milliseconds (ms), and the horizontal axis shows the change over time.

To view project-specific latency data between Google Cloud and the internet, complete the following steps.

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
  3. In the **View options** panel, in the **Traffic type** section, select **To the internet** to view latency data between VMs and internet endpoints.

  4. In the **Metric** section, select **Latency (RTT)**.

  5. In the **Time period** section, choose the view interval from **1 hour** to **6 weeks**.

  6. In the **Google Cloud regions** section, select the regions for which you want to view data. You can select up to five regions.

  7. In the **Network tier** section, select **Show data only for the selected tier**.

  8. In the **Network tier** menu, select **Standard** or **Premium**. For more information about tiers, see the [Network Service Tiers overview](https://docs.cloud.google.com/network-tiers/docs/overview).

  9. To view the latency summary, select one of these three views:

     * **Table** view
     * **Map** view
     * **Timeline** view
  10. In the **Table** view, do the following:

     1. To view the latency metrics from a country to the regions that contain VM instances in your project, click **View**. The country-specific details appear in a sidebar that shows the traffic from the selected country to the regions that contain VM instances in your project.
     2. To view the latency details on the graph, select the specific country to region path.
     3. To view the latency details for a specific time, point to the traffic path on the graph.
  11. In the **Map** view, do the following:

     1. To view the latency details of a specific location, point to the geographic location on the map.
     2. To view the median latency between a Google Cloud region and geographic locations, click the Google Cloud region. The map refreshes to display the locations with traffic with the selected region.
     3. To view the latency details over a time period, click a geographic location. The location-specific details appear in a sidebar that shows the traffic from the selected location to the regions that contain VM instances in your project.
     4. To view the latency details of a specific traffic path, select the traffic path from the list of available traffic paths.
  12. In the **Timeline** view, do the following:

     1. To select a specific country, in the **Filter** field, use the **Country** property.
     2. In the Latency table, click **View** to view the latency between the VMs in the selected locations and internet endpoints.
     3. Refine the graph further by using the properties in the **Filter** field.

The latency graph shows the latency details for the selected time interval along with aggregate latency values in the legend that follows the graph.




## What's next

  * [View project-specific packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-project-specific-packet-loss)
  * [View Google Cloud packet loss dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-packet-loss)
  * [View Google Cloud latency dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency)
  * [Performance Dashboard metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/viewing-perf-dash-metrics)
  * [Troubleshoot Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
