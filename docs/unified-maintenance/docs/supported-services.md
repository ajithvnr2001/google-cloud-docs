---
url: https://docs.cloud.google.com/unified-maintenance/docs/supported-services/
title: Supported services \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:05.359920+00:00
---

# Supported services  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/supported-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Resources ](https://docs.cloud.google.com/unified-maintenance/docs/resources)



Send feedback 

#  Supported services Stay organized with collections  Save and categorize content based on your preferences. 

This table lists services supported by Unified Maintenance. If a service isn't listed, that service is unsupported or isn't subject to disruptive maintenance events.

Product | Resource types | Can support reschedule? | Can support on-demand update? | Monitored Resource Type  
---|---|---|---|---  
**AlloyDB for PostgreSQL** | `alloydb.googleapis.com/Cluster` | No | [Yes](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance) | `alloydb.googleapis.com/Cluster`  
**Apigee** | `apigee.googleapis.com/Instance` | No | No | `apigee.googleapis.com/Instance`  
**Backup and DR Service** | `backupdr.googleapis.com/ManagementServer`  
  
`backupdr.googleapis.com/BackupVault` | No | No | `backupdr.googleapis.com/ManagementConsole`  
  
`backupdr.googleapis.com/BackupVault`  
**Bare Metal Solution** | `compute.googleapis.com/Instance` | No | [Yes](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | `gce_instance`  
Unified Maintenance supports these Bare Metal Solution virtual machine instances types. |  | 

**General-purpose**
    C3
**Memory-optimized**
    X4
| 

**Storage-optimized**
    Z3  
---|---|---|---  
**Cloud Data Fusion** | `datafusion.googleapis.com/Instance` | No | No | `datafusion.googleapis.com/InstanceV3`  
**Cloud Interconnect** | `compute.googleapis.com/Interconnect` | No | No | `interconnect`  
**Cloud Service Mesh** | `container.googleapis.com/Cluster` | No | No | `gke_cluster`  
**Cloud SQL - MySQL** | `sqladmin.googleapis.com/Instance` | [Yes](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window#reschedule) | [Yes](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) | `cloudsql_database`  
**Cloud SQL - Postgres** | `sqladmin.googleapis.com/Instance` | [Yes](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window#reschedule) | [Yes](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) | `cloudsql_database`  
**Cloud SQL - SQL Server** | `sqladmin.googleapis.com/Instance` | [Yes](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window#reschedule) | [Yes](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance) | `cloudsql_database`  
**Compute Engine** | `compute.googleapis.com/Instance` | No | [Yes](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) | `gce_instance`  
Unified Maintenance supports these Compute Engine virtual machine instances types. For more information, see [Monitor and plan for a host maintenance event.](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#limitations) |  | 

**Accelerator-optimized**
    A2, A3, A4, A4X, CT4P, CT5P, CT5LP, CT6E, G2
**Cloud TPU**
    V4, V5E, V5P, V6E
**Compute-optimized**
    C2, C2D, H3, H4D
| 

**General-purpose**
    C3, C3D, C4, C4A, C4D, N1, N2, N2D
**Memory-optimized**
    M1, M2, M3, M4, X4
**Storage-optimized**
    Z3  
---|---|---|---  
**Filestore** | `file.googleapis.com/Instance` | No | No | `filestore_instance`  
**Google Kubernetes Engine** | `container.googleapis.com/Cluster`  
  
`container.googleapis.com/NodePool` | No | [Yes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) | `gke_cluster`  
`gke_nodepool`  
**Looker** | `looker.googleapis.com/Instance` | No | No | `looker.googleapis.com/Instance`  
**Managed Service for Apache Airflow** | `composer.googleapis.com/Environment` | No | No | `environment`  
**Memorystore - Memcached** | `memcache.googleapis.com/Instance` | [Yes](https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance#rescheduling_maintenance) | [Yes](https://docs.cloud.google.com/memorystore/docs/memcached/self-service-maintenance) | `memcache_node`  
**Memorystore - Redis** | `redis.googleapis.com/Instance` | [Yes](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance#rescheduling_maintenance) | [Yes](https://docs.cloud.google.com/memorystore/docs/redis/self-service-maintenance) | `redis_instance`  
**Note:** You can reschedule, postpone, or manage Google Kubernetes Engine maintenance using maintenance windows and maintenance exclusions. While you cannot manually move an automatic upgrade to a precise custom date, you can block maintenance during critical periods, change the maintenance window to specify when maintenance can happen and initiate the maintenances.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
