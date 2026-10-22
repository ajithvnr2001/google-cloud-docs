---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/about-pglogical/
title: About the pglogical extension \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:40:25.224804+00:00
---

# About the pglogical extension  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/about-pglogical/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  About the pglogical extension Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/about-pglogical)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/about-pglogical)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/about-pglogical)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/about-pglogical)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/about-pglogical)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/about-pglogical)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/about-pglogical)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/about-pglogical)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/about-pglogical)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/about-pglogical)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/about-pglogical)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/about-pglogical)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/about-pglogical)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/about-pglogical)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/about-pglogical)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/about-pglogical)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/about-pglogical)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/about-pglogical)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/about-pglogical)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/about-pglogical)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/about-pglogical)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/about-pglogical)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/about-pglogical)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/about-pglogical)

This page provides an overview of the `pglogical` extension, its benefits, and limitations. 

The information on this page applies only to AlloyDB Omni using containers. It does not apply to AlloyDB Omni using the container orchestrator.

## Overview

The [`pglogical` extension](https://github.com/2ndQuadrant/pglogical) is a robust and flexible logical replication tool designed for PostgreSQL, and it also supports high availability (HA) and disaster recovery (DR).

Standard binary replication, commonly known as _physical replication_ , replicates changes at the file system and block level, resulting in a physical mirror in the target system. Even though the physical replication is robust and protects the entire database cluster, it is unidirectional only and requires access to the underlying database data file and write-ahead log (WAL) files.

Whereas, the `pglogical` extension extracts SQL changes from a provider database and replicates them, and then replays them against one or more subscriber databases. This replication is known as _logical replication_.

**Note:** The `pglogical` extension uses the terms `provider` and `subscriber` to describe the endpoints that are used in a replication topology. These terms are synonyms for terms such as source/target, publisher/subscriber, and primary/standby.

By using the `pglogical` extension, you can do the following:

  * Replicate data between multiple AlloyDB Omni databases.
  * Replicate data between AlloyDB Omni and Google Cloud AlloyDB.
  * Replicate data between AlloyDB Omni and other PostgreSQL distributions that include many in third-party cloud services.



## Benefits

Logical replication with the `pglogical` extension offers the following benefits:

  * **Selective replication:** provides the flexibility to set filters and rules to determine what data you want to replicate and where to. You can choose which tables are included and how new tables are handled whether they're included or not. You can also add column and row filters. An optional `apply delay` can be added for situations where you want the subscriber to represent some trailing point in time from the provider.

  * **Bi-directional and multi-primary replication:** all member databases are open in a read or write state and are fully usable. Each endpoint database acts as both provider and subscriber, allowing the creation of advanced replication scenarios, and enabling the possibility of data updates that are made at different endpoints.

  * **Cloud provider support:** Cloud providers such as Google recognize the value of the `pglogical` extension and integrate it into their Cloud services, such as Google Cloud SQL for PostgreSQL and AlloyDB. Other cloud providers also include the `pglogical` extension as an option, allowing multi-cloud or hybrid-cloud configurations.

  * **Cross-version replication:** as pglogical replicates the actual SQL statements, it allows replication between major versions of PostgreSQL. Especially when the provider source database is a lower version than the subscriber target database, cross-version replication can be implemented with reliability.

The `pglogical` extension offers support for many earlier versions of PostgreSQL such as version 9.4 and higher. This makes it an optimal choice for scenarios where you are dealing with legacy systems and want to replicate data into more modern versions of PostgreSQL such as those used in AlloyDB Omni and Google Cloud AlloyDB.




In summary, the `pglogical` extension provides a feature-rich logical replication solution, with compatibility for earlier versions of PostgreSQL and Cloud-managed services that include Google Cloud SQL for PostgreSQL and AlloyDB.

## Limitations of logical replication

All logical replication technologies, including those used with other relational database platforms, have some limitations, and any mismanagement can break the replication process.

Consider the following points for a reliable implementation:

  * Consideration on how to handle database-scoped and cluster-scoped objects that are outside of the replication scope. The `pglogical` extension works at the database level and against a specified set of tables and sequences only. Other object types, such as functions and procedures, must be replicated using some other method.
  * It is recommended that all replication tables must have a primary key. It is possible to use the table `REPLICA IDENTITY` feature to inform the `pglogical` extension about which columns uniquely identify the rows. This must be avoided where possible. Tables that don't have primary keys, are static in nature, and are never `UPDATED` or `DELETED`, and supports only `INSERTS`. These types of tables don't need primary keys.
  * Management of triggers and sequences in subscriber databases. By default, triggers are defined as `ORIGIN` or `LOCAL` triggers, and don't fire on the subscriber database when the rows are replicated. All triggers should be checked to ensure that the `REPLICA` option is set for any trigger so that it does not fire on the subscriber end unless it is required.
  * Dealing with conflict resolution either manually or automatically through `who wins` rules.
  * Replication of Data Definition Language (DDL) commands by either manually implementing on all endpoints, or automatically replicating DDL to subscriber databases using the appropriate `pglogical` API function on the provider database.
  * Ensuring that newly created tables and sequences are manually or automatically added to replication sets on primary databases.
  * Ensuring that a robust, performant, reliable, and secured TCP network exists between all endpoints in the replication topology.



Additional restrictions and limitations of the `pglogical` extension include the following:

  * Superuser permissions are required for `pglogical` version 2.4.3.
  * While most tables and sequences can be replicated, other object types are not replicated by the `pglogical` extension, and `TEMPORARY` and `UNLOGGED` tables are not replicated.
  * To replicate DDL, the pglogical API function must be used. Standard DDL commands are not replicated, except for the `TRUNCATE` command.
  * Operates on an object level per table and per sequence, and is deployed per database. This means that some objects, including cluster-scoped objects such as `users` and `roles`, are excluded from the replication and must be managed separately.



## What's next

  * [Replicate data between AlloyDB for PostgreSQL and AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/replicate-data-alloydb-omni).
  * [Replicate data between AlloyDB Omni and other databases](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/replicate-data-omni-other-db).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
