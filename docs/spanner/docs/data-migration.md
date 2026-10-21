---
url: https://docs.cloud.google.com/spanner/docs/data-migration/
title: Migrate your data \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:14.124349+00:00
---

# Migrate your data  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/data-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Migrate your data Stay organized with collections  Save and categorize content based on your preferences. 

After optimizing your Spanner schema and migrating your application, you can move your data into an empty production-sized Spanner database, and then switch over your application to use the Spanner database.

Depending on your use case, you might be able to perform a live data migration with minimal downtime, or you might require prolonged downtime to perform the data migration.

If your application can't afford a lot of downtime, consider performing a live data migration. If your application can handle downtime, you can consider migrating with downtime.

In a live data migration, you need to configure the network infrastructure required for data to flow between your source database, the target Spanner database, and the tools you're using to perform the data migration. You need to decide on either private or public network connectivity depending on your organization's compliance requirements. You might need your organization's network administrator to set up the infrastructure.

## Live data migration

A live data migration consists of two components:

  * Migrating the data in a consistent snapshot of your source database.
  * Migrating the stream of changes (inserts, updates and deletes) since that snapshot, referred to as change data capture (CDC).



While live data migrations help protect your data, the process involves challenges, including the following:

  * Storing CDC data while the snapshot is migrating.
  * Writing the CDC data to Spanner while capturing the incoming CDC stream.
  * Ensuring that the migration of CDC data to Spanner is faster than the incoming CDC stream.



## Migration with downtime

If your source database can export to CSV or Avro, then you can migrate to Spanner with downtime. For more information, see [Spanner import and export overview](https://docs.cloud.google.com/spanner/docs/import-export-overview).

Migrations with downtime can be used for test environments or applications that can handle a few hours of downtime. On a live database, a migration with downtime might result in data loss.

To perform a downtime migration, consider the following high-level approach:

  1. Stop your application and generate a dump file of the data from the source database.
  2. Upload the dump file to Cloud Storage in a MySQL, PostgreSQL, Avro, or CSV dump format.
  3. Load the dump file into Spanner using Dataflow or the Spanner migration tool.



Generating multiple small dump files makes it quicker to write to Spanner, as Spanner can read multiple dump files in parallel.

When generating a dump file from the source database, keep the following in mind to generate a consistent snapshot of data:

  * Before you perform the dump, apply a read lock on the source database to prevent the data from changing during the generation of the dump file.
  * Alternatively, generate the dump file using a read replica from the source database with replication disabled.



## Source-specific guides

  * MySQL: [Migrate your MySQL data](https://docs.cloud.google.com/spanner/docs/mysql-live-data-migration).



[ Previous arrow_back  Optimize your schema and application performance  ](https://docs.cloud.google.com/spanner/docs/optimize-schema-performance)

[ Next Validate your data  arrow_forward  ](https://docs.cloud.google.com/spanner/docs/data-validation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
