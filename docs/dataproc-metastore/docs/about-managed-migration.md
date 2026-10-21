---
url: https://docs.cloud.google.com/dataproc-metastore/docs/about-managed-migration/
title: About managed migration \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:57.659181+00:00
---

# About managed migration  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/about-managed-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  About managed migration Stay organized with collections  Save and categorize content based on your preferences. 

Managed migration is an automated feature that helps you migrate data from a self-managed Hive Metastore to a Dataproc Metastore service, without any sizable downtime (otherwise known as a [flag day](https://en.wikipedia.org/wiki/Flag_day_\(computing\))).

## Managed Migration Architecture

The following diagram provides the high-level architecture of a managed migration.

![Dataproc Metastore managed migration](https://docs.cloud.google.com/static/dataproc-metastore/images/dpms-managed-migration.png)

### Managed migration flow

To complete a managed migration, your service runs through two migration processes—[ _start migration_](https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration#start_migration) and [_complete migration_](https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration#complete_migration). You can cancel a migration at any time with the _cancel migration_ process. There are also a number of operational commands you can run, which aren't required to complete a migration. For example, [_list migrations_](https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration#list_migrations) or [_delete migrations_](https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration#delete_migrations).

As your service moves through this process, it also moves between various _migration states_ and _migration phases_. These states and phases represent the processes that are occurring in the background. For example, the `MIGRATING` state indicates that your service is actively transferring data from your Cloud SQL database to Dataproc Metastore.

**Start Migration**

  * **Dataproc Metastore establishes a connection with your private IP Cloud SQL instance**. After the connection is made, Dataproc Metastore uses the Cloud SQL instance as its Hive Metastore (HMS) backend database. It also remains as the source of truth for your data during the migration. Metadata reads and writes still occur in Cloud SQL when the migration is active.

  * **A change data capture (CDC) pipeline is started**. This pipeline keeps the Cloud SQL instance in your project and Spanner in the Dataproc Metastore managed project in sync. This means that all changes to the HMS database in the Cloud SQL instance are captured through Datastream and written to the Dataproc Metastore Spanner database.




Once the start migration process is successful, you can start routing data workloads to Dataproc Metastore. At this point, Cloud SQL is still the source of truth for your data.

**Complete migration**

After you finish moving your workloads to Dataproc Metastore, you can complete the migration. When a _complete migration_ process is called, the following occurs:

  * Dataproc Metastore transitions into a read-only mode until the _complete migration_ process finishes.
  * The CDC stream transfers all in-flight data to Dataproc Metastore.
  * Dataproc Metastore connects to Spanner and disconnects from Cloud SQL. Dataproc Metastore now acts as the source of truth for your HMS data.



## Proxy and pipeline considerations

**Proxies**

Dataproc Metastore uses a [Cloud SQL Auth proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) chained to a SOCKS5 proxy to connect to your private IP Cloud SQL instance. The SOCKS5 proxy servers are exposed through a service attachment as shown in previous architecture diagram.

  * Each migration requires a dedicated NAT subnet. This is because a NAT subnet can't have more than one service attachment.

  * To avoid cross-region latency issues, provide subnets that are in the same region as your Cloud SQL instance to host the SOCKS5 proxy. For example, `proxy_subnet` and `nat_subnet`.




**Change data capture pipeline**

The change data capture pipeline uses VPC peering to establish a connection between Datastream and private IP Cloud SQL.

  * For each migration, a new private connection is created and a new peering connection is established.

  * The VPC network hosting the Cloud SQL instance has as many peering connections as there are active migrations. Make sure that your VPC network has the capacity to host all of the necessary peering connections.




## What's next

  * [Prerequisites for managed migration ](https://docs.cloud.google.com/dataproc-metastore/docs/managed-migration-prerequisites)
  * [Use managed migration](https://docs.cloud.google.com/dataproc-metastore/docs/use-managed-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
