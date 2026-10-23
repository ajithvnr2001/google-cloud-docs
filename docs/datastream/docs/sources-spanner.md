---
url: https://docs.cloud.google.com/datastream/docs/sources-spanner/
title: Stream data from Spanner sources \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:31.080458+00:00
---

# Stream data from Spanner sources  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-spanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from Spanner sources Stay organized with collections  Save and categorize content based on your preferences. 

Using a Spanner database as a source in Datastream lets you replicate historical data and change stream events into your destination for real-time analytics.

To prepare your Spanner source in Datastream, review the replication behavior, supported editions, and known limitations.

## Behavior

Spanner is a fully managed, scalable, and highly available database service that you can use as a source with Datastream. Datastream uses a Spanner change stream to track changes made in Spanner databases. The changes included in the change stream are then replicated to the destination to reproduce the source events.

Datastream doesn't create or modify change streams, so the database objects that aren't tracked by the provided Spanner change stream can't be included in your Datastream stream.

For more information about Spanner, see the [Spanner documentation](https://docs.cloud.google.com/spanner/docs).

## Versions

Datastream supports all available Spanner editions:

  * Standard edition
  * Enterprise edition
  * Enterprise Plus edition



For an overview of each version, see [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview).

## Free Tier

Datastream lets you stream from Spanner to BigQuery using the Free Tier, providing up to 100 GiB of change data capture data free every month. For more information, see [Datastream pricing](https://cloud.google.com/datastream/pricing).

## Known limitations

Known limitations for using a Spanner database as a source include:

  * Only change streams using the `NEW_ROW` or `NEW_ROW_AND_OLD_VALUES` value capture types are supported.
  * Datastream doesn't support the `PROTO` or `ENUM` data type columns.
  * Datastream doesn't support arrays of `DATE` or `TIMESTAMP` data types.
  * Backfills for databases of over 3 tebibytes (TiB) in size can take over 24 hours to complete.
  * Backfills create snapshot epochs, a type of backup created for a specific timestamp that retain the data versions for that timestamp. Snapshot epochs delay major compactions until the backfill is complete. To learn more about compactions, see [Spanner columnar engine overview](https://docs.cloud.google.com/spanner/docs/columnar-engine).
  * Datastream might have issues keeping up with Spanner change streams that have more than 10,000 partitions. This means that the change events might arrive delayed, or the stream might eventually fail.
  * Datastream might have issues keeping up with Spanner change streams with over 60,000 updates per second. This means that the change events might arrive delayed, or the stream might eventually fail.
  * Datastream might have issues keeping up with Spanner change streams with over 60 mebibytes (MiB) per second throughput. This means that the change events might arrive delayed, or the stream might eventually fail.
  * Replicating geo-partitioned data isn't supported because Spanner change streams don't support partitioned data.



## What's next

  * Learn how to [configure a Spanner source](https://docs.cloud.google.com/datastream/docs/configure-spanner) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
