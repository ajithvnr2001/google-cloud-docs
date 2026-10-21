---
url: https://docs.cloud.google.com/spanner/docs/cutover-fallback/
title: Configure fallback and cutover \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:43.334270+00:00
---

# Configure fallback and cutover  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/cutover-fallback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Configure fallback and cutover Stay organized with collections  Save and categorize content based on your preferences. 

Migrations are often time-consuming and complex. It is possible that after data migration and cutover, you might encounter inconsistent performance or issues with the Spanner database.

We recommend configuring fallback from your Spanner database before performing cutover to avoid significant impact if an error occurs during migration. Fallback lets you revert to the source database with minimal downtime.

Reverse replication supports fallback by replicating data written to Spanner back to your source database. If you need to fall back, you can then point your application to the source database and continue serving requests with minimal downtime.

Spanner provides prebuilt reverse replication pipelines that handle this process out of the box, so you don't need to build custom reverse replication tooling. The pipeline automatically does the following:

  * Handles changes in data types and schema mappings between Spanner and your source database.
  * Reverses any transformations performed during the forward migration.
  * Routes data to the appropriate destination, taking into account sharding schemes on the source database.
  * Captures changes from Spanner change streams before writing to your source database, ensuring consistency eventually.
  * Manages error handling and retries through dead-letter queues.



## Source-specific guides

Use the following guides for each phase of fallback and cutover:

  * MySQL: 
    * [Configure fallback to MySQL](https://docs.cloud.google.com/spanner/docs/mysql-configure-fallback).
    * [Perform cutover from MySQL](https://docs.cloud.google.com/spanner/docs/mysql-perform-cutover).
    * [Perform fallback to MySQL](https://docs.cloud.google.com/spanner/docs/mysql-fallback).



[ Previous arrow_back  Validate your data  ](https://docs.cloud.google.com/spanner/docs/data-validation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
