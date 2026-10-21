---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/get-started/
title: Get started with AlloyDB Omni on VMs \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:34:41.011655+00:00
---

# Get started with AlloyDB Omni on VMs  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/get-started/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Get started with AlloyDB Omni on VMs Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/get-started)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

AlloyDB Omni is a downloadable database software package that lets you deploy a streamlined edition of AlloyDB for PostgreSQL in your own computing environment. You can run AlloyDB Omni in private data centers, on public clouds, and on developer laptops.

To get started with AlloyDB Omni, use the following guides, which provide detailed information about how to install and use AlloyDB Omni in virtual machine (VM) environments. 

  * [AlloyDB Omni Installation Guide](https://docs.cloud.google.com/static/alloydb/omni/kubernetes/15.5.5/docs/pdfs/AlloyDB_Omni_Installation_Guide.pdf)
  * [AlloyDB Omni Configuration Guide](https://docs.cloud.google.com/static/alloydb/omni/kubernetes/15.5.5/docs/pdfs/AlloyDB_Omni_Configuration_Guide.pdf)
  * [AlloyDB Omni Developers Guide](https://docs.cloud.google.com/static/alloydb/omni/kubernetes/15.5.5/docs/pdfs/AlloyDB_Omni_Developers_Guide.pdf)
  * [AlloyDB Omni Performance Management Guide](https://docs.cloud.google.com/static/alloydb/omni/kubernetes/15.5.5/docs/pdfs/AlloyDB_Omni_Performance_Management_Guide.pdf)

**Note:** The information in these documents is in addition to the AlloyDB Omni documentation that describes how to install and use AlloyDB Omni in VM and Kubernetes environments. Information in these guides might also be duplicated in other AlloyDB Omni documents.

AlloyDB Omni doesn't include some AlloyDB for PostgreSQL features that rely on operation within Google Cloud. If you want to upgrade your project to the fully managed scaling, security, and availability features of AlloyDB for PostgreSQL, you can migrate your AlloyDB Omni data into an AlloyDB for PostgreSQL cluster like any other initial data import.

## Use cases

AlloyDB Omni is well-suited to the following scenarios:

  * You need a scalable and performant version of PostgreSQL, but you can't run a database in the cloud due to regulatory or data sovereignty requirements.
  * You need a database that keeps running even when it's disconnected from the internet.
  * You want to physically locate your database as close as possible to your users, in order to minimize latency.
  * You want to migrate away from a legacy database without committing to a full cloud migration.
  * You have workloads that need to run in multiple public clouds, or in a hybrid cloud with private data centers and public clouds intermixed.



## What it's good for

AlloyDB Omni includes many of the performance improvements in AlloyDB for PostgreSQL. AlloyDB Omni has more than twice the throughput of open source PostgreSQL on TPC-C-like tests with HammerDB, and it offers an improvement in response time by up to a hundred times for TPC-H-like analytical queries.

AlloyDB Omni also supports autopilot features from AlloyDB for PostgreSQL in Google Cloud, allowing it to self-update and self-tune. These autopilot features include automatic memory management, adaptive autovacuum, and index advisor. AlloyDB Omni also supports the columnar engine, which can accelerate analytical queries on large data sets by up to 100 times.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
