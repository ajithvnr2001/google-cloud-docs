---
url: https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools/
title: Debugging and other tools \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:20.476810+00:00
---

# Debugging and other tools  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/debugging-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Resources ](https://docs.cloud.google.com/database-migration/docs/postgres/resources)



Send feedback 

#  Debugging and other tools Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-tools "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

This page includes scripts that help with debugging and using PostgreSQL.

## Migrate UPDATE and DELETE operations for non-primary key tables

For tables that don't have primary keys, Database Migration Service supports migration of the initial snapshot and `INSERT` statements during the change data capture (CDC) phase.

To update the missing `UPDATE` and `DELETE` processes, refer to the later sections of this document.

### Detect missing data between the source and Cloud SQL destination instances

  1. Identify which tables don't have primary keys: 
         
         select tab.table_schema,
                tab.table_name
         from information_schema.tables tab
         left join information_schema.table_constraints tco 
                   on tab.table_schema = tco.table_schema
                   and tab.table_name = tco.table_name 
                   and tco.constraint_type = 'PRIMARY KEY'
         where tab.table_type = 'BASE TABLE'
               and tab.table_schema not in ('pg_catalog', 'information_schema', 'pglogical')
               and tco.constraint_name is null
         order by table_schema,
                  table_name;
         

  2. Before starting the migration, for all tables without primary keys, check if there are any updates or deletes using this query: 
         
         SELECT schemaname,
               relname,
               n_tup_ins,
               n_tup_upd,
               n_tup_del
           FROM  pg_stat_user_tables
           WHERE schemaname NOT IN
           ('pglogical', 'pg_catalog', 'information_schema');
         

Where: 
     * `n_tup_ins`: number of rows inserted
     * `n_tup_upd`: number of rows updated (includes HOT updated rows)
     * `n_tup_del`: number of rows deleted
  3. Save these results either in a separate table or in a file.
  4. After the migration setup is complete, run the query again.
  5. Compare the results with the results from step 3.



If there are differences in values of `n_tup_upd` or `n_tup_del` on the source during migration, there might be some updates or deletes on the source.

**Note:** You can manually reset `pg_stat_user_tables` using the `pg_stat_reset()` function. If this function is run on the source, the statistics might not reflect accurate information.

### Manually migrate data from the source to the Cloud SQL destination instances

If you detect there are some discrepancies between the source and Cloud SQL destination instance, you can migrate the data using one of the options:

  * **Option 1** : Manually compare the data between the source and Cloud SQL destination and execute appropriate SQL queries to update only the data that is different between the source and the replica.

  * **Option 2** : Run `pg_dump` and `pg_restore` for the tables without primary keys. See [Export data from an on-premises PostgreSQL server using pg_dump](https://docs.cloud.google.com/sql/docs/postgres/import-export/import-export-dmp#external-server) for more information.

  * **Option 3** : Use Postgres `COPY` command to migrate your data. See [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-copy.html) for more information. Note that this step requires the replica VM to be able to connect to the source VM.


For **Option 2** and **Option 3** , if there is any data that is already migrated on to the replica, those records might require cleanup before running the `pg_restore` or `COPY` commands. Please make changes accordingly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


