---
url: https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database/
title: Configure a source Oracle database \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:30.613467+00:00
---

# Configure a source Oracle database  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a source Oracle database Stay organized with collections  Save and categorize content based on your preferences. 

Datastream lets you stream change data capture (CDC) updates from an Oracle database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. Depending on whether your database is on-premises or cloud-hosted, you configure redo log access and user privileges for your deployment type and CDC method.

## Methods for querying redo log files

Datastream can use the following methods to query redo log files:

  * Binary log reader, [Preview](https://cloud.google.com/products#product-launch-stages): select this method if you need to query both online and archived redo log files. Binary reader can access log files using Automatic Storage Management or database directory objects. This method is multithreaded and supports low-latency CDC.

  * **LogMiner API** : select this method if you only need to work with archived redo log files. The Oracle LogMiner is single-threaded and can be subject to higher latency and lower throughput. However, this method supports most data types and Oracle database features.

For more information about these methods, see [Overview of Oracle as a source](https://docs.cloud.google.com/datastream/docs/sources-oracle#behavior) and [Work with Oracle database redo log files](https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files). For information about how to configure your database type for each of these methods, see the respective configuration pages.




## Supported databases

Datastream works with the following types of Oracle databases:

  * Amazon RDS for Oracle
  * Self-managed Oracle database
  * Self-hosted Oracle pluggable database



## What's next

  * Learn how to configure an [Amazon RDS for Oracle](https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-oracle) database to work with Datastream.
  * Learn how to configure a [self-managed Oracle database](https://docs.cloud.google.com/datastream/docs/configure-self-managed-oracle) to work with Datastream.
  * Learn how to configure a [self-hosted Oracle pluggable database](https://docs.cloud.google.com/datastream/docs/configure-pluggable-oracle) to work with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
