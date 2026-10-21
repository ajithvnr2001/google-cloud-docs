---
url: https://docs.cloud.google.com/bigtable/docs/migrate/
title: Migrate data to Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:20.324311+00:00
---

# Migrate data to Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate data to Bigtable

This page provides guidelines to help you plan your data migration to Bigtable from other database services. These resources cover different strategies to migrate workloads, including online replication and offline methods.

To understand the workloads that are best suited for Bigtable, see the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview). The guides listed on this page can help you plan and achieve your database migration.

## Migrate data from HBase

When you migrate from an HBase installation to Bigtable, you can use Google-provided open source tools that assist with your data migration and validation.

  * [Replicate from HBase to Bigtable](https://docs.cloud.google.com/bigtable/docs/hbase-replication): Complete an online migration with almost no downtime using the Bigtable HBase replication library.
  * [Migrating data from HBase to Bigtable offline](https://docs.cloud.google.com/bigtable/docs/migrate-hbase-data-to-bigtable): Migrate from an Apache HBase cluster to a Bigtable instance on Google Cloud offline.



## Migrate data from Cassandra

The following resources are useful if you are an administrator planning to migrate workloads from Apache Cassandra to Bigtable.

  * [Bigtable for Cassandra users](https://docs.cloud.google.com/bigtable/docs/cloud-bigtable-for-cassandra-users): Learn the core similarities and differences between the two services.
  * [Migrating from Cassandra](https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra): Use open-source tooling to migrate from Apache Cassandra and interact with Bigtable using Cassandra Query Language (CQL) syntax.
  * [Bigtable codelab for Cassandra users](https://codelabs.developers.google.com/codelabs/cbt-for-cassandra/index.html#0): Practice migrating queries from Cassandra to Bigtable.



## Migrate data from DynamoDB

If you are considering a migration from DynamoDB to Bigtable, read the following guide for a discussion of similarities and differences between the two.

  * [Migrate from DynamoDB to Bigtable](https://docs.cloud.google.com/bigtable/docs/dynamodb-users)



Use a Google-provided migration tool that helps you migrate your data from DynamoDB to Bigtable.

  * [DynamoDB to Bigtable Migration Utility](https://github.com/GoogleCloudPlatform/professional-services/tree/main/tools/dynamodb-bigtable-migration#bigtable-data-bridge---dynamodb-to-bigtable-migration-utility)



## Migrate data from Aerospike

If you are planning to migrate from Aerospike to Bigtable, use the following tutorial to get started.

  * [Migrate from Aerospike to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable)



## Migrate from Vertex AI Feature Store (Legacy)

To prepare for a migration from Vertex AI Feature Store (Legacy) to Bigtable, read the overview:

  * [Migrate from Vertex AI Feature Store (Legacy) to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-vertex-ai-legacy-bigtable)



## What's next

  * [Import and export](https://docs.cloud.google.com/bigtable/docs/import-export)
  * [Choose between SSD and HDD storage](https://docs.cloud.google.com/bigtable/docs/choosing-ssd-hdd)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
