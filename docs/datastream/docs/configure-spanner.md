---
url: https://docs.cloud.google.com/datastream/docs/configure-spanner/
title: Configure a source Spanner database \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:52.224539+00:00
---

# Configure a source Spanner database  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a source Spanner database Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure change data capture (CDC) to stream data from a Spanner database to a supported destination, such as BigQuery or Cloud Storage.

## Before you begin

If your Spanner instance exists in a Google Cloud project other than the one where Datastream is running, you need to provide the Datastream service agent the `spanner.databaseReader` IAM role, and if you plan to use Data Boost, the `spanner.databaseReaderWithDataBoost` role.

If you'd rather use a fine-grained access control database role, see Create a Spanner connection profile and stream for individual permissions required.

## Create a Spanner database

To start replicating change data from Spanner, you first need to [create a Spanner instance](https://docs.cloud.google.com/spanner/docs/create-manage-instances) and a [Spanner database](https://docs.cloud.google.com/spanner/docs/create-manage-databases).

## Create a change stream

Spanner uses change streams to track and stream data changes such as inserts, updates, and deletes. To configure your Spanner source for replication in Datastream, you need to create and configure a Spanner change stream. You need to specify the `NEW_ROW` [value capture type](https://docs.cloud.google.com/spanner/docs/change-streams#value-capture-type) for your change stream.

For more information, see [Change streams overview](https://docs.cloud.google.com/spanner/docs/change-streams).

## Create a Spanner connection profile and stream

When you create a new Spanner connection profile, you need to specify the Spanner database that you created. The database name needs to have the following format:

`projects/PROJECT_ID/instances/INSTANCE/databases/DATABASE_ID`

When you create a stream, you can optionally supply:

  * The objects to be included and excluded.
  * The maximum number of concurrent reads for backfill or change stream queries.

Setting the maximum number of concurrent reads for change stream queries (the CDC concurrency limit) might increase streaming latency. This is because change streams are divided into partitions, and limiting concurrency prevents Datastream from reading multiple partitions simultaneously. We recommend setting this value only if you've observed significant CPU usage. 
  * Whether to have Datastream use [Data Boost](https://docs.cloud.google.com/spanner/docs/databoost/databoost-overview) when querying Spanner.

  * A fine-grained access control database role for Datastream to use when querying Spanner. To use this role, Datastream needs the following IAM permissions at minimum:

    * `spanner.databases.useRoleBasedAccess`
    * `spanner.databaseRoles.list`
    * `spanner.databases.useDataBoost` (if you choose to use Spanner Data Boost)

In addition, the Spanner database role must have the following permissions:

    * `SELECT` permissions for the tables being streamed.
    * Fine-grained permissions for the change stream. For more information, see [Fine-grained access control for change streams](https://docs.cloud.google.com/spanner/docs/fgac-change-streams).
  * Spanner remote procedure call (RPC) priority for Datastream to use.




## What's next

  * Learn more about [Spanner as a source](https://docs.cloud.google.com/datastream/docs/sources-spanner).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
