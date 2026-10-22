---
url: https://docs.cloud.google.com/compute/docs/hpc/cluster-capabilities/
title: Enhanced HPC cluster management with H4D instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:01.022340+00:00
---

# Enhanced HPC cluster management with H4D instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/cluster-capabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enhanced HPC cluster management with H4D instances Stay organized with collections  Save and categorize content based on your preferences. 

Enhanced HPC cluster management capabilities enable you to run large-scale, densely deployed HPC clusters and provides the following cluster management capabilities:

  * HPC cluster resources colocation
  * Cluster topology-aware placement
  * Cluster operational mode
  * Cluster maintenance scheduling and controls
  * Cluster monitoring and diagnostic tooling



## HPC infrastructure resources colocation

When you use the H4D instances with enhanced management capabilities, you can request Compute Engine to provision your instances as close together a possible. These machines offer the following features:

  * Compute Engine provisions the machines as [blocks of resources](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#block).

  * Improved workload scalability through Cloud RDMA-enabled 200 Gbps networking.




This resource arrangement minimizes network hops and optimizes for lowest network latency. To learn more about how to obtain capacity to deploy densely allocated blocks of machines, see [Create an HPC cluster with enhanced management capabilities](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity).

## Cluster topology-aware placement

After you create VMs or clusters of H4D VMs, you can get topology information at the node and cluster levels. This information helps you do the following:

  * Adjust your application or workload design to further minimize network latency.

  * Understand and troubleshoot network latency and performance issues for VMs that communicate frequently with each other. These issues can occur if the VMs are unexpectedly located far apart.




For more information, see [View topology of a compute instance](https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology).

## Managed maintenance and recovery of your H4D VMs

When you reserve capacity to create H4D VMs or clusters, Google Cloud automatically manages the maintenance and recovery process of your VMs after [host errors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror) or faulty host reports. This approach, referred to as the _managed mode_ , is ideal when your workload requires high stability, and needs an automated process to minimize downtimes.

The managed mode has the following features:

  * **Only use reserved capacity for recovery** : Compute Engine only uses your reserved capacity to restart VMs. If there's no available capacity in your reservations, then Compute Engine only restarts VMs after you obtain more capacity.

  * **Automated VM restarts** : Google Cloud handles the entire recovery process for a VM. When host maintenance is required, Compute Engine automatically migrates your VMs on other available machines within your reservation and restarts the VMs.

  * **Block management and visibility** : you can view the topology, health, and maintenance status of individual reservations and reservation blocks. You can also receive maintenance notifications, and optionally start maintenance before the scheduled maintenance time, for these resources.

  * **Potential API rate limits** : calls to the report faulty host API may be rate-limited per reservation.




## Cluster maintenance scheduling and controls

You control maintenance of H4D instances by using topology-aware scheduling in a block of resources. This capability helps synchronize upgrades so that your workloads are more resilient to host events and minimizes disruptions.

To facilitate full control of maintenance events, you can use the following features:

  * Maintenance scheduling type

  * Manage host events




### Maintenance scheduling type

When you reserve capacity to create VMs or clusters of H4D VM instances, you can define how Compute Engine maintains the infrastructure that your VMs run on. You can specify whether to group VMs and have synchronized maintenance scheduling (_grouped_), or the VMs can be loosely coupled and have independent maintenance scheduling (_independent_).

**Grouped maintenance scheduling**

The grouped maintenance scheduling type helps ensure that, no matter when Compute Engine provisions a VM, all VMs running the same workload have the same planned maintenance frequency. This tightly-coupled maintenance lets you optimize your job's performance by giving you complete control over your used and unused capacity.

A group maintenance scheduling type is useful in the following cases:

  * Your environment uses a job scheduler, such as Slurm or Google Kubernetes Engine.
  * You want to run highly parallelized-computing workloads.



**Independent maintenance scheduling**

Independent maintenance scheduling type gives VMs different maintenance schedules. This configuration is ideal if you have workloads that run more efficiently when the VMs have separate maintenance schedules.

### Manage host events

After you create H4D VMs and start your workload, you can set up alerts and receive notifications when maintenance for your VMs or reserved blocks is scheduled, starts, or is completed. You can also view and, if needed, manually start maintenance on a VM or reserved block before its scheduled time. These options help you proactively control and minimize downtimes to your workloads.

For more information, see the following:

  * [Manage host events across H4D VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-vms-h4d)

  * [Manage host events across reservations](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d)




## Cluster monitoring and diagnostic tooling

For monitoring and troubleshooting, H4D instances include a [Faulty host reporting](https://docs.cloud.google.com/compute/docs/hpc/report-faulty-host-h4d) service, which you can use to flag issues with individual host machines.

## What's next?

  * Create an HPC cluster with enhanced cluster management capabilities by using one of the following methods:

    * [Create a SLURM cluster with H4D instances](https://docs.cloud.google.com/compute/docs/hpc/create-slurm-cluster-h4d)
    * [Bulk create HPC VMs](https://docs.cloud.google.com/compute/docs/hpc/bulk-create-hpc-vms)
    * [Create a HPC MIG with H4D machine series](https://docs.cloud.google.com/compute/docs/hpc/create-mig-hpc-dense)
  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)

  * [View H4D cluster topology](https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology)

  * [Manage host events across VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-vms-h4d)

  * [Manage host events across reservations](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d)

  * [Observe and monitor VMs](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms) in your Slurm cluster

  * [Report faulty host](https://docs.cloud.google.com/compute/docs/hpc/report-faulty-host-h4d)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
