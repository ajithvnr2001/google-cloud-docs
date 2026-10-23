---
url: https://docs.cloud.google.com/alloydb/docs/high-availability/
title: AlloyDB high availability overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:21.672226+00:00
---

# AlloyDB high availability overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB high availability overview Stay organized with collections  Save and categorize content based on your preferences. 

High availability (HA) in AlloyDB for PostgreSQL keeps your database operational and your data accessible to client applications during zonal or instance failures. Unlike zonal instances, which can experience extended downtime during an outage, HA instances automatically fail over between active and standby nodes across zones. To configure an instance for HA, see [View cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/reference/cluster-settings?resource=prim-instance).

## Primary and secondary instances

An AlloyDB primary instance configured with high availability includes an active node and a standby node, which are located in different zones. For storage, AlloyDB uses a regional log persistor to store database write-ahead logs (WAL) and the AlloyDB regional storage service to store data blocks. The instance's IP address routes traffic to the active node using a load balancer.

When processing writes, the AlloyDB database first writes WAL to its regional log persistor on the active node and then asynchronously transfers the logs to the regional log processing servers in AlloyDB, which materialize the logs into data blocks for long-term storage. AlloyDB then cleans up the logs that are successfully processed.

The following diagram shows the high availability architecture.

![High availability architecture](https://docs.cloud.google.com/static/alloydb/images/adb-high-availability.png)

**Fig. 1.** High availability architecture.

## Failover

If the active node becomes unavailable, AlloyDB automatically fails over the primary instance to its standby node, which becomes the new active node. The load balancer recognizes the new active node and begins routing traffic to it. After a failover, the new active node remains active even after the original node comes back online. No data loss occurs during failover due to synchronous WAL writes to the regional log persistor.

The following diagram shows the traffic flow after failover.

![Traffic flow after
failover](https://docs.cloud.google.com/static/alloydb/images/adb-high-availability-failover.png)

**Fig. 2.** Traffic flow after failover.

A failover occurs in the following sequence of events:

  1. The active node or zone fails. The AlloyDB health monitoring system periodically checks whether the active node is healthy. If the health monitoring system fails multiple checks, it initiates failover. This detection can take up to 30 seconds.
  2. The database starts on the standby node and begins accepting connections. This typically takes less than 30 seconds.
  3. The standby node is promoted to primary. Using the instance's static IP address, the new primary node begins serving data, and client queries succeed after a reconnect. 
  4. AlloyDB recreates a standby node in the previously active zone. This standby node is then ready for future failovers.



### Requirements

For AlloyDB to allow failover, the configuration must meet these requirements:

  * The primary instance must be in a normal operating state (not stopped or undergoing maintenance).
  * The standby zone and standby node must both be healthy.



## Hot standby architecture

AlloyDB instances with PostgreSQL 18 provide improved failover using the hot standby feature.

With the hot standby feature, AlloyDB runs the standby node as a replica. During failover, this replica can transition to a read-write mode faster, reducing downtime. Additionally, the replication enables warm caches, which helps ensure consistent query performance after failover.

The following diagram shows the high availability architecture with the hot standby included. ![Hot standby](https://docs.cloud.google.com/static/alloydb/images/adb-high-availability-hot-standby.png)

**Fig. 3.** Hot standby.

## Read pools

Read pool instances with two or more nodes are highly available. Nodes are distributed evenly across zones, creating resilience to failure events. In case of failure events like a node or zone failure, a regional load balancer routes traffic to the remaining healthy nodes, ensuring no downtime for your clients. 

Read pools stay online during a primary instance failover. WAL replication from the primary instance pauses temporarily during failover and resumes automatically after the primary instance is recovered.

## What's next

  * [Fail over a primary or secondary instance manually](https://docs.cloud.google.com/alloydb/docs/instance-primary-secondary-failover).
  * [Test a primary instance for high availability](https://docs.cloud.google.com/alloydb/docs/test-high-availability).
  * [Reduce costs using basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
