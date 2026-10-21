---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/high-availability/overview/
title: High availability and data resilience \u00a0|\u00a0 AlloyDB Omni for containers: 17.5.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:45.985794+00:00
---

# High availability and data resilience  |  AlloyDB Omni for containers: 17.5.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/high-availability/overview/

This page documents AlloyDB Omni version **17.5.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)



Send feedback 

#  High availability and data resilience Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.5.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/high-availability/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/high-availability/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/high-availability/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/high-availability/overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/high-availability/overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/high-availability/overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/high-availability/overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/high-availability/overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/high-availability/overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/high-availability/overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/high-availability/overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/high-availability/overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/high-availability/overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/high-availability/overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/high-availability/overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/high-availability/overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/high-availability/overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/high-availability/overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/high-availability/overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/high-availability/overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/high-availability/overview)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page describes high availability and the tools we recommend using.

## About data resilience

You can think of data resilience in terms of availability, time to restore service, and data loss. Availability is usually measured in terms of uptime and expressed as the percentage of time the database is available. For example, to achieve 99.99% availability, your database can't be down for more than 52.6 minutes per year, or 4.38 minutes per month. The time to restore service after an outage is called Recovery Time Objective, or RTO. The amount of acceptable data loss due to an outage is called Recovery Point Objective, or RPO, and is expressed as the amount of time for which transactions are lost. For example, an RPO of 10 minutes means that in the event of a failure, you could lose up to 10 minutes worth of data.

It's common to set an availability target, or Service Level Objective (SLO), together with targets for RTO and RPO. For example, for a given workload, you might set the SLO to 99.99%, and also require a RPO of 0, no data loss on any failure, and a RTO of 30 seconds. For another workload, you might set the SLO to 99.9%, the RPO to 5 minutes, and the RTO to 10 minutes.

You can implement basic database resilience with database backups. AlloyDB Omni supports backups using [pgBackRest](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/backup-overview) and also archives the database Write Ahead Log (WAL) files to minimize data loss. With this approach, if your primary database goes down, it can be restored from a backup with an RPO of minutes, and a RTO of minutes to hours, depending on the size of the database.

For stricter RPO and RTO requirements, you can set up AlloyDB Omni in a high availability configuration using [Patroni](https://patroni.readthedocs.io/en/latest/). In this architecture, there is a primary database and two standby, or replica, databases. You can configure AlloyDB Omni to use standard PostgreSQL streaming replication to ensure each transaction that is committed on the primary is synchronously replicated to both standby databases. This provides a RPO of zero, and a RTO of less than sixty seconds for most failure scenarios.

Depending on your cluster configuration, synchronous replication might impact response time for transactions, and you can choose to risk a small amount of data loss. For example, you can have a non-zero RPO in exchange for lower transactional latency by implementing high availability with asynchronous replication instead of synchronous. Due to the potential impact of synchronous replication on transaction latency, high availability architectures are almost always implemented within a single data center, or between data centers that are close together (tens of km apart / <10 milliseconds of latency apart). However, note that this documentation uses synchronous replication as the default.

For disaster recovery, which is protection against the loss of a data center or a region where there are multiple data centers close together, AlloyDB Omni can be configured with asynchronous streaming replication from the primary region to a secondary region, typically hundreds or thousands of km apart, or 10s to 100s of milliseconds apart. In this configuration, the primary region is configured with synchronous streaming replication between the primary and standby databases within the region, and asynchronous streaming replication is configured from the primary region to one or more secondary regions. AlloyDB Omni can be configured in the secondary region with multiple database instances to ensure that it is protected immediately after a failover from the primary region.

## How high availability works

The specific techniques and tools used to implement high availability for databases can vary depending on the database management system. The following are some of the techniques and tools usually involved in implementing high availability for databases, which can vary depending on the database management system:

  * Redundancy: Replicating your database across multiple servers or geographical regions provides failover options if a primary instance goes down.

  * Automated Failover: Mechanism to detect failures and seamlessly switch to a healthy replica, minimizing downtime. Queries are routed so that application requests reach the new primary node.

  * Data Continuity: Safeguards are implemented to protect data integrity during failures. This includes replication techniques and data consistency checks.

  * Clustering: Clustering involves grouping multiple database servers to work together as a single system. In this way, all nodes in the cluster are active and handle requests which provides load balancing and redundancy.

  * Fallback: Methods to fall back to the original architecture using pre-failover primary and replica nodes in their original capacities.

  * Load Balancing: Distributing database requests across multiple instances improves performance and handles increased traffic.

  * Monitoring and Alerts: Monitoring tools detect issues like server failure, high latency, resource exhaustion and trigger alerts, or automatic failover procedures.

  * Backup and Restore: Backups can be used to restore databases to a previous state in case of data corruption or catastrophic failure.

  * Connection pooling (optional): Optimizes the performance and scalability of applications that interact with your databases.




## High availability tools

Patroni is an open-source cluster management tool for PostgreSQL databases designed to manage and automate high availability for PostgreSQL clusters. Patroni uses various distributed consensus systems like [etcd](https://etcd.io/), [Consul](https://www.consul.io/), or [Zookeeper](https://zookeeper.apache.org/) to coordinate and manage the cluster state. Some key features and components of Patroni include high availability with automatic failover, leader election, replication, and recovery. Patroni runs alongside the PostgreSQL service on database server instances, managing their health, failovers, and replication to ensure high availability and reliability.

Patroni uses a distributed consensus system to store metadata and manage the cluster. In this guide we use a Distributed Configuration Store (DCS) called etcd. One of the uses of etcd is to store and retrieve distributed systems information such as configuration, health, and current status, ensuring consistent configuration across all nodes.

[High Availability Proxy (HAProxy)](https://www.haproxy.org/) is an open-source software used for load balancing and proxying TCP and HTTP-based applications, used to improve the performance and reliability of web applications by distributing incoming requests across multiple servers. HAProxy offers load balancing by distributing network traffic across multiple servers. HAProxy also maintains the health state of the backend servers it connects to by performing health checks. If a server fails a health check, HAProxy stops sending traffic to it until it passes the health checks again.

### Synchronous and asynchronous replication considerations

In a Patroni-managed PostgreSQL cluster, replication can be configured in both synchronous and asynchronous modes. By default, Patroni uses asynchronous streaming replication. For strict RPO requirements, we recommend using synchronous replication.

Synchronous replication in PostgreSQL ensures data consistency by waiting for transactions to be written to both the primary and at least one synchronous standby before committing. Synchronous replication ensures that data is not lost in the event of a primary failure, providing strong data durability and consistency. The primary waits for acknowledgments from the synchronous standby, which can lead to higher latency and potentially lower throughput due to the added round-trip time. This can reduce overall system throughput, especially under high load.

Asynchronous replication allows transactions to be committed on the primary cluster without waiting for acknowledgments from standby clusters. The primary sends WAL records to standbys, which apply them asynchronously. This asynchronous approach reduces write latency and improves performance, but comes with the risk of data loss if the primary fails before the standby has caught up. Standbys might be behind the primary, leading to potential inconsistencies during failover.

The choice between synchronous and asynchronous replication in a Patroni cluster depends on the specific requirements for data durability, consistency, and performance. Synchronous replication is preferable in scenarios where data integrity and minimal data loss are critical, while asynchronous replication suits environments where performance and lower latency are prioritized. You can configure a mixed solution that involves having a three node cluster with a synchronous standby in the same region but a different nearby zone or data center, and a second asynchronous standby in a different region or a more distant data center to protect against potential regional outages.

## What's next

  * [Create a high availability setup](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/high-availability/setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
