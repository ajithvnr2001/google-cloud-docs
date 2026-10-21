---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview/
title: AlloyDB Omni 15.5.5 overview \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:32:53.498475+00:00
---

# AlloyDB Omni 15.5.5 overview  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  AlloyDB Omni 15.5.5 overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/overview)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/overview)

AlloyDB Omni is a downloadable database software package that lets you deploy a streamlined edition of [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) in your own computing environment. The portability of AlloyDB Omni lets it run in a wide variety of environments, including the following: 

  * Data centers
  * Laptops
  * Cloud-based VM instances



AlloyDB Omni is well-suited to the following scenarios:

  * You need a scalable and performant version of PostgreSQL, but you can't run a database in the cloud due to regulatory or data-sovereignty requirements.
  * You need a database that keeps running even when it is disconnected from the internet.
  * You want to physically locate your database as close as possible your users, in order to minimize latency.
  * You would like a way to migrate away from a legacy database, but without committing to a full cloud migration.



AlloyDB Omni does not include AlloyDB features that rely on operation within Google Cloud. If you want to upgrade your project to the fully managed scaling, security, and availability features of AlloyDB, you can migrate your AlloyDB Omni data into an AlloyDB cluster just as you can with any other initial data import.

## Key features

  * A PostgreSQL-compatible database server.
  * Support for [AlloyDB AI](https://cloud.google.com/alloydb/ai), an integrated set of capabilities built into AlloyDB, to help you build enterprise-grade generative AI applications using your operational data.
  * Integrations with the Google Cloud AI ecosystem including the [Vertex AI Model Garden](https://cloud.google.com/model-garden) and open source generative AI tools.
  * An [index advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor) that analyzes frequently run queries and recommends new indexes for better query performance.
  * The AlloyDB [columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about), which keeps frequently queried data in an in-memory columnar format for faster performance on business intelligence, reporting, and hybrid transactional and analytical processing (HTAP) workloads.

**Note:** The columnar engine is unavailable on Arm architectures.
  * Other optimizations and enhancements over a stock PostgreSQL server, like automatic memory management and [adaptive autovacuum](https://docs.cloud.google.com/alloydb/docs/adaptive-autovacuum) of stale data.




## How AlloyDB Omni works

AlloyDB Omni can be installed either as a standalone server or as part of a Kubernetes environment.

AlloyDB Omni runs in a Docker container that you [install onto your own environment](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install). We recommend running AlloyDB Omni on a Linux system with SSD storage and at least 8 GB of memory per CPU.

The AlloyDB Omni Kubernetes Operator is an extension to the Kubernetes API that lets you ​​run AlloyDB Omni in most CNCF-compliant Kubernetes environments. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/deploy-kubernetes).

Your applications connect to and communicate with your AlloyDB Omni installation exactly as they would with an ordinary PostgreSQL database server. User access control relies on PostgreSQL standards, as well.

You can configure the behavior of AlloyDB Omni using the [same database flags that are available to AlloyDB](https://docs.cloud.google.com/alloydb/docs/reference/database-flags).

## Data backup and disaster recovery

AlloyDB Omni features a continuous backup and recovery system that lets you create a new database cluster based on any point in time within an adjustable retention period. This lets you recover quickly from data-loss accidents.

In addition, AlloyDB Omni can create and store complete backups of your database cluster's data, either on demand or on a regular schedule. At any time, you can restore from a backup to an AlloyDB Omni database cluster that contains all the data from the original database cluster at the moment of the backup's creation.

For more information, see [Back up and restore AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/backup-overview).

As a further method of disaster recovery, you can achieve cross data center replication by creating secondary database clusters in separate data centers. AlloyDB Omni asynchronously streams data from a designated primary database cluster to each of its secondary clusters. Whenever needed, you can promote a secondary database cluster into a primary AlloyDB Omni database cluster.

For more information, see [About cross-data-center replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/cross-data-center-replication/about-cross-data-center-replication)

## Documentation for the latest version of AlloyDB Omni

For information about the latest version of AlloyDB Omni, refer to the [AlloyDB Omni documentation set](https://docs.cloud.google.com/alloydb/omni/docs).

## Documentation for AlloyDB Omni version 15.5.2 and earlier

For information about the previous version of AlloyDB Omni, refer to the [Multi-container AlloyDB Omni documentation set](https://docs.cloud.google.com/alloydb/omni/15.5.2/docs/overview).

## What's next

  * [Quickstart: Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/quickstart)

  * [Set up AlloyDB Omni for production](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/configure-omni)

  * [Install the psql client tool](https://docs.cloud.google.com/alloydb/docs/install-psql)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
