---
url: https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview/
title: Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:44.876907+00:00
---

# Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Database Migration Service for MySQL Stay organized with collections  Save and categorize content based on your preferences. 

You can migrate MySQL databases to Cloud SQL for MySQL instances with Database Migration Service. Database Migration Service uses the native MySQL replication capabilities to replicate data from your source database to the destination Cloud SQL for MySQL instance.

This page provides an overview of the key Database Migration Service features for homogeneous MySQL migrations:

  * Supported source and destination lists all MySQL versions supported by Database Migration Service.

  * Migration data flow provides an end-to-end overview of how your data moves in Google Cloud during the migration process.

  * Monitoring gives an introduction for logs and metrics that can help you observe the progress and health of your migration job.




## Supported source and destination databases

You can use Database Migration Service to migrate between the same MySQL version, or from earlier versions of MySQL to later versions supported in Cloud SQL.

The following table lists all supported MySQL source and destination database offerings. For the full list of exact versions and cross-version support, see [ Versions support](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest).

Source databases | Destination databases  
---|---  
Amazon RDS |  Cloud SQL for MySQL  
Amazon Aurora  
Microsoft Azure Database for MySQL  
Self-managed MySQL (on premises or on any cloud VM that you fully control)  
  
## Migration data flow

For homogeneous MySQL migrations to Cloud SQL, Database Migration Service connects to the _destination_ Cloud SQL instance and then manages the migration process on its behalf. It's the destination instance that establishes the connection to your source instance, but Database Migration Service oversees the process.

![MySQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql_hmm_end2end_flow.svg) **Figure 1.** Data movement during Database Migration Service for MySQL migrations. (click to enlarge) ![MySQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql_hmm_end2end_flow.svg)

For homogeneous MySQL migrations to Cloud SQL, Database Migration Service supports _continuous_ and _one-time_ migration flows. With continuous migrations, your data is first loaded from a full dump, and then continuously updated based on data change information surfaced from database log files.

For a detailed walkthrough of all migration types and phases, see [ Migration types and phases](https://docs.cloud.google.com/database-migration/docs/mysql/migration-types).

## Monitoring

![Example diagram for migration job replication delay in
      Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql_metrics.png) **Figure 2.** Sample observability diagram in Database Migration Service. (click to enlarge) ![Example diagram for migration job replication delay in
      Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql_metrics.png)

Database Migration Service provides extensive logging and observability capabilities to help you monitor the migration progress. These features include real-time diagnostics for replication delay, as well as detailed logs for Cloud SQL for MySQL destination instance health and migration job state.

For more details, see [Migration job metrics](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-metrics).

## What's next

  * To learn more about MySQL data and feature support in Database Migration Service, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
