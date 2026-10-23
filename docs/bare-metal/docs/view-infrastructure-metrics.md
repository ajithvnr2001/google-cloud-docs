---
url: https://docs.cloud.google.com/bare-metal/docs/view-infrastructure-metrics/
title: View Bare Metal Solution metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:33.112411+00:00
---

# View Bare Metal Solution metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/view-infrastructure-metrics/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View Bare Metal Solution metrics

This page describes how to access and view Bare Metal Solution metrics.

Bare Metal Solution collects metrics at regular intervals and makes them available for analysis. You can use these metrics to analyze the performance of your Bare Metal Solution infrastructure and troubleshoot issues.

Google Cloud console provides a predefined dashboard using which you can monitor your Bare Metal Solution servers and volumes.

**Note:** Bare Metal Solution metrics data is available at a low granularity and might include gaps. Metrics are sampled every 5 minutes. After sampling, the data is not visible for up to 30 minutes. Also, for this reason, we don't recommend creating alerts for the metrics.

## Before you begin

Optional: [Set up Ops Agent](https://docs.cloud.google.com/bare-metal/docs/set-up-ops-agent-for-bms) to gather more detailed data from your Bare Metal Solution servers.

## View server metrics

Bare Metal Solution collects server metrics at the network switch level.

All servers have the following basic metrics available:

  * Network traffic totals
  * Network traffic logical interface



The following additional insights are available upon installing the Ops Agent:

  * CPU utilization
  * Memory utilization
  * Disk space utilization
  * Disk throughput



To view metrics for your server, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Servers**](https://console.cloud.google.com/compute/bareMetalSolution/servers) page.
  2. Click the name of the server.
  3. Click the **Observability** tab.
  4. From the **Chart** menu, select the chart for the metric that you want to view.

The following charts are available:

Metric | Description  
---|---  
**Network traffic totals** | The rate of network data sent and received by the server.  
**Network traffic logical interface** | The rate of network data sent and received by each logical interface of the server.  
  
If you've set up Ops Agent on your server, the following charts are also available:

Metric | Description  
---|---  
**CPU utilization** | CPU Usage is the time-weighted average number of CPUs that were utilized on the machine over a given minute.  
**Memory utilization** | Percent of memory used by this server, excluding disk caches. For Linux VMs, this also excludes kernel memory and so is usage by user space only.  
**Disk utilization** | Disk space used in percent per the OS disk device.  
**Disk throughput** | The average rate of bytes written to and read from the OS disk devices. This doesn't include network storage.  
  5. Select the interval from the interval picker to display data for the chosen timeframe.

By default, the data is displayed for the last 6 hours. You can choose intervals ranging from 1 hour to 30 days.

You can also set a custom interval by following these steps:

     1. In the interval picker, click **Custom**.
     2. Set the **Start date and time** and the **End date and time**.
     3. Click **Apply**.



## View storage volume and LUN metrics

The metrics for a storage volume and its LUNs are collected only when the storage volume is attached to a server.

To view metrics for your storage volume or LUNs, follow these steps:

  1. In the Google Cloud console, go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.
  2. Click the name of the volume.
  3. Click the **Observability** tab.
  4. To view metrics for the LUNs of the storage volume, click the **Show LUN details** toggle.

The following charts are available:

Metric | Description  
---|---  
**LUN throughput** | The average rate of bytes written to and read from the LUN.  
**LUN IOPs** | The average rate of I/O read and write operations to the LUN.  
**LUN latency** | From the **Chart** menu, select the chart that you want to view:
     * **LUN total latency:** The average latency of I/O operations to the LUN.
     * **LUN latency:** The average latency of I/O read and write operations to the LUN.  
**LUN size** | LUN space used and available.  
  
If you don't toggle **Show LUN details** , the **Observability** tab displays the storage volume metrics.

The following charts are available:

Metric | Description  
---|---  
**Volume throughput** | The average rate of bytes written to and read from the storage volume.  
**Volume IOPs** | The average rate of I/O read and write operations to the storage volume.  
**Volume latency** | From the **Chart** menu, select the chart that you want to view:
     * **Volume total latency:** The average latency of I/O operations to the storage volume.
     * **Volume latency:** The average latency of I/O read and write operations to the storage volume.  
**Volume size** | The storage volume space that includes both used and available space.  
  5. Select the interval from the interval picker to display data for the chosen timeframe.

By default, the data is displayed for the last 6 hours. You can choose intervals ranging from 1 hour to 30 days.

You can also set a custom interval by following these steps:

     1. In the interval picker, click **Custom**.
     2. Set the **Start date and time** and the **End date and time** fields.
     3. Click **Apply**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
