---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/address-allocation/
title: Distributed Cloud connected Pod and Service network address allocation \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:59.085967+00:00
---

# Distributed Cloud connected Pod and Service network address allocation  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/address-allocation/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Distributed Cloud connected Pod and Service network address allocation Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for allocating network addresses to Kubernetes Pods and Services running on your Google Distributed Cloud connected installation.

Distributed Cloud Pod and Distributed Cloud Service address blocks must not overlap with the [reserved CIDR blocks](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges) for the corresponding region. For example, you must not assign the `10.128.0.0/20` CIDR block in the `us-central1` region.

When creating a Distributed Cloud connected cluster, you can specify an IPv4 CIDR block for your Distributed Cloud Pods and Distributed Cloud Services. For IPv4, use the RFC 1918 address range.

Each Distributed Cloud connected cluster accepts a single contiguous Distributed Cloud Pod CIDR block and a single contiguous Distributed Cloud Service CIDR block. The Distributed Cloud Service CIDR block covers only ClusterIP Services running within the target Distributed Cloud connected cluster. For external-facing Distributed Cloud Services, see [Load balancing](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networking#load-balancing).

You must ensure the following:

  * The Distributed Cloud Pod CIDR block and the Distributed Cloud Service CIDR block must not conflict with each other or with any other CIDR blocks on your local network.
  * The Distributed Cloud connected node CIDR block must not conflict with the Distributed Cloud connected management CIDR blocks.
  * Distributed Cloud load balancer virtual IP pools must not conflict across Distributed Cloud connected clusters.
  * If you are connecting to a Virtual Private Cloud (VPC) network by using Cloud VPN, the Pod and Service CIDR blocks must not conflict with any CIDR blocks on your VPC network.
  * To prevent indeterministic behavior, the CIDR blocks for Distributed Cloud connected clusters, your private network, and VPC subnetworks used for Distributed Cloud connectivity must not overlap.



Distributed Cloud connected automatically allocates portions of the specified Distributed Cloud Pod CIDR block as fixed-size Pod sub-CIDR blocks for each node in the zone based on the node's configured maximum Pod count. By default, Distributed Cloud sets the maximum Pod count per node to 128, which results in the allocation of a `/24` CIDR block per node. You can change this count by using the `default-max-pods-per-node` flag. Distributed Cloud connected automatically scales the Pod CIDR size based on the value that you specify.

The following table lists the Pods-per-node counts and their corresponding CIDR sizes:

Maximum Pods per node | IPv4 Pod CIDR block size  
---|---  
32 | `/26`  
33-64 | `/25`  
65-128 | `/24`  
129-256 | `/23`  
  
After you create the Distributed Cloud connected cluster, you cannot modify the CIDR block and Pods-per-node values described in this section. You must delete and re-create the cluster with the new values.

### Address allocation for multi-rack deployments

For multi-rack deployments of Distributed Cloud connected where a base rack aggregates the resources of one or more standalone racks into a single zone, you must allocate a /25 CIDR block. This ensures address availability up to the maximum supported number of nodes.

## What's next

  * [Configure Network Function operator resources](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/network-function)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
