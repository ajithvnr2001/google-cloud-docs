---
url: https://docs.cloud.google.com/vpc/docs/monitoring-packet-mirroring/
title: Monitor Packet Mirroring \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:16:01.315294+00:00
---

# Monitor Packet Mirroring  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/monitoring-packet-mirroring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor Packet Mirroring

Packet Mirroring exports monitoring data about mirrored traffic to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). You can use monitoring metrics to check whether traffic from a virtual machine (VM) instance is being mirrored as intended. For example, you can view the mirrored packet or byte count for a particular instance.

You can view the monitoring metrics of mirrored VM instances or instances that are part of the collector destination (internal passthrough Network Load Balancer). For mirrored VM instances, Packet Mirroring provides metrics specific to mirrored packets, such as `/mirroring/mirrored_packets_count`, `/mirroring/mirrored_bytes_count`, and `/mirroring/dropped_packets_count`. For more information, see the [metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) for Compute Engine in the Monitoring documentation. 

The metrics for the collector destination provides an aggregate view of all mirrored traffic that it collects. However, for the individual mirrored instances, you can view the number of mirrored packets that were dropped. Metrics for the collector destination don't include dropped packets. For more information about monitoring the collector destination, see [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring). 

## View packet mirroring metrics in the Compute Engine console

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the project that contains the mirrored instance.

  3. Click the name of the mirrored instance to view its details.

  4. Click the **Monitoring** tab.

  5. View the **Mirrored Network Bytes** and **Mirrored Network Packets** charts to see the mirrored bytes and mirrored packets. The Mirrored Network Packets chart shows the number of successful and dropped mirrored packets.




## View the monitoring dashboard for a mirrored instance

To view the automatically created monitoring dashboard for a mirrored instance, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **All Dashboards** pane, select the **Mirrored Instances** from the list.

  3. Click list **List** and then select the name of a mirrored instance.




When you access the dashboard, Cloud Monitoring shows time series charts, such as the number of packets mirrored.

## Define Monitoring alerts

You can define [alerts](https://docs.cloud.google.com/monitoring/alerts) over the packet mirroring metrics:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Click **Alerting**.

  3. Click **Create Policy**.

  4. Click **Add Condition** and select condition type.

  5. In the **Metric** tab, select a target.

     1. For the resource type, **VM Instance**.
     2. Select a [packet mirroring metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).
  6. Click **Save Condition**.

  7. Enter a policy name in the **Name this policy** field and click **Save Policy**.




## Define custom dashboards

In addition to the predefined dashboards in Cloud Monitoring, you can create custom dashboards, set up alert policies, and query the metrics through the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api).

On the Cloud Monitoring dashboard, **Open Incidents** are driven by the alerting policies that you configure. Alerts appear as _incidents_ on the dashboard when the alert is triggered. These are general functions of Cloud Monitoring.

You can create custom Cloud Monitoring dashboards over packet mirroring metrics:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Click **Dashboards**.

  3. Click **Create Dashboard**.

  4. Select a chart type to create.

  5. Give the chart a title.

  6. In the **Metric** tab, select a target.

     1. For the resource type, **VM Instance**.
     2. Select a [packet mirroring metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute).
  7. Click **Save**.




## Metric reporting frequency and retention

Metrics for the VPC security policies are exported to Cloud Monitoring in 1-minute granularity batches. Monitoring data is retained for six weeks. The dashboard provides data analysis in the following default intervals:

  * 1H (one hour)
  * 6H (six hours)
  * 1D (one day)
  * 1W (one week)
  * 6W (six weeks)



Using the controls in the upper-right hand corner of the Cloud Monitoring page, you can manually request analysis in any interval from 6W to 1 minute. For more information about Cloud Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

## What's next

For more information about Cloud Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
