---
url: https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-resiliency/
title: Use Protective ReRoute to optimize TCP network resiliency \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:00:19.129354+00:00
---

# Use Protective ReRoute to optimize TCP network resiliency  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-resiliency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use Protective ReRoute to optimize TCP network resiliency Stay organized with collections  Save and categorize content based on your preferences. 

[Protective ReRoute (PRR)](https://dl.acm.org/doi/10.1145/3603269.3604867) is a host-based technique to route packets around faults in a multipath network. PRR is deployed across Google's global network, where it works with existing resiliency mechanisms to improve network availability for all users.

## Choose a PRR mode

Google Cloud provides PRR in two modes: Hypervisor mode and Guest mode.

**Note:** PRR in Hypervisor mode is available for both VM instances and bare metal instances. 

PRR in hypervisor mode
    

PRR in hypervisor mode protects most traffic by default, but has the following limitations:

  * If an instance has a huge traffic fan-out, for example, if an instance is actively sending packets to thousands of cross-region instances at the same time, not all packets are protected.

  * Hypervisor mode PRR protects key segments of the network path but isn't fully end-to-end.

  * Hypervisor mode PRR reacts within single-digit seconds.



PRR in guest mode
    

Guest mode PRR can be used for critical applications that are particularly sensitive to short-duration network events, have large fanout patterns, are highly sensitive to packet loss, or require the fastest possible network recovery time (at RTT timescale).

All Google Cloud customers automatically get hypervisor mode PRR with no configuration actions required.

## Configure guest mode PRR

You should use guest mode for applications that are highly sensitive to packet loss, require large fan-out patterns, or need the fastest possible network recovery.

To configure guest mode PRR, performing the following steps.

  1. Verify the version of the Linux kernel. Use the following command to confirm that the instance OS is using version 4.20 or later:
         
         uname -r
         

  2. Verify that IPv6 flow labels are automatically generated. Use the following command to check that the [`/proc/sys/net/ipv6/auto_flowlabels`](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt) setting is enabled. This `sysctl` setting is often enabled by default.
         
         cat /proc/sys/net/ipv6/auto_flowlabels
         

If the value is not `1`, then enable it in your system configuration.

  3. Use the [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) network interface driver for full PRR support. To protect both IPv4 and IPv6 traffic, your instance must use a gVNIC network interface. If the instance uses the VirtIO network interface, then PRR protects only IPv6 traffic.




## What's next

  * Learn about [global networking products](https://cloud.google.com/products/networking/) for Google Cloud.
  * Read more about [network service tiers](https://cloud.google.com/blog/products/gcp/introducing-network-service-tiers-your-cloud-network-your-way) for Google Cloud.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
