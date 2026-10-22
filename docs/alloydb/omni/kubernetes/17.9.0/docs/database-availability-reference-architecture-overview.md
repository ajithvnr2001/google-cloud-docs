---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/database-availability-reference-architecture-overview/
title: AlloyDB Omni availability reference architecture overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:38.949130+00:00
---

# AlloyDB Omni availability reference architecture overview  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/database-availability-reference-architecture-overview/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  AlloyDB Omni availability reference architecture overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/database-availability-reference-architecture-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/database-availability-reference-architecture-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/database-availability-reference-architecture-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/database-availability-reference-architecture-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/database-availability-reference-architecture-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/database-availability-reference-architecture-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/database-availability-reference-architecture-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/database-availability-reference-architecture-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/database-availability-reference-architecture-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/database-availability-reference-architecture-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/database-availability-reference-architecture-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/database-availability-reference-architecture-overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/database-availability-reference-architecture-overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/database-availability-reference-architecture-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/database-availability-reference-architecture-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/database-availability-reference-architecture-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/database-availability-reference-architecture-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/database-availability-reference-architecture-overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/database-availability-reference-architecture-overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/database-availability-reference-architecture-overview)

This page introduces the AlloyDB Omni availability architectures that you can use to ensure that your AlloyDB Omni database is restorable in a timely manner with little or no data loss. 

To ensure business continuity and to minimize data loss, high availability (HA) and disaster recovery (DR) are crucial data protection strategies for AlloyDB Omni. HA focuses on maintaining database availability and minimizing Recovery Time Objective (RTO), while DR addresses recovery from catastrophic events and minimizing Recovery Point Objective (RPO).

RTO and RPO are aligned with business requirements and are defined as follows:

  * [RTO ](https://en.wikipedia.org/wiki/IT_disaster_recovery#Recovery_Time_Objective) is the maximum time that a database can be down or unavailable before the business experiences unacceptable consequences, such as loss of revenue or productivity.
  * [RPO](https://en.wikipedia.org/wiki/IT_disaster_recovery#Recovery_Point_Objective) is the maximum amount of data loss that a business can experience before it impacts business requirements. For example, inventory systems that require a full audit trail might have a requirement for zero data loss.



AlloyDB Omni offers the following availability reference architectures that provide increasing levels of availability:

  1. [Standard availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-backups): protects your data using backups.
  2. [Enhanced availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-zonal-replication): protects your data using zonal replication in a region (HA).
  3. [Premium availability](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-zonal-regional-replication): protects your data using zonal and regional replication (HA and DR).



## Availability mechanisms

The following are the main mechanisms that ensure availability:

  * Database backups
  * Database replication



### Database backups

Database backups, a fundamental aspect of data protection, involve creating physical copies of database data files. Different backup types—full, incremental, and differential—offer varying balances between recovery point objective (RPO), backup size and duration, and restoration time.

To ensure efficient recovery and to minimize data loss in the event of system failures, a robust backup strategy must include both database and write-ahead log (WAL) file backups. Regular (typically daily) backups of data files are crucial. You must also back up WAL files, which record database modifications and are critical for point-in-time recovery and maintaining data integrity during restoration.

### Database replication

PostgreSQL offers replica servers for increased reliability. These replicas are classified as either _warm_ standbys, which don't accept application connections, or _hot_ standbys, which operate in a read-only mode. Changes from the primary database are continuously applied to the replica to keep the replica's data current. If the primary database fails, the replica is promoted to primary status and assumes the primary database's responsibilities.

Database replicas can be placed in the same zone or data center as the primary instance, in a different zone, in a different region, or in a mix of these locations. The farther the replica is located from the primary database, the greater the latency when sending changes to keep the replicas up to date. For deployments across distant locations to mitigate large-scale failures, such as regional fault, data replication is typically done asynchronously. This approach avoids performance degradation that can occur in such setups.

In high availability deployments, replicas are typically deployed in close proximity to the primary database. For example, replicas that are deployed in a different zone within the same data center offer low RTOs and close to zero RPO. On the other hand, in disaster recovery configurations, replicas are deployed in separate data centers or regions, depending on the required level of protection against outages. This approach results in higher RPO (as the replication might be asynchronous) and varied RTO.

The following table summarizes the mechanisms used for the AlloyDB Omni availability reference architectures:

**Feature** | **Standard** | **Enhanced** | **Premium**  
---|---|---|---  
Backup | Yes | Yes | Yes  
Zonal Replica | No | Yes | Yes  
Cross-Zone Replica  | No | Yes | Yes  
Regional Replica  | No | No | Yes  
  
**Table 1**. Supported AlloyDB Omni availability mechanisms

## Database failures and recovery scenarios

Database failure can occur at the following levels:

  * Instance (node or server) failure: the database itself fails.
  * Server failure: the server that hosts the database fails.
  * Zonal failure: the whole data center housing the server fails.
  * Region failure: the whole region containing multiple data centers (availability zones) is unavailable, for example, due to flood or a large magnitude earthquake.



The likelihood and the risk of a disaster decrease when there are fewer events and the cost of preventing these events increases. Businesses must determine their risk tolerance and choose whether to accept potential disruptions or invest in more resilient architectures to minimize risks.

The following table summarizes the recovery scenarios that AlloyDB Omni reference architectures support:

**Disaster Type** | **Standard** | **Enhanced** | **Premium**  
---|---|---|---  
VM/Instance Failure | Yes | Yes | Yes  
Node/Server Failure | Yes | Yes | Yes  
Zone Failure  | No | Yes | Yes  
Regional Failure | No | No | Yes  
  
**Table 2**. Supported recovery scenarios

Consider your business objectives for your AlloyDB Omni database, such as a critical need for several 9s (99.99%) of availability and zero data loss upon recovery for mission-critical applications. The goal of the availability reference architectures is to address RTO and RPO requirements.

AlloyDB Omni offers standard, enhanced, and premium availability architectures to protect databases from planned and unplanned outages, aligning with varying business needs. For example, development environments might use basic protection with backups, whereas mission-critical applications could employ high availability and disaster recovery setups.

## What's next

Learn more about the AlloyDB Omni availability reference architectures:

  * [Protect your data using backups (Standard Availability)](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-backups).
  * [Protect your data using zonal replication in a region (Enhanced Availability)](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-zonal-replication).
  * [Protect your data using zonal and regional replication (Premium Availability)](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/protect-data-using-zonal-regional-replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
