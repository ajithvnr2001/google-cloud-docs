---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/monitor/monitor-metrics/
title: Monitor VM metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:14.349023+00:00
---

# Monitor VM metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/monitor/monitor-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitor VM metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the Google Distributed Cloud (GDC) air-gapped VM dashboard and the type of information made available by the different graphs. To learn more about monitoring, visualization, and how to configure alerts, see the following supplemental pages:

  * [Observability monitoring and visualizing](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/observability-monitoring-and-visualizing) for detailed information about collecting metrics, viewing metrics, and managing your dashboards.
  * [Alerting](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/observability-alerting) for information about, for example, alerts and creating alert rules.



The VM-level metrics dashboard provides you with graphs for viewing VM-specific metrics for your projects. Access the dashboard from this address:

`https://GDC_HOST/PROJECT/grafana/d/vm-metrics/workload-vms`

  * Replace GDC_HOST with your hostname.
  * Replace PROJECT with the name of your project.

**Note:** GDC doesn't support guest environment metrics on Windows VMs.

This document is for developers in platform administrator or application operator groups that monitor VM metrics using dashboards in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

### Request IAM roles

To monitor VM metrics with dashboards, contact your IAM Project Admin to request the appropriate monitoring role. Review the list of [project-level predefined roles for monitoring resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-iam-permissions#mon-roles-project) for more information.

All roles must bind to the namespace of the project where the VM resides.

## VM dashboard

The VM dashboard presents graphs that contain information regarding the following for each VM in each of your project namespaces:

  * CPU
  * Memory
  * Network
  * Disk



These graph types are generated using the VM monitoring metrics. The metrics are named and described according to their type, labels, and meanings.

In the dashboard view, from the selection box at the beginning of the page, which is marked in the following image as "vm", choose the VM you want to observe. The image shows that vm1 was selected.

![Choose the VM to view.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/vm_dropdown_selection.png)  


## CPU

View the CPU utilization - the amount of time that each vCPU spends in different states. The graph displays information for each of the vCPUs specified by your machine type.

![View CPU utilization](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/vm_cpu_usage_graph.png)

## Memory

From the memory graph, view attributes like the total memory allocated to the VM, the amount of memory available, and the amount of memory your instances use.

![View memory allocation and usage](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/vm_memory_graph.png)

## Network

Use the **Network** page to view the following:

  * The number of packets received from and sent to the network.
  * The quantity of bytes received from and sent to the network.
  * The number of receive and transmit packets that have been dropped on virtual network interface card (vNIC) interfaces.
  * The network transmit error packet count.



![View network data](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/vm_network_graph.png)

## Disk

View the **Disk** page to see the following:

  * A bytes count for reads from or writes to a disk
  * A count of write or read IO operations.
  * The cumulative time taken for a read or write operation: 
    * The time the operation is in queue
    * The time spent actually executing the operation (disk busy)
  * Disk flush request numbers, and the time spent on cache flushing.



![View disk data](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/vm_disk_graph.png)

## Metrics list

To view a list of metrics definitions, see [Virtual Machine Management (VMM) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-vmm#metrics-list).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
