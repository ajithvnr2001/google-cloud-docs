---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance/
title: Troubleshooting compute instance performance issues \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:46.854989+00:00
---

# Troubleshooting compute instance performance issues  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting compute instance performance issues Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to diagnose and mitigate CPU, memory, and storage performance issues on Compute Engine virtual machine (VM) and bare metal instances.

## Before you begin

  * [Install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index) to view full instance performance metrics, such as memory and disk space utilization



## View performance metrics

To view performance metrics for your compute instances, use the Cloud Monitoring observability metrics available in the Google Cloud console.

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. You can view metrics for individual instances or for the five instances that are consuming the largest amount of a resource.

To view metrics for individual instances, do the following:

     1. Click the name of the instance that you want to view performance metrics for. The instance **Details** page opens.

     2. Click the **Observability** tab to open the Observability **Overview** page.

To view metrics for the five instances consuming the largest amount of a resource, click the **Observability** tab on the **VM instances** page.

  3. Explore the instance's performance metrics. View the **Overview** , **CPU** , **Memory** , **Network** and **Disk** sections to see detailed metrics about each topic. The following are key metrics that indicate instance performance:

     * On the **Overview** page:

       * **CPU Utilization.** The percent of CPU used by the instance.

       * **Memory Utilization.** The percent of memory used by the instance, excluding disk caches. For instances that use a Linux OS, this also excludes kernel memory.

       * **Network Traffic.** The average rate of bytes sent and received in one minute intervals.

       * **New Connections with VMs/External/Google.** The estimated number of distinct TCP/UDP flows in one minute, grouped by peer type.

       * **Disk Throughput.** The average rate of bytes written to and read from disks.

       * **Disk IOPS.** The average rate of I/O read and write operations to disks.

     * On the **Network Summary** page:

       * **Sent to VMs/External/Google.** The rate of network traffic rate sent to Google services, instances, and external destinations, based on a sample of packets. The metric is scaled so that the sum matches the total sent network traffic.

       * **Received from VMs/External/Google.** The rate of network traffic received from Google services, instances, and external sources, based on a sample of packets. The metric is scaled so that the sum matches the total received network traffic.

       * **Network Packet Totals.** The total rate of sent and received packets in one minute intervals.

       * **Packet Mean Size.** The mean size of packets, in bytes, sent and received in one minute intervals.

       * **Firewall Incoming Packets Denied.** The rate of incoming network packets sent to the instance, but not received by the instance, because they were denied by firewall rules.

     * On the **Disks Performance** page:

       * **I/O Size Avg.** The average size of I/O read and write operations to disks. Small (4 to 16 KiB) random I/Os are usually limited by IOPS and sequential or large (256 KiB to 1 MiB) I/Os are limited by throughput.

       * **Queue Length Avg.** The number of queued and running disk I/O operations, also called queue depth, for the top 5 devices. To reach the performance limits of your disks, [use a high I/O queue depth](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#io-queue-depth). Persistent Disk and Google Cloud Hyperdisk are networked storage and generally have higher latency compared to physical disks or Local SSD disks.

       * **I/O Latency Avg.** The average latency of I/O read and write operations aggregated across operations of all disks attached to the instance, measured by the Ops Agent. This value includes operating system and file system processing latency, and is dependent on queue length and I/O size.




## Understand performance metrics

Instance performance is affected by the hardware that the instance runs on, the workload running on the instance, and the instance's machine type. If the hardware cannot support the workload or network traffic of your instance, your instance's performance might be affected.

### CPU and memory performance

#### Hardware details

CPU and memory performance is affected by the following hardware constraints:

  * Each virtual CPU (vCPU) is implemented as a single hardware multi thread on a CPU processor.
  * [Intel Xeon CPU processors](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_cpu_processors) support multiple app threads on a single processor core.
  * VMs that use [C2 machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_machine_types) have fixed virtual-to-physical core mapping and expose [NUMA](https://www.kernel.org/doc/html/v4.18/vm/numa.html) cell architecture to the guest OS.
  * Most VMs get the all-core turbo frequency listed on [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms), even if only the base frequency is advertised to the guest environment
  * Shared-core machine types use context-switching to share a physical core between vCPUs for multitasking. They also offer bursting capabilities during which the CPU utilization for a VM can go over 100%. For more information, see [Shared-core machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#sharedcore).



To understand an instance's CPU and memory performance, view performance metrics for **CPU Utilization** and **Memory Utilization**. You can additionally use [process metrics](https://docs.cloud.google.com/monitoring/agent/process-metrics) to view running processes, attribute anomalies in resource consumption to a specific process, or identify your instance's most expensive resource consumers.

Consistently high CPU or memory utilization indicate the need to scale up the size of a VM. If the VM consistently uses greater than 90% of its CPU or memory, [change the VM's machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type) to a machine type with more vCPUs or memory.

Unusually high or unusually low CPU utilization might indicate your VM is experiencing a CPU soft lockup. For more information, see [Troubleshooting vCPU soft lockups](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-cpu-soft-lockup).

### Network performance

#### Hardware details

Network performance is affected by the following hardware constraints:

  * Each machine type has a specific egress bandwidth cap. To find the maximum egress bandwidth for your instance's machine type, visit the page that corresponds to your [instance's machine family](https://docs.cloud.google.com/compute/docs/machine-resource). 
  * Adding additional network interfaces or adding additional IP addresses per network interface to a VM doesn't increase the VM's ingress or egress [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth), but you can configure some machine types for higher bandwidth. For more information, see [Configuring a VM with higher bandwidth](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).



To understand an instance's network performance, view performance metrics for **Network Packet Totals** , **Packet Mean Size** , **New Connections with VMs/External/Google** , **Sent to VMs/External/Google** , **Received From VMs/External/Google** , and **Firewall Incoming Packets Denied**.

Review whether **Network Packet Totals** , **Packet Mean Size** , and **New Connections with VMs/External/Google** are typical for your workload. For example, a web server might experience many connections and small packets, while a database might experience few connections and large packets.

Consistently high outgoing network traffic might indicate the need to [change the VM's machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type) to a machine type that has a higher egress bandwidth limit.

If you notice high numbers of incoming packets denied by firewalls, visit the **Network Intelligence Firewall Insights** page in the Google Cloud console to learn more about the origins of denied packets.

[Go to the Firewall Insights page](https://console.cloud.google.com/net-intelligence/firewalls)

If you think your own traffic is being incorrectly denied by firewalls, you can [create and run connectivity tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

If your instance sends and receives a high amount of traffic from instances in different zones or regions, consider modifying your workload to keep more data within a zone or region to increase latency and decrease costs. For more information, see [VM-VM data transfer pricing within Google Cloud](https://docs.cloud.google.com/vpc/network-pricing#egress-within-gcp). If your instance sends a large amount of traffic to other instances within the same zone, consider a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) to achieve low network latency.

#### Bare metal instances

Similar to on-premise hardware, Compute Engine bare metal instances have all [CPU sleep states](https://builders.intel.com/docs/networkbuilders/power-management-dynamic-receive-side-to-increase-sleep-state-residency-solution-brief-1708941763.pdf) enabled by default. This can cause idle cores to enter a sleep state and can result in reduced network performance of bare metal instances. These sleep states can be disabled in the operating system if you need full network bandwidth performance.

  * To disable the sleep states on a [bare metal instance](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances) without needing to restart the instance, use the following script:
        
        for cpu in {0..191}; do
        echo "1" | sudo tee /sys/devices/system/cpu/cpu$cpu/cpuidle/state3/disable
        echo "1" | sudo tee /sys/devices/system/cpu/cpu$cpu/cpuidle/state2/disable
        done
        

  * Alternatively, you can update the GRUB configuration file to persist the changes across instance restarts.
        
        # add intel_idle.max_cstate=1 processor.max_cstate=1 to GRUB_CMDLINE_LINUX
        sudo vim /etc/default/grub
        sudo grub2-mkconfig -o /boot/grub2/grub.cfg
        sudo reboot

  * After the reboot, verify that the C6 and C1E sleep states are disabled:
        
        ls /sys/devices/system/cpu/cpu0/cpuidle/
        state0  state1
        
        cat /sys/devices/system/cpu/cpu0/cpuidle/state*/name
        POLL
        C1




The Input-output Memory Management Unit (IOMMU) is a CPU feature that provides address virtualization for PCI devices. IOMMU can negatively impact networking performance if there are a lot of `I/O translation lookaside buffer` (IOTLB) misses.

  * You are more likely to have misses when small pages are used.
  * For best performance, it is recommended to use large pages (2 MB to 1 GB in size).



### Storage performance

#### Hardware details

Storage is affected by the following hardware constraints:

  * The total size of all persistent disks combined with the number of vCPUs determine total storage performance. If there are different types of persistent disks attached to a VM, the SSD persistent disk performance limit is shared by all disks on the VM. For more information,see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison).
  * When Persistent Disk and Hyperdisk compete with outbound data transfer traffic, 60% of the maximum outbound network bandwidth is used for Persistent Disk and Hyperdisk, and the remaining 40% can be used for outbound network data transfer. For more information, see [Other factors that affect performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors).
  * I/O size and queue depth performance are dependent on workloads. Some workloads might not be large enough to use full I/O size and queue depth performance limits.
  * A VM's machine type affects its storage performance. For more information, see [Machine type and vCPU count](https://docs.cloud.google.com/compute/docs/disks/performance#machine-type-disk-limits).



To understand a VM's storage performance, view performance metrics for **Throughput** , **Operations (IOPS)** , **I/O Size** , **I/O Latency** , and **Queue Length**.

Disk throughput and IOPS indicate whether the VM workload is operating as expected. If throughput or IOPS is lower than the expected maximum listed in the [disk type chart](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison), then I/O size, queue length, or I/O latency performance issues might be present.

You can expect I/O size to be between 4-16 KiB for workloads that require high IOPS and low latency, and 256 KiB-1 MiB for workloads that involve sequential or large write sizes. I/O size outside of these ranges indicate disk performance issues.

Queue length, also known as queue depth, is a factor of throughput and IOPS. When a disk performs well, its queue length should be about the same as the queue length recommended to achieve a particular throughput or IOPS level, listed in the [Recommended I/O queue depth](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#io-queue-depth) chart.

I/O latency is dependent on queue length and I/O size. If the queue length or I/O size for a disk is high, the latency will also be high.

If any storage performance metrics indicate disk performance issues, do one or more of the following:

  * Review [Optimizing Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance) or [Optimize Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk) and implement the best practices suggested to improve performance.
  * If you're using Persistent Disk and your [instance's machine series supports Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support), consider [replacing your Persistent Disk volume with a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).

Otherwise, consider [adding a new Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) to your instance to increase the disk performance limits. Persistent Disk performance is based on the total amount of storage attached to an instance. This option is the least disruptive as it does not require you to unmount the file system, restart, or shutdown the instance.

  * If you're using Hyperdisk, you can [modify the Hyperdisk volume's provisioned performance](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks) to increase the per-disk IOPS and throughput limits.

For Persistent Disk, you must [increase the size of the disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) to increase the per-disk IOPS and throughput limits. Disks don't have any reserved, unusable capacity, so you can use the full disk without performance degradation.

  * [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#disk_type) to a disk type that offers higher performance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
