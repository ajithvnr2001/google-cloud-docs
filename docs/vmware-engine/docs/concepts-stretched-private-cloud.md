---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud/
title: VMware Engine stretched private clouds \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:23.707921+00:00
---

# VMware Engine stretched private clouds  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine stretched private clouds

A Google Cloud VMware Engine stretched private cloud is a private cloud that is stretched across two data zones and a witness zone, all within the same Google Cloud region. Stretched private clouds use vSphere and vSAN stretched clusters to provide compute and storage high availability against zone-level failures. All clusters of a stretched private cloud are considered VMware Engine stretched clusters, including the primary cluster.

**Note:** Once a stretched private cloud is created, it cannot be converted back to a standard private cloud. Additionally, you cannot convert an existing private cloud to a stretched private cloud.

## Stretched private cloud operation

All of the clusters of a stretched private cloud are stretched across the same two data zones and share the same witness zone. Each stretched cluster has its own set of data nodes in each data zone, and each stretched cluster has a witness node in the witness zone. Stretched qualifies as any two zones in a given Google Cloud region that are more than 10 Km geodesic distance apart but have less than 5 msec RTT latency between them.

The witness node is managed by VMware Engine and runs on a Compute Engine instance running ESXi in nested mode. You don't need to specify a witness zone and don't have to manage the lifecycle of the witness node.

Each of the three zones used by a stretched cluster are independent failure domains. The main benefit of this setup is that a cluster stretched across the three zones can survive a complete failure of any single zone.

## Stretched private cloud node configuration

Stretched clusters have an equal number of nodes in data zones. For example, three nodes in each data site - denoted as 3+3, or four nodes in each data site, denoted as 4+4. Configurations such as 4+3, therefore, are not allowed in Google Cloud VMware Engine stretched private clouds. A stretched cluster in Google Cloud VMware Engine must have a minimum of six data nodes (3+3) and a maximum of 32 (16+16) data nodes.

## Stretched private cloud environment

You manage your stretched private clouds through the Google Cloud console. All stretched clusters in a stretched private cloud have half of their capacity in each zone - for example, an eight-node stretched cluster in a stretched private cloud must have four nodes in each zone. Only an identical number of nodes from each zone can be added and removed from the stretched clusters. For example, you can add two nodes to each zone or remove three nodes from each zone in a stretched cluster.

A stretched private cloud can have multiple stretched clusters, but each must have exactly two Google Cloud zones for data nodes and one zone for the witness node.

## vSAN data encryption in stretched private clouds

vSAN data encryption at rest is enabled by default in all stretched clusters of a stretched private cloud. By default, a Google key provider is used for vSAN encryption. This key provider uses Cloud Key Management Service and is deployed in a highly available configuration across two zones. You can also use any external 3P Cloud KMS server (deployed as an HA pair across the two zones) and manage it yourself.

## Storage policies in stretched private clouds

The management VMs of a stretched private cloud run on the first stretched cluster (for example, 'cluster 0'). The management VMs are affixed to the primary site of the stretched cluster using affinity rules and are configured with the following storage policy:

  * Site Disaster tolerance=1 (protect against one site failure)
  * FTT=1 (for a six-node stretched ('cluster 0'))
  * FTT=2 (for a node stretched greater than or equal to 10 ('cluster 0'))



The default storage policy in a stretched cluster for workload VMs also follows the previous policy.

You can create new storage policies for workload VMs, and each stretched cluster in a stretched private cloud can use different storage policies.

## What's next

  * Learn about [VLANs and subnets](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
