---
url: https://docs.cloud.google.com/managed-lustre/docs/performance/
title: Performance considerations \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:27.028514+00:00
---

# Performance considerations  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Performance considerations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on configuring your Google Cloud Managed Lustre environment to obtain the best performance.

To see performance numbers specific to each performance tier, see [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers).

## Performance after increasing capacity

Increasing the storage capacity of an existing instance increases its maximum throughput and IOPS, and possibly its metadata performance.

Read throughput performance gradually improves as new data is written and redistributed across the additional storage. Write throughput performance increases immediately.

**Note:** Metadata performance may not increase if the increase in capacity did not result in an additional 72 GBps of provisioned throughput.

## High capacity utilization

Once an instance's storage capacity utilization reaches 90%, the instance's performance may be reduced. Consider [increasing the capacity of your Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity). You may need to [request additional quota](https://docs.cloud.google.com/managed-lustre/docs/quotas#request_additional_quota) before expansion.

If you're seeing `No space left on device` errors but your instance shows remaining capacity, refer to [`No space left on device` errors](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity#enospc).

## VPC network maximum transmission unit (MTU)

When creating your VPC network, setting the value of `mtu` (_maximum transmission unit_ , or the size of the largest IP packet that can be transmitted on this network) to the maximum allowed value of 8896 improves performance up to 10% compared to the default value of 1460 bytes.

You can see the current MTU value of your network with the following command:
    
    
    gcloud compute networks describe NETWORK_NAME --format="value(mtu)"
    

The MTU value of a network can be updated after the network has been created, but there are important considerations. See [Change the MTU of a network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network#change-mtu) for details.

## Compute Engine machine types

Network throughput can be affected by your choice of machine type. In general, to obtain the best throughput:

  * Increase the number of vCPUs. Per-instance maximum egress bandwidth is generally 2 Gbps per vCPU, up to the machine type maximum.
  * Select a machine series that supports higher ingress and egress limits. For example, C2 instances with Tier_1 networking support up to 100 Gbps egress bandwidth. C3 instances with Tier_1 networking support up to 200 Gbps.
  * Enable [per VM Tier_1 networking performance](https://cloud.google.com/blog/products/compute/increasing-bandwidth-to-compute-engine-vms-with-tier_1-networking) with larger machine types.
  * Use [Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) (gVNIC). gVNIC is the only option for Generation 3 and newer machine types. gVNIC is required when using Tier_1 networking.



For detailed information, refer to [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

## Multi-NIC configuration

By using Lustre's built-in multi-rail capability, clients can stripe network traffic across multiple network interface cards (multi-NIC). This aggregates bandwidth to saturate high-capacity Managed Lustre instances.

To configure multi-NIC, you must:

  * Select a machine type with multiple physical NICs.
  * Create a subnet for each NIC and assign each NIC to its subnet.
  * Follow the multi-NIC steps when connecting from [Compute Engine](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine) or [GKE](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume).



### Verify traffic balancing

Once you've configured multi-NIC, verify that data is balancing correctly.

###  Compute Engine 

Verify data balancing directly on the VM by monitoring the configured network interfaces (for example, `eth0` and `eth1`) using `nload` while generating traffic to the Managed Lustre backend:
    
    
    nload -m eth0 eth1
    

In a successful multi-NIC configuration, the outgoing bitrates should be roughly equivalent across all configured interfaces.

###  GKE 

Confirm that network traffic from your workload is balanced across multiple NICs by deploying a temporary network-debugger Pod to the node where your workload is scheduled:

  1. Identify the node where your workload is scheduled:
         
         kubectl get pod POD_NAME -o wide
         

Replace POD_NAME with the name of your Pod. In the command output, note the name in the `NODE` column.

  2. Launch the network debugger on that node:
         
         kubectl run multi-nic-debug --rm -i --tty --image=nicolaka/netshoot \
           --overrides='{"spec": {"hostNetwork": true, "nodeSelector": {"kubernetes.io/hostname": "NODE_NAME"}, "tolerations": [{"key": "nvidia.com/gpu", "operator": "Exists", "effect": "NoSchedule"}]}}' \
           -- /bin/bash -c "apk update && apk add nload && nload -m eth0 eth1"
         

Replace NODE_NAME with the node name from the previous step.

  3. In the output, analyze the **Outgoing** column bitrates for `eth0` and `eth1`. If the configuration is successful, the bitrates are roughly equivalent. The output is similar to the following:
         
         Device eth0 [10.1.0.50] (1/2):
         ==========================================================================
         Incoming:                               Outgoing:
         Curr: 1.63 MBit/s                       Curr: 1.46 GBit/s
         Avg: 1.60 MBit/s                        Avg: 1.44 GBit/s
         Min: 1.40 MBit/s                        Min: 1.25 GBit/s
         Max: 1.64 MBit/s                        Max: 1.47 GBit/s
         Ttl: 590.94 GByte                       Ttl: 405.19 GByte
         
         Device eth1 [172.16.15.5] (2/2):
         ==========================================================================
         Incoming:                               Outgoing:
         Curr: 1.64 MBit/s                       Curr: 1.47 GBit/s
         Avg: 1.62 MBit/s                        Avg: 1.44 GBit/s
         Min: 1.42 MBit/s                        Min: 1.26 GBit/s
         Max: 1.66 MBit/s                        Max: 1.47 GBit/s
         Ttl: 587.68 GByte                       Ttl: 406.36 GByte
         

  4. Exit the debugger by pressing **Ctrl+C**.




## Troubleshooting common bottlenecks

If your workload performance is significantly lower than expected for your Managed Lustre performance tier, check for the following common issues:

  * **Insufficient client machine count:** A single client machine is bottlenecked by its own virtual CPU (vCPU) and single-link network processing limits. To saturate high-throughput tiers, you must distribute the load. For example, to saturate a 100,000 MBps Managed Lustre file system, you typically need at least 60 standard client machines (or 12 client machines configured to use Tier 1 high-bandwidth networking) writing in parallel. For the maximum instance size of any performance tier, you may need over 2,500 client machines configured to use Tier 1 high-bandwidth networking.

  * **Non-ideal Virtual Private Cloud (VPC) MTU:** By default, VPC networks use an MTU of `1460` (standard Ethernet frames). For high-performance storage like Managed Lustre, you must configure jumbo frames with an MTU of `8896`. Running with a standard `1460` MTU forces the CPU to process more than double the number of network packets, adding CPU overhead and capping maximum bandwidth.

  * **Missing Tier 1 Network Bandwidth configuration:** Many high-performance machine types require you to explicitly opt into Tier 1 network bandwidth.

    * On Compute Engine and GKE Standard node pools, use the `--network-performance-configs=total-egress-bandwidth-tier=TIER_1` flag during creation. Without this flag, a VM or node may be capped at a lower default egress limit.
    * On GKE Autopilot, you don't specify this flag directly. Instead, select a machine series that supports higher bandwidth (such as `c3`) using node selectors in your Pod specifications.

For more information, see Compute Engine machine types.

  * **Imbalanced Lustre Object Storage Target (OST) usage:** Managed Lustre splits file data across multiple Object Storage Targets (OSTs). If your test or workload writes to a single unstriped file, or if client tasks write patterns that overload a single OST, that OST becomes a bottleneck while the rest of the file system sits idle. To avoid this, ensure you balance the write payload evenly across all available OSTs (for example, by using file-per-process mode in benchmarks).

  * **Shared network bandwidth contention:** Egress bandwidth on client machines (Compute Engine VMs or GKE nodes) is shared across all network operations on the machine. If your client machines or pods are simultaneously downloading large packages, running heavy logging sweeps, or communicating heavily with other cluster nodes, your storage performance will be limited to the remaining network bandwidth.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
