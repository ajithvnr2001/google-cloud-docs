---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview/
title: AlloyDB Omni version 15.5.2 and earlier overview \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:37:38.652950+00:00
---

# AlloyDB Omni version 15.5.2 and earlier overview  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  AlloyDB Omni version 15.5.2 and earlier overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)

AlloyDB Omni 15.5.2 is a downloadable database software package that lets you deploy a streamlined edition of [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) in your own computing environment. The portability of AlloyDB Omni lets it run in a wide variety of environments, including the following: 

  * Datacenters
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
  * Other optimizations and enhancements over a stock PostgreSQL server, like automatic memory management and [adaptive autovacuum](https://docs.cloud.google.com/alloydb/docs/adaptive-autovacuum) of stale data.



## How AlloyDB Omni works

AlloyDB Omni can be installed either as a standalone server or as part of a Kubernetes environment.

AlloyDB Omni runs in a Docker container that you [install onto your own environment](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install) using a command-line program provided by Google. We recommend running AlloyDB Omni on a Linux system with SSD storage and at least 8 GB of memory per CPU.

The AlloyDB Omni Kubernetes Operator is an extension to the Kubernetes API that lets you ​​run AlloyDB Omni in most CNCF-compliant Kubernetes environments. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes).

Your applications connect to and communicate with your AlloyDB Omni installation exactly as they would with an ordinary PostgreSQL database server. User access control relies on PostgreSQL standards, as well.

You can configure the behavior of AlloyDB Omni using the [same database flags that are available to AlloyDB](https://docs.cloud.google.com/alloydb/docs/reference/database-flags).

## Documentation for the latest version of AlloyDB Omni

For information about the latest version of AlloyDB Omni, refer to the [AlloyDB Omni documentation set](https://docs.cloud.google.com/alloydb/docs/omni).

## What's next

  * [Quickstart: Install AlloyDB Omni on Debian or Ubuntu](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/quickstart)

  * [Customize your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
