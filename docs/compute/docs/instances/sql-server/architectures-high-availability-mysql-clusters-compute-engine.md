---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/architectures-high-availability-mysql-clusters-compute-engine/
title: Architectures for high availability of MySQL clusters on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:54:08.534694+00:00
---

# Architectures for high availability of MySQL clusters on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/architectures-high-availability-mysql-clusters-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Architectures for high availability of MySQL clusters on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-03-12 UTC

This document describes several architectures that provide [high availability (HA)](https://wikipedia.org/wiki/High_availability) for MySQL deployments on Google Cloud. HA is the measure of system resiliency in response to underlying infrastructure failure. In this document, HA addresses the availability of MySQL clusters within a single cloud [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

This document is intended for database administrators, cloud architects, and DevOps engineers, who want to learn how to increase MySQL data-tier reliability by improving overall system uptime. This document is intended for you if you are running MySQL on Compute Engine. If you use Cloud SQL for MySQL, this document is not intended for you.

For a system or application that requires a persistent state to handle requests or transactions, the data persistence layer must be available to successfully handle requests for data queries or mutations. If the application must interact with the data tier to service requests, any downtime in the data tier prevents the application from performing the necessary tasks.

Depending on the system service level objectives (SLOs) of your system, you might require an architectural topology that provides a higher level of availability. There is more than one way to achieve HA, but in general you provision redundant infrastructure that you can quickly make accessible to your application.

This document discusses the following topics:

  * Define terms to help you understand HA database concepts.
  * Help you understand several options for HA MySQL topologies.
  * Provide contextual information to help you understand what to consider in each option.



## Terminology

There are several terms and concepts that are industry-standard and useful to understand for purposes beyond the scope of this document.

**Replication.** The process by which write transactions (`INSERT`, `UPDATE`, or `DELETE`) are reliably captured, logged, and then serially applied to all database nodes in the topology.

**Synchronous replication.** A data replication method that ensures real-time data consistency by writing to both primary and replica databases simultaneously.

**Semi-synchronous replication.** A data replication method that ensures a limited degree of data consistency by writing to both primary and at least one other replica database simultaneously.

**Asynchronous replication.** A data replication method that allows a delay between the primary and replica updates, prioritizing performance over immediate consistency.

**Source node.** All database writes must be directed to a source node. The source node provides a read with the most up-to-date state of persisted data.

**Replica node.** An online copy of the source database node. Changes are near-synchronously replicated to replica nodes from the source node. You can read from replica nodes with the understanding that the data might be slightly delayed due to replication lag.

**Replication lag.** A time measurement that expresses the difference between when a transaction is applied to the replica compared to when it is applied to the source node.

**Uptime.** The percent of time that a resource is working and capable of delivering a response to a request.

**Failure detection.** The process of identifying that an infrastructure failure has occurred.

**Failover.** The process to promote the standby infrastructure (in this case, the replica node) to become the primary infrastructure (the source node).

**Recovery time objective (RTO).** The duration, in elapsed real time, that is acceptable, from a business perspective, for the data tier to be offline until the failover process completes.

**Recovery point objective (RPO).** The duration, in elapsed real time, that is acceptable, from a business perspective, for data to be lost until the failover process completes.

**Fallback.** The process to reinstate the former source node after a failover has occurred.

**Self-healing.** The capability of a system to resolve issues without external actions by a human operator.

**Network partition.** A condition when two nodes in a topology, for example the source and replica nodes, can't communicate with one another over the network.

**Split brain.** A condition that occurs when two nodes simultaneously believe that they are the source node.

**Node group.** A set of compute resource tasks that provide a service. For this document, that service is the data persistence tier.

**Witness or quorum node.** A separate compute resource that helps a node group determine what to do when a split-brain condition occurs.

**Source or leader election.** The process by which a group of peer-aware nodes, including witness nodes, determine which node should be the source node.

**Node group.** A set of compute resource tasks that provide a service. For this document, that service is the data persistence tier.

**Hot standby.** A node that represents a close copy of another source node and can become the new source node with minimal downtime.

## When to consider an HA architecture

HA architectures provide increased protection against data-tier downtime. Understanding your tolerance for downtime, and the respective tradeoffs of the various architectures, is paramount to choosing the option that is right for your business use case.

Use an HA topology when you want to provide increased data-tier uptime to meet the reliability requirements for your workloads and services. For environments where some amount of downtime is tolerated, an HA topology introduces unnecessary cost and complexity. For example, development or test environments infrequently need high database tier availability.

## Consider your requirements for HA

Cost is a notable consideration, because you should expect your compute infrastructure and storage costs to at least double, in order to provide HA. It's important that you thoroughly assess this cost against the potential financial impact of downtime. When you assess the possible MySQL HA options, consider the following questions:

  * What services or customers rely on your data tier?
  * What is your operational budget?
  * What is the cost to your business in the event of downtime in the data persistence tier?
  * How automated does the process need to be?
  * What level of availability do you hope to achieve, 99.5%, 99.9%, or 99.99%?
  * How quickly do you need to fail over? What is your RTO and RPO?



The following contribute to recovery time and should be considered when establishing your RTO and RPO:

  * Detection of the outage
  * Secondary virtual machine (VM) instance readiness
  * Replication type and backup frequency
  * Storage failover
  * Database recovery time
  * Application recovery time



## MySQL HA architectures

At the most basic level, HA in the data tier consists of the following:

  * A mechanism to identify that a failure of the source node has occurred.
  * A process to perform a failover where the replica node is promoted to be a source node.
  * A process to change the query routing so that application requests reach the new source node.
  * Optionally, a method to fall back to the original topology using source and replica nodes.



This document discusses the following three HA architectures:

  * Regional Persistent Disk
  * Hot standby and witness node
  * Orchestrator and ProxySQL



In addition to infrastructure failure, each of these architectures can help minimize downtime in the unlikely event of a zonal outage. You use these architectures with Domain Name System (DNS) changes to provide multi-region HA to guard against regional service interruption, but this document discusses zonal outages.

## HA with regional Persistent Disks

HA in the data tier always relies on some type of data replication. The simplest replication is one that you don't have to manage.

With the [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#repds) storage option from Compute Engine, you can provision a block storage device that provides synchronous data replication between two zones in a region. Regional Persistent Disks provide a strong foundational building block for implementing HA services in Compute Engine.

The following diagram illustrates the architecture of HA with regional Persistent Disks.

![Architecture for using regional Persistent Disks to achieve HA.](https://docs.cloud.google.com/static/architecture/images/architectures-high-availability-mysql-clusters-compute-engine-1-ha-pd.svg)

If your source node VM instance becomes unavailable due to infrastructure failure or zonal outage, you can [force the regional Persistent Disk to attach](https://docs.cloud.google.com/compute/docs/disks/repd-failover#force-attach) to a VM instance in your backup zone in the same region.

To perform this task, you must do one of the following:

  * Start another VM instance in the backup zone where access to the shared regional Persistent Disk is available.
  * Maintain a _hot standby_ VM instance in the backup zone. A hot standby VM instance is a running VM instance that is identical to the instance that you are using. After you attach the regional Persistent Disk, you can start the database engine.



If the data service outage is promptly identified, the force-attach operation typically completes in less than one minute, which means that an RTO measured in minutes is attainable, with zero RPO.

If your business can tolerate the additional downtime required for you to detect and communicate an outage, and for you to perform the failover manually, then there is no need to automate the process.

If your RTO tolerance is lower, you can automate the detection and failover process. If you automate this architecture, the system is further complicated because there are several edge cases in the failover and fallback process that you need to consider. For more information about a fully automated implementation of this architecture, see the [Cloud SQL high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability#normal).

### Advantages

There are several advantages of achieving HA by using regional Persistent Disks due to the following features:

  * This architecture provides simultaneous protection against several failure modes: source server zone infrastructure failure, single-zone block-storage degradation, or full-zone outage.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 
  * The application or database layer replication is not required because regional Persistent Disks provide continuous and synchronous block-level data replication, which is fully managed by Google Cloud. A regional Persistent Disk automatically detects errors and slowness, switches the replication mode, and performs catch up of data that is replicated to only one zone.

  * If there are storage problems in a primary zone, a regional Persistent Disk automatically performs reads from the secondary zone. This operation can result in increased read latency, but your application can continue to operate without any manual action.




### Considerations

The limitations of this architecture are related to the single region nature of this topology and some of the following inherent constraints of regional Persistent Disks:

  * The regional Persistent Disk can only be mounted to one database. Even if the standby database VM instance is running, that instance cannot be used to serve database reads. However, with Google Cloud Hyperdisk Balanced High Availability in multi-writer mode, multiple instances can read and write to the same disk. For more information about Hyperdisk, see [About Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The foundational technology behind this architecture allows only for replication between zones in the _same_ region. As a result, regional failover is not an option when solely using this architecture.
  * The regional Persistent Disk's [write throughput is halved](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) compared to zonal Persistent Disks. Make sure that throughput limits are within your required tolerance.
  * The regional Persistent Disk's write latency is slightly higher than zonal Persistent Disk. We recommend that you test your workload to verify that the write performance is acceptable for your requirements.
  * During a failure event and the resulting cutover, you need to force the regional Persistent Disk to attach to the standby zone VM. The force-attach operation typically executes in less than one minute, so you must consider this time when assessing your RTO.
  * The RTO estimate must account for the time required for the force attachment of the regional Persistent Disk and the VM file system detection of hot-attached disk.



## HA with hot standby and witness node

If you want an automated failover, a different architecture is required. One option is to deploy a group of at least two database nodes, configure database asynchronous replication, and launch witness nodes to help ensure that a quorum can be reached during a source node election.

The source database node processes write transactions and serve read queries. The database replication process transmits changes to the online hot standby replica node.

Because the witness node can be a small virtual machine, it provides a low-cost mechanism to ensure that a group majority is available for a source node election.

Group nodes continually assess the status of the other group nodes. The signals that these status checks consume every few seconds are called heartbeats because they are used to assess the health of the other group nodes. A timely assessment of database node health is important because an unhealthy source database node must be quickly identified so that a failover of the hot standby can be initiated.

The node group quorum is determined by the number of voting elements that must be part of active cluster membership for that cluster to start properly or continue running. For a node group to reach a quorum in a source database node election, a majority of the nodes in the group must participate. To guard against a split-brain condition, the majority requirement ensures that in the event of a network partition, two voting groups cannot concurrently have enough nodes to vote.

A group majority consists of (_n_ +1)/2 nodes, where _n_ is the total number of nodes in the group. For example, if there are three nodes in a group, at least two nodes must be operating for a source node election. If there are five nodes in a group, at least three nodes are required.

Groups are sized with an odd number of nodes in case there is a network partition that prevents communication between subgroups of the node group. If the group is even, there is a greater chance that both subgroups can possess less than the majority. If the group size is odd, it is more likely that either one of the subgroups can have a majority or neither group has a majority.

The following diagram compares a healthy node group with a degraded node group.

![Architecture comparing a healthy node group to a degraded node group.](https://docs.cloud.google.com/static/architecture/images/architectures-high-availability-mysql-clusters-compute-engine-2-degraded-node.svg)

The diagram shows two node groups—a functional node group and a degraded node group. The fully functional and healthy node group has three group members. In this state, the source and replica database nodes are providing their expected purpose. The necessary quorum for this node group is two nodes.

The degraded node group shows the state where the source node heartbeats are no longer sent due to an infrastructure failure. This state might be the result of source database node instance failure, or the source node might still be running. Alternatively, a network partition might prevent communication between the source node and the other nodes in the group.

Regardless of the cause, the result is that both the replica and the witness determine that the source node is no longer healthy. At this point, the group majority conducts a source node election, determines that the hot standby node should become the source node, and initiates a failover.

The following diagram shows the database transaction, replication, and heartbeat flow in the witness node architecture.

![Architecture of using hot standby and witness node to achieve HA.](https://docs.cloud.google.com/static/architecture/images/architectures-high-availability-mysql-clusters-compute-engine-3-witness-node.svg)

In the preceding diagram, this HA architecture relies on the hot-standby replica node to quickly start processing production writes upon a failover. The mechanics of the failover—for example, source node promotion—are carried out by the database nodes in the group.

To implement this architecture, consider the following two projects:

  * [MySQL Group Replication](https://dev.mysql.com/doc/refman/8.0/en/group-replication.html) is an open source plugin for MySQL that facilitates the creation of HA topologies.
  * [Galera Cluster](https://galeracluster.com/) and [Percona XtraDB Cluster](https://www.percona.com/software/mysql-database/percona-xtradb-cluster) are other open source options that can provide high availability.



### Advantages

The hot standby architecture has few moving parts, is straightforward to deploy, and provides several advantages:

  * With only one additional, low-cost witness node, fully automated failover is provided.
  * This architecture can effectively address long-term infrastructure failures and transient failures (for example, due to a system reboot).
  * With some associated replication latency, multi-region HA is provided.



### Considerations

The failover is automatic, however, the following operational tasks remain:

  * You manage the replication between the source and replica nodes.
  * You manage the witness nodes.
  * You must deploy and manage the connection routing using a load balancer.
  * Without changes to your application logic, which are out of scope for this document, you can't direct reads to the replica node.



## HA with Orchestrator and ProxySQL

If you combine the open source components, [Orchestrator](https://github.com/percona/orchestrator) and [ProxySQL](https://proxysql.com/), you have architecture that can detect outages and automatically failover traffic from an afflicted source node to a newly promoted healthy replica.

Furthermore, you can transparently route queries to the appropriate read or read and write nodes to improve steady-state data tier performance.

Orchestrator is an open source MySQL replication topology manager and failover solution. The software lets you detect, query, and refactor complex replication topologies, and provides reliable failure detection, intelligent recovery, and promotion.

ProxySQL is an open source, high performance, and highly available database protocol aware proxy for MySQL. ProxySQL scales to millions of connections across hundreds of thousands of backend servers.

The following diagram shows the combined Orchestrator and ProxySQL architecture.

![Architecture using Orchestrator and ProxySQL to achieve HA.](https://docs.cloud.google.com/static/architecture/images/architectures-high-availability-mysql-clusters-compute-engine-4-orchestrator.svg)

In this architecture, as illustrated by the preceding diagram, database-bound traffic is routed by an internal load balancer to redundant ProxySQL instances. These instances route traffic to a write- or read-capable database instance based on the ProxySQL configuration.

Orchestrator provides the following failure detection and recovery steps:

  1. Orchestrator determines that the source database node is not available.
  2. All replica nodes are queried to provide a second opinion about the status of the source node.
  3. If the replicas provide a consistent assessment that the source is not available, the failover proceeds.
  4. As defined by the topology, the promoted node becomes the new source node during the failover.
  5. When the failover is complete, Orchestrator helps ensure that the correct number of new replication nodes are provisioned according to the topology.



On-going replication between the source database in zone A and the database replicas in alternate zones keeps the replicas up-to-date with any writes routed to the source. Orchestrator checks the health of the source and replica databases by continually sending heartbeats. Orchestrator application state is persisted in a separate Cloud SQL database. If changes in the topology are required, Orchestrator can also send commands to the databases.

ProxySQL routes the traffic appropriately to the new source and replica nodes when the failover is complete. Services continue to address the data tier using the IP address of the load balancer. The virtual IP address is switched seamlessly from the earlier source node to the new source node.

### Advantages

The architectural components and automation provides the following advantages:

  * The software used in this architecture provides various observability features including replication topology graphs, and query traffic visibility.
  * ProxySQL and Orchestrator coordinate to provide automatic replica promotion and failover.
  * The replica promotion policy is fully configurable. Unlike other HA configurations, you can choose to promote a specific replica node to source in case of failover.
  * After a failover, new replicas are provisioned declaratively according to the topology.
  * ProxySQL provides a supplementary load-balancing benefit as it transparently routes read and write requests to the appropriate replica and source nodes based on the configured policies.



### Considerations

This architecture increases operational responsibility and incurs additional hosting cost due to the following considerations:

  * Both Orchestrator and ProxySQL must be deployed and maintained.
  * Orchestrator needs a separate database for maintaining state.
  * Both Orchestrator and ProxySQL need to be set up for HA, so there is additional configuration and deployment complexity.



Further, Orchestrator doesn't support multi-source replications, doesn't support all types of parallel replication, and can't be combined with clustering software such as Galera or Percona XtraDB. For more information about the current limitations, see the [Orchestrator FAQ](https://github.com/percona/orchestrator/blob/master/docs/faq.md).

## What's next

  * Read about the [Cloud SQL high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability#normal).
  * Learn more about [High availability options using regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk).
  * Review the [MySQL Group Replication](https://dev.mysql.com/doc/refman/8.0/en/group-replication.html) documentation.
  * Learn about [Galera Cluster](https://galeracluster.com/library/documentation/overview.html) or the related [Percona XtraDB Cluster](https://www.percona.com/doc/percona-xtradb-cluster/LATEST/intro.html).
  * Review the [Orchestrator](https://github.com/percona/orchestrator) documentation.
  * Learn more about [ProxySQL](https://proxysql.com/documentation/).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-12 UTC."],[],[]] 
