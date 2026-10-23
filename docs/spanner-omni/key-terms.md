---
url: https://docs.cloud.google.com/spanner-omni/key-terms/
title: Spanner Omni key terms \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:46.944621+00:00
---

# Spanner Omni key terms  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Spanner Omni key terms Stay organized with collections  Save and categorize content based on your preferences. 

This document defines the core concepts and deployment topologies for Spanner Omni. It covers the hierarchical relationship between regions, zones, and servers, and explains how these components relate to data replication and storage within a deployment.

## Spanner Omni concepts

The following sections provide detailed definitions of the terminologies used throughout the Spanner Omni documentation. Familiarizing yourself with these concepts ensures a clear understanding of the system's architecture and operational behavior.

### Deployment

A deployment of Spanner Omni, which lets you use the databases in your data centers or your public cloud accounts. You create the deployment according to the parameters specified in deployment configuration. A Spanner Omni deployment is equivalent to a [Spanner instance](https://docs.cloud.google.com/spanner/docs/instances) in Google Cloud.

### Deployment configuration

Provides the placement and specification of regions, zones, and servers for your Spanner Omni deployment. You can choose a single server, single region, or multi-region deployment configuration. For more information, see [Deployment configurations](https://docs.cloud.google.com/spanner-omni/deployment-configuration).

### Location

The equivalent of region in Google Cloud terms. The network latency between two regions is non-trivial. For on-premises deployments, you can define your own regions. For cloud deployments, the region must align with the regions in the respective cloud provider. One region can have multiple zones.

### Process

The Spanner server forks and manages multiple processes. For example, TimeServer, spanserver are all processes in Spanner. Individual processes may have monitoring statistics like CPU and memory usage. A process can open ports to communicate with other servers in the deployment.

### Replica

Spanner replicates data to provide data availability and geographic locality. At a high level, Spanner organizes all data into rows. Spanner creates multiple copies, or replicas of these rows, then stores these replicas in different geographic areas. Spanner uses a synchronous, Paxos-based replication scheme, in which voting replicas vote on every write request before it commits the write to the database. Like in Spanner, there are three replica types in Spanner Omni: _read-write_ , _read-only_ , and _witness_. For more information, see [replica types](https://docs.cloud.google.com/spanner/docs/replication#replica-types) in Spanner documentation.

### Server

A server is a compute resource, such as a VM or container, where the Spanner Omni server runs. Each server has its own system resources: CPU, memory, and storage. The server provides Spanner Omni's capabilities by storing and serving user data.

#### Root servers

Root servers store critical metadata to support the zone. For example, the root server stores server membership and other zone configuration information.

The number of root servers per zone must be an odd number between one and nine, inclusive, to ensure quorum for consistency. If the number of servers is an even number, deployments might fail. When configuring your zones, designate servers as root servers. We recommend that you use one for development or testing and three for highly available production zones. 

Consider the number of root servers carefully while planning the deployment. While you can change the number of root servers in the deployment after you create it, we don't recommend doing so.

#### Non-root servers

Non-root servers store and serve user data and provide a way to scale the compute capacity and storage of a zone. You can add as many non-root servers to your deployment as the workload demands. You can change the number of non-root servers after you create the deployment.

### Split

A Spanner split holds a range of contiguous rows of data, where Spanner orders the rows by primary key. Spanner creates replicas of each split that it stores in each zone.

### Storage

The permanent storage attached to the server.

### Zone

A group of one or more servers. For data replication, you should create one zone per replica. For on-premises deployments, we recommend minimizing infrastructure sharing (VMs, disks) between zones. For cloud deployments, align zones to the availability zones in AWS, or zones in Google Cloud.

### Worker

A dedicated, stateless compute node designed to offload background and resource-intensive operations, such as building vector indexes on large tables. Workers are available in the Commercial edition of Spanner Omni and are billed at the same compute rate as servers in the deployment. The Developer edition doesn't support workers. Unlike servers, workers don't host user data, serve user traffic, participate in leader elections, or belong to a specific zone; instead, they register with a location. For more information, see [Deploy and manage workers](https://docs.cloud.google.com/spanner-omni/manage-workers).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
