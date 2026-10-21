---
url: https://docs.cloud.google.com/database-migration/docs/mysql/migration-types/
title: Migration flow \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:14.316784+00:00
---

# Migration flow  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/migration-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Migration flow Stay organized with collections  Save and categorize content based on your preferences. 

For homogeneous MySQL migrations to Cloud SQL, Database Migration Service connects to the _destination_ Cloud SQL instance and then manages the migration process on its behalf. It's the destination instance that establishes the connection to your source instance, but it's Database Migration Service that oversees the process.

![MySQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql_hmm_end2end_flow.svg) **Figure 1.** Data movement during Database Migration Service for MySQL migrations. (click to enlarge) ![MySQL migration flow overview](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql_hmm_end2end_flow.svg)

For homogeneous MySQL migrations to Cloud SQL, Database Migration Service supports _continuous_ and _one-time_ migration flows. With continuous migrations, your data is first loaded from a full dump, and then continuously updated based on data change information surfaced from database log files. At a high level, migration phases progress as follows:

### One-time migrations

  1. When you create the migration job, Database Migration Service creates a temporary orchestration instance to manage replication and turns your destination Cloud SQL into a [ Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server). There are no additional costs associated with this orchestration instance. 

![View of the demoted destination instance in Cloud SQL Console.
              The image shows how the destination instance is managed by the
              temporary orchestration instance.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/demoted_destination_hmm_mysql.png) **Figure 2.** Destination instance displayed under the temporary orchestration instance in the Google Cloud console. ![View of the demoted destination instance in Cloud SQL Console.
              The image shows how the destination instance is managed by the
              temporary orchestration instance.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/demoted_destination_hmm_mysql.png)
  2. When you start the migration job, Database Migration Service begins the **full dump phase**. For one-time migrations, this is the only migration phase.

During full dump, Database Migration Service connects to your source instance, reads the contents of the databases you selected for migration, and then loads the data to the destination instance. 

For one-time migrations, we recommend that you disable writes on the source database during the full dump phase. This way you can avoid avoid losing data created after the migration process starts. 

You can also provide your own dump files for Database Migration Service. Note that any data that was added to the database after you created the dump files isn't going to be migrated. The network connection to your database is still established for consistency checks. 

  3. When the full dump phase is over, Database Migration Service automatically promotes the destination database and completes the migration. At that point, you can switch your application to use the new destination database. 



### Continuous migrations

  1. When you create the migration job, Database Migration Service creates a temporary orchestration instance to manage replication and turns your destination Cloud SQL into a [ Cloud SQL replica](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server). There are no additional costs associated with this orchestration instance. 

![View of the demoted destination instance in Cloud SQL Console.
              The image shows how the destination instance is managed by the
              temporary orchestration instance.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/demoted_destination_hmm_mysql.png) **Figure 2.** Destination instance displayed under the temporary orchestration instance in the Google Cloud console. ![View of the demoted destination instance in Cloud SQL Console.
              The image shows how the destination instance is managed by the
              temporary orchestration instance.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/demoted_destination_hmm_mysql.png)
  2. When you start the migration job, Database Migration Service begins the **full dump phase**. 

During full dump, Database Migration Service connects to your source instance, reads the contents of the databases you selected for migration, and then loads the data to the destination instance. 

You can also provide your own dump files for Database Migration Service. Note that any data that was added to the database after you created the dump files isn't going to be migrated. The network connection to your database is still established for consistency checks. 

  3. For continuous migrations, when the full dump phase is over, Database Migration Service switches to the **CDC phase**. During CDC, Database Migration Service keeps monitoring your source databases for changes, and then continuously replicates them on the destination instance. 

In the CDC phase, Database Migration Service doesn't copy actual data from your source tables: instead, it reads information extracted from database log files to replicate changes in the destination. You can stop the ongoing replication and promote the migration job when you want to switch your application so that it uses your destination instance as the production database. 




## What's next

  * To learn more about MySQL data and feature support in Database Migration Service, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations).

  * To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for MySQL migrations](https://docs.cloud.google.com/database-migration/docs/mysql/get-started-with-mysql-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
