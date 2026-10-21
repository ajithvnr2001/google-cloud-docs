---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cluster-overview/
title: Minimum cluster configurations \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:42:50.195315+00:00
---

# Minimum cluster configurations  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cluster-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Minimum cluster configurations Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cluster-overview.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cluster-overview.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cluster-overview.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cluster-overview.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cluster-overview.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cluster-overview.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cluster-overview.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-overview.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cluster-overview.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cluster-overview.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cluster-overview.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cluster-overview.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cluster-overview.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cluster-overview.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cluster-overview.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cluster-overview.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cluster-overview.html)



This topic describes minimum cluster configurations for Apigee hybrid. These minimum configurations apply to all of the supported [Kubernetes platforms](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms). The recommendations in this topic apply for non-production installations, such as trial or testing scenarios. Keep these recommendations in mind when performing the Apigee hybrid installation steps. 

##  About node pools 

A node pool is a group of nodes within a cluster that all have the same configuration. By default, hybrid assigns all pods to the default node pool; however, you can create dedicated node pools and assign hybrid components to them as a way of distributing resources. 

Typically, you define dedicated node pools when you have pods with differing resource requirements. For example, the `apigee-cassandra` pods require persistent storage, while the other Apigee hybrid pods do not. For this reason, we recommend that you create a stateful node pool for Cassandra and a stateless node pool for the rest of the hybrid runtime services. See [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configure-dedicated-nodes) for details. 

The following section lists configurations for both stateful and stateless node pools. 

##  Minimum configurations 

Use these minimum configurations when setting up your cluster: 

Configuration | Stateful node pool | Stateless node pool  
---|---|---  
Purpose | A stateful node pool used for the Cassandra database. | A stateless node pool used by the runtime message processor.  
Label name | apigee-data | apigee-runtime  
Number of nodes | 1 per zone (3 per region) | 1 per zone (3 per region)  
CPU | 8 (Prod)  
4 (Non-prod) | 8 (Prod)  
4 (Non-prod)  
RAM | 32 (Prod)  
16 (Non-prod) | 32 (Prod)  
16 (Non-prod)  
Storage | dynamic | Managed with the [ApigeeDeployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/apigee-deployment-services) CRD  
Minimum disk IOPS | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS. | 2000 IOPS with SAN or directly attached storage. NFS is not recommended even if it can support the required IOPS.  
Network bandwidth for each machine instance type | 1 Gbps | 1 Gbps  
**Note:** For **production** environments, we recommend a minimum of two clusters.

##  Cassandra network requirements 

This section discusses network requirements and recommendations to follow when setting up Apigee hybrid.

### Network bandwidth

Cassandra uses the [Gossip protocol](https://en.wikipedia.org/wiki/Gossip_protocol) to exchange information with other nodes about network topology. The use of Gossip plus the distributed nature of Cassandra—which involves talking to multiple nodes for read and write operations—results in a lot of data transfer through the network. 

Cassandra requires a minimum of 1 Gbps of network bandwidth for each machine instance. For example, on GKE, the minimum recommended machine type, `e2-standard-4`, has a minimum bandwidth of 1 Gbps. For production installations, a higher Gbps is recommended.

The maximum or 99th percentile latency for Cassandra should be below 100 milliseconds.

### Secure network connectivity between regions

When installing hybrid in [multiple regions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/multi-region), ensure that the connections between regions is secure:

  * Use a virtual private network solution, such as Google [Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs/overview) (VPC), to secure connectivity between regions.
  * Open a firewall to ensure that Cassandra nodes can connect between regions in non-overlapping subnets and can resolve those network IPs.
  * Always use port 7001 for Cassandra. All other ports are local to the region. See also [Secure ports usage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/ports).



##  Cassandra NTP requirements 

Cassandra data synchronizes based on the timestamp of the system. Ensure that the time is synchronized across all pods and all regions within the Cassandra cluster. Time delays between the nodes and regions causes data inconsistencies. 

##  Scaling the configuration 

If you need to scale your initial configuration based on additional capacity or throughput needs, see the following topics: 

  * [Configuring Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-production)
  * [Scaling Cassandra pods](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-scaling)
  * [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configure-dedicated-nodes)
  * [Scale and autoscale runtime services](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/scale-and-autoscale)
  * [Multi-region deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/multi-region)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
