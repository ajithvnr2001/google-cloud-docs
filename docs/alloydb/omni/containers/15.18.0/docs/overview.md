---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview/
title: AlloyDB Omni using containers overview \u00a0|\u00a0 AlloyDB Omni using containers: 15.18.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:42:24.338927+00:00
---

# AlloyDB Omni using containers overview  |  AlloyDB Omni using containers: 15.18.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview/

This page documents AlloyDB Omni version **15.18.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview)



Send feedback 

#  AlloyDB Omni using containers overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.18.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



AlloyDB Omni using containers is a downloadable database software package that offers a streamlined version of AlloyDB for PostgreSQL for deployment in a standalone instance in your environment. While sharing core components with the fully-managed AlloyDB for PostgreSQL service on Google Cloud, AlloyDB Omni uses the standard file system interface used by PostgreSQL, as opposed to AlloyDB for PostgreSQL's cloud-native storage layer.

The container deployment option acts like a highly optimized, self-managing PostgreSQL database that brings Google Cloud's performance and AI capabilities to your local or private cloud infrastructure, offering flexibility and powerful features without requiring a full public cloud commitment.

## Use cases

The container deployment option is best-suited for the following use cases:

  * Single instance database: You just need a single instance database. You don't need features like high availability and disaster recovery.
  * Development and testing: The container deployment option is well-suited for setting up an AlloyDB Omni on your laptop or in a testing environment, including performance.
  * Non-Kubernetes environments: When your infrastructure doesn't use Kubernetes or when the complexity of a container orchestrator isn't needed.
  * Offline operations: For applications that must continue to function even when disconnected from the internet.
  * Low-latency requirements: When you need to place the database geographically close to your users to ensure the fastest possible response times.



You can also create [Transparent Data Encryption (TDE)-enabled clusters](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/transparent-data-encryption-omni), which let you secure all data at rest in your AlloyDB Omni clusters without modifying your application code. By enabling this feature, you ensure that all critical data at rest is automatically encrypted before being written to disk. This helps you meet any compliance requirements and protects sensitive information.

## Key features and performance

**Note:** To unlock additional features, including support for PostgreSQL version 18, sign up using the [AlloyDB Omni incentives form](https://docs.google.com/forms/d/e/1FAIpQLSep1HzCiseWXq_0oTPs9wOTVWQuH2yAK225SbggvvuqWzMPjQ/viewform).

AlloyDB Omni provides a PostgreSQL-compatible database server. It includes support for AlloyDB AI, enabling the creation of enterprise-grade generative AI applications using operational data, with integrations into the Google Cloud AI ecosystem.

Key autopilot features from AlloyDB for PostgreSQL are also present, allowing AlloyDB Omni to self-manage and self-tune. This includes automatic memory management, which continuously monitors and optimizes memory consumption, dynamically adjusting the shared buffer cache size based on memory pressure. By default, it sets an upper limit of 80% of system memory and allocates 10% for the shared buffer cache. Another autopilot feature is adaptive autovacuum, which analyzes database workloads and automatically adjusts the frequency and intensity of vacuuming to maintain peak performance without interference. An index advisor also analyzes frequently run queries and recommends new indexes for improved query performance.

For accelerating analytical queries, AlloyDB Omni features a columnar engine. This engine keeps frequently queried data in an in-memory columnar format, significantly boosting performance for business intelligence, reporting, and hybrid transactional and analytical processing (HTAP) workloads. Our performance tests indicate that transactional workloads in AlloyDB Omni are more than 2X faster, and analytical queries are up to 100X faster than standard PostgreSQL.

## How it works

The container deployment option runs in a Docker container that you install onto your own environment, such as a Linux system with SSD storage and at least 8GB of memory per CPU. Your applications connect and communicate with AlloyDB Omni just like a standard PostgreSQL database server, with user access control relying on PostgreSQL standards. Configuration of database behavior, from logging to the columnar engine, is managed through database flags.

The containerized distribution offers advantages like transparent dependency management, portability across environments, security isolation, resource management, and seamless patching and upgrades.

## Architecture

The container deployment option comprises PostgreSQL components with AlloyDB for PostgreSQL enhancements and dedicated AlloyDB for PostgreSQL components.

  * Database engine: translates client queries into executable plans, finds necessary data, performs filtering, ordering, and aggregation, and returns results. It aims to respond to queries using minimal resources, emphasizing good data models and query design.
  * Data storage: data is stored in fixed-size pages in the underlying file system. AlloyDB Omni first checks the buffer pool when accessing data; if not found, it reads from the file system. Maximizing buffer pool size is crucial for performance. AlloyDB Omni uses dynamic memory management, allowing the buffer pool to grow and shrink dynamically within configured bounds, eliminating the need to manually tune its size.
  * Resource management: query processing requires CPU, memory, I/O, network, and synchronization primitives. Monitoring CPU utilization (aiming for ~70% steady state) and IOPS is important to avoid bottlenecks. Minimizing reads and writes to storage by maximizing data in the buffer pool helps avoid IOPS limits.
  * AI/ML worker: in a VM environment, the AI/ML background worker provides all capabilities needed for calling Vertex AI models directly from the database, running as the `omni ml worker` process. 



## Data backup and disaster recovery

The container deployment option features a continuous backup and recovery system, allowing the creation of a new database cluster from any point in time within an adjustable retention period. It can also create and store complete backups of your database cluster's data, on demand or on a schedule, enabling restoration to an AlloyDB Omni cluster.

For disaster recovery, cross-data-center replication can be achieved by creating secondary database clusters in separate data centers. AlloyDB Omni asynchronously streams data from a primary to secondary clusters, and a secondary cluster can be promoted to a primary when needed.

To upgrade to the fully managed scaling, security, and availability features of AlloyDB for PostgreSQL, you can migrate your AlloyDB Omni data into an AlloyDB for PostgreSQL cluster.

## What's next

  * [Subscribe to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/run-alloydb-omni-production#subscribe).
  * Learn about [AlloyDB for PostgreSQL additions to standard PostgreSQL](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/additions-to-postgresql).
  * Choose an [AlloyDB for PostgreSQL download or installation option](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/available-download-install-options).
  * Choose an [AlloyDB Omni availability reference architecture](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/database-availability-reference-architecture-overview).
  * [Plan your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/plan-installation). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
